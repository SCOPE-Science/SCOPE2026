# Review

## Correctness

**PASS.** Holt's published multiplication formula is reconstructed from the elementary column equations and specialized with correct index reversal. The \(\ell\)-adic two-case argument covers all primes dividing \(n-1\), including the potential common factor \(\gcd(n-1,n+1)=2\): no coprimality condition on base and multiplier is inserted. The first case starts with \(c_1\) using a precise valuation from the nonzero trailing digit; induction then propagates divisibility. In the second case a globally least valuation produces a genuine contradiction to a fixed modulus. Endpoint carries are zero; if no interior carry exists, the nonzero first carry equation excludes the palintiple. After obtaining divisibility, the standard carry bounds force binary carries, \(c_1=n-1\) and \(n+1\mid b\). The reverse direction is Holt (2014), Theorem 6. The optional finite checks do not substitute for this proof.

## Originality

**PASS, subject to residual publication risk.** Holt (2014) established sufficiency and a converse requiring \(\gcd(b,n-1)=1\), but expressly posed the general converse. Holt (2015) separately states this exact all-length carry divisibility as Conjecture 1. Kendrick (2015, Remark 4) says that the stronger symmetric-palintiple-to-1089-graph implication remains conjectural, despite proving the graph isomorphism criterion. The 2025 permutiple construction paper does not state this general converse. The new argument removes the coprimality obstruction by a local valuation minimum argument for primes dividing both base and \(n-1\). Searches of related work and mathematical-result records found no equivalent statement; missing sources remain a real originality risk, not evidence of uniqueness.

## Mathematical value

**PASS.** Settles a concrete long-standing, explicitly formulated arithmetic conjecture on reverse multiples, establishes a structural dichotomy for all digits and bases, and translates it into an exact base/multiplier criterion. The formerly uncontrolled case \(\gcd(b,n-1)>1\) is the source of the mathematical obstruction; the proof eliminates it uniformly rather than merely verifying a new finite range.

## Closest work and limitations

Holt (2014), Theorems 6 and 7, and Holt (2015), Conjecture 1, are closest; Kendrick (2015), Theorem 3.1 and Remark 4, gives graph-theoretic context. Verification enumerates only finite carry tuples; the theorem covers all lengths. No classification of the asymmetric and shifted-symmetric classes is asserted, and independent validation remains pending.

Self-review: passed. Independent audit: not yet performed.
