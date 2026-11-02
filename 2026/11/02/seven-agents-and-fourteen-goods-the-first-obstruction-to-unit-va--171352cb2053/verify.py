from itertools import combinations

def connected(n,edges):
    adj=[0]*n
    for i,j in edges:
        adj[i]|=1<<j;adj[j]|=1<<i
    visited=1; new=1
    while new:
        u=new & -new;new-=u
        j=u.bit_length()-1
        delta=adj[j]&~visited
        visited|=delta;new|=delta
    return visited==(1<<n)-1

def feasible_cut(n,edges):
    m=len(edges);q,r=divmod(m,n)
    if not edges: return True
    for s in range(1,1<<n):
        inc=0;inside=0;sz=s.bit_count()
        for a,b in edges:
            x=(s>>a)&1;y=(s>>b)&1
            inc+=x|y;inside+=x&y
        if inside>(q+1)*sz or inc<q*sz: return False
    return True

def run():
    allct=0; allbad=0
    for n in range(2,7):
        e=list(combinations(range(n),2));ct=0;bad=0
        for mask in range(1<<len(e)):
            es=[x for k,x in enumerate(e) if mask>>k&1]
            if len(es)<n-1 or not connected(n,es): continue
            ct+=1
            if not feasible_cut(n,es):bad+=1
        print('n',n,'connected',ct,'nonEQ1',bad,flush=True)
        assert bad==0
    n=7;m=14;ed=list(combinations(range(n),2));cnt=fail=leaves=0
    for ids in combinations(range(len(ed)),m):
        es=[ed[i] for i in ids]
        if not connected(n,es):continue
        cnt+=1
        mindeg=min(sum(i in edge for edge in es) for i in range(n))
        bad=not feasible_cut(n,es)
        if bad:fail+=1
        if mindeg==1:leaves+=1
        assert bad==(mindeg==1),(es,bad,mindeg)
    print('n7_m14 connected',cnt,'nonEQ1',fail,'leaves',leaves,flush=True)
if __name__=='__main__':run()
