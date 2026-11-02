"""Reproduce finite-instance checks for the linear-atom BALFI countermodel lemma.
Run: python checker.py. Uses only the Python standard library.
This is a test suite, not a proof of the general theorem.
"""
from itertools import product
from random import Random

rng = Random(20261025)
OPS = ('and','or','imp','neg','circ')


def subterms(term):
    out = []
    seen = set()
    def walk(x):
        if x in seen: return
        for y in x[1:]:
            if isinstance(y, tuple): walk(y)
        seen.add(x)
        out.append(x)
    walk(term)
    return out


def value(term, variables, neg, circ, top):
    op = term[0]
    if op == 'atom': return variables[term[1]]
    if op == 'neg': return neg[value(term[1],variables,neg,circ,top)]
    if op == 'circ': return circ[value(term[1],variables,neg,circ,top)]
    a = value(term[1],variables,neg,circ,top)
    b = value(term[2],variables,neg,circ,top)
    if op == 'and': return a & b
    if op == 'or': return a | b
    if op == 'imp': return (top ^ a) | b
    raise ValueError(term)


def all_balfi_pairs(atoms):
    top = (1 << atoms)-1
    choices=[]
    for x in range(top+1):
        local=[]
        for nx in range(top+1):
            if (x|nx)!=top: continue
            for cx in range(top+1):
                if x & nx & cx == 0:
                    local.append((nx,cx))
        choices.append(local)
    for combo in product(*choices):
        yield tuple(z[0] for z in combo),tuple(z[1] for z in combo)


def random_balfi(atoms):
    top=(1<<atoms)-1
    n=[];c=[]
    for x in range(top+1):
        nx=(top^x)|(rng.randrange(top+1)&x)
        cx=rng.randrange(top+1)&(top^(x&nx))
        n.append(nx);c.append(cx)
    return n,c


def random_formula(d):
    if d==0 or rng.random()<0.21: return ('atom',rng.choice(('p','q','r')))
    op=rng.choice(OPS)
    if op in ('neg','circ'): return (op,random_formula(d-1))
    return (op,random_formula(d-1),random_formula(d-1))


def project_word(x,coords):
    return sum(((x>>i)&1)<<j for j,i in enumerate(coords))


def compress(term,vars_,N,C,atoms):
    top=(1<<atoms)-1
    terms=subterms(term)
    vals={s:value(s,vars_,N,C,top) for s in terms}
    S=set(vals.values())|{top}
    coords=[]
    while len({project_word(x,coords) for x in S})<len(S):
        groups={}
        for x in S:groups.setdefault(project_word(x,coords),[]).append(x)
        best=None;gain=-1
        for i in range(atoms):
            if i in coords: continue
            score=sum(bool(set((x>>i)&1 for x in group)=={0,1}) for group in groups.values())
            if score>gain: best,gain=i,score
        assert gain>0
        coords.append(best)
    if not coords: coords=[0]
    assert len(coords)<=max(1,len(S)-1), (len(coords),len(S))
    nvals={}
    cvals={}
    for s in terms:
        if s[0] not in ('neg','circ'): continue
        x=project_word(vals[s[1]],coords)
        z=project_word(vals[s],coords)
        table=nvals if s[0]=='neg' else cvals
        assert x not in table or table[x]==z
        table[x]=z
    m=len(coords);allt=(1<<m)-1
    newN=[nvals.get(x,allt^x) for x in range(allt+1)]
    newC=[cvals.get(x,0) for x in range(allt+1)]
    for x in range(allt+1):
        assert (x|newN[x])==allt
        assert (x&newN[x]&newC[x])==0
    newvars={p:project_word(x,coords) for p,x in vars_.items()}
    for s in terms:
        assert value(s,newvars,newN,newC,allt)==project_word(vals[s],coords)
    if vals[term]!=top:assert value(term,newvars,newN,newC,allt)!=allt
    # Verify succinct certification solely from subformula bitvectors:
    bits={s:project_word(vals[s],coords) for s in terms}
    for s in terms:
        if s[0] in ('and','or','imp'):
            x,y=bits[s[1]],bits[s[2]]
            assert bits[s]=={'and':lambda:x&y,'or':lambda:x|y,'imp':lambda:(allt^x)|y}[s[0]]()
    for s in terms:
        if s[0]=='neg':
            assert (bits[s[1]]|bits[s])==allt
    for a in terms:
        if a[0]!='neg':continue
        for b in terms:
            if b[0]=='neg' and bits[a[1]]==bits[b[1]]:assert bits[a]==bits[b]
            if b[0]=='circ' and bits[a[1]]==bits[b[1]]:assert (bits[a[1]]&bits[a]&bits[b])==0
    for a in terms:
        if a[0]!='circ':continue
        for b in terms:
            if b[0]=='circ' and bits[a[1]]==bits[b[1]]:assert bits[a]==bits[b]
    return m


def exhaustive_test():
    small=[('atom','p'),('neg',('atom','p')),('circ',('atom','p')),
           ('imp',('neg',('atom','p')),('atom','p')),
           ('and',('atom','p'),('neg',('atom','p'))),
           ('circ',('neg',('atom','p'))),
           ('imp',('circ',('atom','p')),('neg',('atom','p'))),
           ('imp',('atom','p'),('circ',('atom','p')))]
    cases=0
    for m in (1,2):
        for N,C in all_balfi_pairs(m):
            for p in range(1<<m):
                for term in small:
                    compress(term,{'p':p},N,C,m)
                    cases+=1
    return cases


def random_test():
    cases=0
    for m in (2,3,4,5,6):
        for _ in range(400):
            N,C=random_balfi(m)
            variables={name:rng.randrange(1<<m) for name in ('p','q','r')}
            term=random_formula(5)
            compress(term,variables,N,C,m)
            cases+=1
    return cases


def two_atom_obstruction():
    p=('atom','p');q=('atom','q')
    def iff(a,b):return ('and',('imp',a,b),('imp',b,a))
    f=('imp',iff(p,q),iff(('neg',p),('neg',q)))
    for N,C in all_balfi_pairs(1):
        for a,b in product(range(2),repeat=2):
            assert value(f,{'p':a,'q':b},N,C,1)==1
    N=[3,3,1,0]
    C=[0,0,0,3]
    assert all((x|N[x])==3 and (x&N[x]&C[x])==0 for x in range(4))
    assert value(f,{'p':1,'q':3},N,C,3)==2
    return True

if __name__=='__main__':
    e=exhaustive_test()
    r=random_test()
    assert two_atom_obstruction()
    print(f'EXHAUSTIVE_CASES={e}')
    print(f'SEEDED_RANDOM_CASES={r}')
    print('ONE_ATOM_INSUFFICIENCY_WITNESS=OK')
    print('ALL_CHECKS_OK')
