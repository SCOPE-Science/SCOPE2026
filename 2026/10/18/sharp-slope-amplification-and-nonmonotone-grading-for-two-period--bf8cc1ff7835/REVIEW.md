# Self-review

**Correctness — PASS.** The stated infinite Gram operator is strictly diagonally dominant. The two-step positive Green recurrence fixes the unique decaying solution, and the alternating-sign affine kernel can be integrated exactly; the two cell classes exhaust all possible slopes. The special-value derivatives and comparisons were reconstructed from the formula. Independent finite-period inversion checks passed for both edge types over nine ratios. Finite numerics do not establish the infinite result.

**Originality — PASS within examined evidence.** The full texts of Passenbrunner–Shadrin (2013), Foucart (2005 preprint), Foucart's related open-questions note, and Passenbrunner (2016) were compared by mathematical implication. They address generic spline projection max-norm or convergence and inverse-Gram bounds, not the two-periodic sharp derivative norm or its nonmonotonicity. An existing exact two-periodic projector max-norm and an existing uniform periodic projector gradient norm were separately compared; neither implies the graded gradient classification. Semantic database searches for two-periodic spline gradients and exact parameter values returned no equivalent statement. This is not proof of priority. Jia's 1987 multiple-geometric-mesh paper remained inaccessible and is a specific risk.

**Value — PASS.** The sharp gradient stability invariant is natural for approximation and finite-element slope control. The exact full-parameter two-branch formula establishes a qualitative instability of mesh grading: a modest distortion can worsen the worst-case slope even though larger grading improves it. The derivative and finite special-value witnesses are mathematically meaningful beyond routine sup-norm stability estimates.

**Limitations.** Bi-infinite degree-one real-valued splines only; no uniqueness of optimal grading, no higher degree or general grids. Bibliographic historical priority remains open. Verification is same-model only.

Self-review: passed. Independent audit: not yet performed.
