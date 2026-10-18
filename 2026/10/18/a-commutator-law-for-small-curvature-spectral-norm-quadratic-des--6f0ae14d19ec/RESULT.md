# A commutator law for small-curvature spectral-norm quadratic descent

## Finding

Consider the unique minimizer \(D_\varepsilon\) of a strictly convex Kronecker-quadratic model over a matrix operator-norm ball. For every invertible real square gradient \(G=U\Sigma V^{\mathsf T}\), every symmetric positive-definite \(A,B\), and every radius \(\rho>0\), define \(M=U^{\mathsf T}BU\), \(N=V^{\mathsf T}AV\), and the skew-symmetric commutator \(C=MN-NM\). For all sufficiently small nonnegative \(\varepsilon\), the optimizer has **exactly flat singular values**, but its polar orientation generally changes:

\[
D_\varepsilon=-\rho U\exp(K(\varepsilon))V^{\mathsf T},\qquad
K_{ij}(\varepsilon)=-\frac{\varepsilon\rho C_{ij}}{\sigma_i+\sigma_j}+O(\varepsilon^2)\quad (i\ne j),
\]

where \(K\) is skew-symmetric and \(\Sigma=\operatorname{diag}(\sigma_1,\ldots,\sigma_n)\) with every \(\sigma_i>0\). The exact minimizer improves the quadratic surrogate over the unrotated matrix-sign step \(D_0=-\rho UV^{\mathsf T}\) by

\[
F_\varepsilon(D_0)-F_\varepsilon(D_\varepsilon)
=\frac{\varepsilon^2\rho^3}{2}
\sum_{1\le i<j\le n}\frac{C_{ij}^2}{\sigma_i+\sigma_j}
+O(\varepsilon^3).
\]

The coefficient is strictly positive if and only if \(M\) and \(N\) do not commute. Indeed, for **every** \(\varepsilon>0\), not just small values, the unrotated matrix-sign step is globally optimal exactly when the product \(MN\) is symmetric and

\[
\Sigma-\varepsilon\rho MN\succeq0.
\]

Thus if \(C\ne0\), even arbitrarily weak positive curvature forces a strictly different optimizer. If \(C=0\), the unrotated step is exactly optimal for \(0\le\varepsilon\le\varepsilon_{\mathrm{crit}}\), where

\[
\varepsilon_{\mathrm{crit}}
=\bigl[\rho\,\lambda_{\max}(\Sigma^{-1/2}MN\Sigma^{-1/2})\bigr]^{-1}.
\]

## Assumptions and scope

Let \(n\ge2\) be any integer. All matrices are real \(n\times n\). Let \(G\) be invertible with an arbitrary singular-value decomposition \(G=U\Sigma V^{\mathsf T}\), where \(U,V\) are orthogonal and the diagonal entries of \(\Sigma\) are strictly positive. Singular values need not be distinct. Let \(A\) and \(B\) be symmetric positive-definite, \(\rho>0\), and \(\varepsilon\ge0\). Set

\[
F_\varepsilon(D)=\operatorname{tr}(G^{\mathsf T}D)
+\frac{\varepsilon}{2}\operatorname{tr}(D^{\mathsf T}BDA),
\qquad \|D\|_2\le\rho.
\]

At \(\varepsilon>0\), the quadratic form is strictly convex because \(A\) and \(B\) are positive-definite. At \(\varepsilon=0\), invertibility of \(G\) ensures that \(D_0=-\rho UV^{\mathsf T}\) is the unique minimizer of the linear objective over the spectral-norm ball. The asymptotic error constants may depend on the fixed matrices and \(\rho\); there is no uniform claim as the least singular value of \(G\) tends to zero. No assertion is made for indefinite curvature or rectangular or complex matrix variables.

## Proof

**1. Exact convex optimality at a flat-spectrum boundary point.** Let \(R\) be orthogonal and \(D=-\rho URV^{\mathsf T}\). The gradient of the model is

\[
\nabla F_\varepsilon(D)
=U\bigl(\Sigma-\varepsilon\rho MRN\bigr)V^{\mathsf T}.
\]

Such a \(D\) is optimal over \(\|D\|_2\le\rho\) if and only if

\[
S(R,\varepsilon)=R^{\mathsf T}(\Sigma-\varepsilon\rho MRN)
\quad\text{is symmetric positive-semidefinite}.
\]

For sufficiency, the gradient equals \(URS(R,\varepsilon)V^{\mathsf T}\). Since \(\|U^{\mathsf T}XV\|_2\le\rho\) for every feasible \(X\), duality between the nuclear and spectral norms gives

\[
\langle \nabla F_\varepsilon(D),X-D\rangle
\ge -\rho\operatorname{tr}S+\rho\operatorname{tr}S=0.
\]

Convexity therefore implies optimality. Necessity follows from the normal cone of the spectral-norm ball at a scaled orthogonal matrix, which consists of that orthogonal matrix multiplied by a symmetric positive-semidefinite matrix. For \(\varepsilon>0\), strict convexity gives uniqueness.

**2. A locally analytic orthogonal optimizer exists.** Write \(R=\exp K\) with \(K^{\mathsf T}=-K\), restricting to a neighborhood of \(K=0\). Demand that the skew part of \(S(\exp K,\varepsilon)\) vanish. At \((K,\varepsilon)=(0,0)\), \(S=\Sigma\succ0\). The derivative of the skew part with respect to \(K\) maps an infinitesimal skew matrix \(H\) to the skew part of \(-H\Sigma\), whose \((i,j)\) entry is \(-\tfrac12(\sigma_i+\sigma_j)H_{ij}\). All denominators are positive, so this is an invertible linear map on skew matrices, including when singular values coincide. The analytic implicit-function theorem supplies a unique analytic \(K(\varepsilon)\) for all sufficiently small \(|\varepsilon|\). By continuity, \(S(\exp K(\varepsilon),\varepsilon)\succ0\). Step 1 proves that the resulting flat-spectrum matrix is the **global**, not merely orthogonally constrained, minimizer for sufficiently small nonnegative \(\varepsilon\).

**3. First-order polar response.** Differentiate \(S(\exp K(\varepsilon),\varepsilon)\) at zero. Denoting \(H=K'(0)\),

\[
S'(0)=-H\Sigma-\rho MN.
\]

Symmetry requires

\[
H\Sigma+\Sigma H=-\rho(MN-NM)=-\rho C.
\]

Hence \(H_{ij}=-\rho C_{ij}/(\sigma_i+\sigma_j)\) for \(i\ne j\), and \(H_{ii}=0\). Analyticity gives the stated \(O(\varepsilon^2)\) remainder.

**4. The sharp second-order objective gain.** For skew \(K\to0\), expansion of the exponential and cyclicity of trace give

\[
\begin{aligned}
F_\varepsilon(-\rho U\exp K V^{\mathsf T})-F_\varepsilon(D_0)
={}&\frac{\rho}{2}\sum_{i<j}(\sigma_i+\sigma_j)K_{ij}^2\\
&+\varepsilon\rho^2\sum_{i<j} C_{ij}K_{ij}
+O(\|K\|_F^3+\varepsilon\|K\|_F^2).
\end{aligned}
\]

Substituting \(K_{ij}=-\varepsilon\rho C_{ij}/(\sigma_i+\sigma_j)+O(\varepsilon^2)\) yields

\[
F_\varepsilon(D_\varepsilon)-F_\varepsilon(D_0)
=-\frac{\varepsilon^2\rho^3}{2}\sum_{i<j}\frac{C_{ij}^2}{\sigma_i+\sigma_j}+O(\varepsilon^3).
\]

Each denominator is positive, so the coefficient vanishes precisely when \(C=0\).

**5. Exact persistence threshold.** At \(R=I\), the condition of Step 1 becomes \(\Sigma-\varepsilon\rho MN\succeq0\). For \(\varepsilon>0\) its symmetry is equivalent to \(MN=NM\), since \(M,N\) are symmetric. Under commutation, \(MN\) is positive-definite. Congruence by \(\Sigma^{-1/2}\) proves the exact critical formula. Otherwise symmetry fails at every positive \(\varepsilon\), so \(D_0\) is never optimal. This also proves strict improvement without assuming smallness, because the minimizer is unique.

The quantity in the gain formula does not depend on a choice of singular vectors within a repeated-singular-value subspace: it is the uniquely defined objective coefficient. Equivalently, simultaneous orthogonal basis changes in repeated-singular-value blocks preserve the weighted Frobenius norms of the commutator blocks.

## Verification

A deterministic numerical checker is included as `checks/commutator_check.py`. It evaluates the constrained-optimum certificate on explicit \(2\times2\) and \(3\times3\) positive-definite models, compares the observed polar-rotation derivatives with their Sylvester-equation predictions, and compares scaled objective improvements with the second-order coefficient. Numerical minimization is performed *on the orthogonal branch only*, after which the positive-definite certificate from Step 1 verifies global optimality for each tested parameter. The checks are corroboration, not a substitute for Steps 1–5.

For \(\Sigma=\operatorname{diag}(3,1)\), \(\rho=1\), \(M=\operatorname{diag}(2,1)\), and \(N=\begin{psmallmatrix}2&1/2\\1/2&3\end{psmallmatrix}\), the predicted off-diagonal polar generator slope is \(-1/8\) and the predicted gain coefficient is \(1/32\). An exact Taylor expansion on the planar rotation family gives the candidate improvement \(\varepsilon^2/32-\varepsilon^3/128+O(\varepsilon^4)\), consistent with the optimizer's leading coefficient. The checker also uses a noncommuting three-dimensional example and verifies positivity of the optimality-certificate matrix.

## Relationship to prior work

Zhang, Sun, and Liu introduce quadratic spectral descent with the same spectral-norm constrained quadratic model, report curvature-induced changes to singular values and directions, and give general optimality and Frank–Wolfe statements [1]. This finding addresses the **different quantitative local question** of how the exact optimal polar orientation and optimal-model improvement depend on infinitesimal Kronecker curvature. It isolates a computable commutator and yields the complete second-order value coefficient together with a global exactness threshold for the matrix-sign baseline. The generic fact that the quadratic minimizer cannot be worse than the baseline is already part of that established framework and is not claimed as new. Only the specific sensitivity and threshold formulas are the candidate contribution.

Higham derives polar-factor properties and perturbation bounds, including a Sylvester equation for the derivative of the positive polar factor [2]. Bhatia and Mukherjea study derivatives of the unitary polar factor of a perturbed input matrix [3]. Those tools motivate the denominator structure but neither inspected source supplies the two-sided Kronecker-quadratic self-consistency equation or the sharp squared-curvature surrogate improvement in this setting. The earlier spectral-norm interpretation of Muon in [4] supplies the linear baseline but not a curvature-response formula.

## Limitations

The exact formula is local as \(\varepsilon\downarrow0\); it does not describe the optimizer after singular values begin shrinking away from the spectral-norm boundary. In particular, the noncommuting case only guarantees that the unrotated matrix-sign step is suboptimal for every positive \(\varepsilon\), not that the optimizer remains a scaled orthogonal matrix for all of them. Results are for a real, square, invertible gradient and strictly positive-definite Kronecker factors. They concern the quadratic surrogate, **not** the actual decrease of a nonlinear training loss or an empirical algorithmic speedup. The published QSD manuscript could not be read in full through accessible routes; the available primary abstract and external technical summaries were compared, leaving residual risk that a detailed appendix already contains related asymptotic coefficients. Independent mathematical assessment remains outstanding.

## References

1. Qiaozhe Zhang, Jun Sun, Yingzhuang Liu, *Beyond the Matrix Sign: Quadratic Spectral Descent*, arXiv:2609.07597, first posted 7 September 2026, https://arxiv.org/abs/2609.07597.
2. Nicholas J. Higham, *Computing the Polar Decomposition—with Applications*, SIAM Journal on Scientific and Statistical Computing 7(4), 1160–1174 (1986), https://doi.org/10.1137/0907079; lawful open copy https://eprints.maths.manchester.ac.uk/694/1/high86p.pdf.
3. Rajendra Bhatia and Kalyan Mukherjea, *Variation of the Unitary Part of a Matrix*, SIAM Journal on Matrix Analysis and Applications 15(3), 1007–1014 (1994), https://doi.org/10.1137/S0895479892243237.
4. Lizhang Chen, Jonathan Li, Qiang Liu, *Muon Optimizes Under Spectral Norm Constraints*, arXiv:2506.15054, first posted 18 June 2025, https://arxiv.org/abs/2506.15054.
