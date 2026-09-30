# Independent Audit — 2026-09-29

**Record:** `2026/09/20/heavy-ball-real-root-acceleration-barrier--5f3230b80158`  
**Title:** Uniform real-root barrier for fixed-parameter heavy-ball acceleration  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `0378bf6711fa5def2e60f85f110311c5bd0f734f`  
**Disposition:** **PASSED**

## Three-axis assessment

- **Correctness — PASS:** The real-root dichotomy is correct. With t=sqrt(beta), s_lambda=1+t^2-alpha lambda is a connected decreasing interval; if every modal discriminant is nonnegative, the interval cannot cross (-2t,2t), so either s_L>=2t or s_mu<=-2t. On the positive branch the best admissible step is alpha=(1-t)^2/L and the largest root at mu is strictly worse than 1-mu/L, hence worse than optimal gradient descent. On the negative branch the endpoint-L magnitude is bounded below using alpha mu>=(1+t)^2, and the polynomial evaluated at q_GD is negative for 0<t<q_GD; for t>=q_GD the root product already gives the bound. The t=0 case reduces to the standard minimax gradient-descent balance. I also performed randomized interval scans over condition numbers 1.1 to 100 and found no all-real parameter pair below q_GD.
- **Originality — PASS:** The complete Torii–Hagan (2002) paper was obtained through authorized institutional access after OA/preprint routes did not provide it. It analyzes real/complex modal roots, stability, and a generally fastest momentum choice for a fixed learning rate, but it does not state the present continuous-interval minimax problem constrained to all-real roots or the exact conclusion that the constrained optimum collapses uniquely to optimal gradient descent. Zhang (2015) advertises globally optimal double parameters for fastest convergence without this all-real constraint. Later heavy-ball analyses located likewise discuss optimal tuning and oscillatory/complex regimes rather than this converse barrier. The precise constrained theorem therefore passes originality to the best of the evidence.
- **Scientific value — PASS:** The theorem gives a sharp structural necessity for interval-robust acceleration: strict improvement over optimal fixed-step gradient descent requires an oscillatory complex-root regime somewhere in the curvature interval. This cleanly separates acceleration from overdamped/nonoscillatory behavior and is useful for interpreting heavy-ball tuning.

## Independent findings
- Continuity of s_lambda reduces the all-real condition to exactly two branches, positive or negative, eliminating mixed-sign real-root configurations across a connected curvature interval.
- Equality at the gradient-descent factor occurs only at beta=0 and alpha=2/(L+mu).
- The stronger nonnegative-root restriction has optimum beta=0, alpha=1/L with factor 1-mu/L, so positive momentum strictly worsens the best nonoscillatory rate.
- Torii–Hagan's full five-page article contains the complex-root threshold and stability cases but not the audited interval-constrained minimax converse.

## Independent checks
- Re-derived the positive-branch polynomial test at r=1-mu/L.
- Re-derived the negative-branch q_GD test after substituting kappa=(1+q)/(1-q).
- Ran independent randomized interval scans across several condition numbers; no all-real counterexample below q_GD appeared.
- Read the complete Torii–Hagan (2002) text through authorized institutional access and compared its statements with the filed theorem; checked Zhang (2015) and later-paper abstracts for scope.

## Literature evidence
- https://doi.org/10.1109/TNN.2002.1000143 — Torii–Hagan (2002), complete text obtained via authorized institutional access; treats modal root regimes and stability but not the filed all-real interval-minimax converse.
- https://doi.org/10.1162/NECO_a_00710 — Zhang (2015); abstract states simultaneous globally optimal learning-rate and momentum parameters for fastest convergence, without the filed all-real constraint.
- https://arxiv.org/abs/1811.00658 — Danilova–Kulakova–Polyak; modern analysis of heavy-ball non-monotonicity and classical complex/repeated root behavior.
- https://doi.org/10.1007/s10957-023-02261-w — Hagedorn–Jarre fixed-step spectral analysis context.

## Limitations
- The result concerns fixed alpha and nonnegative beta<1 for exact-gradient strongly convex quadratics and the full continuous curvature interval.
- It does not say every accelerated finite matrix has an actual complex-root eigenmode if its spectrum skips the complex interval.
- The complete Zhang (2015) theorem text was not independently obtained in this run; its abstract and secondary indexing were inspected, leaving a residual originality caveat.

The assigned source tree remained unchanged from the inventory/source-tree-check interval through current main commit `eff2c6312cec5b0dee5115e5f42211a853092dfb`; the exact tree audited is `0378bf6711fa5def2e60f85f110311c5bd0f734f` and matches the assignment guard. GitHub was used only as read-only evidence; no repository writes were made. Audit timestamps and this audit-file date use UTC under the task-specific audit contract.
