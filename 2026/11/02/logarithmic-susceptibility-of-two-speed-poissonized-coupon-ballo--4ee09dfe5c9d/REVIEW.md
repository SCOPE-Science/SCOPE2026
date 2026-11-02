# Scientific assessment

## Correctness — PASS

The precise object is a pair of independent Poisson first-arrival coupon processes with a common two-speed label profile, fixed finite positive group sizes, and a right derivative in the slow rate. The full proof reduces the event to a Dyck arrival word, computes the single early-slow hazard, counts the fast balanced words by the first visit to height \(-1\), and sums the resulting inverse remaining-fast rates as harmonic differences. Analyticity of the finite exponential-race recursion controls the fixed-size remainder. The large-group asymptotic uses uniform central-binomial bounds and a summable Catalan majorant. The supplied independent rational/event-enumeration checker produced 137 assertions with no failures. Finite checks corroborate but do not prove the infinite assertions. The endpoint is a limit, and there is no unproved simultaneous \(m\)-versus-rate assertion.

## Originality — PASS (best-knowledge, residual historical risk)

Long (2026, arXiv:2605.09641v1, reviewed in original full text including introduction, discrete-state recursion and final directions) proves a \(2/d\) limit for **simultaneous-round uniform** two-player competition. Myers–Wilf (2003, arXiv:math/0304229v1, reviewed in original text introduction and two-player section) give discrete-time finite formulas. Neither formulation implies the present rate-perturbed **independent-clock** ballot probability, its first derivative, or logarithmic coefficient merely by a change of variables. Classical Dyck enumeration gives the zeroth-order limit but not the new first-order weighting of early slow arrivals. Relevant indexed-search comparisons including balanced nonuniform reset collectors involve distinct restarted models. No directly covering identity emerged from the actual targeted searches; failed search is not proof of priority. Residual risk: an older weighted exponential-arrival ballot enumeration may contain this rational first variation.

## Mathematical value — PASS

Heterogeneous coupon speeds are a motivated extension of a two-collector ballot question. The theorem gives a sharp sensitivity to the first breakdown of complete timescale separation, with strictly positive derivative and a nontrivial \((\log m)/m\) decay that is not apparent from independent Catalan blocks. It quantifies how even a very rare slow arrival destabilizes the separated fast/slow ballot law, and supplies an exact finite expression for arbitrary natural group sizes rather than an arbitrary fixed parameter example. This contribution is limited in scope and not a solution of the simultaneous-round generalization.

## Closest literature and limitations

Long, *The Ballot Event for Two-Player Coupon Collection* (2026); Myers–Wilf, *Some New Aspects of the Coupon-Collector's Problem* (2003); classical Catalan ballot/reflection enumeration. Mathematical-record searches were inconclusive concerning older weighted clock-order results. No independent audit or exhaustive historical-priority verification has been performed.

Self-review: passed. Independent audit: not yet performed.
