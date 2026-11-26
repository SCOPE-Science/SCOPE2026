# Independent mathematical audit

## correctness

PASS

An even solution has odd beta(n), so every odd-prime exponent is even: n=2^a t^2 with t odd. For at most eight primes dividing t, the first eight odd primes minimize the product of p/(p+1) and give beta(t^2)/t^2>2/5; t=1 also satisfies the bound. The factor beta(2^a)/2^a is at least 1/2, so the positive odd quotient (n-1)/beta(n) is below 5. If the quotient is 3 then n=1 mod 3, forcing even a and 3 not dividing t. Omitting 3 from the smallest eligible primes gives beta(t^2)/t^2>1/2, and even a gives beta(2^a)/2^a>2/3, contradicting quotient 3. For t>1, beta(n)<(2^a-1)t^2<n-1, ruling out quotient 1; for t=1, the explicit power-of-two formula leaves only 2 and 4. An independent divisor convolution beta(n)=sum over d|n of d times Liouville(n/d) gave only 2 and 4 through 500000 among even inputs. Independent exact products gave 1062347/2654208, 30808063/59719680, and 20928465245153916450 for twice the square of the first nine odd primes. The finite computation corroborates but does not establish the unrestricted argument; the submitted script was inspected, not executed.

## originality

PASS

The square odd part is known: it follows immediately from Tóth's published parity characterization and is also explicit in the October 13 Resultary proof. That proof uses a closely related odd-quotient and prime-product argument, and its even conclusion is only omega(n)>=5 for n>4. The supported distinct contribution is the tightening to omega(n)>=10 and the resulting explicit size bound. In particular, tracking the valuation of 2 after quotient 3 is forced to be a multiple of 3 is not needed in the earlier three-odd-prime argument but supplies the stronger factor bound here. No inspected source gives the ten-prime implication for even beta solutions.

## value

PASS

Improving the earlier five-prime even obstruction to ten is a substantial unrestricted exclusion, obtained without any exponent cap. The parity-dependent treatment of the quotient exposes an arithmetic constraint absent from a finite search and supplies a concrete lower bound on n. This advances the posed beta analogue without claiming to settle it or treating the known parity characterization as the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
