# Self-review

**Correctness (PASS).** Proposition 4.3 of [1] supplies the universal upper bound. The affine counterexample gives the exact matching residual \(2r-1\) for every real \(r\geq1\); at \(r=1\) the original certificate is saturated. Its unique optimum, optimal multiplier, strict Slater point, and global quadratic-growth modulus are computed explicitly in the proof. `CHECK.py` supplies independent-of-floating-point arithmetic spot checks; the quantifier over all real ratios is established algebraically rather than experimentally.

**Originality (PASS, subject to literature coverage).** The primary source's Proposition 4.3 states and proves the upper transfer bound but does not state or supply worst-case attainment. Pages 13--17 and remaining results/appendices were inspected for stronger coverage. The specific lower-bound construction and its invariance to all cutting-plane additions are not implied by an upper bound alone. Targeted published-record searches for the source identifier, the coefficient, the constrained certificate, and exact affine sharpness found no directly covering record. Searches do not prove absolute novelty.

**Value (PASS).** This answers the natural optimal-constant question for the very transfer inequality used by penalty-parameter adaptation. The loss cannot be reduced just by introducing more cuts, and ordinary regularity such as strict feasibility, a unique optimizer, and global quadratic growth does not improve the worst case. These obstructions delimit possible future certificate-design improvements: additional information or a new candidate is required to beat the factor uniformly.

**Closest literature and risks.** Lin--Zhang [1] provides the upper transfer statement and its proof; the unconstrained APEX predecessor described there does not have this penalty update. The main remaining risk is unindexed or unpublished sharpness work. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
