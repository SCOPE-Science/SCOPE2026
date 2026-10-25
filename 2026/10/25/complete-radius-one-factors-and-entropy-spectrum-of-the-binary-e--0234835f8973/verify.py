#!/usr/bin/env python3
"""Exact finite-state certificates for one-step radius-one factors of the even shift."""
from collections import deque, Counter
from itertools import product

# 0 = even count of zeros since last 1, 1 = odd count.
DELTA = {(0, 0): 1, (0, 1): 0, (1, 0): 0}
STATES = [(s,a,b) for s in (0,1) for a in (0,1)
          if (s,a) in DELTA for b in (0,1)
          if (DELTA[(s,a)],b) in DELTA]
assert len(STATES) == 5
IX = {t:i for i,t in enumerate(STATES)}
ALL = frozenset(range(5))

def graph(rule):
    edges = [[] for _ in STATES]
    for i,(s,a,b) in enumerate(STATES):
        t=DELTA[(s,a)]
        for c in (0,1):
            if (DELTA[(t,b)],c) in DELTA:
                j=IX[(t,b,c)]
                label=(rule >> ((a<<2)|(b<<1)|c))&1
                edges[i].append((j,label))
    return edges

def step(g,states,sym):
    return frozenset(j for i in states for j,z in g[i] if z==sym)

def dfa_even(q,z):
    # 2 = finite word has not encountered a 1; -1 = forbidden.
    if q==2:return 2 if z==0 else 0
    if q==0:return 1 if z==0 else 0
    if q==1:return 0 if z==0 else -1
    return -1

def subset_closure(g):
    states=[ALL]; ind={ALL:0}; transitions=[]
    for s in states:
        row=[]
        for z in (0,1):
            t=step(g,s,z)
            if t and t not in ind:
                ind[t]=len(states); states.append(t)
            row.append(ind[t] if t else -1)
        transitions.append(row)
    return states,transitions

def find_bad_output(g):
    # Find a non-even word emitted by the full bi-infinite predecessor graph.
    q=deque([(ALL,2,'')]); seen={(ALL,2)}
    while q:
        ss,a,w=q.popleft()
        for z in (0,1):
            t=step(g,ss,z)
            if not t:continue
            b=dfa_even(a,z)
            if b<0:return w+str(z)
            v=(t,b)
            if v not in seen:
                seen.add(v);q.append((t,b,w+str(z)))
    return None

def is_onto_even(g):
    q=deque([(ALL,2,'')]);seen={(ALL,2)}
    while q:
        ss,a,w=q.popleft()
        for z in (0,1):
            b=dfa_even(a,z)
            if b<0:continue
            t=step(g,ss,z)
            if not t:return False,w+str(z)
            v=(t,b)
            if v not in seen:
                seen.add(v);q.append((t,b,w+str(z)))
    return True,None

def image_difference(g,h):
    q=deque([(ALL,ALL,'')]);seen={(ALL,ALL)}
    while q:
        a,b,w=q.popleft()
        for z in (0,1):
            x=step(g,a,z);y=step(h,b,z)
            if bool(x)!=bool(y):return w+str(z)
            v=(x,y)
            if v not in seen:
                seen.add(v);q.append((x,y,w+str(z)))
    return None

def pattern_step(q,z,patterns,force_even):
    p,suff=q
    pp=dfa_even(p,z) if force_even else 2
    if pp<0:return None
    w=suff+str(z)
    if any(w.endswith(pat) for pat in patterns):return None
    candidates=[w[-j:] for j in range(1,len(w)+1)
                if any(pat.startswith(w[-j:]) for pat in patterns)]
    return (pp, max(candidates,key=len,default=''))

def compare_to_forbidden(g,patterns,force_even):
    start=(ALL,(2,''));q=deque([(start,'')]);seen={start}
    while q:
        (S,d),w=q.popleft()
        for z in (0,1):
            t=step(g,S,z);e=pattern_step(d,z,patterns,force_even)
            if bool(t)!=(e is not None):return False,w+str(z)
            if t and (t,e) not in seen:
                seen.add((t,e));q.append(((t,e),w+str(z)))
    return True,len(seen)

def mmul(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def charpoly(A):
    n=len(A);B=[[int(i==j) for j in range(n)] for i in range(n)]
    coeff=[1]
    for k in range(1,n+1):
        C=mmul(A,B);tr=sum(C[i][i] for i in range(n))
        assert tr%k==0
        c=-tr//k;coeff.append(c)
        B=[[C[i][j]+(c if i==j else 0) for j in range(n)] for i in range(n)]
    assert not any(any(row) for row in B)
    return coeff

def mat_of_transitions(T):
    n=len(T);A=[[0]*n for _ in range(n)]
    for i,row in enumerate(T):
        for j in row:
            if j>=0:A[i][j]+=1
    return A

def valid_word(w):
    q=2
    for c in w:
        q=dfa_even(q,int(c))
        if q<0:return False
    return True

def finite_direct(rule,n):
    result=set()
    for tup in product('01',repeat=n+2):
        w=''.join(tup)
        if not valid_word(w):continue
        result.add(''.join(str((rule>>int(w[i:i+3],2))&1) for i in range(n)))
    return result

def finite_graph(rule,n):
    g=graph(rule);v={(ALL,'')}
    for _ in range(n):
        v={(step(g,s,z),w+str(z)) for s,w in v for z in (0,1) if step(g,s,z)}
    return {w for s,w in v}

def check():
    # This five-state graph is an essential strongly connected presentation.
    base=graph(204)
    def reachable(k):
        s={k};q=[k]
        while q:
            i=q.pop()
            for j,z in base[i]:
                if j not in s:s.add(j);q.append(j)
        return s
    assert all(len(reachable(i))==5 for i in range(5))
    good=[r for r in range(256) if find_bad_output(graph(r)) is None]
    expected=[0,32,138,139,170,171,204,208,209,222,223,236,240,241,254,255]
    assert good==expected,good
    assert {find_bad_output(graph(r)) is None for r in good}=={True}
    # The only globally distinct mappings differ by the forbidden input triple 101.
    pairs=[(0,32),(138,170),(139,171),(204,236),
           (208,240),(209,241),(222,254),(223,255)]
    assert sorted(sum((list(p) for p in pairs),[]))==good
    for a,b in pairs:
        assert a^b==32
    onto=[r for r in good if is_onto_even(graph(r))[0]]
    assert onto==[138,170,204,208,236,240],onto
    assert image_difference(graph(139),graph(209)) is None
    assert image_difference(graph(170),graph(204)) is None
    assert image_difference(graph(204),graph(208)) is None
    yes1,N1=compare_to_forbidden(graph(139),['000','101'],False)
    yes2,N2=compare_to_forbidden(graph(209),['000','101'],False)
    yes3,N3=compare_to_forbidden(graph(222),['010','0110'],True)
    assert yes1 and yes2 and yes3, (yes1,yes2,yes3)
    # Distinct proper images, plus distinct fixed-point contents.
    assert image_difference(graph(139),graph(222))=='000'
    assert image_difference(graph(139),graph(170))=='000'
    assert image_difference(graph(222),graph(170))=='010'
    expected_polys={
       139:[1,-1,-1,0,1,1,-1,-1,0], # may be replaced below by exact factor products
    }
    # Each integer characteristic polynomial is computed from the *entire* reachable DFA.
    polys={r:charpoly(mat_of_transitions(subset_closure(graph(r))[1])) for r in (139,209,222)}
    def mulpoly(p,q):
        a=[0]*(len(p)+len(q)-1)
        for i,x in enumerate(p):
            for j,y in enumerate(q):a[i+j]+=x*y
        return a
    def xp(k):return [1]+[0]*k
    p3=[1,-1,0,-1]
    p5=[1,-1,-1,1,0,-1]
    assert polys[139]==mulpoly(mulpoly(mulpoly([1,-1],[1,1]),p3),[1,0,0,0]),polys[139]
    assert polys[209]==mulpoly(p3,[1,0,0,0]),polys[209]
    assert polys[222]==mulpoly(mulpoly([1,-1],p5),[1,0,0]),polys[222]
    for r in (0,139,170,204,208,209,222,255):
        for n in range(1,9):
            assert finite_direct(r,n)==finite_graph(r,n),(r,n)
    # For other rules, every failure is witnessed by finite output non-even word.
    bad_lengths=Counter(len(find_bad_output(graph(r))) for r in range(256) if r not in good)
    print('VERIFY_OK: 256 rules; 16 codes/8 maps; 6 codes/3 onto shifts;'
          ' exact 2 proper image languages and entropy polynomials;'
          ' direct input enumeration for 8 representatives, lengths 1..8;'
          ' reachable automata',[(r,len(subset_closure(graph(r))[0])) for r in (139,209,222)],
          ' forbidden DFA closures',(N1,N2,N3),'bad lengths',dict(sorted(bad_lengths.items())))
    return polys

if __name__=='__main__':check()
