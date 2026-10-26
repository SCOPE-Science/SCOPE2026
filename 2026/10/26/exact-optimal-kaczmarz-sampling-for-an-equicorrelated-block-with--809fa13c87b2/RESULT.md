# Exact optimal Kaczmarz sampling for an equicorrelated block with one exceptional row

## Finding

Let \(m\ge 2\) be an integer, \(0<\alpha<1\), and \(0\le\beta<\sqrt{a}\), where
\[
\eta=1-\alpha,\qquad a=\alpha+\frac{\eta}{m}.
\]
Consider \(m+1\) unit-norm, linearly independent real measurement rows with Gram matrix
\[
G=\begin{pmatrix}(1-\alpha)I_m+\alpha\mathbf1\mathbf1^\mathsf T&\beta\mathbf1\\
\beta\mathbf1^\mathsf T&1\end{pmatrix}.
\]
Each of the first \(m\) rows has common mutual inner product \(\alpha\); the last row has inner product \(\beta\) with each of them. Select one row independently at every randomized Kaczmarz step, with any probability vector \(p\) on the \(m+1\) rows. Define its sharp uniform-in-error expected squared-error decrease
\[
\mu(p)=\lambda_{\min}\!\left(\sum_{i=1}^{m+1}p_i u_i u_i^\mathsf T\right).
\]
Then the globally optimal sampling law is **unique**. It assigns equal probability \(q_*\) to each of the first \(m\) rows and probability \(r_*\) to the exceptional row. Set
\[
\beta_c=\frac{\sqrt{(1-\alpha)^2+4m^2\alpha}-(1-\alpha)}{2m},
\qquad W=1+a+2\beta.
\]
The exact optimum \(\mu_*\), and its unique law, are
\[
\begin{array}{c|c|c|c}
\text{range}&q_*&r_*&\mu_*\\\hline
0\le\beta\le\beta_c&
\dfrac{\alpha-\beta^2}{m(\alpha-\beta^2)+\alpha(1-\alpha)}&
\dfrac{\alpha(1-\alpha)}{m(\alpha-\beta^2)+\alpha(1-\alpha)}&
\dfrac{(1-\alpha)(\alpha-\beta^2)}{m(\alpha-\beta^2)+\alpha(1-\alpha)}\\[8pt]
\beta_c\le\beta<\sqrt a&
\dfrac{1+\beta}{mW}&\dfrac{a+\beta}{W}&\dfrac{a-\beta^2}{W}
\end{array}
\]
The branches coincide at \(\beta_c\). At the threshold, the active smallest eigenvalue switches from a contrast mode involving the repeated rows to a coupled common-mode/exceptional-row mode. Uniform row sampling is optimal **if and only if** \(\beta=\alpha\). The exact sharp worst-direction one-step expected squared-error factor is \(1-\mu_*\); this is also a valid per-step factor for arbitrary current errors and hence yields an iterated expectation bound, but it is not claimed to be the exact long-time mean-square exponent.

## Assumptions and scope

All vectors are real. The rows are unit normalized and form a basis in an \((m+1)\)-dimensional Euclidean space; any square Gram factor of \(G\) is an admissible realization. The upper bound \(\beta<\sqrt a\) is exactly the nonsingularity condition: the \(m-1\) contrast eigenvalues of \(G\) equal \(1-\alpha>0\), and the determinant of its remaining two-dimensional block is \(m(a-\beta^2)>0\). The linear system is consistent, and no adaptive, block, or without-replacement row sampling is asserted. All probability vectors, including asymmetric and boundary vectors, are allowed in the optimization.

## Proof

**1. Reduction without assuming a symmetric competitor.** For fixed \(p\), projecting an error \(e\) onto the hyperplane normal to row \(u_i\) changes its squared norm by \(-|u_i^\mathsf T e|^2\). Therefore
\[
\mathbb E[\|e_+\|^2\mid e]=\|e\|^2-\sum_i p_i|u_i^\mathsf T e|^2,
\]
and the sharp worst-direction decrease equals \(\mu(p)\) by the Rayleigh principle. Writing the square row matrix as \(U\), the weighted information matrix \(U^\mathsf T\operatorname{diag}(p)U\) has the same eigenvalues as \(G^{1/2}\operatorname{diag}(p)G^{1/2}\). This matrix is affine in \(p\), so its smallest eigenvalue is concave. Its value is unchanged under any permutation of the first \(m\) rows, because \(G\) commutes with these permutations. Averaging every feasible \(p\) over this group cannot decrease the objective. Thus the unrestricted optimum is attained by a law \((q,\ldots,q,r)\), with \(mq+r=1\).

**2. The two spectral bottlenecks.** For such a law, the \(m-1\) contrast eigenvalues are all \(\eta q\). The remaining two eigenvalues are those of
\[
M(r)=\begin{pmatrix}a(1-r)&\beta\sqrt{r(1-r)}\\
\beta\sqrt{r(1-r)}&r\end{pmatrix},
\qquad q=\frac{1-r}{m}.
\]
Its smaller eigenvalue is
\[
\ell(r)=\frac{a(1-r)+r-\sqrt{[a(1-r)-r]^2+4\beta^2r(1-r)}}2.
\]
Consequently \(\mu(q,\ldots,q,r)=\min\{\eta(1-r)/m,\ell(r)\}\). Put \(d=1+a+2\beta\), \(r_0=(a+\beta)/d\), and \(L_0=(a-\beta^2)/d\). Direct expansion yields the exact quadratic certificate
\[
\det(M(r)-L_0 I_2)=-(a-\beta^2)(r-r_0)^2\le0.
\]
Thus \(\ell(r)\le L_0\) for every \(0\le r\le1\); equality holds only at \(r=r_0\). At \(r_0\), the two eigenvalues of \(M\) are \(L_0\) and \(L_0+\beta\). For clarity, the two eigenvalues of \(M(r)\) are also the eigenvalues of the affine rank-one pencil \((1-r)vv^\mathsf T+rww^\mathsf T\), with \(v=(\sqrt a,0)^\mathsf T\) and \(w=(\beta/\sqrt a,\sqrt{1-\beta^2/a})^\mathsf T\), because both matrices have trace \(a(1-r)+r\) and determinant \((a-\beta^2)r(1-r)\). Hence \(\ell(r)\) is concave. It is therefore nondecreasing before its unique maximum and nonincreasing afterward; for \(\beta=0\), the explicit minimum of two linear functions gives the same ordering.

**3. Crossover and the optimal probabilities.** For \(\beta^2<\alpha\), the matrix inequality \(M(r)\succeq\eta(1-r)I_2/m\) holds precisely when
\[
r\ge r_c:=\frac{\alpha\eta}{m(\alpha-\beta^2)+\alpha\eta}.
\]
Indeed, the upper-left excess is \(m\alpha q>0\), while the determinant of the excess is \(m q[(\alpha-\beta^2)r-\alpha\eta q]\). When \(\beta^2\ge\alpha\), the inequality never holds for \(0<r<1\), so only the coupled eigenvalue can be active. The unique positive solution of
\[
m(\alpha-\beta^2)=\eta\beta
\]
is \(\beta_c\), and \(0<\beta_c<\sqrt\alpha\). Elementary cross multiplication shows \(r_c\le r_0\) exactly for \(0\le\beta\le\beta_c\). In that regime \(\ell\) increases until the crossing, after which the contrast value strictly decreases, giving the first displayed branch at \(r_c\). In the complementary regime the coupled eigenvalue reaches its unique maximum at \(r_0\) before any crossing; this gives the second branch. Equality of the two formulas at \(\beta_c\) follows from the defining quadratic equation.

**4. Uniqueness even among asymmetric probabilities.** A symmetrized version of any globally optimal law must be the unique optimal symmetric law established above, so its exceptional probability equals \(r_*\). For \(\beta>0\), choose a bottom eigenvector \(v\) of the symmetric optimum from its coupled two-dimensional invariant subspace. The first \(m\) coordinates of \(y=G^{1/2}v\) are all the same and nonzero: otherwise the \(\beta r_*\) coupling in the equivalent eigenproblem for \(G\operatorname{diag}(p_*)\) is contradicted. For any asymmetric optimal law \(p\) with the same symmetrization, the Rayleigh quotient of \(v\) still equals \(\mu_*\) because \(|y_i|^2\) is constant across the first \(m\) indices. Positive semidefiniteness of \(G^{1/2}\operatorname{diag}(p)G^{1/2}-\mu_* I\) forces \(v\) into its kernel. Subtracting the symmetric eigen-equation and using invertibility of \(G^{1/2}\) gives \((p_i-q_*)y_i=0\) for every repeated row, hence \(p_i=q_*\). If \(\beta=0\), the \(m-1\) repeated-row contrast eigenvectors of the symmetric optimum provide the same argument, and each repeated-row coordinate occurs nontrivially in their span. Thus all optimizers coincide.

**5. Uniform law.** On the first branch, \(r_*=q_*\) is equivalent to \(\beta^2=\alpha^2\), hence to \(\beta=\alpha\). On the second branch, \(r_*=q_*\) would require \(\beta=-\alpha\), impossible. Since \(\beta_c>\alpha\) for \(m\ge2\), the stated equivalence holds.

## Verification

The standalone script `verify.py` checks the displayed formulas against the smallest eigenvalue of the full weighted Gram matrix for 270 parameter configurations spanning both sides of the threshold. It tests 6,480 independently sampled asymmetric probability laws, compares 11 generic constrained numerical optimizations, evaluates five exact-rational characteristic-polynomial identities, and checks the symbolic quadratic certificate. Expected output is in `verification_output.txt`. These finite tests are independent consistency checks; the all-parameter assertion and uniqueness rest on the proof above. As a rational high-correlation example, for \(m=3\), \(\alpha=1/10\), and \(\beta=1/4\), the unique law is \((25/114,25/114,25/114,13/38)\) with \(\mu_*=27/152\); uniform sampling gives the strictly smaller \((22-\sqrt{79})/80\).

## Relationship to prior work

Strohmer–Vershynin introduced norm-proportional randomized Kaczmarz with an exponential mean-square bound. Dai–Soltanalian–Pelckmans derive the general row-probability SDP for the worst-direction one-step contraction, and Gower–Richtárik place randomized projection methods in a broader iterative framework. Agaskar–Wang–Lu instead optimize an exact long-time mean-square error exponent using a higher-dimensional operator. The present contribution explicitly solves Dai and colleagues' SDP on a structured all-dimension correlation family, proves a closed phase boundary and uniqueness over **all** probabilities, and is not a claim that the general SDP or the basic Kaczmarz contraction identity is new. A published inverse-positive-Hessian coordinate-sampling theorem has different hypotheses: its inverse-positivity premise does not hold for the positive equicorrelated Gram blocks here. A related pooled-measurement star design has different row inner products and does not imply this two-coherence law.

## Limitations

The result optimizes the sharp worst-direction conditional **one-step squared-error decrease**, not the true multi-step annealed or quenched exponent, and need not minimize application runtime. It assumes an invertible square row matrix with this exact Gram law, independent stationary sampling, and exact projections. The strict singular-boundary case \(\beta=\sqrt a\) is excluded. No claim is made about inconsistent systems, approximate projections, nonsquare ambient systems without restriction to row span, or nonstationary sampling. Specialized prior exact design formulas outside the inspected literature could overlap; independent validation has not been performed.

## References

1. T. Strohmer and R. Vershynin, *A randomized Kaczmarz algorithm with exponential convergence*, arXiv:math/0702226, first posted February 8, 2007. https://arxiv.org/html/math/0702226v1
2. L. Dai, M. Soltanalian, and K. Pelckmans, *On the Randomized Kaczmarz Algorithm*, arXiv:1402.2863, first posted February 12, 2014; IEEE Signal Processing Letters 21 (2014). https://arxiv.org/abs/1402.2863
3. A. Agaskar, C. Wang, and Y. M. Lu, *Randomized Kaczmarz algorithms: Exact MSE analysis and optimal sampling probabilities*, GlobalSIP 2014. https://dash.harvard.edu/server/api/core/bitstreams/7312037d-8b4a-6bd4-e053-0100007fdf3b/content
4. R. M. Gower and P. Richtárik, *Randomized Iterative Methods for Linear Systems*, SIAM J. Matrix Anal. Appl. 36 (2015), 1660–1690. https://doi.org/10.1137/15M1025487
