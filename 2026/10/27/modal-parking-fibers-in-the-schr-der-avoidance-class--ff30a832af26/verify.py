"""Independent finite checks for the modal fiber theorem in Av(1234,2134).
Run: python3 verify.py . No third-party modules required.
"""
from itertools import combinations, permutations, product
from collections import Counter

def avoids(p):
    n=len(p)
    for i,j,k,t in combinations(range(n),4):
        if p[k]>max(p[i],p[j]) and p[t]>p[k]:
            return False
    return True

def fiber(p):
    prod=1
    for i,x in enumerate(p):
        j=i-1
        while j>=0 and p[j]<x:
            j-=1
        prod*=i-j
    return prod

def outcome(prefs):
    n=len(prefs)
    parked=[0]*n
    for car,requested in enumerate(prefs,1):
        j=requested-1
        while j<n and parked[j]:
            j+=1
        if j>=n:return None
        parked[j]=car
    return tuple(parked)

def close_form(n):
    base={0:1,1:1,2:2,3:6,4:8,5:20,6:36,7:56}
    if n<=7:return base[n]
    a=max(k for k in range(n//5+1) if (n-5*k)%3==0)
    b=(n-5*a)//3
    return 20**a*6**b

def main():
    expected=[1,1,2,6,8,20,36,56,120,216]
    assert all(close_form(n)==expected[n] for n in range(10))
    for n in range(1,10):
        best=0
        count=0
        witness=None
        for p in permutations(range(1,n+1)):
            if avoids(p):
                count+=1
                w=fiber(p)
                if w>best:
                    best=w;witness=p
        assert best==close_form(n),(n,best,close_form(n))
        print('enumeration',n,count,best,witness)
    for n in range(1,6):
        histogram=Counter()
        for alpha in product(range(1,n+1),repeat=n):
            p=outcome(alpha)
            if p is not None:
                histogram[p]+=1
        assert sum(histogram.values())==(n+1)**(n-1)
        assert all(v==fiber(p) for p,v in histogram.items())
        assert max((v for p,v in histogram.items() if avoids(p)))==close_form(n)
        print('physical_parking',n,(n+1)**(n-1),'fiber_product_agrees')
    M=[1]
    for n in range(1,151):
        value=max(j*2**((j-1)//2)*M[n-j] for j in range(1,n+1))
        assert value==close_form(n),(n,value,close_form(n))
        M.append(value)
    for n in range(8,146):
        assert M[n+5]==20*M[n]
    for j in range(8,151):
        w=lambda k:k*2**((k-1)//2)
        assert w(j)<w(5)*w(j-5)
    print('recurrence_and_eventual_5_step_growth_checked_to_n=150')
    print('VERIFY_OK')

if __name__=='__main__':main()
