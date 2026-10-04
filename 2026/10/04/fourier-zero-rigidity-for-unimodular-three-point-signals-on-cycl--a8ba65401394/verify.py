#!/usr/bin/env python3
from math import gcd


def paired_criterion(N,a,b):
    g=gcd(N,gcd(a,b))
    n=N//g
    A=(a//g)%n
    B=(b//g)%n
    return (n%3==0) and ((A+B)%3==0)


def brute_ratio_in_image(N,a,b):
    # (omega^(a d),omega^(b d))=(rho,rho^2) requires 3|N
    if N%3:
        return False
    one=N//3
    two=2*one
    return any((a*d)%N==one and (b*d)%N==two for d in range(N))


def kernel_size(N,a,b):
    return sum(1 for k in range(N) if (a*k)%N==0 and (b*k)%N==0)


def zero_count_for_constructed(N,a,b):
    # Choose phases so k=0 is a + orientation zero: u=rho, v=rho^2.
    # A zero at k has either orientation.  Use exact modular conditions on
    # exponents in the common group of lcm(N,3)-th roots.
    L=3*N//gcd(3,N)
    step=L//N
    third=L//3
    count=0
    for k in range(N):
        # u*omega^(ak) has exponent third + step*a*k mod L;
        # v*omega^(bk) has exponent 2third + step*b*k mod L.
        p=(third + step*a*k)%L
        q=(2*third + step*b*k)%L
        if (p==third and q==2*third) or (p==2*third and q==third):
            count+=1
    return count


def main():
    checked=0
    paired=0
    single=0
    for N in range(3,181):
        for a in range(1,N):
            for b in range(a+1,N):
                g=gcd(N,gcd(a,b))
                n=N//g
                if n<3:
                    continue
                crit=paired_criterion(N,a,b)
                brute=brute_ratio_in_image(N,a,b)
                assert crit==brute, (N,a,b,g,crit,brute)
                assert kernel_size(N,a,b)==g, (N,a,b,g,kernel_size(N,a,b))
                z=zero_count_for_constructed(N,a,b)
                expected=2*g if crit else g
                assert z==expected, (N,a,b,g,crit,z,expected)
                checked+=1
                paired+=int(crit)
                single+=int(not crit)
    # Prime corollary: for p>3 the paired case never occurs.
    primes=[]
    for p in range(5,181):
        if all(p%d for d in range(2,int(p**0.5)+1)):
            primes.append(p)
            for a in range(1,p):
                for b in range(a+1,p):
                    assert not paired_criterion(p,a,b)
    print(f"VERIFY_OK triples={checked} paired={paired} single={single} primes_gt3={len(primes)} N_max=180")

if __name__=='__main__':
    main()
