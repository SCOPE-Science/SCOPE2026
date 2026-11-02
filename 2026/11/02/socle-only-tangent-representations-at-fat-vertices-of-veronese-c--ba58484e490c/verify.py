"""Independent monomial-syzygy check for Hilbert tangents at vertex powers."""

def kernel_grade(d, r, t):
    """Free dimension from all binomial monomial syzygies, over any field."""
    gen= d*r+1
    basis=d*t+1
    count=gen*basis
    zero=count
    par=list(range(count+1))
    size=[1]*(count+1)
    def root(x):
        while par[x]!=x:
            par[x]=par[par[x]]
            x=par[x]
        return x
    def union(a,b):
        a=root(a); b=root(b)
        if a==b:return
        if size[a]<size[b]:a,b=b,a
        par[b]=a; size[a]+=size[b]
    relations=0
    for k in range(1,r-t):
        for i in range(gen):
            for j in range(i+1,gen):
                for h in range(d*k+1):
                    hh=i+h-j
                    if not 0<=hh<=d*k:continue
                    relations+=1
                    for z in range(d*(t+k)+1):
                        s=z-h
                        ss=z-hh
                        a=i*basis+s if 0<=s<basis else zero
                        b=j*basis+ss if 0<=ss<basis else zero
                        if a!=zero or b!=zero:union(a,b)
    zero_root=root(zero)
    free=len({root(v) for v in range(count) if root(v)!=zero_root})
    return free,relations

def run():
    cases=0
    for d in range(1,7):
        for r in range(1,6):
            by_grade=[kernel_grade(d,r,t) for t in range(r)]
            observed=sum(n for n,k in by_grade)
            length=r+d*r*(r-1)//2
            predicted=(d*r+1)*(d*(r-1)+1)
            assert observed==predicted,(d,r,observed,predicted,by_grade)
            assert all(n==0 for n,k in by_grade[:-1])
            assert by_grade[-1][0]==predicted
            print(f'd={d} r={r} colength={length} T={observed} grades={[x[0] for x in by_grade]} tested_relations={sum(x[1] for x in by_grade)}')
            cases+=1
    print(f'VERIFY_OK: {cases} Veronese-cone pairs, monomial syzygy constraints checked')

if __name__=='__main__':run()
