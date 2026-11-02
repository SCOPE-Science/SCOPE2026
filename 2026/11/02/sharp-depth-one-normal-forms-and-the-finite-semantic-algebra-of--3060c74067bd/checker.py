"""Standalone finite semantic regression tests for four-valued S5 essence modalities.

Run with Python 3: python checker.py
This checker supports the proof's finite truth tables and sampled normal forms;
the unrestricted claims are proved symbolically in RESULT.md.
"""
import itertools
import random

V = ('t', 'b', 'n', 'f')
CLASSICAL = {'t', 'f'}
T = {'t', 'b'}
F = {'b', 'f'}
CONFLATE = {'t': 't', 'b': 'n', 'n': 'b', 'f': 'f'}
BITS = {'t': (1, 0), 'b': (1, 1), 'n': (0, 0), 'f': (0, 1)}
VAL = {v:k for k,v in BITS.items()}


def prop(j): return ('p', j)
def dm(a): return ('neg', a)
def boo(a): return ('sim', a)
def conj(*a):
    a = list(a)
    if not a: raise ValueError('empty conjunction')
    z=a[0]
    for x in a[1:]: z=('and',z,x)
    return z

def disj(*a):
    a = list(a)
    if not a: raise ValueError('empty disjunction')
    z=a[0]
    for x in a[1:]: z=('or',z,x)
    return z

def imp(a,b): return ('imp',a,b)
def modal(name,kind,a): return ('modal',name,kind,a)

def evaluate(a, state, support, cache=None):
    """Value at state in a single S5 equivalence class with given support."""
    if cache is None: cache={}
    key=(a,state)
    if key in cache: return cache[key]
    op=a[0]
    if op=='p': v=state[a[1]]
    elif op in ('neg','sim'):
        t,f=BITS[evaluate(a[1],state,support,cache)]
        v=VAL[(f,t) if op=='neg' else (1-t,1-f)]
    elif op in ('and','or','imp'):
        x,y=BITS[evaluate(a[1],state,support,cache)]
        z,w=BITS[evaluate(a[2],state,support,cache)]
        if op=='and': v=VAL[(x&z,y|w)]
        elif op=='or': v=VAL[(x|z,y&w)]
        else: v=VAL[((not x) or z,x&w)]
    elif op=='modal':
        name,i,z=a[1:]
        current=evaluate(z,state,support,cache)
        values={evaluate(z,s,support,cache) for s in support}
        if i in V:
            star=CONFLATE[i]
            if name=='circ':
                truth=(current!=i or all(v==i for v in values))
                false=(current==i and any(v!=star for v in values))
            elif name=='tcirc':
                truth=(current==i or all(v!=i for v in values))
                false=(current!=i and star in values)
            elif name=='bullet':
                truth=(current==i and any(v!=i for v in values))
                false=(current!=star or all(v==star for v in values))
            elif name=='tbullet':
                truth=(current!=i and i in values)
                false=(current==star or all(v!=star for v in values))
            else: raise AssertionError(name)
        else:
            s=T if i=='T' else F
            other=F if i=='T' else T
            yes=(current in s)
            no=(current in other)
            if name=='circ':
                truth=(not yes or all(v in s for v in values))
                false=(yes and any(v in other for v in values))
            elif name=='tcirc':
                truth=(yes or all(v not in s for v in values))
                false=(not yes and any(v not in other for v in values))
            elif name=='bullet':
                truth=(yes and any(v not in s for v in values))
                false=(no or all(v not in other for v in values))
            elif name=='tbullet':
                truth=(not yes and any(v in s for v in values))
                false=(not no or all(v in other for v in values))
            else: raise AssertionError(name)
        v=VAL[(int(truth),int(false))]
    else: raise AssertionError(a)
    cache[key]=v
    return v


def delta(a,i):
    if i=='t': return dm(disj(dm(a),boo(a)))
    if i=='b': return disj(dm(imp(a,a)),boo(imp(a,a)))
    if i=='n': return imp(disj(a,dm(a)),conj(a,boo(a)))
    if i=='f': return conj(dm(a),boo(a))
    raise AssertionError(i)


def local_type(a): return conj(*(delta(prop(j),v) for j,v in enumerate(a)))

def exists_type(a):
    d=local_type(a)
    return disj(d,modal('tbullet','t',d))


def support_guard(S,all_types):
    fs=[]
    for a in all_types:
        x=exists_type(a)
        fs.append(x if a in S else boo(x))
    return conj(*fs)


def pointed_guard(a,S,all_types):
    return conj(local_type(a),support_guard(S,all_types))


def beta(p,i):
    return conj(delta(p,i),p if i=='b' else boo(p))


def global_b_for_bf(z):
    return disj(conj(modal('circ','b',z),z),modal('bullet','b',z),modal('tbullet','b',z))


def nonclassical_flag(k):
    return disj(*(global_b_for_bf(beta(prop(j),v)) for j in range(k) for v in ('b','n')))


def nonclassical_n_flag(k):
    b=nonclassical_flag(k)
    return conj(delta(b,'b'),boo(b))


def all_types(k): return tuple(itertools.product(V, repeat=k))

def states(k):
    Q=all_types(k)
    for mask in range(1,1<<len(Q)):
        S=tuple(a for j,a in enumerate(Q) if mask>>j & 1)
        for a in S: yield (a,S)


def tests():
    checked=0
    for i in V:
        for a in V:
            got=evaluate(delta(prop(0),i),(a,),((a,),))
            assert got==('t' if a==i else 'f'), (i,a,got)
            checked+=1
    # Every primitive modality must preserve classical output on all-classical cells.
    cc=((('t',),), (('f',),), (('t',),('f',)))
    for S in cc:
        for a in S:
            for i in (*V,'T','F'):
                for name in ('circ','tcirc','bullet','tbullet'):
                    got=evaluate(modal(name,i,prop(0)),a,S)
                    assert got in CLASSICAL, (name,i,a,S,got)
                    checked+=1
    Q=all_types(1)
    for a,S in states(1):
        for x in Q:
            val=evaluate(exists_type(x),a,S)
            assert val==('t' if x in S else 'f'), (a,S,x,val)
            checked+=1
        for x in Q:
            val=evaluate(pointed_guard(x,S,Q),a,S)
            assert val==('t' if x==a else 'f'), (a,S,x,val)
            checked+=1
        B=evaluate(nonclassical_flag(1),a,S)
        C=evaluate(nonclassical_n_flag(1),a,S)
        expect=any(v[0] not in CLASSICAL for v in S)
        assert B==('b' if expect else 'f')
        assert C==('n' if expect else 'f')
        checked+=2
    # Full four-valued prescribed maps for all 32 pointed support states, with
    # classical outputs required on states whose support is wholly classical.
    all_states=list(states(1))
    rnd=random.Random(72907)
    for iteration in range(12):
        targets={}
        for a,S in all_states:
            targets[(a,S)]=rnd.choice(('t','f') if all(v[0] in CLASSICAL for v in S) else V)
        disjuncts=[]
        B=nonclassical_flag(1)
        N=nonclassical_n_flag(1)
        for (a,S),desired in targets.items():
            guard=pointed_guard(a,S,Q)
            if desired=='t': disjuncts.append(guard)
            if desired=='b': disjuncts.append(conj(guard,B))
            if desired=='n': disjuncts.append(conj(guard,N))
        formula=disj(*disjuncts) if disjuncts else conj(delta(prop(0),'t'),boo(delta(prop(0),'t')))
        for a,S in all_states:
            got=evaluate(formula,a,S)
            assert got==targets[(a,S)], (iteration,a,S,got,targets[(a,S)])
            checked+=1
    # Explicitly exercise the all-f output case, including nonclassical supports.
    bottom=conj(delta(prop(0),'t'),boo(delta(prop(0),'t')))
    for a,S in all_states:
        assert evaluate(bottom,a,S)=='f'
        checked+=1
    # A random sample of supports of size at most eight in the two-variable case.
    QQ=all_types(2)
    for iteration in range(40):
        s=rnd.sample(list(QQ),rnd.randrange(1,9))
        S=tuple(s)
        a=rnd.choice(S)
        B=evaluate(nonclassical_flag(2),a,S)
        expect=any(any(v not in CLASSICAL for v in u) for u in S)
        assert B==('b' if expect else 'f')
        for x in rnd.sample(list(QQ),5):
            assert evaluate(exists_type(x),a,S)==('t' if x in S else 'f')
            checked+=1
        checked+=1
    # Complete semantic-profile arithmetic.
    for k,N,Nc,exponent in [(1,32,4,60),(2,524288,32,1048544)]:
        q=4**k;c=2**k
        assert (q*2**(q-1),c*2**(c-1),2*q*2**(q-1)-c*2**(c-1))==(N,Nc,exponent)
        checked+=1
    print('ALL_CHECKS_OK',checked,'finite semantic checks')

if __name__=='__main__': tests()
