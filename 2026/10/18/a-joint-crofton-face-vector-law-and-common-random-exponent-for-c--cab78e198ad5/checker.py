"""Reproducible finite checks for Crofton sections of regular cross-polytopes.
Uses only Python standard library. All infinite-dimensional assertions require the proof."""
import math,random,itertools
from math import comb

def positive_normal_tail(s):
    return math.erfc(s/math.sqrt(2.0))

def integrate(f,T=12.0,steps=30000):
    # Composite Simpson integration; uniform mesh on [0,T].
    if steps%2: steps+=1
    h=T/steps
    val=f(0.0)+f(T)
    for z in range(1,steps):
        val+=(4 if z%2 else 2)*f(h*z)
    return h*val/3

def mean_max_abs(n):
    return integrate(lambda s: 1-(1-positive_normal_tail(s))**n)

def mean_max_gaussians(r):
    return integrate(lambda s: 1-(1-positive_normal_tail(s)/2)**r-(positive_normal_tail(s)/2)**r)

def level_law(n):
    den=mean_max_abs(n)
    p=[0.0]+[comb(n,k)*integrate(lambda s,k=k: positive_normal_tail(s)**k*(1-positive_normal_tail(s))**(n-k))/den for k in range(1,n+1)]
    return p

def predicted_face_vector(n,k):
    ans=[]
    for r in range(2,n+1):
        low=sum(comb(k,a)*comb(n-k,r-a)*2**(r-a) for a in range(max(0,r-(n-k)),min(k,r)+1))
        ans.append(2**r*comb(n,r)-comb(k,r) if k>=r else 2**r*comb(n,r))
        ans[-1]-=low
    return ans

def brute_face_vector(g,s):
    n=len(g)
    vec=[]
    for r in range(2,n+1):
        count=0
        for idx in itertools.combinations(range(n),r):
            for signs in itertools.product([-1,+1],repeat=r):
                vals=[g[i]*e for i,e in zip(idx,signs)]
                if min(vals)<s<max(vals):count+=1
        vec.append(count)
    return vec

def main():
    random.seed(192026)
    tests=0
    for n in range(2,9):
        pmf=level_law(n)
        assert abs(sum(pmf)-1)<2e-7,(n,sum(pmf))
        for k in range(1,n+1):
            vec=predicted_face_vector(n,k)
            assert vec[0]==k*(2*n-k-1),(n,k,vec)
        expect_faces=[sum(pmf[k]*predicted_face_vector(n,k)[j] for k in range(1,n+1)) for j in range(n-1)]
        want_faces=[2**(j+2)*comb(n,j+2)*mean_max_gaussians(j+2)/mean_max_abs(n) for j in range(n-1)]
        for x,y in zip(expect_faces,want_faces):
            assert abs(x-y)<2e-7,(n,x,y)
        for _ in range(12):
            g=[random.gauss(0,1) for i in range(n)]
            s=random.uniform(-max(map(abs,g)), max(map(abs,g)))
            k=sum(abs(x)>abs(s) for x in g)
            got=brute_face_vector(g,s)
            want=predicted_face_vector(n,k)
            assert got==want,(n,k,s,got,want)
            tests+=1
        if n<=5:
            print('n=',n,'pK=',[round(x,7) for x in pmf[1:]],'E(f_0)=',round(expect_faces[0],7))
    print('PASS:',tests,'direct face enumerations and 7 integrated exact distributions/expectations')
    for n in (5000,50000):
        rng=random.Random(n)
        exponents=[]
        for _ in range(1000):
            g=[rng.gauss(0,1) for __ in range(n)]
            M=max(map(abs,g));s=rng.random()*M
            k=sum(abs(x)>s for x in g)
            v=k*(2*n-k-1)
            exponents.append(math.log(v)/math.log(n))
        print('illustrative, unweighted samples n=',n,'mean log exponent=',round(sum(exponents)/len(exponents),5))
    print('Finite checks are not proof of asymptotics.')
if __name__=='__main__':main()
