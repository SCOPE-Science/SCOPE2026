# Scientific review: Sharp mean-crossing inequality for up to six weighted Bernoulli trials

## Correctness — PASS
For normalized six-coordinate weights, a coordinate of weight at least \(p\) alone yields probability at least \(p\); the only equality case occurs when its complement has weight below \(p\), equivalently a weight exceeds \(1-p\). In the complementary case all weights lie below \(p\). Dividing \(p\in(1/6,1/3]\) into three intervals, the proof gives explicit strictly positive rational-polynomial lower bounds. The difficult interval uses a 15-perfect-matching incidence argument, injection from losing triples to winning-edge triangles, and the complete six-vertex graph inequality \(t\le2k-8\). The supplied checker exhausts all \(2^{15}\) graph masks and verifies every positivity polynomial exactly; analytic inequalities prove all real-parameter claims. No finite sample is used as an infinite proof.

## Originality — PASS, subject to residual priority uncertainty
Milojević–Sudakov, arXiv:2606.30287 (2026-06-29), formulate the universal bound for every number of iid Bernoulli variables and all \(p\le1/3\). The inspected original article proves only very small positive \(p\) for arbitrary numbers of summands and credits isolated reciprocal-integer values; it does not supply the full continuum for \(m\le6\) or the equality classification. Fokkink–Meester–Pelekis's optimal-stakes paper studies upper-tail maxima, not a lower-tail minimum over normalized weights. Alon–Huang–Sudakov's MMS bounds on much larger systems do not imply the finite six-coordinate theorem. Public mathematical-record and literature queries found no covering theorem, but unindexed equivalent results remain a risk; search absence is not proof of novelty.

## Mathematical value — PASS
The exact cutoff at six variables and exhaustive equality characterization settle a nontrivial natural finite-dimensional subfamily of an explicitly stated 2026 probability-theoretic conjecture for the conjectured full \(p\) interval. The matching–triangle constraint gives a structural explanation rather than an arbitrary numerical instance. This is not a theorem for \(m\ge7\), and no optimality of the internal lower-bound polynomials is claimed.

## Sources and limitations
Principal source: A. Milojević and B. Sudakov, *On the Probability a Weighted Bernoulli Sum Exceeds Its Mean*, arXiv:2606.30287 (2026-06-29). Comparison: R. Fokkink, L. Meester and C. Pelekis, *Optimizing stakes in simultaneous bets*, arXiv:2002.06804; N. Alon, H. Huang and B. Sudakov, *Nonnegative k-sums, fractional covers, and probability of small deviations*, arXiv:1104.1753. Source-access and unindexed-priority limitations are recorded in the structured audit.

Self-review: passed. Independent audit: not yet performed.
