#!/usr/bin/env python3
"""Exact GF(2) matrix checks for toggled incidence graphs of odd-block/even-lambda symmetric designs."""
from itertools import product

def bits_to_rows(B):
    return [sum(bit << j for j,bit in enumerate(row)) for row in B]

def mm(X,Y,n):
    cols=[sum(((Y[i]>>j)&1)<<i for i in range(n)) for j in range(n)]
    return [sum(((x & col).bit_count()&1)<<j for j,col in enumerate(cols)) for x in X]

def rank(rows,n):
    basis={}
    for row in rows:
        r=row
        while r:
            p=r.bit_length()-1
            if p in basis:r^=basis[p]
            else:basis[p]=r;break
    return len(basis)

def idm(n):return [1<<i for i in range(n)]
def powmat(M,e,n):
    ret=idm(n)
    while e:
        if e&1:ret=mm(ret,M,n)
        M=mm(M,M,n);e>>=1
    return ret

def mfix(M,d,n):return n-rank([x^y for x,y in zip(powmat(M,d,n),idm(n))],n)

def adjacency(B,i,j):
    n=len(B);M=[0]*(2*n)
    for x in range(n):
        for y in range(n):
            if B[x][y]^(x==i and y==j):
                M[x] |=1<<(n+y)
                M[n+y]|=1<<x
    return M

def cases():
    data=[('trivial_4', [[int(i!=j) for j in range(4)] for i in range(4)])]
    residues={1,3,4,5,9}
    data.append(('biplane_11',[[int((j-i)%11 in residues) for j in range(11)] for i in range(11)]))
    for name,B in data:
        n=len(B);R=bits_to_rows(B)
        assert mm(R,[sum(B[i][j]<<i for i in range(n)) for j in range(n)],n)==idm(n)
        assert all(sum(row)%2==1 for row in B)
        checked=0
        for i,j in product(range(n),repeat=2):
            M=adjacency(B,i,j);N=2*n
            r1,r2=rank(M,N),rank(mm(M,M,N),N)
            if B[i][j]:
                assert r1==2*n-2 and r2==2*n-2,(name,i,j,'rank delete',r1,r2)
                assert powmat(M,5,N)==M,(name,i,j,'period2')
                assert powmat(M,3,N)!=M,(name,i,j,'sharp')
                assert [mfix(M,d,N) for d in (1,2,4)]==[n-2,2*n-4,2*n-2],(name,i,j,'fixed')
            else:
                assert r1==2*n and r2==2*n,(name,i,j,'rank insert')
                assert powmat(M,6,N)==idm(N),(name,i,j,'period6')
                assert [mfix(M,d,N) for d in (1,2,3,6)]==[n-2,2*n-4,n,2*n],(name,i,j,'fixed')
            checked+=1
        print(name,'n',n,'toggle_count',checked,'all_verified',True)
    for name,B in data:
        if len(B)>4:continue
        n=len(B)
        for kind in ('delete','insert'):
            i=0;j=next(j for j in range(n) if B[i][j]==int(kind=='delete'))
            M=adjacency(B,i,j);N=2*n
            def adv(state):
                return sum(((row&state).bit_count()%2)<<v for v,row in enumerate(M))
            cycles={1:0,2:0,3:0,4:0,6:0}; transient={0:0,1:0,2:0}
            for s in range(1<<N):
                past={};cur=s;step=0
                while cur not in past:
                    past[cur]=step;step+=1;cur=adv(cur)
                t=past[cur];p=step-t
                assert p in cycles and t in transient
                transient[t]+=1
                if t==0:cycles[p]+=1
            q=2
            if kind=='insert':
                expected={1:q**(n-2), 2:q**(2*n-4)-q**(n-2), 3:q**n-q**(n-2),4:0,6:q**(2*n)-q**(2*n-4)-q**n+q**(n-2)}
                assert cycles==expected,(cycles,expected)
                assert transient=={0:2**(2*n),1:0,2:0}
            else:
                expected={1:q**(n-2),2:q**(2*n-4)-q**(n-2),3:0,4:q**(2*n-2)-q**(2*n-4),6:0}
                assert cycles==expected,(cycles,expected)
                assert transient=={0:q**(2*n-2),1:q**(2*n)-q**(2*n-2),2:0}
            print('exhaustive',name,kind,'periodic_point_counts',cycles,'first_entry',transient)
if __name__=='__main__':cases()
