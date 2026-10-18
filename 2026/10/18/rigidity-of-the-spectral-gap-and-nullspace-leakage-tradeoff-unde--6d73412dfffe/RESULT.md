# Rigidity of the spectral-gap and nullspace-leakage tradeoff under diagonal splitting

## Finding
For a real unit vector \(u\in\mathbb R^3\), let \(A=uu^{\mathsf T}\) and let \(D=\operatorname{diag}(d_1,d_2,d_3)\) be nonnegative diagonal. Consider the diagonal splitting
\[
 B_\varepsilon=A^{\mathsf T}A+\varepsilon D=uu^{\mathsf T}+\varepsilon D,
 \qquad \varepsilon>0.
\]
Write \(\lambda_1(\varepsilon)\le\lambda_2(\varepsilon)\le\lambda_3(\varepsilon)\) for its eigenvalues, and let \(V_\varepsilon\) be any orthonormal basis of the invariant subspace belonging to the two smaller eigenvalues. The limits
\[
 G_u(D)=\lim_{\varepsilon\downarrow0}
 \frac{\lambda_2(\varepsilon)-\lambda_1(\varepsilon)}{\varepsilon},
 \qquad
 L_u(D)=\lim_{\varepsilon\downarrow0}
 \frac{\|A V_\varepsilon\|_2}{\varepsilon}
\]
exist, even when the two small eigenvalues have equal first derivatives.

**Rigidity theorem.** There exists a constant \(c>0\), depending on \(u\) but not on \(D\), such that
\[
 G_u(D)=c L_u(D)\quad\text{for every nonnegative diagonal }D
\]
**if and only if**
\[
 |u_1|=|u_2|=|u_3|=\frac1{\sqrt3}.
\]
In this case the constant is uniquely \(c=\sqrt2\). More precisely, with \(S(d)=\sum_{1\le i<j\le3}(d_i-d_j)^2\),
\[
 \boxed{G_u(D)^2=\frac29 S(d),\quad L_u(D)^2=\frac19 S(d),
 \quad G_u(D)=\sqrt2 L_u(D).}
\]
Thus the unique full-coordinate-balanced rank-one normal has a *pointwise*, rather than merely expectation-level, equality between first-order random eigenvalue repulsion and perturbation-induced nullspace residual. No such universal proportionality exists for any other orientation.

**Uniform-random calibration.** When \(d_1,d_2,d_3\) are independent \(\operatorname{Uniform}[0,1]\) random variables and \(u\) is balanced, the known three-observation sample-variance distribution transfers to the joint limiting gap and residual. Put
\[
 F(g)=\frac{3\sqrt3\pi}{2}g^2-9g^3,
 \qquad 0\le g\le\frac1{\sqrt3}.
\]
For \(0\le g\le\sqrt2\ell\le1/\sqrt3\),
\[
 \boxed{\lim_{\varepsilon\downarrow0}\Pr\!\left\{
 \frac{\lambda_2(\varepsilon)-\lambda_1(\varepsilon)}{\varepsilon}\ge g,
 \frac{\|A V_\varepsilon\|_2}{\varepsilon}\le\ell\right\}
 =F(\sqrt2\ell)-F(g).}
\]
For \(g>\sqrt2\ell\), the limiting probability vanishes. This probability identity is a *consequence* of the gap--residual coupling and a previously known sample-variance CDF; novelty is not claimed for the marginal CDF itself.

## Assumptions and scope
The three-dimensional Gram matrix \(A^{\mathsf T}A=uu^{\mathsf T}\) has a two-dimensional nullspace. The diagonal perturbation is symmetric and nonnegative, and for the limits \(D\) is fixed as \(\varepsilon\to0^+\). For uniform error terms it suffices to restrict \(0\le d_i\le1\). \(V_\varepsilon\) contains **exact** eigenvectors, not finite-step Lanczos approximations. The operator \(2\)-norm of \(A V_\varepsilon\) is the original-system nullspace residual; its leading coefficient is not a squared residual. All eigenvalue orderings and subspaces are unambiguous when \(\varepsilon\) is small enough that the largest eigenvalue is separated from the smaller pair. The two small eigenvalues need not be separated from each other.

## Proof
**First-order block reduction.** Let \(P=I-uu^{\mathsf T}\), and let \(U\in\mathbb R^{3\times2}\) be any orthonormal basis of \(u^\perp\). With \(T=U^{\mathsf T}DU\) and \(b=U^{\mathsf T}Du\), the perturbed matrix in the orthogonal coordinates \([U,u]\) is
\[
 \begin{pmatrix}\varepsilon T&\varepsilon b\\
 \varepsilon b^{\mathsf T}&1+\varepsilon u^{\mathsf T}Du\end{pmatrix}.
\]
Degenerate symmetric perturbation theory, or its two-by-two Schur complement at spectral arguments of order \(\varepsilon\), gives
\[
 \lambda_j(\varepsilon)=\varepsilon\mu_j(T)+O(\varepsilon^2),
 \quad j=1,2,
\]
where \(\mu_1(T)\le\mu_2(T)\). The normalized dominant eigenvector satisfies
\[
 w_\varepsilon=u+\varepsilon PDu+O(\varepsilon^2)
\]
after choosing its sign so that \(u^{\mathsf T}w_\varepsilon>0\). The bottom invariant space is \(w_\varepsilon^\perp\), so
\[
 \|A V_\varepsilon\|_2
 =\|u^{\mathsf T}V_\varepsilon\|_2
 =\sqrt{1-(u^{\mathsf T}w_\varepsilon)^2}
 =\varepsilon\|PDu\|_2+O(\varepsilon^2).
\]
The last step follows by projecting the displayed eigenvector expansion onto \(u^\perp\), then normalizing. Therefore
\[
 G_u(D)=\mu_2(T)-\mu_1(T),\qquad
 L_u(D)=\|PDu\|_2.
\]
The remainders are uniform when \(\|D\|_2\le1\), by the unperturbed unit spectral gap.

**Necessity and uniqueness.** Test the claimed proportionality on each of the three allowed coordinate perturbations \(D_i=e_ie_i^{\mathsf T}\), and write \(p_i=u_i^2\). The compression \(U^{\mathsf T}D_iU\) has eigenvalues \(0\) and \(1-p_i\). Meanwhile
\[
 \|PD_i u\|_2^2=p_i(1-p_i).
\]
If any \(p_i=0\), this test yields a positive gap and zero residual, incompatible with finite \(c\). Hence all \(p_i>0\); also every \(p_i<1\) since their sum is one. Consequently
\[
 c^2=\frac{1-p_i}{p_i}
\]
for each \(i\). The function \(p\mapsto(1-p)/p\) is strictly decreasing on \((0,1)\), so all three \(p_i\) coincide. Their sum being one, \(p_i=1/3\), and \(c^2=2\). The three coordinate probes also prove that every other orientation fails the asserted universal proportionality.

**Sufficiency and exact coefficients.** Conjugation by a diagonal sign matrix reduces every balanced \(u\) to \((1,1,1)^{\mathsf T}/\sqrt3\) without changing diagonal \(D\), gaps, or residual norms. Choose
\[
 U=\begin{pmatrix}1/\sqrt2&1/\sqrt6\\-1/\sqrt2&1/\sqrt6\\0&-2/\sqrt6\end{pmatrix}.
\]
Then
\[
 T=\begin{pmatrix}
 (d_1+d_2)/2&(d_1-d_2)/\sqrt{12}\\
 (d_1-d_2)/\sqrt{12}&(d_1+d_2+4d_3)/6
 \end{pmatrix},
 \quad
 b=\begin{pmatrix}(d_1-d_2)/\sqrt6\\(d_1+d_2-2d_3)/\sqrt{18}\end{pmatrix}.
\]
The square of the eigenvalue separation of a symmetric two-by-two matrix is its squared diagonal difference plus four times the squared off-diagonal. Direct substitution yields
\[
 (\mu_2(T)-\mu_1(T))^2=\frac29 S(d),
 \qquad b^{\mathsf T}b=\frac19S(d).
\]
Both quantities are nonnegative. Taking square roots proves every identity, including for scalar \(D\) when both sides vanish.

**The joint uniform probability.** For independent continuous uniform diagonal samples, the limiting gap \(G\) has no atoms: the only zero configuration is \(d_1=d_2=d_3\), and every positive level set is a two-dimensional surface of Lebesgue measure zero. Thus the deterministic first-order expansions and bounded convergence transfer a fixed two-threshold event to \(\Pr\{g\le G\le\sqrt2\ell\}\). The equality \(G=\sqrt2L\) reduces the joint law to the marginal CDF \(F\).

For completeness, the displayed *lower branch* of the known uniform sample-variance CDF also has a short direct geometric verification. Put \(d=m(1,1,1)^{\mathsf T}+z\), \(z\perp(1,1,1)\), and \(R=\|z\|_2\). Since \(G=\sqrt{2/3}\,R\), the condition \(G\le1/\sqrt3\) is exactly \(R\le1/\sqrt2\). At each direction \(z=R v(\theta)\), the admissible interval of the mean \(m\) inside the unit cube has length \(1-R(\max_j v_j-\min_j v_j)\). This length is nonnegative for all angles in the stated regime, because \(\max_j v_j-\min_j v_j\le\sqrt2\). The Jacobian is \(\sqrt3 R\,dR\,d\theta\), and
\[
 \int_0^{2\pi}(\max_j v_j(\theta)-\min_j v_j(\theta))\,d\theta=6\sqrt2.
\]
Indeed the range of three numbers equals half the sum of their three pairwise absolute differences, each pairwise difference having amplitude \(\sqrt2\) and absolute-sine integral four. Integrating over the disk of radius \(R_0\le1/\sqrt2\) gives \(\sqrt3\pi R_0^2-2\sqrt6R_0^3\). Substituting \(R_0=\sqrt{3/2}\,g\) yields precisely \(F(g)\). This geometric CDF is not asserted as a previously unknown distribution.

## Verification
The standalone file `verify.py` symbolically reconstructs the compression \(T\), coupling \(b\), and the exact two polynomial identities. It checks coordinate-probe rigidity for several balanced and unbalanced normals, independently computes exact perturbed eigenspaces for 288 deterministic pseudorandom comparisons (four normals, thirty-six diagonal choices, two perturbation amplitudes), and compares five CDF values to seeded Monte Carlo with 600,000 draws each. The recorded replay passed. The symbolic identities and analytical proof, not the finite sampling, justify the universal statements and probability limit. The Monte Carlo checks are approximate and do not establish the analytic CDF.

## Relationship to prior work
Kressner and Shao (arXiv:2407.04634v1, 5 July 2024, Sections 2.1–2.3) introduce random diagonal splitting \(A^{\mathsf T}A+\varepsilon D\), give eigenvalue-repulsion bounds (Theorem 4), and bound attainable nullspace quality (Theorem 6). These foundational claims are not new here. General eigenvector perturbation and two-by-two compression formulas are classical. The present assertion is the **complete if-and-only-if classification of rank-one normal orientations** allowing a samplewise proportionality between *two separate first-order numerical quality metrics*, including its sharp coefficient. It does not follow from a general upper bound on the residual or from a separate marginal gap law. Existing exact studies of small graph-derived zero clusters reveal other joint gap/error phenomena for *different*, nonbalanced normal orientations, but do not imply the balanced rigidity statement.

The uniform three-point sample-variance CDF is classical (Rietz, 1931), and the explicit modern rederivation by Osan, Chu, and Yu (arXiv:2609.25333v1, 2026) is acknowledged. The marginal \(F\) formula, the quadratic small-gap power, and its threshold are **not** claimed as new; they are used only to translate the structural identity into a concrete joint numerical-design probability. The evidence supports a distinct structural classification but cannot rule out an equivalent older formulation in spectral perturbation literature.

## Limitations
This is an exact-eigenspace, infinitesimal-perturbation theorem for three coordinates and a rank-one Gram matrix. It is not a convergence theorem for finite-step Lanczos, is not an assertion of a gap/leakage tradeoff for general dimensions or matrices, and does not assert equality at any fixed positive \(\varepsilon\). The probability formula is stated only for the lower CDF branch, not the full marginal CDF above \(1/\sqrt3\). The mathematical novelty rests on the orientation rigidity and its numerical coupling interpretation; the ingredients (degenerate perturbation, rank-one probes, known variance law) are elementary or established. Specialized equivalent statements may exist elsewhere, and independent priority verification has not been performed.

## References
1. Daniel Kressner and Nian Shao, *A randomized small-block Lanczos method for large-scale null space computations*, arXiv:2407.04634v1 (first publicly submitted 5 July 2024), Sections 1–3, especially Theorems 4 and 6. https://arxiv.org/html/2407.04634v1
2. Daniel Kressner and Nian Shao, *On a randomized small-block Lanczos method for large-scale null space computations*, arXiv:2407.04634v2 (2025), revised analysis. https://arxiv.org/html/2407.04634v2
3. Remus Osan, Kevin T. Chu, and Ron Yu, *Closed forms and open obstructions: the sample variance of three observations*, arXiv:2609.25333v1 (21 September 2026), including historical attribution to Rietz (1931) and the uniform-parent CDF. https://arxiv.org/html/2609.25333v1
4. G. W. Stewart and J.-G. Sun, *Matrix Perturbation Theory*, Academic Press, 1990 (standard invariant-subspace perturbation background).
