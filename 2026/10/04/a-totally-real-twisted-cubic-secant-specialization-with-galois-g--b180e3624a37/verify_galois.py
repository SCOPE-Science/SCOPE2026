# Standard-library exact finite-field certificate for the degree-10 secant polynomial.
P = [
4097057871858200718399710457050029783860448093883227674718933457227000000000000,
886550574980216626763495644940579931850647416367114988341240632505000000000000,
-14583445523408363563043807155529990819517874422341082510349311651322000000000000,
-5275699128677051945839235006808320077582295289599096827353598942811453300000000,
17554592606358550297152133225066058371683785754779718519967513497275130300000000,
8606156808171959940381182770903055017106302150492576001858996085131852000000000,
-6999255125012068183983935339635630280233270657536727356116586004108299033030000,
-4299485645818848556385308962411578844253286727339888981739646169646110507450000,
-143456610277323149419672668802489602321319249963404595109173337004241260620000,
4519935476335806902498900300573315260877836169182856532548525582293189114273,
30338654869700262466652210847156386094220876251571377982129917845522862489,
]

def trim(a):
    while len(a)>1 and a[-1]==0: a.pop()
    return a

def desc_to_asc(c,p): return [x%p for x in reversed(c)]
def monic(a,p):
    a=trim([x%p for x in a]); inv=pow(a[-1],-1,p); return [(x*inv)%p for x in a]
def add(a,b,p):
    n=max(len(a),len(b)); c=[0]*n
    for i in range(n): c[i]=((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0))%p
    return trim(c)
def sub(a,b,p):
    n=max(len(a),len(b)); c=[0]*n
    for i in range(n): c[i]=((a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0))%p
    return trim(c)
def mul(a,b,p):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]=(c[i+j]+x*y)%p
    return trim(c)
def divmod_poly(a,b,p):
    a=trim([x%p for x in a]); b=trim([x%p for x in b]); q=[0]*max(1,len(a)-len(b)+1)
    ib=pow(b[-1],-1,p)
    while len(a)>=len(b) and a!=[0]:
        k=len(a)-len(b); c=a[-1]*ib%p; q[k]=c
        for j in range(len(b)): a[j+k]=(a[j+k]-c*b[j])%p
        trim(a)
    return trim(q),a
def mod_poly(a,f,p): return divmod_poly(a,f,p)[1]
def gcd_poly(a,b,p):
    while b!=[0]: a,b=b,divmod_poly(a,b,p)[1]
    return monic(a,p)
def powmod_poly(base,e,f,p):
    r=[1]; base=mod_poly(base,f,p)
    while e:
        if e&1:r=mod_poly(mul(r,base,p),f,p)
        base=mod_poly(mul(base,base,p),f,p); e//=2
    return r
def irreducible_monic(f,p):
    f=monic(f,p); n=len(f)-1; x=[0,1]
    # Rabin: x^(p^n)=x and gcd(x^(p^(n/q))-x,f)=1 for prime q|n.
    h=x[:]
    for _ in range(n): h=powmod_poly(h,p,f,p)
    if mod_poly(sub(h,x,p),f,p)!=[0]: return False
    qs=[]; m=n; q=2
    while q*q<=m:
        if m%q==0:
            qs.append(q)
            while m%q==0:m//=q
        q+=1
    if m>1:qs.append(m)
    for q in qs:
        h=x[:]
        for _ in range(n//q): h=powmod_poly(h,p,f,p)
        if len(gcd_poly(sub(h,x,p),f,p))>1:return False
    return True

# p=19: reduction is irreducible degree 10, hence P is irreducible over Q and
# Frobenius supplies a 10-cycle.
p=19
f19=monic(desc_to_asc(P,p),p)
assert list(reversed(f19)) == [1,1,4,7,4,17,10,9,13,7,18]
assert irreducible_monic(f19,p)
print('MOD19_IRREDUCIBLE_DEGREE10_OK')

# p=17: squarefree factorization into irreducibles of degrees 3 and 7.
p=17
f17=monic(desc_to_asc(P,p),p)
f3=desc_to_asc([1,3,6,15],p)
f7=desc_to_asc([1,0,10,10,2,10,13,11],p)
assert irreducible_monic(f3,p) and irreducible_monic(f7,p)
assert monic(mul(f3,f7,p),p)==f17
assert gcd_poly(f3,f7,p)==[1]
print('MOD17_FACTOR_DEGREES_7_3_OK')
print('FROBENIUS_CYCLE_TYPES_10_AND_7+3_OK')
print('GROUP_CERTIFICATE_OK')
print('VERIFY_OK')
