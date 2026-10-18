#!/usr/bin/env python3
"""Standalone arithmetic test for adjoint-rank census of UT_3(F_q[epsilon]/epsilon^2).
Independent rank computation on block k-linear commutator maps.
"""
import itertools,collections

def gf_rank(mat,q):
    m=[row[:] for row in mat]; nrows=len(m); ncols=len(m[0]); p=0
    for c in range(ncols):
        i=next((i for i in range(p,nrows) if m[i][c]%q),None)
        if i is None:continue
        m[p],m[i]=m[i],m[p]
        inv=pow(m[p][c],-1,q)
        m[p]=[(z*inv)%q for z in m[p]]
        for j in range(p+1,nrows):
            if (v:=m[j][c]):
                m[j]=[(z-v*y)%q for z,y in zip(m[j],m[p])]
        p+=1
        if p==nrows:break
    return p

def mtx(a,b,u,v,w):
    return [[a,0,0,-u,0], [0,b,0,0,-v], [-v,u,a+b,-w,-w]]

def direct(q):
    tally=collections.Counter()
    for z in itertools.product(range(q),repeat=10):
        a,b,u,v,w=z[:5]; A,B,U,V,W=z[5:]
        m0=mtx(a,b,u,v,w); m1=mtx(A,B,U,V,W)
        full=[[(a%q) for a in row]+[0]*5 for row in m0]
        full += [[(a%q) for a in row]+[(b%q) for b in row1] for row,row1 in zip(m1,m0)]
        tally[gf_rank(full,q)]+=1
    return {j:q*q*tally[j] for j in range(7)}

def predicted(q):
    return [q**2,q**2*(q-1),3*q**3*(q-1)*(q+1),q**3*(q-1)*(q**3+4*q**2-4*q-2),q**4*(q-1)*(6*q**3-3*q+2),q**7*(q-1)**2*(3*q+5),q**8*(q-1)*(q**3+q**2-2*q-1)]

if __name__=='__main__':
    for q in (2,3):
        data=direct(q); expected=predicted(q)
        print('q',q,'measured',data,'predicted',expected)
        assert [data[i] for i in range(7)]==expected,(q,data,expected)
        assert sum(expected)==q**12
    print('VERIFY_UT3_DUAL_OK')
