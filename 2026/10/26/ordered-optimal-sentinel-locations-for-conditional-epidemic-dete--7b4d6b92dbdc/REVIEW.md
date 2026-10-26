# Scientific review: conditional epidemic detection on paths

## Correctness — PASS

The exact path-distance law gives unconditional detection probability \(F_j/(n-1)\) and conditional mean \(pF_j'/F_j\). A one-step inward sentinel relocation changes only two distance terms, producing an explicit sign test. Its comparison function is strictly decreasing while the conditional mean is strictly increasing, so each nontrivial adjacent comparison switches exactly once. A strict hyperbolic-cotangent inequality orders every switch, proving a global centerward progression on all path lengths. The endpoint exception, reflection symmetry, full range \(0<p<1\), and the five-vertex square-root threshold are covered. The bundled verifier checks finite examples with exact rational state enumeration; it is corroboration, not the proof of the infinite statement.

## Originality — PASS, with residual risk

The exact all-path phase ordering is not established in the inspected Christakis–Fowler 2010 empirical sentinel study, Sun et al. 2014 network simulation, Ciccolini et al. 2014 multi-hospital optimization, or Holme 2017 small-graph continuous-time SIR analysis. Holme already introduced a *conditional* discovery-time objective, and this antecedent is explicitly acknowledged rather than presented as novel. Its distinct timing dynamics and finite-graph analysis do not imply the independent-edge deterministic-delay all-path threshold theorem. Related earlier path vaccination and two-seed influence results have different objectives. There is residual risk of the same phase ordering existing under logarithmic derivatives of exponential distance sums, and independent bibliographic review remains appropriate.

## Mathematical value — PASS

The result gives a complete decision diagram for the conditional speed-versus-coverage conflict at every path size, including exact uniqueness and ordering of all thresholds, nonempty intervals for every possible intermediate location, and a sharp minimum size. This is a structural classification of a practically motivated early-warning statistic, not an arbitrary finite calculation. It also warns that a conditional-latency measure alone can favor a lower-probability surveillance site.

## Scope and risks

Independent homogeneous contacts; one uniformly located nonsentinel source; fixed unit traversal time; no repeated attempts or latent/recovery delays. This is not a statistical or empirical performance guarantee. The literature comparison is strong for the cited directly relevant sources, but an unlocated exact exponential-family optimality result is possible. No independent scientific audit was performed.

Self-review: passed. Independent audit: not yet performed.
