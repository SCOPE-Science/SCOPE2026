"""Exact finite checks for signed Lefschetz characters of bipartite Boolean complexes."""
from itertools import permutations, combinations
from collections import Counter
from functools import lru_cache
from math import comb, factorial

@lru_cache(None)
def oriented_edges(a,b):
    """Distinct acyclic orientations, represented by left-to-right Boolean edge signs."""
    items=list(range(a+b))
    edges=[(u,v) for u in range(a) for v in range(a,a+b)]
    out=set()
    for order in permutations(items):
        pos={x:i for i,x in enumerate(order)}
        bits=tuple(pos[u]<pos[v] for u,v in edges)
        out.add(bits)
    return tuple(sorted(out))

def cycles(p):
    seen=set();ans=[]
    for x in range(len(p)):
        if x not in seen:
            cycle=[];y=x
            while y not in seen:
                seen.add(y);cycle.append(y);y=p[y]
            ans.append(tuple(cycle))
    return ans

def sign_restricted(p,S):
    return (-1)**(len(S)-len([c for c in cycles(p) if c[0] in S]))

def fo(a,b,ls,rs,pl,pr):
    """Number of acyclic orientations invariant under a selected bipartite automorphism."""
    lle={x:i for i,x in enumerate(ls)}
    rre={x:i for i,x in enumerate(rs)}
    perm_l=[lle[pl[x]] for x in ls]
    perm_r=[rre[pr[y]] for y in rs]
    cnt=0
    for ori in oriented_edges(a,b):
        if all(ori[i*b+j]==ori[perm_l[i]*b+perm_r[j]] for i in range(a) for j in range(b)):
            cnt+=1
    return cnt

def top_trace_direct(pl,pr):
    m,n=len(pl),len(pr)
    ans=-1  # reduced empty word
    for a in range(m+1):
      for b in range(n+1):
       if a+b==0: continue
       for ls in combinations(range(m),a):
        if any(pl[x] not in ls for x in ls):continue
        for rs in combinations(range(n),b):
         if any(pr[x] not in rs for x in rs):continue
         ans+=(-1)**(a+b-1)*sign_restricted(pl,ls)*sign_restricted(pr,rs)*fo(a,b,ls,rs,pl,pr)
    return (-1)**(m+n-1)*ans

def stirling2(n,k):
    if n==k==0:return 1
    if k==0 or k>n:return 0
    return stirling2(n-1,k-1)+k*stirling2(n-1,k)

def beta(m,n):
    from math import factorial
    return sum((-1)**(m-j)*factorial(j)*stirling2(m+1,j+1)*j**n for j in range(1,m+1))

def class_reps(n):
    out={}
    for p in permutations(range(n)):
        cs=tuple(sorted((len(c) for c in cycles(p)),reverse=True))
        out.setdefault(cs,p)
    return out

def run():
    tests=0
    for m,n in [(1,1),(1,2),(2,2),(2,3),(3,3),(2,4),(3,4)]:
        for cl,pl in class_reps(m).items():
            for cr,pr in class_reps(n).items():
                lhs=top_trace_direct(pl,pr)
                rhs=sign_restricted(pl,tuple(range(m)))*sign_restricted(pr,tuple(range(n)))*beta(len(cl),len(cr))
                assert lhs==rhs,(m,n,cl,cr,lhs,rhs)
                tests+=1
        ident=tuple(range(m)); ident2=tuple(range(n))
        assert top_trace_direct(ident,ident2)==beta(m,n)
        print(f'K_{{{m},{n}}}: dim={beta(m,n)}; checked {len(class_reps(m))*len(class_reps(n))} conjugacy-class pairs')
    # Independent finite consequence: the invariant top-homology line exists iff m=n.
    for m in range(1,6):
      for n in range(1,6):
        total=0
        for pl in permutations(range(m)):
          for pr in permutations(range(n)):
            total+=sign_restricted(pl,tuple(range(m)))*sign_restricted(pr,tuple(range(n)))*beta(len(cycles(pl)),len(cycles(pr)))
        assert total==int(m==n)*factorial(m)*factorial(n),(m,n,total)
    print(f'PASS: {tests} exact signed fixed-cell comparisons and 25 invariant-dimension tests')
if __name__=='__main__':run()
