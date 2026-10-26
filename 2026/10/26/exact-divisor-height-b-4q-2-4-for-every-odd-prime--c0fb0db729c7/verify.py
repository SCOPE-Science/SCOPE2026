"""Independent exact enumerator of polynomial divisors and residue-slice bounds."""
from itertools import product

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:c[i+j]+=x*y
    return c

def factors(q):
    one=[-1,1]
    two=[1,1]
    four=[1,0,1]
    u=[1]*q
    v=[(-1)**j for j in range(q)]
    w=[0]*(2*q-1)
    for j in range(q):w[2*j]=(-1)**j
    def lift(a):
        ans=[0]*(q*(len(a)-1)+1)
        for j,x in enumerate(a):ans[j*q]=x
        return ans
    return [one,two,four,u,v,w,lift(u),lift(v),lift(w)]

def combinations(q):
    fac=factors(q)
    products=[[1]]
    for t in fac:
        products += [mul(p,t) for p in products[:]]
    assert len(products)==512
    low=products[:64]
    return products,low

def main():
    for q in (3,5,7,11,13):
        polys,low=combinations(q)
        max_slice=max(sum(abs(p[j]) for j in range(r,len(p),q)) for p in low for r in range(q))
        max_h=max(max(map(abs,p)) for p in polys)
        assert max_slice == 4, (q,max_slice)
        assert max_h == 4, (q,max_h)
        base=mul([1]*4,[1]*(q*q))
        assert base[3]==4
        # The witness factorizes as Phi_2 Phi_4 Phi_q Phi_{q^2}.
        f=factors(q)
        witness=mul(mul(f[1],f[2]),mul(f[3],f[6]))
        assert witness==base
        print('q',q,'divisors',len(polys),'slice',max_slice,'height',max_h)
    print('VERIFY_OK')
if __name__=='__main__':main()
