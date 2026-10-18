"""Finite diagnostics for contracting rotation composition mixtures.
Only examples, not proof of asymptotic statements.
"""
import cmath, math


def count_rational_difference(p, q, r, L):
    """For C_(r z)-C_(r exp(2*pi*i*p/q)z), count singular values > exp(-L)."""
    log_r = math.log(r)
    cutoff = (L+math.log(2.0))/(-log_r)
    count=0
    for n in range(int(cutoff)+3):
        if n % q == 0:
            continue   # exact zero, not a floating-point approximation
        amplitude=2*abs(math.sin(math.pi*((p*n)%q)/q))
        if n*log_r+math.log(amplitude)>-L:
            count+=1
    return count


def count_irrational_difference(theta, r, L):
    log_r=math.log(r)
    count=0
    for n in range(int((L+math.log(2))/-log_r)+3):
        amplitude=2*abs(math.sin(math.pi*((n*theta)%1.0)))
        if amplitude and n*log_r+math.log(amplitude)>-L:
            count+=1
    return count


def dft_residue_profile(q, residues):
    """Fourier inversion constructing a filter supported on chosen residues."""
    coeff=[sum(cmath.exp(-2j*math.pi*j*k/q) for k in residues)/q for j in range(q)]
    vals=[sum(coeff[j]*cmath.exp(2j*math.pi*j*n/q) for j in range(q)) for n in range(q)]
    for n,v in enumerate(vals):
        expected=1 if n in residues else 0
        assert abs(v-expected)<1e-10, (q,n,v,expected)
    return coeff


def main():
    tests=0
    r=math.exp(-.4)
    for q in [2,3,4,5,7,11]:
        for p in range(1,q):
            if math.gcd(p,q)>1: continue
            for L in [20,40,80,160,240]:
                v=count_rational_difference(p,q,r,L)
                predicted=(1-1/q)*L/.4
                assert abs(v-predicted)<8, (p,q,L,v,predicted)
                tests+=1
    phi=(math.sqrt(5)-1)/2
    for L in [40,80,160,240,360]:
        v=count_irrational_difference(phi,r,L)
        assert abs(v-L/.4)<12, (L,v,L/.4)
        tests+=1
    for q in range(2,15):
        for h in range(1,q+1):
            dft_residue_profile(q,set(range(h)))
            tests+=q
    print('PASS',tests,'finite example diagnostics; analytic zero-density proof required')

if __name__=='__main__':
    main()
