"""Exact verification of explicit high-level denumerant drop witnesses.

Run: python3 check_witnesses.py
Uses integer arithmetic only.  This is finite corroboration, not the proof
of the formula for every odd starting generator.
"""

def formula(a):
    assert a >= 3 and a % 2 == 1
    b = a + 2
    P = a*b*(a+4)
    if a % 4 == 3:
        q = (a+1)//4
        K = (b*b-7)//2
        R = (a+1)*(a+4)*(a**3-a*a-2*a+4)//32
    else:
        q = (a-1)//4
        K = (2*b*b-b-11)//2
        R = (a**5+4*a**4-7*a**3-22*a*a+16*a+40)//32
    t = q - 1
    N = b*K+t*P
    return b, P, q, K, t, N, R


def exact_r_by_two_loops(a, target):
    # Sum over the third denomination; solve each remaining two-coin
    # congruence directly with a modular inverse (no recurrence used).
    b, c = a+2, a+4
    inv_b = pow(b,-1,a)
    ans = 0
    for z in range(target//c + 1):
        rem_z=target-c*z
        y0=(rem_z*inv_b)%a
        ymax=rem_z//b
        if y0<=ymax:
            ans += (ymax-y0)//a+1
    return ans


def exact_r_by_floor_sums(a, m):
    # An independently indexed count via the middle generator residue.
    b = a+2
    K, residue = divmod(m, b)
    inv2 = (b+1)//2
    h = (residue * inv2) % b
    # Writing z-x=h+bj gives independent j>=0 and j<0 branches.
    ans = 0
    j = 0
    while True:
        bound = K-(h+(1 if residue else 0)+(b+2)*j)
        if bound < 0:
            break
        ans += bound//2+1
        j += 1
    i = 1
    while True:
        bound = K+h-(b-2)*i
        if h == 0:
            bound = K-(b-2)*i
        # For m=bK+1, the actual equation adds -1 in both branches.
        bound -= 1 if residue else 0
        if bound < 0:
            break
        ans += bound//2+1
        i += 1
    return ans


def main():
    case_count = 0
    for a in range(3, 40, 2):
        b,P,q,K,t,N,R = formula(a)
        n0=b*K
        # The two implementations use distinct loops and divisibility tests.
        for x, expected in [(n0, None), (n0+1, None), (N,R), (N+1,R-1)]:
            v = exact_r_by_two_loops(a,x)
            assert v == exact_r_by_floor_sums(a,x), (a,x,v,exact_r_by_floor_sums(a,x))
            if x == n0:
                assert v == (8*q**3+6*q*q if a%4==3 else 32*q**3+64*q*q+35*q+4)
            elif x == n0+1:
                assert v == (8*q**3+6*q*q-q if a%4==3 else 32*q**3+64*q*q+34*q+4)
            else:
                assert v == expected, (a,x,v,expected)
            case_count += 1
        # Independent polynomial generation of counts over one period verifies
        # the exact period-shift identity at several small offsets.
        sample_offsets = [0,1,a-1,a,2*a,3*a+5]
        cutoff = P+max(sample_offsets)
        counts=[0]*(cutoff+1)
        counts[0]=1
        for g in (a,b,a+4):
            for n in range(g,cutoff+1):
                counts[n]+=counts[n-g]
        C=(P+3*b)//2
        for s in sample_offsets:
            assert counts[s+P]-counts[s]==s+C, (a,s)
            case_count += 1
    print('VERIFIED_OK odd_a=3..39_step2 checks=%d independent_integer_routes=2 period_shift_samples_per_a=6' % case_count)
    for a in (3,5,7,9,11,13,17,19,25,37):
        _,_,_,_,_,N,R = formula(a)
        print('a=%d n=%d r_n=%d r_next=%d' % (a,N,R,R-1))

if __name__=='__main__':
    main()
