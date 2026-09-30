# Independent audit — 2026-09-29

Record: `2026/09/11/081`  
Audited tree: `fcab13e96d6aad6bf6ddba22ed8a8afbef72d024`  
Disposition: **passed**

## Correctness

For a prime q in (Q0,2Q0], no prime in the N/3-centered short interval is divisible by q for large N, so E0=0 and exact character orthogonality gives sum_a S(a/q)=0. Hence some a!=0 has |S(a/q)|>=T/(q-1). Rational spacing places all such a/q outside major arcs of half-width at most (log N)^B/N, and the short-interval PNT at exponent 5/6 gives T~2h. Thus the lower bound is ~h/(log N)^A and defeats every fixed power saving.

## Originality

The nearest open literature supplies short-prime exponential-sum upper bounds and short-interval prime distribution, not this exact lower-bound obstruction for the stated polylogarithmic major-arc threshold. The audit claims only target-specific originality.

## Scientific value

The argument rules out the proposed uniform power saving and in fact every fixed N^{-delta} saving under the stated arc system, providing a clear structural barrier rather than a numerical counterexample.

## Limitations

- The asymptotic total mass T~2h uses the classical short-interval prime number theorem rather than a self-contained proof.
- The result concerns the stated major-arc widths and denominator threshold.
- No direct sixth-moment theorem is disproved except insofar as it would imply the false sup bound.

## Sources

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/11/081
- https://arxiv.org/abs/1902.04708
- https://www.math.princeton.edu/events/primes-and-other-interesting-sequences-short-intervals-2020-05-27t170000
