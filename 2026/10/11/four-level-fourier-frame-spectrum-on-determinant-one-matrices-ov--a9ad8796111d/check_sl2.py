#!/usr/bin/env python3
"""Independent small-field tests of a Fourier restriction spectrum on SL_2.

Dependency: NumPy. This script does not establish the universal theorem.
"""
import cmath
import itertools
import math
import numpy as np

# Field elements are base-p coefficient tuples encoded as integers.
# Each modulus is monic, in ascending coefficient order.
FIELDS = [(2, [0, 1]), (3, [0, 1]), (5, [0, 1]),
          (7, [0, 1]), (11, [0, 1]),
          (2, [1, 1, 1]), (2, [1, 1, 0, 1]),
          (3, [1, 0, 1])]


def make_field(p, modulus):
    degree = len(modulus) - 1
    q = p ** degree
    def digits(a):
        return [(a // p**j) % p for j in range(degree)]
    vec = [digits(a) for a in range(q)]
    def encode(v):
        return sum((w % p) * p**j for j, w in enumerate(v))
    add = [[encode([(vec[a][i] + vec[b][i]) % p for i in range(degree)])
            for b in range(q)] for a in range(q)]
    neg = [encode([(-vec[a][i]) % p for i in range(degree)]) for a in range(q)]
    mul = [[0]*q for _ in range(q)]
    for a in range(q):
        for b in range(q):
            coeff = [0]*(2*degree-1)
            for i, aa in enumerate(vec[a]):
                for j, bb in enumerate(vec[b]):
                    coeff[i+j] = (coeff[i+j]+aa*bb) % p
            for k in range(2*degree-2, degree-1, -1):
                if coeff[k]:
                    factor=coeff[k]
                    for j in range(degree):
                        coeff[k-degree+j]=(coeff[k-degree+j]-factor*modulus[j])%p
                    coeff[k]=0
            mul[a][b]=encode(coeff[:degree])
    def powf(a, m):
        out=1
        while m:
            if m&1:out=mul[out][a]
            a=mul[a][a]
            m//=2
        return out
    trace=[]
    for x in range(q):
        r=x;z=x
        for _ in range(1, degree):
            z=powf(z,p);r=add[r][z]
        # Fp embed agrees with 0,...,p-1 under the encoding.
        assert r<p, (p,modulus,x,r)
        trace.append(r)
    psi=np.array([cmath.exp(2j*math.pi*trace[x]/p) for x in range(q)])
    return q,add,neg,mul,psi


def check_field(p,modulus):
    q,add,neg,mul,psi=make_field(p,modulus)
    sub=lambda x,y:add[x][neg[y]]
    group=[(a,b,c,d) for a,b,c,d in itertools.product(range(q),repeat=4)
           if sub(mul[a][d],mul[b][c])==1]
    assert len(group)==q*(q*q-1)
    F=np.empty((len(group),1+4*(q-1)),dtype=complex)
    F[:,0]=1
    for j,matrix in enumerate(group):
        for i in range(4):
            for u in range(1,q):
                F[j,1+i*(q-1)+(u-1)]=psi[mul[u][matrix[i]]]
    gram=F.conj().T@F / len(group)
    assert np.max(np.abs(np.diag(gram)-1)) < 2e-12
    c=1/(q*q-1)
    delta=9*q*q-14*q+9
    root=(math.sqrt(delta))/(2*(q*q-1))
    mu0=1-(3*q-5)/(2*(q*q-1))
    low=mu0-root;high=mu0+root
    neg_eig=q/(q+1);pos_eig=q/(q-1)
    spectrum=sorted([low,high]+[neg_eig]*(2*q-2)+[pos_eig]*(2*q-3))
    numer=np.linalg.eigvalsh(gram)
    discrepancy=float(np.max(np.abs(numer-np.array(spectrum))))
    assert discrepancy < 3e-10,(q, discrepancy)
    # Check the universal Kloosterman matrix identity by enumerating the field.
    inv={a:next(b for b in range(1,q) if mul[a][b]==1) for a in range(1,q)}
    Kdict={}
    for sign in (1,-1):
        K=np.zeros((q-1,q-1),dtype=complex)
        for i,u in enumerate(range(1,q)):
            for j,v in enumerate(range(1,q)):
                K[i,j]=sum(psi[add[mul[u][z]][mul[(v if sign==1 else neg[v])][inv[z]]]] for z in range(1,q))
        Kdict[sign]=K
        J=np.ones((q-1,q-1))
        assert np.max(np.abs(K@K.conj().T-(q*q*np.eye(q-1)-(q+1)*J))) < 2e-10
        assert np.max(np.abs(K.sum(axis=0)-1)) < 2e-10
    model=np.empty_like(gram)
    model[0,0]=1
    for i in range(4):
        for u in range(1,q):
            ix=1+i*(q-1)+(u-1)
            model[0,ix]=model[ix,0]=-c
            for j in range(4):
                for v in range(1,q):
                    jx=1+j*(q-1)+(v-1)
                    if i==j:
                        model[ix,jx]=(1 if u==v else -c)
                    elif {i,j}=={0,3}:
                        model[ix,jx]=c*Kdict[-1][u-1,v-1]
                    elif {i,j}=={1,2}:
                        model[ix,jx]=c*Kdict[+1][u-1,v-1]
                    else:
                        model[ix,jx]=-c
    assert np.max(np.abs(gram-model)) < 5e-12,(q,np.max(np.abs(gram-model)))
    N=1+4*(q-1)
    m=[]
    for i in range(4):
        w=np.zeros(N,complex)
        w[1+i*(q-1):1+(i+1)*(q-1)]=1/math.sqrt(q-1)
        m.append(w)
    constant=np.zeros(N,complex);constant[0]=1
    v_uniform=sum(m)/2
    eigen_checks=[((m[0]-m[1]-m[2]+m[3])/2,pos_eig),
                  ((m[0]-m[3])/math.sqrt(2),neg_eig),
                  ((m[1]-m[2])/math.sqrt(2),neg_eig)]
    for mu in (low, high):
        eigen_checks.append((2*math.sqrt(q-1)*c*constant+(1-mu)*v_uniform,mu))
    for i,j,sgn in [(0,3,-1),(1,2,+1)]:
        for r in range(q-2):
            w=np.zeros(q-1,complex)
            w[r]=1;w[-1]=-1
            for sign,evalue in [(1,pos_eig),(-1,neg_eig)]:
                v=np.zeros(N,complex)
                v[1+i*(q-1):1+(i+1)*(q-1)]=w
                v[1+j*(q-1):1+(j+1)*(q-1)]=sign*Kdict[sgn]@w/q
                eigen_checks.append((v,evalue))
    assert len(eigen_checks)==N
    for v,evalue in eigen_checks:
        assert np.linalg.norm(gram@v-evalue*v)<4e-11,(q,evalue)
    assert 0 < low < neg_eig < high < pos_eig
    return q,len(group),F.shape[1],discrepancy


def main():
    info=[check_field(*spec) for spec in FIELDS]
    print('VERIFY_OK tested_fields='+repr([x[0] for x in info])+
          ' sampled_matrices='+str(sum(x[1] for x in info))+
          ' Fourier_columns='+str(sum(x[2] for x in info))+
          ' all_Kloosterman_unitarity=PASS all_Gram_entries=PASS all_equality_spaces=PASS all_Gram_spectra=PASS'+
          ' max_error='+format(max(x[3] for x in info),'.3g'))
if __name__=='__main__':
    main()
