"""Finite reproducibility checks for square-torus cut and cycle projectors.
No third-party dependencies. This checks finite instances only, not the asymptotic proof.
"""
from fractions import Fraction as F
from math import cos, sin, pi, log, sqrt
from cmath import exp


def solve(A, rhs):
    n = len(A)
    M = [[F(v) for v in A[i]] + [F(rhs[i])] for i in range(n)]
    for i in range(n):
        j = next(j for j in range(i,n) if M[j][i])
        M[i], M[j] = M[j], M[i]
        p=M[i][i]
        M[i] = [t/p for t in M[i]]
        for j in range(n):
            if j!=i and M[j][i]:
                p=M[j][i]
                M[j] = [u-p*v for u,v in zip(M[j],M[i])]
    return [row[-1] for row in M]


def exact_norms(n):
    N=n*n
    edges=[]
    for x in range(n):
        for y in range(n):
            v=n*x+y
            edges += [(v,n*((x+1)%n)+y), (v,n*x+(y+1)%n)]
    assert len(set(tuple(sorted(e)) for e in edges)) == 2*N
    L=[[0]*N for _ in range(N)]
    for u,v in edges:
        L[u][u]+=1; L[v][v]+=1;L[u][v]-=1;L[v][u]-=1
    A=[row[:-1] for row in L[:-1]]
    qcols=[]; ccols=[]
    for u,v in edges:
        b=[F((i==u)-(i==v)) for i in range(N-1)]
        potential=solve(A,b)+[F(0)]
        q=[potential[a]-potential[b] for a,b in edges]
        own=edges.index((u,v))
        assert q[own]==F(N-1,2*N)
        qcols.append(sum(abs(x) for x in q))
        ccols.append(sum(abs(F(j==own)-q[j]) for j in range(2*N)))
    assert len(set(qcols))==1 and len(set(ccols))==1
    assert ccols[0]-qcols[0]==F(1,N)
    return qcols[0], ccols[0]


def fourier_norm(n):
    k=[2*pi*j/n for j in range(n)]
    E=[complex(cos(t),sin(t))-1 for t in k]
    modes=[]
    for a in range(n):
        for b in range(n):
            if a==b==0:continue
            den=(E[a].real**2+E[a].imag**2)+(E[b].real**2+E[b].imag**2)
            modes.append((a,b,(E[a].conjugate()*E[a])/den,
                             (E[b].conjugate()*E[a])/den))
    root=[complex(cos(t),sin(t)) for t in k]
    norm=0.0
    for x in range(n):
        for y in range(n):
            xx=0j;xy=0j
            for a,b,aa,ab in modes:
                phase=root[(a*x+b*y)%n]
                xx+=aa*phase;xy+=ab*phase
            norm+=(abs(xx.real)+abs(xy.real))/(n*n)
    return norm


def main():
    pairs=[]
    for n in range(3,7):
        q,c=exact_norms(n)
        value=fourier_norm(n)
        assert abs(value-float(q))<2e-10,(n,value,q)
        pairs.append((n,str(q),str(c)))
    print('PASS exact rational all columns n=3..6',pairs)
    for n in (8,12,16,24,32):
        val=fourier_norm(n)
        print('Fourier n=%d norm=%.12f remainder=%.12f'%(n,val,val-4/pi*log(n)))
    print('PASS finite cross-representation checks; infinity relies on analytical argument')
if __name__=='__main__':main()
