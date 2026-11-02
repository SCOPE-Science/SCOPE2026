import numpy as np

def exact_formula(n):
    assert n>=3
    numer=4*n-(4 if n%2==0 else 2)+8*int(n%4==0)+8*int(n%6==0)
    return numer/(4*n*n)

def numerical_multiplicity(n):
    eigs=[]
    for k in range(n):
        for s in (-1,1):
            eigs.append(2*np.cos(2*np.pi*k/n)+s)
    eigs=sorted(eigs)
    bins=[]
    for e in eigs:
        if bins and abs(e-bins[-1][0])<1e-9: bins[-1][1]+=1
        else: bins.append([e,1])
    return sum(m*m for _,m in bins)/(4*n*n)

def diagonalization(n):
    A=np.zeros((2*n,2*n))
    for k in range(n):
        for s in range(2):
            u=2*k+s;v=2*((k+1)%n)+s
            A[u,v]=A[v,u]=1
        A[2*k,2*k+1]=A[2*k+1,2*k]=1
    eig=np.linalg.eigvalsh(A)
    bins=[]
    for e in eig:
        if bins and abs(e-bins[-1][0])<1e-8: bins[-1][1]+=1
        else: bins.append([e,1])
    return sum(m*m for _,m in bins)/(4*n*n)

for n in range(3,601):
    x=exact_formula(n); y=numerical_multiplicity(n)
    assert abs(x-y)<1e-12,(n,x,y)
for n in range(3,51):
    x=exact_formula(n); z=diagonalization(n)
    assert abs(x-z)<1e-12,(n,x,z)
print('PASS', 598,'spectral multiplicity cases',48,'independent adjacency diagonalizations')
for n in (3,4,5,6,8,10,12,15,18,24,60):print(n,exact_formula(n))
