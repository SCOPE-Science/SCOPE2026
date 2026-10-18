from itertools import permutations
from math import lcm

def compose(a,b): return tuple(a[b[i]] for i in range(len(a)))
def power(a,e):
    b=tuple(range(len(a)))
    while e:
        if e&1:b=compose(b,a)
        a=compose(a,a);e>>=1
    return b

def smallcriterion(r,s,n):
    if n<=2:return False
    if n==3:return bool((r%2 and s%2) or (r%2 and s%2==0 and s%3) or (s%2 and r%2==0 and r%3))
    if n==4:return r%12!=0 and s%12!=0 and not(r%6==0 and s%6==0)
    L=1
    for k in range(1,n+1):L=lcm(L,k)
    return r%L!=0 and s%L!=0

def group_test(n,r,s):
    ps=list(permutations(range(n)))
    pp=set(power(x,r) for x in ps)
    qq=set(power(x,s) for x in ps)
    return any(compose(x,y)!=compose(y,x) for x in pp for y in qq)
for n in range(1,7):
    for r in range(1,33):
        for s in range(1,33):
            got=group_test(n,r,s)
            want=smallcriterion(r,s,n)
            if got!=want:raise AssertionError((n,r,s,got,want))
    print(n,'passed 1024 exponent pairs')
print('ALL CASES PASS')
