"""Independent exhaustive finite-field checks for square-zero elements in dihedral nilCoxeter algebras.
Uses the concatenation multiplication law on alternating Coxeter words, not the proof's triangular parametrization.
Run: python3 verify.py
"""
from itertools import product


def field(q):
    if q in (2, 3, 5):
        return lambda a,b:(a+b)%q, lambda a,b:(a*b)%q
    if q == 4:
        # GF(2)[h]/(h^2+h+1), two binary coordinates.
        def add(a,b):return a^b
        def mul(a,b):
            a0,a1=a&1,a>>1
            b0,b1=b&1,b>>1
            c0=a0*b0
            c1=a0*b1+a1*b0
            c2=a1*b1
            return ((c0+c2)&1) | (((c1+c2)&1)<<1)
        return add,mul
    if q == 9:
        # GF(3)[h]/(h^2+1), two ternary coordinates.
        def add(a,b):return ((a%3+b%3)%3)+3*((a//3+b//3)%3)
        def mul(a,b):
            a0,a1=a%3,a//3
            b0,b1=b%3,b//3
            return ((a0*b0-a1*b1)%3)+3*((a0*b1+a1*b0)%3)
        return add,mul
    raise ValueError(q)


def predicted(m,q):
    if m%2:
        d=(m-1)//2
        return q**(m-1)*(q+2*((d+1)//2)*(q-1))
    d=m//2
    k=d//2
    if q%2==0:
        central=q*q if d%2 else q
        return q**(m-1)*(2*k*q*(q-1)+central)
    central=(2*q-1) if (d%2 or q%4==1) else 1
    return q**(m-1)*(2*k*(q-1)+central)


def is_square_zero(m,q,coeffs,add,mul):
    # a_l, b_l are length-l basis coefficients, for 1<=l<m; the longest
    # coefficient is omitted because it annihilates the radical.
    for target_len in range(2,m+1):
        ans=[]
        for start in (0,1):
            s=0
            for left_len in range(1,target_len):
                right_len=target_len-left_len
                left=coeffs[2*(left_len-1)+start]
                right_start=start if left_len%2==0 else 1-start
                right=coeffs[2*(right_len-1)+right_start]
                s=add(s,mul(left,right))
            ans.append(s)
        if target_len<m and (ans[0] or ans[1]):
            return False
        if target_len==m and add(ans[0],ans[1]):
            return False
    return True


def run(m,q):
    add,mul=field(q)
    hist={}
    hits=0
    nvars=2*(m-1)
    for c in product(range(q),repeat=nvars):
        if is_square_zero(m,q,c,add,mul):
            hits+=1
            leading=next((i for i in range(1,m) if c[2*i-2] or c[2*i-1]),m)
            hist[leading]=hist.get(leading,0)+1
    hits*=q # independent top-length socle coordinate
    target=predicted(m,q)
    assert hits==target,(m,q,hits,target,hist)
    print('PASS m=%d q=%d square_zero=%d predicted=%d leading_profile=%s'%(m,q,hits,target,hist))

if __name__=='__main__':
    for m,q in ((3,2),(3,3),(3,4),(3,9),
                (4,2),(4,3),(4,4),(4,5),
                (5,2),(5,3),
                (6,2),(6,3),
                (7,2),(8,2),(9,2)):
        run(m,q)
    print('VERIFY_OK')
