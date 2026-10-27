# The optimal one-sweep order for three Kaczmarz equations

## Finding

Let \(u_1,u_2,u_3\in\mathbb R^3\) be linearly independent unit vectors and consider exact, unrelaxed cyclic Kaczmarz applied to the consistent system \(u_i^\top x=b_i\), where the three equations are each visited exactly once in a prescribed order. Write \(P_i=I-u_i u_i^\top\). For a permutation \((i,j,k)\), the one-sweep error operator is \(M_{ijk}=P_kP_jP_i\). Define
\[
 a=\langle u_i,u_j\rangle,\qquad b=\langle u_i,u_k\rangle,\qquad c=\langle u_j,u_k\rangle,
 \qquad Q=\sum_{p<q}\langle u_p,u_q\rangle^2-2\prod_{p<q}\langle u_p,u_q\rangle.
\]
Here \(Q=1-\det G\in[0,1)\), where \(G=(\langle u_p,u_q\rangle)_{p,q=1}^3\). The exact worst-case squared error contraction of the sweep is
\[
 \boxed{\|M_{ijk}\|_2^2=\frac{Q+a^2c^2+\sqrt{(Q+a^2c^2)^2-4a^2c^2}}{2}.}
\]
For fixed three rows this quantity is **strictly decreasing as a function of the product \(a^2c^2\)** over the feasible values. Thus an optimal order puts the common endpoint of the **two largest absolute pairwise row correlations in the middle**; equivalently, the weakest-correlation pair may occupy the first and last positions. Precisely, the complete set of optimal permutations maximizes the product of the two adjacent absolute correlations; this formulation covers all ties, including zero correlations. Every order has **the same sweep eigenvalues**, even when their one-sweep Euclidean worst-case errors differ.

For nonorthogonal triples define the ordering penalty
\[
 R=\frac{\max_{(i,j,k)}\|M_{ijk}\|_2}{\min_{(i,j,k)}\|M_{ijk}\|_2}.
\]
Then \(1\le R<\sqrt2\), and the universal constant is sharp: \(\sup R=\sqrt2\) over linearly independent triples of unit normals. When the normals are pairwise orthogonal, every sweep solves the system exactly, and the ratio is not defined.

## Assumptions and scope

The ambient space is exactly \(\mathbb R^3\), the three normalized rows are linearly independent, the system is consistent, and each row is visited once with exact orthogonal projection and no relaxation. Since the system is square and nonsingular, there is a unique solution \(x_*\); the statement concerns the induced Euclidean operator norm on the error \(e=x-x_*\), not an average over initial guesses or the residual norm \(\|Ae\|_2\). The normalization of nonzero rows leaves Kaczmarz projections unchanged. The optimal ordering minimizes \(\sup_{e\ne0}\|M_{ijk}e\|_2/\|e\|_2\) for one **complete** sweep, not necessarily for several sweeps or finite-precision execution.

## Proof

**(1) Reduction and singular values.** For the order \((i,j,k)\), let \(a=u_i^\top u_j\), \(b=u_i^\top u_k\) and \(c=u_j^\top u_k\). The error after one sweep is \(M=P_kP_jP_i\) times the initial error. Every \(P_\ell\) is an orthogonal rank-two projector; hence \(\operatorname{rank}M\le2\). Let \(\lambda_+\ge\lambda_-\ge0\) be the two possibly nonzero eigenvalues of \(M^\top M\).

Since \(P_i^2=P_i\) and trace is cyclic,
\[
\begin{aligned}
 \operatorname{tr}(M^\top M)
 &=\operatorname{tr}(P_jP_kP_jP_i)\\
 &=\operatorname{tr}(P_jP_i)-(P_ju_k)^\top P_i(P_ju_k)\\
 &=(1+a^2)-\bigl[(1-c^2)-(b-ac)^2\bigr]\\
 &=a^2+c^2+(b-ac)^2=Q+a^2c^2.
\end{aligned}
\]
Under the Hodge-star identification of \(\bigwedge^2\mathbb R^3\) with \(\mathbb R^3\), the exterior-square action of \(P_\ell\) is the rank-one projector \(u_\ell u_\ell^\top\). Therefore
\[
 \bigwedge^2M\simeq (u_ku_k^\top)(u_ju_j^\top)(u_iu_i^\top)=ac\,u_ku_i^\top.
\]
The squared Frobenius norm of \(\bigwedge^2M\) is the product of the two nonzero squared singular values, so \(\lambda_+\lambda_-=a^2c^2\). Their sum is \(Q+a^2c^2\). Solving this quadratic gives the boxed expression. The radicand is nonnegative because it is \((\lambda_+-\lambda_-)^2\).

**(2) Ordering classification.** The Gram determinant identity is
\[
 \det G=1+2abc-(a^2+b^2+c^2)>0.
\]
It is at most one by Hadamard's determinant inequality, with equality only for three mutually orthogonal rows. Hence \(0\le Q<1\). For any fixed nonorthogonal triple, write \(p=a^2c^2\). The larger root is
\[
 L_Q(p)=\frac{Q+p+\sqrt{(Q+p)^2-4p}}2.
\]
Because a product of orthogonal projections cannot preserve the norm of a nonzero vector when the three independent normals span \(\mathbb R^3\), \(0<L_Q(p)<1\). Its quadratic identity yields
\[
 L_Q(p)(L_Q(p)-Q)=p(L_Q(p)-1)\le0,
\]
so \(L_Q(p)\le Q\). The discriminant is nonnegative and \(p<1\), which confines the actual values of \(p\) to
\[
 0\le p\le(1-\sqrt{1-Q})^2.
\]
Indeed the two roots, regarded as a quadratic in \(p\), are \((1\pm\sqrt{1-Q})^2\), with the upper one exceeding one. In the interior of this feasible interval,
\[
 \frac{dL_Q}{dp}=\frac{L_Q(p)-1}{\sqrt{(Q+p)^2-4p}}<0;
\]
continuity handles the degenerate endpoint. Thus \(L_Q\) is strictly decreasing on feasible \(p\). To maximize \(p\), choose the two incident edges with the largest absolute correlations as consecutive pairs in the ordering. The remaining pair, whose correlation has the smallest absolute value, lies in the first and last positions. Every maximizing order and no other order (apart from product ties) minimizes the one-sweep norm.

**(3) Spectrum does not detect the effect.** Expanding \(P_kP_jP_i\), or taking traces of its first and second exterior powers, gives the characteristic polynomial
\[
 \det(zI-M_{ijk})=
 z\left[z^2-\bigl(a^2+b^2+c^2-abc\bigr)z+abc\right].
\]
This depends only on the three unordered pairwise correlations, and not on the permutation. Therefore all six sweeps have exactly the same eigenvalues, including algebraic multiplicities. Their largest singular values can nevertheless differ, so identical asymptotic spectral radii do not settle the one-sweep worst-case error.

**(4) Universal ordering penalty and sharpness.** Since \(\lambda_+\ge(\lambda_++\lambda_-)/2=(Q+p)/2\ge Q/2\) and \(\lambda_+\le Q\), every nonorthogonal triple obeys
\[
 \frac Q2\le\|M_{ijk}\|_2^2\le Q.
\]
For any fixed triple \(Q>0\), the lower inequality is strict, hence \(R<\sqrt2\).

For \(0<t<1/\sqrt2\), choose
\[
 u_1=(\sqrt{1-2t^2},t,t),\qquad u_2=(0,1,0),\qquad u_3=(0,0,1).
\]
The Gram matrix is positive definite, with \(u_1^\top u_2=u_1^\top u_3=t\) and \(u_2^\top u_3=0\). A sweep with \(u_1\) at an endpoint has \(p=0\) and squared norm \(2t^2\). A sweep with \(u_1\) in the middle has \(p=t^4\) and squared norm
\[
 \lambda_{\rm mid}=t^2+\frac{t^4}{2}+\frac{t^3}{2}\sqrt{4+t^2}.
\]
Thus \(R(t)=\sqrt{2t^2/\lambda_{\rm mid}}\to\sqrt2\) as \(t\downarrow0\). This proves sharpness while every finite triple remains nonsingular.

A wholly rational-row witness is \(u_1=(7/9,4/9,4/9)\), \(u_2=(0,1,0)\), \(u_3=(0,0,1)\). Endpoint placement of the first row gives squared norm \(32/81\); placing it in the middle gives \((1424+64\sqrt{85})/6561\), which is strictly smaller.

## Verification

The accompanying standard-library Python program `check.py` computes orthogonal projectors with exact rational arithmetic. It reconstructs the two invariants of \(M^\top M\), the sweep characteristic-polynomial coefficients, and all six orderings for 159 nonsingular rational three-row configurations. It separately checks a rational parametrization of the sharpness family for nine parameter values. These checks passed; finite tests are not proofs of the uniform theorem. The preceding exterior-power identity, monotonicity argument and explicit limiting family are the analytical certificates.

To reproduce, run `python3 check.py` with Python 3.10 or later. It requires no external packages, network access, or downloaded data.

## Relationship to prior work

Yu and Diakonikolas (arXiv:2609.32034, 25 September 2026) give tight general cyclic-Kaczmarz estimates through a sweep matrix and derive row-correlation-dependent bounds. Those estimates provide a starting operator description but do not state the three-row permutation optimum, the closed-form singular-value comparison, or the sharp universal \(\sqrt2\) ordering penalty. Hansen and Hochstenbach (arXiv:2601.07498) study initial and asymptotic behavior, including order sensitivity and nonnormality, without this exact worst-case three-equation ordering classification. Ferreira, Acebrón and Monteiro (arXiv:2401.02842) survey randomized and cyclic row-action methods and discuss high-coherence effects; their results do not supply the stated six-permutation minimization. Earlier row-ordering heuristics often seek weakly correlated consecutive rows; the present theorem specifically concerns a one-sweep **worst-case error norm** and shows that the optimal order for three independent rows can instead put the two strongest correlations adjacent. A separate two-row overrelaxation result and greedy row-selection coherence results address different operators and objectives; neither implies this three-row optimal-permutation statement.

## Limitations

Only three independent real rows spanning \(\mathbb R^3\), Euclidean error norm, exact projections, one complete sweep and no relaxation are covered. For more rows, different permutations need not share spectral radii; for more than one sweep the one-sweep optimizer need not remain optimal. The \(\sqrt2\) factor is a sharp **supremum** approached along nonsingular instances, not an equality attained by a finite full-rank triple. Previously published equivalent special-case formulas in older projection-product literature cannot be excluded by a finite literature search; independent mathematical and bibliographic assessment has not been performed.

## References

1. R. Yu and J. Diakonikolas, *Tight Convergence Bounds for the Classical Kaczmarz Method*, arXiv:2609.32034, first posted 25 September 2026. https://arxiv.org/abs/2609.32034
2. P. C. Hansen and M. E. Hochstenbach, *On spectral properties and fast initial convergence of the Kaczmarz method*, arXiv:2601.07498, first posted 12 January 2026. https://arxiv.org/abs/2601.07498
3. I. A. Ferreira, J. A. Acebrón and J. Monteiro, *Survey of a class of iterative row-action methods: The Kaczmarz method*, arXiv:2401.02842, first posted 5 January 2024. https://arxiv.org/abs/2401.02842
4. A. Dax, *Kaczmarz Anomaly in Tomography Problems*, AppliedMath **2** (2022), 196–211, Section 4, doi:10.3390/appliedmath2020012 (search-indexed full-text excerpt; direct page access was rate-limited). https://www.mdpi.com/2673-9909/2/2/12
