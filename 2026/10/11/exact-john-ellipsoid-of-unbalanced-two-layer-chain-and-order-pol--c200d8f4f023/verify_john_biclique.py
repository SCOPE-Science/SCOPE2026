"""Reproduce facet contacts and John optimality matrices for biclique chain polytopes.

The general theorem is algebraic; these finite checks are corroboration only.
Run: python3 verify_john_biclique.py   (requires numpy)
"""
import math
from fractions import Fraction
import numpy as np


def quantities(a, b):
    d = a + b
    delta = (b - a) / d
    s = math.sqrt((2*d - (d+1)*delta**2) / (d-1))
    p, q = (s-delta)/2, (s+delta)/2
    H = 1+p+q
    u, v, w = p/H, q/H, 1/H
    A, B = b*(1+1/p), a*(1+1/q)
    K = np.diag([A]*a + [B]*b)
    K[:a, a:] = K[a:, :a] = 1.0
    gamma = d/(a*b*H)
    Sigma = a*b/(d*H)*np.linalg.inv(K)
    return p,q,H,u,v,w,gamma,K,Sigma,A,B


def test_numeric(a,b):
    d = a+b
    p,q,H,u,v,w,gamma,K,Sigma,A,B = quantities(a,b)
    assert min(p,q,u,v,w,gamma)>0
    assert min(np.linalg.eigvalsh(Sigma))>0
    assert abs((q-p)-(b-a)/d)<1e-11
    assert abs(d*(p*p+q*q)-2*p*q-d)<1e-10
    normals=[]; slacks=[]; weights=[]
    for i in range(a):
        z=np.zeros(d);z[i]=-1
        normals.append(z); slacks.append(u);weights.append(gamma*b*p)
    for j in range(b):
        z=np.zeros(d);z[a+j]=-1
        normals.append(z); slacks.append(v);weights.append(gamma*a*q)
    for i in range(a):
        for j in range(b):
            z=np.zeros(d);z[i]=z[a+j]=1
            normals.append(z);slacks.append(w);weights.append(gamma)
    normals=np.array(normals);slacks=np.array(slacks);weights=np.array(weights)
    assert len(normals)==a+b+a*b
    assert np.max(np.abs(np.einsum('ni,ij,nj->n',normals,Sigma,normals)-slacks**2))<1e-10
    assert np.linalg.norm((weights/slacks)@normals,ord=np.inf)<1e-10
    dual=(normals.T*(weights/slacks**2))@normals
    assert np.linalg.norm(dual@Sigma-np.eye(d),ord=np.inf)<1e-9
    assert abs(sum(weights)-d)<1e-10
    lam=[A]*(a-1)+[B]*(b-1)+[(A+B+math.sqrt((A-B)**2+4*a*b))/2,(A+B-math.sqrt((A-B)**2+4*a*b))/2]
    eig=np.sort((a*b/(d*H))/np.array(lam))
    assert np.max(np.abs(eig-np.linalg.eigvalsh(Sigma)))<1e-10
    det_from_spectrum=(a*b/(d*H))**d/(A**(a-1)*B**(b-1)*(A*B-a*b))
    assert abs(np.linalg.det(Sigma)/det_from_spectrum-1)<1e-10
    return len(normals)


def inverse_fraction(M):
    n=len(M)
    T=[[Fraction(M[i][j]) for j in range(n)]+[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
    for col in range(n):
        piv=next(i for i in range(col,n) if T[i][col])
        T[col],T[piv]=T[piv],T[col]
        fac=T[col][col]
        T[col]=[x/fac for x in T[col]]
        for i in range(n):
            if i!=col and T[i][col]:
                fac=T[i][col]
                T[i]=[x-fac*y for x,y in zip(T[i],T[col])]
    return [r[n:] for r in T]


def test_exact_star(b):
    a,d=1,1+b
    p,q=Fraction(2,b+1),Fraction(1)
    H=1+p+q
    u,v,w=p/H,q/H,1/H
    A,B=b*(1+1/p),a*(1+1/q)
    K=[[Fraction(0) for j in range(d)] for i in range(d)]
    for i in range(d):K[i][i]=A if i<a else B
    for i in range(a):
        for j in range(a,d):K[i][j]=K[j][i]=1
    Ki=inverse_fraction(K)
    Sigma=[[Fraction(a*b,d*H)*Ki[i][j] for j in range(d)] for i in range(d)]
    gamma=Fraction(d,a*b*H)
    normals=[];slacks=[];weights=[]
    for i in range(a):
        n=[Fraction(-int(j==i)) for j in range(d)]
        normals.append(n);slacks.append(u);weights.append(gamma*b*p)
    for i in range(b):
        n=[Fraction(-int(j==a+i)) for j in range(d)]
        normals.append(n);slacks.append(v);weights.append(gamma*a*q)
    for i in range(a):
        for j in range(b):
            n=[Fraction(int(k==i or k==a+j)) for k in range(d)]
            normals.append(n);slacks.append(w);weights.append(gamma)
    assert sum(weights)==d
    for n,h in zip(normals,slacks):
        assert sum(n[i]*Sigma[i][j]*n[j] for i in range(d) for j in range(d))==h*h
    for i in range(d):
        assert sum(weights[z]*normals[z][i]/slacks[z] for z in range(len(normals)))==0
        for j in range(d):
            dual=sum(weights[z]*normals[z][i]*normals[z][j]/slacks[z]**2 for z in range(len(normals)))
            assert dual==K[i][j]*gamma/w**2
    return len(normals)


def main():
    cases=contacts=0
    for a in range(1,14):
        for b in range(1,14):
            contacts+=test_numeric(a,b)
            cases+=1
    exact=sum(test_exact_star(b) for b in range(1,13))
    print('OK: %d numeric dimension pairs, %d facet contacts, 12 rational star instances, %d exact rational contacts' % (cases,contacts,exact))

if __name__=='__main__':main()
