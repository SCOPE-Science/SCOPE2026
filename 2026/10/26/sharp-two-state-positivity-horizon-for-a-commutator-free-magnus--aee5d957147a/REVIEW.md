# Scientific review: Sharp two-state positivity horizon

**Correctness — PASS.** For column Markov generators with a common total rate, the exact quadratic matrix identity makes each exponential affine in its generator. The ordered product reduces to two explicit rates whose sum is \(1-e^{-hs}\). Nonnegative off-diagonals are necessary and sufficient for stochasticity; the coefficient \(eta+lpha e^{-hs/2}\) changes sign at the stated sharp cutoff. The explicit one-way and perturbed irreducible witnesses demonstrate necessity. Exact symbolic and seeded numerical checks in `verify.py` agree with the proof.

**Originality — PASS (best knowledge).** The motivating Magnus paper defines the algorithm and states a sufficient positivity criterion for each factor, but its relevant sections do not provide the exact endpoint threshold or the complete rate classification. The Hofstätter--Koch theorem addresses coefficient positivity for order-five-plus exponential integrators, not the Markov endpoint. Targeted mathematical searches and comparisons with related positivity-frontier records did not identify covering implications. A general older binary Markov-product result might still cover the theorem; independent priority review is outstanding.

**Value — PASS.** An exact sharp threshold for **endpoint** positivity when individual matrix exponentials are not positive measures a genuine reliability margin for a published higher-order method, directly addressing its stated almost-positivity problem. Equal total relaxation rate permits arbitrary directional asymmetry; the complete supercritical inequalities and irreducible sharpness witness make the result a natural two-state classification rather than a numerically tuned example.

**Scope and limitations.** Two states, common positive total exit intensity, exact matrix exponentials, and exactly the displayed endpoint composition, not the full nonlinear scheme or higher-dimensional/unequal-rate cases. The cutoff is uniform across the class, not necessarily sharp for a fixed pair. Computer tests are only supporting checks. Self-review is not independent validation.

Self-review: passed. Independent audit: not yet performed.
