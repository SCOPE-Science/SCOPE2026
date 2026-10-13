# Self-review

## Correctness

**PASS.** The proof reconstructs the recurrence in reduced numerator-denominator coordinates, treats all three possibilities for \(v_p(x_0)\) relative to \(v_p(h)\), and shows that a later obstruction can occur only on the critical valuation layer. On that layer the finite-field ratio follows \(t\mapsto t+t^{-1}\), and the claimed congruence modulo \(p^{v_p(h)+1}\) is equivalent to specifying its starting value. Chinese-remainder multiplication is valid because the local prime-power moduli are coprime. Counting distinct finite hit times rather than primes correctly handles simultaneous failures.

The verifier independently replays the original integer recurrence over complete predicted periods for every \(1\le h\le60\) and all \(4225\) starts modulo the period for \(h=65\). The universal proof does not rely on this finite enumeration.

## Originality

**PASS.** The closest source, arXiv:2610.00765v1, proves the no-cancellation recurrence and the individual-sequence square criterion and explicitly frames the distribution of failures across starting values as a further question. It does not state the prime-power periodic classification, the exact CRT formula, or the collision rule. Jones-Manes (arXiv:1101.4339; DOI 10.4171/CMH/316) studies global preimage-tree Galois theory, not this integer-start distribution. Semantic searches for the same recurrence, first hits of zero, preimage trees, and CRT densities found no stronger result implying the claim.

The main residual risk is terminology: specialized finite-field dynamical literature may encode some local first-hit counts differently. The claim is therefore limited to the proved fixed-\(h\) law and does not assert a new closed formula for all local preimage trees.

## Value

**PASS.** The result answers a motivated question posed by the recent source and upgrades a qualitative per-sequence bound to an exact, finite, computable distribution across all starts. The need to group equal first-hit times from different primes is a genuine structural feature, not a routine substitution. The \(h=65\) example demonstrates a nonzero two-failure class and gives an exact benchmark.

Self-review: passed. Independent audit: not yet performed.
