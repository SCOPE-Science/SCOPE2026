#!/usr/bin/env python3
"""Exact generator identity and rational witness checks for a locally-resetting particle network."""
from fractions import Fraction as Q
from itertools import product


def make_rates(k):
    fitness = [Q(i + 1, k) for i in range(k)]
    death, hop = Q(1,5), Q(1,10)
    reset = [Q(4,5) + Q(i,10) for i in range(k)]
    return fitness, death, hop, reset


def pairs(k):
    return [(i,j) for i in range(k) for j in range(i,k)]


def basis(n, i, j):
    return n[i] * (n[i]-1) if i==j else n[i]*n[j]


def generator(n, f, fitness, death, hop, reset):
    k=len(n)
    total=Q(0)
    for i in range(k):
        nplus=list(n);nplus[i]+=1
        total += fitness[i]*(n[i]+1)*(f(nplus)-f(n))
        if n[i]:
            nminus=list(n);nminus[i]-=1
            total+=death*n[i]*(f(nminus)-f(n))
            for j in range(k):
                if i!=j:
                    nmove=list(n);nmove[i]-=1;nmove[j]+=1
                    total+=hop*n[i]/(k-1)*(f(nmove)-f(n))
            nreset=list(n);nreset[i]=0
            total+=reset[i]*(f(nreset)-f(n))
    return total


def B_matrix(fitness,death,hop,reset):
    k=len(fitness)
    return [[fitness[i]-death-hop-reset[i] if i==j else hop/(k-1) for j in range(k)] for i in range(k)]


def H_entry_formula(n,i,j,fitness,death,hop,reset):
    k=len(n)
    if i==j:
        return ((2*(fitness[i]-death-hop)-reset[i])*basis(n,i,i)
                +2*hop/(k-1)*sum(basis(n,min(i,t),max(i,t)) for t in range(k) if t!=i)
                +4*fitness[i]*n[i])
    return ((fitness[i]+fitness[j]-2*(death+hop)-reset[i]-reset[j])*basis(n,i,j)
            +hop/(k-1)*(basis(n,i,i)+basis(n,j,j)
                +sum(basis(n,min(i,t),max(i,t))+basis(n,min(j,t),max(j,t))
                     for t in range(k) if t not in (i,j)))
            +fitness[i]*n[j]+fitness[j]*n[i])


def mean_formula(n,i,fitness,death,hop,reset):
    B=B_matrix(fitness,death,hop,reset)
    return fitness[i]+sum(B[i][j]*n[j] for j in range(len(n)))


def run():
    checks=0
    for k, limit in ((2,5),(3,4),(4,3)):
        fitness, death, hop, reset=make_rates(k)
        for n in product(range(limit), repeat=k):
            for i in range(k):
                got=generator(n,lambda z,i=i: z[i],fitness,death,hop,reset)
                expected=mean_formula(n,i,fitness,death,hop,reset)
                assert got==expected,(k,n,i,got,expected)
                checks+=1
            for i,j in pairs(k):
                got=generator(n,lambda z,i=i,j=j:basis(z,i,j),fitness,death,hop,reset)
                expected=H_entry_formula(n,i,j,fitness,death,hop,reset)
                assert got==expected,(k,n,i,j,got,expected)
                checks+=1
    l=[Q(1),Q(1,5)];death=Q(1,5);hop=Q(1,10);r=[Q(4,5),Q(1)]
    B=B_matrix(l,death,hop,r)
    assert B==[[Q(-1,10),Q(1,10)],[Q(1,10),Q(-11,10)]]
    checks+=1
    mean=[Q(56,5),Q(6,5)]
    assert [sum(B[i][j]*mean[j] for j in range(2))+l[i] for i in range(2)]==[0,0]
    checks+=1
    assert B[0][0]+B[1][1]==Q(-6,5)
    assert B[0][0]*B[1][1]-B[0][1]*B[1][0]==Q(1,10)
    checks+=2
    lamb=l[0]-death-hop
    assert lamb==Q(7,10) and lamb<r[0]<2*lamb
    checks+=1
    H11=2*(l[0]-death-hop)-r[0]
    assert H11==Q(3,5)>0
    checks+=1
    print(f"PASS {checks} exact generator, spectral witness, and moment-gap checks")
    print("B =", B, "; stationary means =",mean,"; first-site intrinsic growth =",lamb)
    print("First-site quadratic drift coefficient =",H11,"; hence H has positive spectral bound")

if __name__=='__main__':run()
