# Sharp alignment decay in rank-one tangent-polar refinement

## Finding

For the alternating tangent projection and polar orthogonalization used in spectral low-rank optimization, a perfectly legitimate projected gradient can lose normalized gradient alignment **strictly at every additional inner iteration** after the first. On a natural real symmetric rank-one tangent slice, the exact best universal alignment at iteration \(t\ge1\) is
\[
\inf_{a,b>0}\frac{\langle g,X_t\rangle_F}{\|g\|_*}
=\frac{2\sqrt{2^{t+1}}}{2^t+2}.
\]
In particular, the optimal universal constants at three and five inner steps are \(4/5\) and \(8/17\), respectively. These are sharp over the specified family, with explicit equality cases. The lower bound approaches zero with an increasing inner-iteration budget, even though the first polar step has exact normalized alignment \(1\).

## Assumptions and scope

Work over real \(2\times2\) matrices with Frobenius pairing \(\langle U,V\rangle_F=\operatorname{tr}(U^{\mathsf T}V)\). Fix the nonzero rank-one point \(W=e_1e_1^{\mathsf T}\) on the manifold of rank-one matrices. Its tangent space and Frobenius-orthogonal projector are
\[
T_W=\left\{\begin{pmatrix}u&v\\w&0\end{pmatrix}:u,v,w\in\mathbb R\right\},
\qquad
P_T\!\begin{pmatrix}u&v\\w&z\end{pmatrix}=
\begin{pmatrix}u&v\\w&0\end{pmatrix}.
\]
Let \(a>0\) and \(b>0\) and choose the projected gradient
\[
g=\begin{pmatrix}a&b\\b&0\end{pmatrix}\in T_W.
\]
For each nonsingular real square matrix \(Y\), define \(\operatorname{polar}(Y)=Y(Y^{\mathsf T}Y)^{-1/2}\), equivalently its orthogonal polar factor. Starting with \(X_0=g\), run the *unsafeguarded* inner recurrence \(X_{t+1}=P_T(\operatorname{polar}(X_t))\) for integers \(t\ge0\). Each iterate is nonsingular under these assumptions, so the definition has no rank ambiguity.

The alignment \(R_t=\langle g,X_t\rangle_F/\|g\|_*\) is the exact normalized inner-product quantity appearing in the source method's descent-alignment hypothesis. It is **not** called a ratio to the exact tangent spectral-norm linear minimization oracle: the projected polar iterates need not lie in the spectral unit ball.

## Proof

**Polar identity.** For \(u>0\), \(v>0\), the symmetric matrix \(Z=\begin{psmallmatrix}u&v\\v&0\end{psmallmatrix}\) has determinant \(-v^2<0\). Its eigenvalues have opposite signs. Direct diagonalization, or interpolation of the sign function on its two eigenvalues, yields
\[
\operatorname{polar}(Z)=\operatorname{sign}(Z)
=\frac{1}{\sqrt{u^2+4v^2}}
\begin{pmatrix}u&2v\\2v&-u\end{pmatrix}.
\]
The tangent projector drops its bottom-right entry. Scaling \(Z\) by a positive scalar does not change its polar factor; therefore induction gives for every integer \(t\ge1\)
\[
X_t=\frac{1}{\sqrt{a^2+4^t b^2}}
\begin{pmatrix}a&2^t b\\2^t b&0\end{pmatrix}.
\]
The matrix remains nonsingular since its determinant is strictly negative.

**Exact alignment.** The eigenvalues of \(g\) have opposite signs, so their absolute values add to \(\sqrt{a^2+4b^2}\). Thus
\[
\|g\|_*=\sqrt{a^2+4b^2},\qquad
R_t(a,b)=\frac{a^2+2^{t+1}b^2}
{\sqrt{(a^2+4^t b^2)(a^2+4b^2)}}.
\]
At \(t=1\) this equals \(1\). To see strict decline, for real \(k\ge2\) let \(h(k)=(a^2+2kb^2)/\sqrt{a^2+k^2b^2}\). Then
\[
h'(k)=\frac{a^2b^2(2-k)}{(a^2+k^2b^2)^{3/2}}.
\]
This derivative is strictly negative for \(k>2\), and \(2^t\) increases strictly for integers \(t\ge1\). Therefore \(R_{t+1}<R_t\). Taking \(k\to\infty\) gives \(R_t\to2b/\sqrt{a^2+4b^2}\).

**Sharp minimax value.** Put \(k=2^t\) and \(y=b^2/a^2>0\). Then
\[
R_t^2=F_k(y):=\frac{(1+2ky)^2}{(1+k^2y)(1+4y)},
\qquad
F_k'(y)=\frac{(k-2)^2(2ky-1)(2ky+1)}{(1+k^2y)^2(1+4y)^2}.
\]
For \(k=2\), \(F_2\equiv1\). For every \(k>2\), the derivative is negative for \(0<y<1/(2k)\) and positive for \(y>1/(2k)\), giving a unique global minimum at \(y=1/(2k)\). Substitution gives
\[
F_k\!\left(\frac1{2k}\right)=\frac{8k}{(k+2)^2},
\qquad
\inf_{a,b>0}R_t=\frac{2\sqrt{2k}}{k+2}
=\frac{2\sqrt{2^{t+1}}}{2^t+2}.
\]
The attaining condition is exactly \(a^2=2kb^2\) when \(t\ge2\). This proves all equalities and strictness claims. In the worst-case family, the bound is asymptotic to \(2\sqrt2\,2^{-t/2}\), so no constant positive independently of \(t\) works for these unsafeguarded iterates.

## Verification

The standalone `verify.py` uses exact rational arithmetic for 3,240 parameter/horizon combinations, checks the symbolic derivative identity and minimizing substitution, verifies equality at 16 horizons, and compares 900 full alternating SVD/polar iterations with the formula using independently chosen positive input parameters. It returns `SYMBOLIC_OK` and `VERIFY_OK`. These finite checks are diagnostic; the all-parameter and all-integer-horizon proof is the algebra above. Reproduce by running `python3 verify.py` with NumPy and SymPy installed. No spectral-unit-ball feasibility is claimed for \(X_t\).

## Relationship to prior work

Andriianov, Veprikov and Beznosikov [1, Section 3.3, equation (12)] introduce the alternating tangent projection and matrix-sign inner refinement. Their convergence analysis [1, Section 5] explicitly assumes an alignment bound and mentions the alternative of retaining the best-aligned iterate among the inner steps. That safeguard is a **pre-existing proposal**, not a contribution here. Their proofs and empirical studies do not provide this real symmetric rank-one slice's exact monotone alignment decline and sharp \(t\)-dependent envelope. The present theorem analyzes the unsafeguarded raw final inner iterate and does not contradict their conditional convergence proof or their safeguard.

Bogachev and collaborators [2, the discussion around equation (13) and Appendix D] already discuss repeating projected orthogonalization for low-rank geometry and analyze one-step behavior. Their inspected statements do not give this parameterized extremal multi-step alignment law. General alternating-projection convergence literature is not the same assertion as maintaining directional correlation with the initial gradient.

## Limitations

The theorem concerns real symmetric \(2\times2\) matrices at one fixed rank-one tangent plane, positive \(a,b\), and the unsafeguarded iteration. It does not claim such decay for every gradient or higher rank, nor an optimizer-wide convergence failure. Every fixed iteration horizon has a positive family-wide lower bound; only a bound *uniform over arbitrarily many inner steps* fails. The inner iterates need not satisfy a spectral-unit-ball constraint; hence this theorem is an alignment analysis, not a direct suboptimality ratio for the constrained linear optimization oracle. No claim of independent validation is made.

## References

[1] D. Andriianov, A. Veprikov and A. Beznosikov, *LoRA-TSD: Tangent-Space Spectral Descent for LoRA via Muon-Style Updates*, arXiv:2609.02734v1, first posted 2026-09-02. https://arxiv.org/abs/2609.02734 . Relevant complete preprint: https://pdfs.assets.alphaxiv.org/2609.02734v1.pdf .

[2] V. Bogachev et al., *LoRA meets Riemannion: Muon Optimizer for Parametrization-independent Low-Rank Adapters*, arXiv:2507.12142v2, https://arxiv.org/abs/2507.12142 .
