from math import isqrt
LIMIT=30_000_000
N=617_426
SCALE=10**24
K=12

def sieve(limit):
    s=bytearray(b'\x01')*(limit+1)
    s[0:2]=b'\x00\x00'
    for p in range(2,isqrt(limit)+1):
        if s[p]:
            s[p*p:limit+1:p]=b'\x00'*(((limit-p*p)//p)+1)
    return s

# integer interval [lo,hi] for SCALE*ln(1+1/m)
def log1p_recip_interval(m):
    lo=0; hi=0; mp=1
    for k in range(1,K+1):
        mp*=m
        d=k*mp
        fl=SCALE//d
        ce=(SCALE+d-1)//d
        if k&1:
            lo += fl; hi += ce
        else:
            lo -= ce; hi -= fl
    # K even: omitted remainder positive, < next term
    mp*=m
    d=(K+1)*mp
    rem_ce=(SCALE+d-1)//d
    hi += rem_ce
    return lo,hi

def ln_ratio_interval(a,b,terms=120):
    # ln(a/b)=2 sum z^(2j+1)/(2j+1), z=(a-b)/(a+b), positive
    num=a-b; den=a+b
    lo=0; hi=0
    n_pow=num; d_pow=den
    for j in range(terms):
        d=(2*j+1)*d_pow
        val_num=2*SCALE*n_pow
        fl=val_num//d; ce=(val_num+d-1)//d
        lo+=fl; hi+=ce
        n_pow*=num*num; d_pow*=den*den
    # positive tail; bound geometric by first omitted term /(1-z^2)
    j=terms
    # tail <= 2*z^(2j+1)/(2j+1)/(1-z^2)
    # = 2*num^(2j+1)*den^2 / ((2j+1)*den^(2j+1)*(den^2-num^2))
    tail_num=2*SCALE*n_pow*den*den
    tail_den=(2*j+1)*d_pow*(den*den-num*num)
    tail_ce=(tail_num+tail_den-1)//tail_den
    hi+=tail_ce
    return lo,hi

TH={
 '<5':ln_ratio_interval(5,1),
 '<3':ln_ratio_interval(3,1),
 '<7/2':ln_ratio_interval(7,2),
 '<5/2':ln_ratio_interval(5,2),
}
print('threshold intervals',TH,flush=True)
s=sieve(LIMIT)
print('sieve ready',flush=True)
configs={
 'A_all1_under5': (lambda p:p%3==1,N,'<5'),
 'C_even_under7': (lambda p:p%3==1,N-1,'<7/2'),
 'B_all2_under5': (lambda p:p%3==2,N,'<5'),
 'B_no1mod5_under3': (lambda p:p%3==2 and p%5!=1,N,'<3'),
 'B_no2mod5_under3': (lambda p:p%3==2 and p%5!=2,N,'<3'),
 'C_odd_restricted_under5': (lambda p:p%3==1 and p%5!=1,N-2,'<5/2'),
 'C_restricted_next_crosses5': (lambda p:p%3==1 and p%5!=1,N-1,'>5/2'),
}
state={k:[0,0,0,None] for k in configs} # count,lo,hi,last
for p in range(3,LIMIT+1,2):
    if not s[p]: continue
    li=None
    for name,(pred,target,cmpkey) in configs.items():
        st=state[name]
        if st[0] < target and pred(p):
            if li is None: li=log1p_recip_interval(p-2)
            st[0]+=1; st[1]+=li[0]; st[2]+=li[1]; st[3]=p
    if all(state[k][0]>=configs[k][1] for k in configs): break
for name,(pred,target,cmpkey) in configs.items():
    cnt,lo,hi,last=state[name]
    assert cnt==target,(name,cnt,last)
    if cmpkey.startswith('<'):
        key=cmpkey
        tlo,thi=TH[key]
        ok=hi<tlo
        margin=tlo-hi
    else:
        key='<'+cmpkey[1:]
        tlo,thi=TH[key]
        ok=lo>thi
        margin=lo-thi
    print(name,'count='+str(cnt),'terminal='+str(last),'ok='+str(ok),'margin_scaled='+str(margin),flush=True)
    assert ok
print('VERIFY_OK lower_bound=617427 crossing_prime='+str(state['C_restricted_next_crosses5'][3]),flush=True)
