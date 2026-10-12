from fractions import Fraction

# Sparse polynomials in x,y: {(i,j): coefficient}.
def add(a,b):
    out=dict(a)
    for m,c in b.items():
        out[m]=out.get(m,Fraction(0))+c
        if out[m]==0:
            del out[m]
    return out

def mul(a,b):
    out={}
    for (i,j),c in a.items():
        for (k,l),d in b.items():
            m=(i+k,j+l)
            out[m]=out.get(m,Fraction(0))+c*d
    return {m:c for m,c in out.items() if c}

def scale(a,c):
    c=Fraction(c)
    return {m:c*v for m,v in a.items() if c*v}

def power(a,n):
    out={(0,0):Fraction(1)}
    for _ in range(n):
        out=mul(out,a)
    return out

x={(1,0):Fraction(1)}
y={(0,1):Fraction(1)}
H=add(x,y)
xy=mul(x,y)
x2=mul(x,x)
y2=mul(y,y)

# [F] = c_6((Sym^2 S^*)^2) = 16 x^2 y^2 (x+y)^2.
Fclass=scale(mul(mul(x2,y2), power(H,2)),16)

# ch_2(T_F) = -(5/2)(x^2+y^2).
ch2=scale(add(x2,y2), Fraction(-5,2))

# For Gr(2,7): integral f = [x^6 y^5] (x-y)f.
vand=add(x,scale(y,-1))
def integral(f):
    return mul(vand,f).get((6,5),Fraction(0))

ch2_H2=integral(mul(mul(ch2,power(H,2)),Fclass))
H4=integral(mul(power(H,4),Fclass))

print(f"ch2_H2={ch2_H2}")
print(f"H4={H4}")
assert ch2_H2 == -40
assert H4 == 80
print("VERIFY_OK")
