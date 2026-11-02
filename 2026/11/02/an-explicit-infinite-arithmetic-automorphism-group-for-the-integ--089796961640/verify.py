"""Exact integral checks for the explicitly described R8 quandle-algebra automorphism kernel."""
from itertools import product

def mul(x,y):
    z=[0]*8
    for i,xi in enumerate(x):
        if not xi:continue
        for j,yj in enumerate(y):
            if yj:z[(2*j-i)%8]+=xi*yj
    return z

def vec(z):
    a=[0]*8
    for i,c in z.items():a[i]+=c
    return a

def b(i):
    i%=8
    return vec({i:1,(i+4)%8:-1})

def add(*vs):return [sum(x) for x in zip(*vs)]
def scale(k,v):return [k*x for x in v]
def matcols_to_rows(cs):return [list(row) for row in zip(*cs)]
def det(M):
    a=[list(x) for x in M];n=len(a);sgn=1;den=1
    for k in range(n-1):
        if a[k][k]==0:
            j=next((j for j in range(k+1,n) if a[j][k]),None)
            if j is None:return 0
            a[k],a[j]=a[j],a[k];sgn=-sgn
        piv=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                t=a[i][j]*piv-a[i][k]*a[k][j]
                assert t%den==0
                a[i][j]=t//den
            a[i][k]=0
        den=piv
    return sgn*a[n-1][n-1]

def images(a,beta,c,d):
    bs=[b(i) for i in range(4)]
    delta=[
        add(scale(a,bs[0]),scale(-beta,bs[1]),scale(beta,bs[3])),
        add(scale(d,bs[0]),scale(c,bs[1]),scale(d,bs[2])),
        add(scale(a,bs[2]),scale(-beta,bs[1]),scale(-beta,bs[3])),
        add(scale(-d,bs[0]),scale(d,bs[2]),scale(c,bs[3]))]
    delta+= [scale(-1,x) for x in delta]
    images=[]
    for i in range(8):
        e=[0]*8;e[i]=1
        images.append(add(e,delta[i]))
    U=[[(2*a+1),2*d,0,-2*d],[-2*beta,2*c+1,-2*beta,0],[0,2*d,2*a+1,2*d],[2*beta,0,-2*beta,2*c+1]]
    return images,U

def algebra_hom(img):
    for i,j in product(range(8),repeat=2):
        if mul(img[i],img[j])!=img[(2*j-i)%8]:return False
    return True

def apply_cols(cols,v):
    out=[0]*len(cols[0]);
    for c,x in zip(cols,v):
        for i,y in enumerate(c):out[i]+=y*x
    return out

count=valid=0
for a,bb,c,d in product(range(-2,3),repeat=4):
    im,U=images(a,bb,c,d)
    assert algebra_hom(im), (a,bb,c,d,'bad hom')
    t=(2*a+1)*(2*c+1)+8*bb*d
    assert det(U)==t*t,(a,bb,c,d,det(U),t*t)
    assert det(matcols_to_rows(im))==t*t
    for i in range(4):
        assert apply_cols(im,b(i))==[sum(U[j][i]*b(j)[h] for j in range(4)) for h in range(8)]
    count+=1
    if abs(t)==1:valid+=1

lifts=set()
for u,v in product((1,3,5,7),range(8)):
    cols=[]
    for i in range(8):
        x=[0]*8;x[(u*i+v)%8]=1;cols.append(x)
    assert algebra_hom(cols)
    assert abs(det(matcols_to_rows(cols)))==1
    lifts.add((u%4,v%4))
assert len(lifts)==8
# Test nontrivial infinite shear family and group closure via direct compositions.
for n in range(-8,9):
    im,U=images(0,n,0,0)
    assert algebra_hom(im) and det(U)==1
for n,m in product(range(-4,5),repeat=2):
    im,_=images(0,n,0,0)
    jm,_=images(0,m,0,0)
    comp=[apply_cols(im,x) for x in jm]
    assert algebra_hom(comp) and det(matcols_to_rows(comp))==1
print('VERIFY_OK')
print(f'Exact kernel parameter quadruples checked: {count}; integral automorphisms among these: {valid}')
print('Verified 32 affine basis permutations and surjectivity onto 8 quotient affine maps')
print('Verified 17 infinite-family shear samples and 81 compositions')
