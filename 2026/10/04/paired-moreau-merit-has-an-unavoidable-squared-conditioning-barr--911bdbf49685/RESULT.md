# Paired Moreau merit has an unavoidable squared-conditioning barrier on balanced indefinite quadratics
## Finding
Consider the quadratic
\[
E(x)=\frac12 x^{\mathsf T}Ax,
\qquad
A=\operatorname{diag}(-L,-\mu,\mu,L),
\qquad 0<\mu<L.
\]
It belongs to the symmetric uniformly nondegenerate class with positive and negative curvature magnitudes between \(\mu\) and \(L\). In the symmetric-endpoint paired signed-Moreau construction of Su, Zhang, and Zhao, the centering constant is \(c=0\). Let the two admissible regularization parameters be arbitrary numbers \(\Lambda_+>L\) and \(\Lambda_->L\). Then the merit Hessian is diagonal in the eigenbasis of \(A\), and its eigenvalue on a mode \(A u=\lambda u\) is exactly
\[
h(\lambda)=\frac{\lambda^2}{(\Lambda_+-\lambda)(\Lambda_-+\lambda)}.
\]
If \(\kappa=L/\mu\), the merit condition number \(\kappa_V\) obeys
\[
\kappa_V
\ge
\kappa^2
\sqrt{
\frac{(\Lambda_+^2-\mu^2)(\Lambda_-^2-\mu^2)}
{(\Lambda_+^2-L^2)(\Lambda_-^2-L^2)}
}
>\kappa^2.
\]
The infimum over all admissible \(\Lambda_+\) and \(\Lambda_-\) is \(\kappa^2\), approached as both parameters tend to infinity. Therefore the paired-Moreau merit cannot be better conditioned than the squared residual on this balanced four-mode family. The best fixed scalar gradient step on the exact merit has sharp worst-mode Euclidean factor
\[
q_* = \frac{\kappa_V-1}{\kappa_V+1}
>
\frac{\kappa^2-1}{\kappa^2+1},
\]
with infimum \((\kappa^2-1)/(\kappa^2+1)\) over the admissible merit parameters.

## Assumptions and scope
The result concerns the exact paired signed-Moreau merit for a centered quadratic with the four eigenvalues \(-L,-\mu,\mu,L\). Both curvature signs and both endpoint magnitudes are present. The two Moreau regularization parameters may be unequal but must satisfy \(\Lambda_+>L\) and \(\Lambda_->L\), as required for the corresponding signed proximal subproblems to be single-valued on this quadratic. The outer method considered in the rate statement is fixed-step gradient descent applied to the exact merit. No approximation error from the inner proximal solves is included.

The claim does not assert a lower bound for accelerated, variable-step, preconditioned, Krylov, or other algorithms, and it does not assert that the stationary-point problem itself has squared condition-number complexity. It isolates the conditioning of this particular scalar merit and its fixed-step gradient descent.

## Proof
For an eigenmode with eigenvalue \(\lambda\), write its scalar coordinate as \(z\). The positive signed proximal maximizer satisfies
\[
\frac{\lambda}{\Lambda_+}y_+=y_+-z,
\qquad
 y_+=\frac{\Lambda_+}{\Lambda_+-\lambda}z,
\]
so its displacement is
\[
y_+-z=\frac{\lambda}{\Lambda_+-\lambda}z.
\]
The negative signed proximal maximizer satisfies
\[
-\frac{\lambda}{\Lambda_-}y_-=y_--z,
\qquad
 y_-=\frac{\Lambda_-}{\Lambda_-+\lambda}z,
\]
and hence
\[
y_--z=-\frac{\lambda}{\Lambda_-+\lambda}z.
\]
For symmetric spectral endpoints the paired construction has \(c=0\), so its weights reduce to
\[
w_+=\frac{\Lambda_+}{\Lambda_++\Lambda_-},
\qquad
w_-=\frac{\Lambda_-}{\Lambda_++\Lambda_-}.
\]
The merit gradient is the weighted sum of the two proximal displacements. Therefore its scalar derivative is
\[
\begin{aligned}
\nabla V_\lambda(z)
&=\left[
\frac{\Lambda_+}{\Lambda_++\Lambda_-}\frac{\lambda}{\Lambda_+-\lambda}
-
\frac{\Lambda_-}{\Lambda_++\Lambda_-}\frac{\lambda}{\Lambda_-+\lambda}
\right]z\\
&=\frac{\lambda^2}{(\Lambda_+-\lambda)(\Lambda_-+\lambda)}z.
\end{aligned}
\]
Thus \(V\) is a positive-definite quadratic and its Hessian eigenvalue is \(h(\lambda)\) as stated.

Let \(h_{\max}\) and \(h_{\min}\) be the largest and smallest of the four positive numbers \(h(-L),h(-\mu),h(\mu),h(L)\). Since the maximum of two positive numbers is at least their geometric mean and the minimum of two positive numbers is at most their geometric mean,
\[
\frac{h_{\max}}{h_{\min}}
\ge
\sqrt{\frac{h(L)h(-L)}{h(\mu)h(-\mu)}.
\]
Direct multiplication gives
\[
h(t)h(-t)
=
\frac{t^4}{(\Lambda_+^2-t^2)(\Lambda_-^2-t^2)}.
\]
Consequently
\[
\kappa_V
\ge
\left(\frac{L}{\mu}\right)^2
\sqrt{\frac{(\Lambda_+^2-\mu^2)(\Lambda_-^2-\mu^2)}{(\Lambda_+^2-L^2)(\Lambda_-^2-L^2)}.
\]
Each ratio \((\Lambda_\pm^2-\mu^2)/(\Lambda_\pm^2-L^2)\) is strictly larger than one, so every finite admissible parameter pair gives \(\kappa_V>\kappa^2\). Conversely, as \(\Lambda_+\to\infty\) and \(\Lambda_-\to\infty\), all four Hessian eigenvalues are a common factor \((\Lambda_+\Lambda_-)^{-1}\) times \(\lambda^2(1+o(1))\), so \(\kappa_V\to\kappa^2\). This proves the sharp infimum.

For a positive-definite quadratic with extreme Hessian eigenvalues \(m_V\) and \(M_V\), fixed-step gradient descent has worst-mode factor \(\max\{|1-\eta m_V|,|1-\eta M_V|\}\). Its minimum over scalar \(\eta\) occurs at \(\eta=2/(m_V+M_V)\) and equals \((\kappa_V-1)/(\kappa_V+1)\). Substitution of the preceding lower bound yields the stated contraction obstruction. For large \(\kappa\), the limiting best factor is \(1-2/\kappa^2+O(\kappa^{-4})\), so fixed-step outer gradient descent has a worst-case \(\Theta(\kappa^2\log(1/\varepsilon))\) iteration scale on this family.

## Verification
The bundled script `verify_paired_merit.py` independently evaluates the proximal displacements, the closed-form Hessian eigenvalues, the geometric-mean lower bound, and the optimal fixed-step contraction on several admissible parameter pairs. It uses only the Python standard library. Its expected terminal line is `VERIFY_OK`.

The analytic proof, rather than the finite numerical checks, establishes the result for all \(0<\mu<L\) and all finite \(\Lambda_+>L\), \(\Lambda_->L\).

## Relationship to prior work
Su, Zhang, and Zhao introduce uniform nondegeneracy, pair signed Moreau envelopes into a smooth merit, and analyze paired proximal descent with a dimension-free global linear rate. Their full text also relates the merit to the squared gradient residual and gives a class-level deterministic lower benchmark whose symmetric dependence is on \(\kappa\), whereas their first-order upper complexity has the familiar squared endpoint dependence. The present calculation identifies a concrete structural reason that fixed-step descent on their merit cannot close that gap: on the balanced four-mode quadratic, every finite choice of the two regularization parameters has condition number strictly larger than \(\kappa^2\), and the best possible parameter limit is exactly the squared-residual condition number.

Hamiltonian gradient descent provides a neighboring squared-residual construction for minimax operators. On a linear symmetric operator, the squared residual naturally has Hessian proportional to \(A^2\), hence condition number \(\kappa^2\). The paired-Moreau calculation above shows that the new two-sided regularization approaches this same spectral barrier in the large-regularization limit and is strictly worse conditioned for every finite admissible pair on the balanced witness.

Targeted searches of published mathematical findings and the primary literature were compared at the level of statements and implications. No inspected source stated the all-parameter four-mode lower bound, its sharp infimum, or the resulting fixed-step contraction barrier. This is not an assertion that failed searching proves novelty; the residual literature risk is recorded below.

## Limitations
The obstruction is proved for the balanced four-mode quadratic and fixed scalar gradient descent on the exact paired merit. It does not cover asymmetric spectral endpoint classes, alternative centering rules, adaptive or accelerated outer methods, matrix preconditioning, or inexact inner-solve cost. The source paper's general theory is broader than this quadratic witness. An older result in proximal-average, rational-filter, or stationary-equation literature could contain an equivalent spectral calculation under different terminology; the searches performed here did not locate one.

## References
1. H. Su, L. Zhang, and J. Zhao, *First-Order Optimization under Uniform Nondegeneracy: Geometry, Computation, and Information*, arXiv:2609.06946v1, first submitted 2026-09-07. See the uniformly nondegenerate class, paired signed-Moreau construction, paired proximal descent, related discussion of squared residuals, and deterministic lower-bound discussion.
2. J. Abernethy, K. A. Lai, and A. Wibisono, *Last-Iterate Convergence Rates for Min-Max Optimization: Convergence of Hamiltonian Gradient Descent and Consensus Optimization*, Proceedings of Machine Learning Research 132 (2021), 3--47.
