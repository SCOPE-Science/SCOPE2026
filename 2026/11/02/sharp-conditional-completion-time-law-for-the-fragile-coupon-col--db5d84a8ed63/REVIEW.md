# Scientific review

## Correctness — PASS

The survival-weighted geometric stage decomposition follows from independent coupon draws and the exact exposure statistic in the motivating paper. The conditional stage probability is rederived in RESULT.md, including geometric normalization. The sharp constant is not inferred from finite enumeration: an exact Radon–Nikodym density of the finite stage-vector law with respect to the limiting product-geometric measure is proved; its scaled difference converges in \(L^1\) to \(\alpha_s-M\), using the integrable partition size as a dominating function. Projection onto the part count gives the signed \(\ell^1\) expansion. Classical partition generating functions identify the coefficient \(h_k\). Numerical checks reproduce the finite subset-state probability recurrence and the first-order asymptotics, but are supplementary. One nonnegative integrable domination inequality for the density is explicitly proved in RESULT.md.

## Originality — PASS (historical priority qualified)

The motivating Kleiner paper's Sections 2 and 8 were compared directly. It already gives independent ordinary waiting stages and their weighted exposure, so these are not claimed as novel. The paper expressly identifies the conditional completion-time distribution as a future problem and does not state the \(n^{-1}\) total-variation expansion, its explicit coefficient, or a Boltzmann partition interpretation. Euler's \(q\)-binomial theorem already gives the limit partition coefficients, so the new claim is the conditioned coupon-collector limit with exact first-order signed \(\ell^1\) error. Related Boltzmann partition literature considers distinct partition spaces and scales. No equivalent covering statement was located in the indexed mathematical research comparisons. Older conditioned-geometric and partition literature could contain an equivalent formula; that residual risk is not eliminated by searches.

## Mathematical value — PASS

The motivating source explicitly asks for the successful-run conditional completion-time distribution. When fragility is fixed, successes are very rare, so the ordinary coupon-collector extreme-value law does not describe completion within successful runs. The result gives the natural limiting law, exact discrete masses and moments, and a sharp, strictly positive, computable error coefficient, not merely an easy finite-stage restatement. The signed \(\ell^1\) expansion also localizes which completion times contribute to the approximation error. It treats only uniform independent sampling and fixed \(s\in(0,1)\).

Self-review: passed. Independent audit: not yet performed.
