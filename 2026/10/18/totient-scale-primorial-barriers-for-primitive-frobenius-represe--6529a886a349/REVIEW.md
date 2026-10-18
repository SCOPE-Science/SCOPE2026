# Mathematical review

## Correctness — PASS

The congruence \(b_T\equiv-Q_T\pmod a\) forces every admissible coefficient \(y\) into the reduced residue class \(-1\), with \(2\le y\le T\). A composite \(y\) has a prime factor at most \(\sqrt T\); a prime \(y\) itself lies in the prescribed progression. Both possibilities give a common prime divisor of \(x,y\). The fixed-modulus prime number theorem in arithmetic progressions yields the claimed constant. The divisor-cover optimality follows because every prime in the residue class is an obligatory factor. Boundary \(a\ge3\) is essential; there is no assertion for \(a=2\). Finite checks supplement, not replace, the infinite proof.

## Originality — PASS (with residual risk)

Ding--Wang--Zhang, arXiv:2509.08599v1, Theorem 1.7 establishes the correct logarithmic scale but only a positive unspecified constant; inspection of its Section 4 CRT argument does not yield the explicit totient coefficient. The source does not give the asymptotically minimal prime-divisor covering product. The separately recorded large-both-coefficients bound requires \(\min(a,b)\to\infty\) and does not cover fixed \(a\). Searches of mathematical-results records for the exact constant, reduced residue class sieve, aliases and the fixed-parameter primitive Frobenius problem returned no covering result. Independent literature coverage remains incomplete; this is not a uniqueness certificate.

## Mathematical value — PASS

For each fixed coefficient \(a\ge3\), the argument makes the logarithmic lower-growth coefficient explicit as \(\varphi(a)\), which can be arbitrarily large with \(a\), strengthening an unspecified existence bound. It supplies a direct constructive obstruction and proves the asymptotic exponential optimality of the associated prime-divisor cover, pinpointing the relevant arithmetic progression. The result is an exact new quantitative bound, not a claim to solve the open maximal-order problem.

## Scope and limitations

Optimality is only among divisor-cover products, not among all primitive Frobenius obstructions. A possible implicit earlier proof of the quantitative constant is a residual originality risk. The fixed-modulus assumption is necessary for the PNT-in-progressions step as stated. Computation verifies only stated finite samples.

Self-review: passed. Independent audit: not yet performed.
