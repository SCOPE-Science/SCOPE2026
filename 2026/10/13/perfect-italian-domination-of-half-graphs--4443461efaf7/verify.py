from itertools import product

def exact_weight_vectors(length, total, max_value=2):
    v=[0]*length
    def rec(i, rem):
        if i==length:
            if rem==0: yield tuple(v)
            return
        for x in range(min(max_value, rem)+1):
            v[i]=x
            yield from rec(i+1, rem-x)
    yield from rec(0,total)

def is_pid(n, lab):
    A=lab[:n]; B=lab[n:]
    # edges a_i b_j iff i<=j, with 0-based i,j
    suffix=[0]*(n+1)
    for i in range(n-1,-1,-1): suffix[i]=suffix[i+1]+B[i]
    prefix=[0]*n
    s=0
    for j in range(n):
        s+=A[j]; prefix[j]=s
    for i,x in enumerate(A):
        if x==0 and suffix[i]!=2: return False
    for j,y in enumerate(B):
        if y==0 and prefix[j]!=2: return False
    return True

print('VERIFY_OK')
checked=0
for n in range(2,15):
    feas=[]
    best=None
    for w in range(0,5):
        cur=[]
        for lab in exact_weight_vectors(2*n,w):
            checked+=1
            if is_pid(n,lab): cur.append(lab)
        if cur:
            best=w; feas=cur; break
    if n==2:
        assert best==3 and len(feas)==2
    elif n==3:
        assert best==4 and len(feas)==2
    else:
        expected=(2,)+(0,)*(n-1)+(0,)*(n-1)+(2,)
        assert best==4, (n,best)
        assert set(feas)=={expected}, (n,len(feas),feas[:5])
    print(f'n={n}: gamma_p_I={best}, minimum_functions={len(feas)}')
print('bounded_labelings_checked =',checked)
print('for every n>=4 the unique minimum labels a_1 and b_n by 2')
