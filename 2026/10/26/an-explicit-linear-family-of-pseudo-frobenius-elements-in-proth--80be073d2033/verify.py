import heapq

def candidate(n):
    M=7*(1<<n); a=M+1; L=n+2
    coins=[(1<<i)-1 for i in range(1,L+1)]
    gens=[M*(1<<i)+1 for i in range(L+1)]
    d=[10**100]*a;d[0]=0;pq=[(0,0)]
    while pq:
        w,r=heapq.heappop(pq)
        if w!=d[r]:continue
        for g in gens:
            t=(r+g)%a;h=w+g
            if h<d[t]:d[t]=h;heapq.heappush(pq,(h,t))
    maximal={d[r]-a for r in range(a) if all(d[(r+g)%a]<d[r]+g for g in gens[1:])}
    ts=[4*(1<<n)-n-2,6*(1<<n)-n-2]+[M-j for j in range(5,n+3)]+[M-1,M]
    assert len(ts)==n+2==len(set(ts))
    witness={d[(-t)%a]-a for t in ts}
    assert witness <=maximal, (n,witness-maximal)
    # independently validate Apéry greedy criterion on all residues
    def ell(t):
       count=0
       for c in reversed(coins):
          v,t=divmod(t,c);count+=v
       return count
    assert all(d[(-t)%a]==M*t+a*ell(t) for t in range(a))
    assert len(maximal)==n+2,(n,len(maximal))
    print('n=',n,'a=',a,'type=',len(maximal),'witness=',len(witness))

for n in range(3,11):candidate(n)
print('VERIFY_OK')
