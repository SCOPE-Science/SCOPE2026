from itertools import product

def matmul(A,B,add,mul):
    a,b,c,d=A; e,f,g,h=B
    return (add(mul(a,e),mul(b,g)),add(mul(a,f),mul(b,h)),add(mul(c,e),mul(d,g)),add(mul(c,f),mul(d,h)))

def rank2_mod2(A,red):
    a,b,c,d=[red(x)&1 for x in A]
    if (a|b|c|d)==0: return 0
    return 2 if ((a*d)^(b*c)) else 1

def census(name,elems,add,mul,red):
    mats=list(product(elems,repeat=4)); byrank={0:0,1:0,2:0}; fibers={}
    for A in mats:
        found=False
        for X in mats:
            AX=matmul(A,X,add,mul); XA=matmul(X,A,add,mul)
            if AX!=XA: continue
            if matmul(AX,A,add,mul)!=A: continue
            if matmul(XA,X,add,mul)!=X: continue
            found=True; break
        if found:
            r=rank2_mod2(A,red); byrank[r]+=1
            key=tuple(red(x)&1 for x in A); fibers[key]=fibers.get(key,0)+1
    base=[]
    for A in product([0,1],repeat=4):
        r=rank2_mod2(A,lambda x:x)
        A2=matmul(A,A,lambda x,y:x^y,lambda x,y:x&y)
        if rank2_mod2(A2,lambda x:x)==r: base.append((A,r))
    assert len(base)==13
    for A,r in base:
        expected=2**(4-(2-r)**2)
        assert fibers.get(A,0)==expected,(name,A,r,fibers.get(A,0),expected)
    allowed={A for A,r in base}
    assert all(k in allowed for k in fibers)
    assert byrank=={0:1,1:48,2:96}
    print(name,byrank,'total=145')
    return fibers

z4=census('Z/4Z',range(4),lambda x,y:(x+y)%4,lambda x,y:(x*y)%4,lambda x:x%2)

def dadd(x,y): return x^y
def dmul(x,y):
    a,b=x&1,(x>>1)&1; c,d=y&1,(y>>1)&1
    return (a&c) | ((((a&d)^(b&c))&1)<<1)

dual=census('F2[epsilon]/(epsilon^2)',range(4),dadd,dmul,lambda x:x&1)
assert z4==dual
print('VERIFY_OK')
