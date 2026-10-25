# Scientific review

## Correctness — PASS

The finite tree/retention model is explicit. Conditional growth of the retained vertex, total-component, and singleton-component counts gives a complete four-case transition distribution; this directly yields the covariance recurrence. The identities for the first moments and the two auxiliary cross-covariances follow, respectively, from forest edge counting, Bernoulli score differentiation, and the uniform attachment rule. Solving the resulting first-order recurrence by the product factor \(h_n\) proves the all-\(n\) formula. The gamma ratio, shifted harmonic bounds, and a manifestly positive polynomial establish the asymptotic coefficient for every fixed \(0<p<1\). An independent exact-rational checker exhaustively enumerates trees and site outcomes through seven vertices at three retention probabilities and verifies the recurrence at further sample sizes. Such finite computation supports but does not establish the general identity.

## Originality — PASS (with residual priority risk)

The full preprint by Gu and Yuan, arXiv:2408.12515, was inspected, including its Markov transition equation (1.5), law of large numbers, cluster scaling statements, and proof sections. That prior transition mechanism completely defines the model and is not new. Neither its stated main results nor the examined argument gives the explicit mixed covariance \(\operatorname{Cov}(K_n,I_n)\) or its linear coefficient. Kalay–Ben-Naim, arXiv:1409.7106, concerns mean fragment-size laws under fixed-number removal, not this finite independent-retention cross moment. Janson's *Uncovering a graph* studies total-component fluctuations, but no singleton–total cross covariance is identified there. Searches of related terms and mathematical-result records identified no stronger or equivalent theorem. The underlying published transition law in principle permits the new formula to be derived, so a prior unindexed or implicit derivation remains a historical-priority risk.

## Value — PASS

Both observables are natural cluster statistics: total retained components describe macroscopic fragmentation, while singleton components record the smallest fragments. Their dependence is not captured by the separately known first-order cluster proportions or by a total-component fluctuation theorem. The exact finite-sample mixed second moment and positive explicit linear asymptotic coefficient quantify this relationship for every fixed retention parameter, and the shifted-harmonic correction resolves finite-size behavior without simulation. No joint central limit theorem is asserted.

## Limits

The argument is specific to independently retained vertices on uniform random recursive trees, and it proves eventual rather than all-size covariance positivity. A same-paper transition kernel determines all finite distributions abstractly, but does not itself state this closed form. Historical priority is uncertain beyond the inspected sources; independent mathematical validation is outstanding.

Self-review: passed. Independent audit: not yet performed.
