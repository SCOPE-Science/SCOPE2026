# Scientific review

## Correctness — PASS

For all finite rectangular real matrices and the stated strictly positive quadratic curvatures, exact substitution into Algorithm 1 of Condat–Sadiev–Richtárik yields the two-variable singular-mode matrix displayed in the finding. The real quadratic Schur/Jury inequalities have two terms that are strictly positive without parameter restrictions, and the remaining term is precisely the stated bound. Testing the maximal singular value is necessary and sufficient. An eigenvalue \(-1\) arises at equality and an eigenvalue below \(-1\) above it; scalar initializations attain both boundaries. Averaged iterates inherit convergence from their stable scalar filters. Exact-rational checker and independent eigenspectrum tests support, but do not replace, the proof.

## Originality — PASS, with residual risks

The motivating APAPC paper provides a generic sufficient coupling condition rather than the present necessary-and-sufficient finite-curvature quadratic classification. Li–Yan's primal–dual papers already provide the undamped \(4/3\) threshold and essentially the core spectral method, so that endpoint is fully acknowledged. Luke–Shefi study related PAPC linear convergence under different assumptions. Published-research searches also returned related primal–dual numerical-stability results but not an implication covering the exact fixed-parameter APAPC condition with both quadratic curvatures and its unbounded-dual-step regime. No claim of exhaustive unpublished or unindexed coverage is made.

## Value — PASS

The exact stability phase determines when the dual step has a finite ceiling and when no finite ceiling is required. This is a structurally motivated question raised by conservative coupling conditions in a recent primal–dual algorithm. In a concrete, strictly positive-curvature example it permits arbitrarily large dual steps despite a generic \(\tau\leq2\) sufficient restriction. The result is limited to the quadratic autonomous specialization, not a general nonlinear convergence theorem.

## Closest literature and limitations

Condat–Sadiev–Richtárik (2026), Algorithm 1 and Theorem 3.3: APAPC and sufficient Lyapunov steps. Y. Li–M. Yan (2022), Section 3.2: the sharp undamped \(4/3\) limit and characteristic-root method. Z. Li–M. Yan (2017/2021), Sections 1–2.5: related PAPC/PDFP\(^{2}\)O general-step analysis. Luke–Shefi (2017), Section 3: related PAPC linear convergence. Remaining risks include unindexed equivalent LMI/spectral parametrizations and lack of generality beyond strictly positive isotropic quadratic curvatures.

Self-review: passed. Independent audit: not yet performed.
