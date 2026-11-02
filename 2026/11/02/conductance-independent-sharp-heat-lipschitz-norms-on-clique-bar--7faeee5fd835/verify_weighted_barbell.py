#!/usr/bin/env python3
"""Reproducible exact intertwining and independent finite heat checks.
Only standard-library arithmetic. Numerical checks support, not replace, the proof.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext, getcontext
getcontext().prec = 72

def graph(m, seed):
    n=2*m
    edges=[]
    for start in [0,m]:
        for j in range(1,m): edges.append((start,start+j,F(1)))
        for i in range(1,m):
            for j in range(i+1,m):
                c=F(1)+F(((7*i+11*j+3*seed)%17),3)
                edges.append((start+i,start+j,c))
    edges.append((0,m,F(1)))
    return n,edges

def matvec_negL(n,edges,f):
    out=[F(0) for _ in range(n)]
    for x,y,c in edges:
        z=c*(f[y]-f[x]);out[x]+=z;out[y]-=z
    return out

def grad(m,f):
    return [f[i]-f[0] for i in range(1,m)]+[f[m]-f[m+j] for j in range(1,m)]+[f[0]-f[m]]

def grad_system(m,edges,g):
    k=m-1
    z=g[-1]
    v=[-m*g[i]+z for i in range(2*k)]+[sum(g[:-1])-2*z]
    for i,j,c in edges:
        if i==0 or j==0 or i==m or j==m: continue
        if i<m:
            a,b=i-1,j-1
        else:
            a,b=k+i-m-1,k+j-m-1
        v[a]+=(c-1)*(g[b]-g[a])
        v[b]+=(c-1)*(g[a]-g[b])
    return v

def d(x):return Decimal(x.numerator)/Decimal(x.denominator)

def heat(n,edges,t,f):
    with localcontext() as ctx:
        ctx.prec=72
        sums=[Decimal(0)]*n
        degrees=[F(0)]*n
        for i,j,c in edges: degrees[i]+=c;degrees[j]+=c
        q=max(1,max(degrees))
        rq=d(q)
        steps=[[(i,Decimal(1)-d(degrees[i])/rq)] for i in range(n)]
        for i,j,c in edges:
            val=d(c)/rq;steps[i].append((j,val));steps[j].append((i,val))
        cur=[d(x) for x in f]
        weight=(-rq*t).exp()
        for order in range(185):
            for i in range(n): sums[i]+=weight*cur[i]
            nxt=[sum((p*cur[j] for j,p in row),Decimal(0)) for row in steps]
            cur=nxt
            weight=weight*rq*t/Decimal(order+1)
        assert weight<Decimal('1e-52'),(n,t,weight)
        return sums

def expected(m,t):
    with localcontext() as ctx:
        ctx.prec=72
        M=Decimal(m)
        delta=((M+2)**2-8).sqrt()
        alpha=(M+2-delta)/2
        beta=(M+2+delta)/2
        A=(3*M-2-alpha)/delta
        B=(3*M-2-beta)/delta
        return A*(-alpha*t).exp()-B*(-beta*t).exp()

def main():
    total_cases=0; total_lap=0; total_heat=0
    for m in range(2,7):
        for seed in range(3):
            n,edges=graph(m,seed)
            for basis in range(n):
                f=[F(int(i==basis)) for i in range(n)]
                assert grad(m,matvec_negL(n,edges,f))==grad_system(m,edges,grad(m,f))
                total_lap+=1
            f=[F(2)]*m+[F(-1)]*m
            f[0]=F(1);f[m]=F(0)
            assert all(abs(x)==1 for x in grad(m,f))
            for ts in ['0.03125','0.17','0.6']:
                t=Decimal(ts)
                result=heat(n,edges,t,f)
                b=result[0]-result[m]
                err=abs(b-expected(m,t))
                assert err<Decimal('3e-42'),(m,seed,ts,err)
                all_grads=grad(m,result)
                assert all(abs(q)<=b+Decimal('1e-42') for q in all_grads),(m,seed,ts)
                assert all(abs(q)<b-Decimal('1e-26') for q in all_grads[:-1]),(m,seed,ts)
                total_heat+=1
            total_cases+=1
    with localcontext() as ctx:
        ctx.prec=72
        for m in (3,4,10,100,1000):
            M=Decimal(m);D=((M+2)**2-8).sqrt()
            a=(M+2-D)/2;b=(M+2+D)/2
            A=(3*M-2-a)/D;B=A-1
            peak=(b*B/(a*A)).ln()/D
            val=expected(m,peak)
            assert val>1 and val<3
        assert abs(expected(1000,Decimal(0))-1)<Decimal('1e-60')
    print(f'CHECK_OK exact_gradient_intertwining_basis={total_lap} weighted_graphs={total_cases} independent_heat_edge_comparisons={total_heat} root_asymptotic_cases=5')

if __name__=='__main__':main()
