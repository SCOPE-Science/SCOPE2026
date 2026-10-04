# Same-model scientific review

## Correctness
PASS. Summing \(x_i-\varphi(x_i)=x_i-x_{i+1}+k\) around a period gives the exact cototient budget \(\sum_i c(x_i)=Tk\). Every cycle term is at least \(2\), the maximum is composite, and the standard least-prime-factor estimate gives \(c(M)\ge\sqrt M\). The other \(T-1\) cototients contribute at least \(1\) each, yielding \(M\le[T(k-1)+1]^2\). Equality forces every inequality to be tight, which implies a prime square at the maximum and primes at every other term; the recurrence then forces the full progression. The converse is direct. The packaged checker independently verifies the identities and several exact extremal cycles.

## Originality
PASS. Leonetti and Luca's full text proves eventual periodicity and a starting-value-dependent trajectory bound, then explicitly states that sharpness and nontrivial size information remain unanswered and suggests prime-progression cycles with a final composite term. The inspected source does not give the period-sensitive square bound or equality classification. The direct follow-up concerns the separate two-step recurrence. OEIS A051953 records cototients but not the cycle theorem. Targeted semantic, web, and exact-number searches did not locate stronger coverage.

## Value
PASS. The result answers a natural structural question singled out by the source: it gives an exact sharp envelope in terms of period and shift, and proves that the proposed prime-progression construction is precisely the extremal mechanism. The equivalent lower bound on period quantifies how long any cycle with a large maximum must be. Equality examples at periods \(2\), \(3\), and \(4\) show the bound is attained nontrivially.

## Closest literature and limitations
The closest source is Leonetti and Luca, arXiv:2302.01783v1 / DOI 10.1017/S0004972723000394. A later publisher article improves only the two-step recurrence. The equality criterion leaves a simultaneous-primality problem and does not imply infinitely many extremal cycles. Literature non-detection cannot exclude an unindexed equivalent formulation.

Same-model review: passed. Independent audit: not yet performed.
