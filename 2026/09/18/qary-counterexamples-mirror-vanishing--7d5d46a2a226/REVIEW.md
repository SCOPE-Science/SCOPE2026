# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The construction was checked directly from its two generator vectors. Every nonzero multiple of the second generator has weight d. Every codeword with nonzero coefficient on the all-one generator has d+1 coordinates that cannot vanish; among the first d coordinates, cancellation can occur only on positions carrying one specified nonzero field value. Balancing those values bounds the number of cancellations by m=ceil(d/(q-1)), so such a word has weight at least 2d+1-m=d+t+1. Hence the claimed local gap is complete. Nonzero multiples of the all-one vector have weight 2d+1, so the first weight forbidden by the literal mirror conclusion is present. The dimension condition holds with equality.

The exact enumerator follows by grouping the q-1 nonzero ratios beta/alpha according to which field value they cancel. A standalone finite check reproduced the formula for prime q in {3,5,7,11,13} and d from 2 through 14. The general proof uses only finite-field arithmetic and therefore covers all prime powers q>2.

Adversarial checks included the edge cases q=3 and d=2, exponent collisions in the enumerator when d is divisible by q-1 or when some nonzero symbols are unused, and the binary specialization. In the binary specialization the sole nonzero symbol has multiplicity d, producing a weight-(d+1) word; therefore the construction does not satisfy the binary gap hypothesis and does not conflict with the published binary theorem.

## Originality

Originality is assessed to the best of our knowledge. The 17 September 2026 source explicitly proves only the binary theorem and states that a q-ary analogue needs additional assumptions. Its MDS discussion does not itself instantiate the theorem's gap hypothesis, since MDS codes have all weights from d to n. The present family instead satisfies the same dimension and gap hypotheses while violating the proposed mirror conclusion.

Searches covered the exact source title and arXiv identifier, q-ary/ternary mirror-vanishing terminology, the parameter pattern [2d+1,2,d]_q, and synonymous weight-gap formulations. No prior statement of this all-q>2 counterexample family was located. The code family itself is elementary and is not claimed as a new code construction independent of this application. Older work on q-ary minimal codes, few-weight codes, or catalogues of two-dimensional linear codes may contain equivalent codes without the mirror interpretation. Because the source is extremely recent, simultaneous or poorly indexed responses remain a significant residual risk.

The full text of the motivating arXiv paper and the Ashikhmin--Barg minimal-vector source were available for the relevant statements. No inaccessible source is known whose title or abstract strongly suggests that it already contains the mirror counterexample; the principal residual risk is instead terminology mismatch or near-simultaneous work.

## Value

The result supplies what the motivating paper's MDS example does not: a counterexample satisfying the literal hypotheses of the binary mirror theorem. It does so uniformly over every nonbinary finite field and with local gaps that grow without bound for each fixed q>2. The construction also identifies a simple algebraic reason for the binary/nonbinary split: multiple nonzero field values allow partial rather than total cancellation of a minimum-weight support.

## Limitations

The result refutes only the literal same-form q-ary extension. It does not preclude q-dependent thresholds or additional structural hypotheses that restore a mirror theorem. The computational artifact checks only prime fields and is supplementary; the proof is the evidence for prime-power fields. No independent validation, formal verification, or peer review is asserted.
