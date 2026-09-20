# Same-model review

## Correctness

**PASS.** The central criterion reduces to the topology built into the definition of a Steinberg algebra. If a singleton characteristic function \(1_{\{\gamma\}}\) lies in \(A_R(\mathcal G)\), local constancy and \(1_R\neq0\) force \(\{\gamma\}\) to be open; the étale source map then makes \(\{s(\gamma)\}\) open. Conversely, if \(\{x\}\) is open, intersecting a compact open bisection through an arrow \(\gamma\in\mathcal G_x^x\) with \(s^{-1}(\{x\})\) produces the singleton \(\{\gamma\}\), which is compact open. This proves the equivalence without an unproved discreteness assumption.

The corner identification was checked from support: \(e_xAe_x\) consists of functions supported on \(\mathcal G_x^x\), and when \(x\) is isolated this isotropy fiber is discrete. Compact support is therefore finite, so the corner is exactly the group algebra. The same argument gives \(Ae_x\cong RL_x\).

The two-loop graph counterexample satisfies the source paper's hypotheses and has Cantor infinite-path space, hence no isolated units. Therefore the identity point mass \(1_{\{(x,0,x)\}}\) is absent from the Steinberg algebra, so the proposed algebra embedding is not defined.

The finite-dimensional graded obstruction is also exact: for isolated \(x\), each nonzero \(p\in\operatorname{Per}(x)\) gives an invertible homogeneous corner element of degree \(p\). Acting repeatedly on a nonzero homogeneous vector in \(e_xM\) produces nonzero vectors in pairwise distinct degrees, impossible in a finite-dimensional graded module.

## Originality

**PASS, to the best of our knowledge, with a narrow claim.** The general induction theory is not new. Nguyen--Nguyen (arXiv:2006.09931; later Journal of Algebra and Its Applications) explicitly treats Steinberg induction/restriction through isotropy group algebras. Clark et al. (arXiv:2502.15574), in their study of Steinberg-algebra socles, already identify open singleton corners with Laurent group algebras in the \(\mathbb Z^k\)-isotropy case.

Those sources substantially reduce the novelty of any generic “isolated point gives an isotropy corner” statement, and that fact is explicitly excluded from the originality claim. The contribution assessed here is the sharp application to arXiv:2609.20230v1: its Equation (4.1) and Proposition 4.1 use singleton point masses for every boundary path, while those functions exist exactly at isolated units. No source located in the targeted literature states this correction to that preprint, the two-loop counterexample, or the finite-dimensional graded periodicity obstruction in this form.

A residual risk remains because the isolation criterion is elementary and may occur implicitly or explicitly in older Steinberg-algebra literature under corner or open-unit terminology. The full text of every historical induction paper was not exhaustively inspected. This does not affect the mathematical correction of the cited 2026 statement, but it limits the breadth of the originality claim.

## Value

**PASS.** Proposition 4.1 is foundational for the source paper's Section 4: Definition 4.2, the tensor-Hom adjunction, flatness claim, weight-space action, and later restriction statements all use the asserted embedding. The result pinpoints the exact topological hypothesis needed for that construction, supplies a minimal legal graph where it fails, and identifies the correct corner formulation when the hypothesis holds. The graded obstruction further shows that nontrivial periodic isotropy and a nonzero finite-dimensional graded point fiber cannot coexist in the corrected isolated-point setting.

## Scope and limitations

The result concerns the specific point-mass embedding and restriction-of-scalars construction. It does not claim that isotropy representation theory fails at nonisolated units: standard Steinberg induction/restriction through source-fiber or germ constructions remains available and is prior art. It does not audit unrelated claims elsewhere in arXiv:2609.20230v1.

The coefficient ring is assumed nonzero, commutative, and unital so that the singleton-support argument detects the value \(1_R\). Originality is asserted only to the best of our knowledge. No independent validation, formal verification, or peer review is claimed.

**Same-model review: passed. Independent audit: not yet performed.**
