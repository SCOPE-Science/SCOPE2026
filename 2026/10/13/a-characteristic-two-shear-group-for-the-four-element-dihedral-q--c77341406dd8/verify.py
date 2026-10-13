"""Independent finite-field checks for dihedral-quandle algebra automorphisms.
Run: python3 verify.py. Uses the Python standard library only.
"""
from itertools import product

class Field:
    def __init__(self, degree, polynomial):
        self.degree=degree
        self.q=1<<degree
        self.poly=polynomial
    def add(self, x,y): return x^y
    def mul(self,x,y):
        z=0
        while y:
            if y&1: z^=x
            y>>=1
            x<<=1
            if x & self.q: x^=self.poly
        return z

def qmul(F,x,y):
    z=[0]*4
    for i in range(4):
        for j in range(4):
            z[(2*j-i)%4]^=F.mul(x[i],y[j])
    return tuple(z)

def axpy(F,a,x,y):return tuple(y[i]^F.mul(a,x[i]) for i in range(4))

def map_apply(F,columns,v):
    out=(0,0,0,0)
    for k in range(4):out=axpy(F,v[k],columns[k],out)
    return out

def basis(i): return tuple(int(k==i) for k in range(4))

# Adapted ordered basis (h0,h1,u,v)=(e0,e1,e0+e2,e1+e3)
NEW=(basis(0),basis(1),(1,0,1,0),(0,1,0,1))

def to_standard(F, h0,h1,w0,w1):
    out=(0,0,0,0)
    for a,e in zip((h0,h1,w0,w1),NEW):out=axpy(F,a,e,out)
    return out

def predicted(F):
    for sw in (0,1):
        for c in product(range(F.q),repeat=4):
            # Columns in (h0,h1,u,v) coordinates.
            cols_new=[]
            for j in range(4):
                if j<2:
                    h0,h1= ((1,0) if j==0 else (0,1))
                    if sw:h0,h1=h1,h0
                    w0,w1=c[j],c[2+j]
                else:
                    h0=h1=0
                    w0,w1=((1,0) if j==2 else (0,1))
                    if sw:w0,w1=w1,w0
                cols_new.append(to_standard(F,h0,h1,w0,w1))
            # Standard basis e0=h0,e1=h1,e2=u+h0,e3=v+h1.
            cols=(cols_new[0],cols_new[1],tuple(x^y for x,y in zip(cols_new[0],cols_new[2])),tuple(x^y for x,y in zip(cols_new[1],cols_new[3])))
            yield cols

def rank_F2(cols):
    pivots=[0]*4
    r=0
    for col in cols:
        v=sum((x&1)<<i for i,x in enumerate(col))
        while v:
            p=v.bit_length()-1
            if pivots[p]: v^=pivots[p]
            else:
                pivots[p]=v
                r+=1
                break
    return r

def is_automorphism(F,cols):
    for i in range(4):
        for j in range(4):
            if map_apply(F,cols,basis((2*j-i)%4))!=qmul(F,cols[i],cols[j]):return False
    return True

def check():
    f2=Field(1,0b11)
    full=set()
    for entries in product((0,1),repeat=16):
        cols=tuple(tuple(entries[4*j+i] for i in range(4)) for j in range(4))
        if rank_F2(cols)==4 and is_automorphism(f2,cols):full.add(cols)
    calc=set(predicted(f2))
    assert len(full)==len(calc)==32
    assert full==calc
    print('F2_GL4_EXHAUSTIVE_AUTOMORPHISMS',len(full),'PASS')
    for degree,polynomial in ((2,0b111),(3,0b1011)):
        F=Field(degree,polynomial)
        tested=set()
        for cols in predicted(F):
            assert cols not in tested
            tested.add(cols)
            assert is_automorphism(F,cols)
        assert len(tested)==2*(F.q**4)
        print('F'+str(F.q)+'_CONSTRUCTED_AUTOMORPHISMS',len(tested),'PASS')
    print('VERIFY_OK')

if __name__=='__main__':check()
