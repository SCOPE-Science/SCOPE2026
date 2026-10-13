# Self-review

## Correctness

**PASS.** The claim is a Haar-generic theorem, not an inference from random trials. The diagonal pair products give the sharp possible dimensions \(3,7,13,16\). The attached exact verifier supplies a Gaussian-rational Cayley witness whose ranks over a finite-field reduction certify the required characteristic-zero minors for both local parties. Nonzero real-analytic minors have zero sets of Haar measure zero, giving the generic ranks. Cohen's first-round condition then yields LOCC impossibility for \(m\le4\); for \(m\ge5\), a small Hermitian perturbation of the identity coefficient matrix supplies a genuine positive two-outcome local first measurement.

## Originality

**PASS.** The direct 2016 source reports 100 numerical samples for each random-unitary case and describes a sharp transition around global dimension \(D\). In the two-qubit critical case \(N_u=D=4\), it reports numerically that neither party can measure first. The accepted theorem turns that observation into an exact Haar-almost-sure statement and proves full pair-product span from five unitaries onward. The inspected 2019 LOCC resource-bounds paper does not contain this random-unitary threshold, and targeted searches found no implication-equivalent theorem.

## Value

**PASS.** This is a natural analytic closure of an explicit numerical phenomenon in a standard LOCC-impossibility method. It isolates the exact two-qubit threshold, explains the source's critical \(m=4\) behavior by dimension geometry, and sharply separates what is proved below and above the threshold. The result does not overclaim that vanishing of the first-round obstruction implies LOCC.

Closest literature is Cohen's 2016 channel-impossibility paper; the principal limitation is specialization to two qubits and Haar-generic unitary tuples. A differently worded later proof remains a residual literature risk.

Self-review: passed. Independent audit: not yet performed.
