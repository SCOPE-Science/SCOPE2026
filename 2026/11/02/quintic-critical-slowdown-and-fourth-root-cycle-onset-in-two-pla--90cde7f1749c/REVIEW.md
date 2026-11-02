# Self-review

## Correctness — PASS
The best-response rule is derived from strict payoff concavity on the positive branch and substituted into one round's return map. At the cost boundary \(c_*=3-2\sqrt2\), an exact symbolic computation over \(\mathbb Q(\sqrt2)\) verifies cancellation of quadratic, cubic, and quartic terms in the two-round map, with first nonlinear term \(-Kz^5\), where \(K=50688-35840\sqrt2>0\). A local monotone contraction in magnitude, together with fourth-power reciprocal increments, establishes the signed \(k^{-1/4}\) relaxation. Analytic perturbation and four-zero counting establish precisely one nearby primitive two-cycle below the boundary, the \(\delta^{1/4}\) displacement and its leading multiplier. The bundled exact checker and numerical branch tests executed successfully; finite tests are corroboration, not an infinite proof.

## Originality — PASS, with priority risk
Ghosh and Goldberg, *Best-Response Dynamics in Lottery Contests* (arXiv:2305.10881v1), introduces the same response model and asymmetric behavior. Ghosh, *Best-Response Dynamics in Tullock Contests with Convex Costs* (arXiv:2310.03528v2), proves results in more general payoff classes but not the present nonlinear scaling. Milchtaich and Zahojay's 2023 stability test is linear and neutral at the boundary. Critically, an accessible earlier exact result on this identical map already proves the global convergence threshold and nearby period-two existence; **the present novelty claim does not include those facts**, which do not imply the quintic coefficient, critical rate constant or cycle amplitude. Four concrete semantic published-finding searches and previously recorded mathematical claims were compared with exact implications. Different nomenclature or unindexed specialist results remain a genuine priority risk.

## Value — PASS
The critical return-map degeneracy is a mathematically meaningful exception to generic cubic-flip behavior. The exact local rate, fractional-power amplitude and multiplier quantify a transition whose location was already known but whose transient scaling was not. Such rates matter for the number of alternating response rounds required near equilibrium. This is a local result only, not an assertion about arbitrary starting positions or off-model costs.

## Limits and sources
The claimed rate is for two-round iterates; each two-round iterate is four individual best-response moves. Local positivity is essential. No global basin estimate, other-period census or independent priority certification is supplied. Primary sources are arXiv:2305.10881v1, arXiv:2310.03528v2 and the 2023 Milchtaich–Zahojay Tullock manuscript. Detailed implication comparisons, source inspections and outstanding risks appear in `AUDIT.json`.

Self-review: passed. Independent audit: not yet performed.
