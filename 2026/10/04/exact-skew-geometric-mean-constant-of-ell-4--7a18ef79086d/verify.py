from collections import defaultdict

def add(*ps):
    out=defaultdict(int)
    for p in ps:
        for k,v in p.items(): out[k]+=v
    return {k:v for k,v in out.items() if v}

def scale(p,c): return {k:c*v for k,v in p.items() if c*v}
def mul(p,q):
    out=defaultdict(int)
    for (i,j),u in p.items():
        for (k,l),v in q.items(): out[(i+k,j+l)]+=u*v
    return {k:v for k,v in out.items() if v}
def powp(p,n):
    r={(0,0):1}
    for _ in range(n): r=mul(r,p)
    return r
A={(1,0):1}; B={(0,1):1}
a2=powp(A,2); b2=powp(B,2); a4=powp(A,4); b4=powp(B,4)
c=add(a2,b2); d=add(a2,scale(b2,-1)); ab=mul(A,B)
A11=add(powp(c,2),powp(d,2))
A12=scale(mul(ab,d),2)
A22=add(powp(c,2),scale(powp(ab,2),4))
# det((Q)-lambda*diag(2,1)) = 2*(lambda^2 - 2H lambda + c^4).
# Check the constant and linear coefficients symbolically.
const=add(mul(A11,A22),scale(powp(A12,2),-1))
H=add(a4,scale(mul(a2,b2),3),b4)
assert const == scale(powp(c,4),2)
linear=add(scale(A11,-1),scale(A22,-2))
assert linear == scale(H,-4)
# Check H^2-c^4 = a^2 b^2(a^2+2b^2)(2a^2+b^2).
lhs=add(powp(H,2),scale(powp(c,4),-1))
rhs=mul(mul(a2,b2),mul(add(a2,scale(b2,2)),add(scale(a2,2),b2)))
assert lhs==rhs
print('VERIFY_OK')
