from collections import defaultdict
from itertools import product
from math import comb, factorial

def local_poly(n):
    d={(0,0):1}
    for i in range(2,n+1):
        v=defaultdict(int)
        for (a,b),cnt in d.items():
            v[a+1,b]+=cnt
            v[a,b+1]+=cnt
            v[a,b]+=cnt*(a+1)*(b+1)
        d=dict(v)
    return d

def global_poly(n):
    # e,f ranks, g rank -> value by labelled assemblies, EGF exponential Bell transform.
    ans=[]
    for s in range(n+1):
        if s==0:
            ans.append({(0,0,0):1});continue
        d=defaultdict(int)
        for j in range(1,s+1):
            for (ar,br,gr),cnt in ans[s-j].items():
                for (a,b),val in local_poly(j).items():
                    d[ar+a+1,br+b+1,gr+1]+=comb(s-1,j-1)*cnt*val
        ans.append(dict(d))
    return ans[n]

def brute(n):
    maps=[]
    for f in product(*(range(i+1) for i in range(n))):
        if all(f[f[i]]==f[i] for i in range(n)):
            maps.append(f)
    ans=defaultdict(int)
    for f in maps:
        for g in maps:
            if all(f[g[i]]==g[f[i]] for i in range(n)):
                ans[(len(set(f)),len(set(g)),len(set(f[g[i]] for i in range(n))))]+=1
    return dict(ans),len(maps)

if __name__=='__main__':
    for n in range(1,8):
        theory=global_poly(n); empirical,bell=brute(n)
        assert theory==empirical,(n, theory, empirical)
        print(n,bell, sum(theory.values()),sum(v for (a,b,k),v in theory.items() if k==1), local_poly(n) and sum(local_poly(n).values()))
