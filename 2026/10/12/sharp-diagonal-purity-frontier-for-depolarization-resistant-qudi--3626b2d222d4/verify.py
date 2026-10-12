import math, random

def opt_m(d,s):
    assert d>=3 and 1/d-1e-12<=s<=1+1e-12
    if s<=.5:
        return (1+math.sqrt((d-2)*(d*s-1)/2))/d
    return math.sqrt(max(0,(1-s)/2))

def witness(d,s):
    if s<=.5:
        a=opt_m(d,s)
        return [a,a]+[max(0,(1-2*a)/(d-2))]*(d-2)
    t=math.sqrt(min(1,max(0,2*s-1)))
    return [(1+t)/2,(1-t)/2]+[0.0]*(d-2)

checks=0
for d in range(3,19):
 for j in range(101):
    s=1/d+(1-1/d)*j/100
    w=witness(d,s)
    assert abs(sum(w)-1)<1e-12
    assert abs(sum(x*x for x in w)-s)<1e-11
    m=max(math.sqrt(max(0,w[i]*w[j])) for i in range(d) for j in range(i+1,d))
    assert abs(m-opt_m(d,s))<1e-9
    checks+=1
for d in range(3,19):
 for j in range(400):
    x=[random.random()**2 for _ in range(d)]
    x=[t/sum(x) for t in x]
    s=sum(t*t for t in x)
    m=max(math.sqrt(x[i]*x[j]) for i in range(d) for j in range(i+1,d))
    assert m<=opt_m(d,s)+1e-10
    checks+=1
print('VERIFY_OK',checks)
