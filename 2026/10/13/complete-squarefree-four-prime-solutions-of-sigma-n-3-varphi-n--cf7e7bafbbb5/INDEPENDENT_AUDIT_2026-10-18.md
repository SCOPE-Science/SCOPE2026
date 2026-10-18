# Independent mathematical audit

## correctness

PASS

For squarefree n=pqrs with p<q<r<s, the ratio sigma/phi is the strictly decreasing product ∏(p+1)/(p-1). Since p=2 forces >3, while p≥5 gives at most R(5)R(7)R(11)R(13)=14/5, necessarily p=3. R(q)R(r)R(s)=3/2 rules out q=5 and q≥13, leaving q=7 or 11. The q=7 equation is (r-17)(s-17)=288, the q=11 equation (r-9)(s-9)=80; ordered positive divisor pairs and primality leave exactly n=24969,12441,10659. Independent exact divisor enumeration rechecked all candidate factors and witness equations. This is unrestricted over n, not an inference from a search cutoff.

## originality

PASS

OEIS A068391 publishes the three witness values for sigma(n)=3phi(n), so the integers themselves are known. Broughan–Zhou 2014 studies at most three distinct prime factors (Theorem 3) and an exponent algorithm when the prime support is fixed (Theorem 1), neither of which gives unconditional four-prime support classification. Broughan–Delbourgo 2013 addresses especially ratio two. The unrestricted exclusion of every further squarefree four-prime value is not supplied by these sources. Equivalent elementary treatments remain possible.

## value

PASS

Completes the natural next support-size layer of an established multiplicative ratio equation beyond the published ≤3-prime study. It replaces the first numerical witnesses with an all-height theorem and explicit finite prime factor branches; useful precise arithmetic classification, not mere table reproduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
