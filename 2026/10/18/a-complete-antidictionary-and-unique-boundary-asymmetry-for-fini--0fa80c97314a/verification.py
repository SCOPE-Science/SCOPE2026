#!/usr/bin/env python3
"""Independent substring-set and structural checks for finite Fibonacci antidictionaries."""
from collections import Counter

def fibonacci(k):
    f=['0','01']
    while len(f)<=k:
        f.append(f[-1]+f[-2])
    return f

def factors(w):
    return [set(w[i:i+t] for i in range(len(w)-t+1)) for t in range(len(w)+1)]

def absent(w):
    fs=factors(w)
    return {v for t in range(2,len(w)+2) for u in fs[t-2] for a in '01' for b in '01'
            for v in [a+u+b] if v not in (fs[t] if t<=len(w) else set())
            and a+u in fs[t-1] and u+b in fs[t-1]}

def predicted(F,k):
    w=F[k];q=len(F[k-2]);p=len(F[k-1]);
    g={ ('1' if F[j][-2]=='0' else '0') + F[j][:-2] + ('1' if F[j][-2]=='0' else '0')
        for j in range(1,k-1)}
    x=F[k-1][-2]
    t=x+F[k-1][:-2]+x
    e=F[k-3][-1]+F[k-2]+'0'
    assert t==t[::-1] and e!=e[::-1]
    assert len(g)==k-2
    assert {len(x) for x in g}=={len(F[j]) for j in range(1,k-1)}
    assert len(t)==p and len(e)==q+2
    return g|{t,e}

def main():
    F=fibonacci(11)
    cases=0
    for k in range(5,12):
        w=F[k]; n=len(w); q=len(F[k-2]);p=len(F[k-1]); fs=factors(w)
        assert {i for i in range(n-q+1) if w.startswith(F[k-2],i)}=={0,q,p}
        assert {i for i in range(n-(p-2)+1) if w.startswith(F[k-1][:-2],i)}=={0,q}
        assert [len(fs[t]) for t in range(n+1)]==[min(t+1,q+2,n-t+1) for t in range(n+1)]
        for j in range(1,k-1):
            u=F[j][:-2]
            assert all(a+u in w and u+a in w for a in '01')
        bispecial={t:sum(all(a+u in w and u+a in w for a in '01') for u in fs[t]) for t in range(n+1)}
        assert {t for t,c in bispecial.items() if c}=={len(F[j])-2 for j in range(1,k-1)}
        actual=absent(w)
        bylen=Counter(map(len,actual))
        for t in range(2,n+2):
            expected_count=bispecial[t-2]+2*len(fs[t-1])-len(fs[t-2])-(len(fs[t]) if t<=n else 0)
            assert bylen[t]==expected_count,(k,t,bylen[t],expected_count)
        expect=predicted(F,k)
        assert actual==expect,(k,len(actual^expect),actual^expect)
        assert len(actual)==k
        assert sum(z!=z[::-1] for z in actual)==1
        print('k',k,'length',n,'MAWs',len(actual),'lengths',sorted(map(len,actual)))
        cases+=1
    print('FIBONACCI_FINITE_ANTIDICTIONARY_PASS cases',cases)
if __name__=='__main__':main()
