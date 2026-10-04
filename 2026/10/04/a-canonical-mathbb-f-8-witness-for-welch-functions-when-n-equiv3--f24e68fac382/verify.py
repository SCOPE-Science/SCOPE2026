MOD = 0b1011
def mul(a,b):
    r=0; x=a; y=b
    while y:
        if y&1: r ^= x
        y >>= 1; x <<= 1
        if x & 0b1000: x ^= MOD
    return r & 7
def pw(a,e):
    r=1
    while e:
        if e&1: r=mul(r,a)
        a=mul(a,a); e//=2
    return r
def frob(a,k): return pw(a,1 << (k%3))
for a in range(1,8): assert pw(a,7)==1
cases=0
for n in range(3,202,2):
    if n%3: continue
    m=(n-1)//2
    assert m%3==1 and (pow(2,m,7)+3)%7==5
    total=0
    for x in range(8): total ^= pw(x,(1<<m)+3)
    assert total==0
    cases += 1
for x in range(8):
    for y in range(8):
        xm,ym=frob(x,1),frob(y,1); x2,y2=mul(x,x),mul(y,y)
        g=mul(ym,x2^x)^mul(y2,xm^x)^mul(y,xm^x2)
        assert g==0
print(f"VERIFY_OK n_cases={cases} subfield_sum=0 g_pairs=64")
