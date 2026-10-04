# Review of A prime-support sieve for perfect totients of the form \(3^k p\)

## Correctness
PASS. The proof was reconstructed from the definition of the iterated-totient sum. The only auxiliary estimate, \(F(m)\le2\phi(m)-1\) for even \(m\), follows by induction from \(F(m)=\phi(m)+F(\phi(m))\) and \(2\phi(m)\le m\). Substituting the exact first iterate of \(3^k p\) yields the claimed strict Euler-product bound without an asymptotic or computational step. The bundled checker directly verifies the definitions on a finite domain and is corroborative only.

## Originality
PASS. Full-text comparison against the 2003 paper on the exact family, the 2006 paper on global sums of totient iterates, and the 2009 follow-up on deeper nested prime chains found no theorem equivalent to or stronger than the support-density inequality. The natural OEIS table was also checked. The older 1939 and 1982 foundational papers were not directly readable in this run, leaving a disclosed access risk; later inspected literature summarizes their relevant results in narrower forms. Targeted semantic searches found no equivalent statement, but search failure was not used by itself as novelty proof.

## Value
PASS. The condition applies uniformly to the literature's unresolved family \(3^k p\) and excludes infinite arithmetic classes of possible primes through a simple support criterion. It therefore supplies a reusable structural sieve rather than a one-off numerical observation.

## Closest literature and limitations
The closest work is Iannucci–Moujie–Cohen (2003), which studies \(3^k p\) directly but under explicit nested-prime structures, and Deng (2009), which eliminates a deeper prescribed chain. Shparlinski (2006) gives global distribution and congruence results for the same iterated function. The present condition is necessary only and does not settle existence for \(k\ge4\).

Same-model review: passed. Independent audit: not yet performed.
