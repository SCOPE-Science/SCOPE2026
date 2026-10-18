# Sharp Lipschitz moduli of weighted best-line projections in real \(\ell_p^n\)

## Finding
Let \(1<p<\infty\), \(n\ge 1\), and \(0\ne v\in\mathbb R^n\). The metric projection \(P_v\) sends each point of \(\ell_p^n(\mathbb R)\) to its unique nearest point in \(\mathbb Rv\). Write \(I=\{i:v_i\ne0\}\), \(k=|I|\), \(w_i=|v_i|\), \(V=(\sum_{i\in I}w_i^p)^{1/p}\), and \(q=p/(p-1)\). For distinct \(i,j\in I\), set
\[
F_{ij}(p;v)=\frac{\left(w_i^{q(q-1)}+w_j^{q(q-1)}\right)^{1/q}}{w_i^q+w_j^q}.
\]
Then the **exact global Lipschitz constant** \(L_p(v)=\sup_{x\ne y}\|P_vx-P_vy\|_p/\|x-y\|_p\) is
\[
\boxed{L_p(v)=\begin{cases}
1,&k=1\ \text{or}\ p=2,\\
V\max_{i<j,\ i,j\in I} F_{ij}(p;v),&k=2,\ p\ne2,\\
V/\min_{i\in I}w_i,&k\ge3,\ 1<p<2,\\
V\max_{i<j,\ i,j\in I}F_{ij}(p;v),&k\ge3,\ p>2.
\end{cases}}
\]
Here each maximum ranges only over active coordinates. For \(p\ne2\), \(P_v\) is nonexpansive if and only if \(k=1\), or \(k=2\) and the two nonzero coordinate magnitudes are equal. In particular, for non-Hilbert exponents and support at least three, the exact modulus changes discontinuously when the exponent reaches \(2\).

## Assumptions and scope
All vector spaces and scalar optimizations are **real**. The ambient dimension is finite and at least one component of \(v\) is nonzero. Coordinate signs can be removed by an isometry of \(\ell_p^n\), and zero coordinates do not affect \(P_v\) or its Lipschitz constant, so in the proof take \(n=k\) and \(v_i=w_i>0\). The object is the nonlinear nearest-point projection, not a freely chosen linear projection. The exponent \(p=2\) is included separately because the projection is then orthogonal.

## Proof
**1. Scalar equation and derivatives.** Write \(P_vx=t(x)v\). Strict convexity makes \(t(x)\) the unique zero of
\[
F_x(t)=\sum_{i=1}^{k}v_i\operatorname{sgn}(x_i-tv_i)|x_i-tv_i|^{p-1}.
\]
It is continuous in \(x\), since each \(F_x\) is continuous, strictly decreasing, and has opposite signs at sufficiently large negative and positive \(t\). At a point whose residuals \(r_i=x_i-t(x)v_i\) are all nonzero, implicit differentiation gives
\[
\frac{\partial t}{\partial x_i}=\frac{g_i}{\sum_jv_jg_j},\qquad g_i=v_i|r_i|^{p-2},\qquad \sum_i v_i\operatorname{sgn}(r_i)|r_i|^{p-1}=0.
\]
Thus \(\|DP_v(x)\|_{p\to p}=V\|g\|_q/(\sum_jv_jg_j)\). For \(p>2\) the same formula applies whenever \(r\ne0\), including zero residual components (for which \(g_i=0\)). As \(t\) is continuous and differentiable off \(\mathbb Rv\), a uniform bound on these derivatives implies the corresponding global Lipschitz bound: integrate along a segment off \(\mathbb Rv\), splitting at its possible single intersection with the line; segments lying on the line have ratio \(1\).

**2. The case \(p>2\): a two-coordinate reduction.** Put \(\sigma=(p-2)/(p-1)\), so \(0<\sigma<1\), and \(a_i=v_i|r_i|^{p-1}\). The moment equation says that the positive and negative residual index sets \(I_+,I_-\) have equal total \(a\)-mass. Normalize this common positive mass to \(1\); the quotient \(\|g\|_q/(v\cdot g)\) is unchanged. Then, up to a common positive scaling factor that cancels in the norm ratio, \(g_i=v_i^{q-1}a_i^\sigma\), and within either sign set the corresponding \(a_i\) sum to \(1\).

Let \(C=\max_{i<j}F_{ij}(p;v)\). For each pair, the positive two-vector \((v_i^{q-1},v_j^{q-1})\) has \(\ell_q\) norm at most \(C(v_i^q+v_j^q)\). Hence for each \(y\in\mathbb R^k\) with \(\|y\|_p\le1\), after replacing \(y\) by \(|y|\), the numbers
\[
d_i=(y_i-Cv_i)v_i^{q-1}
\]
satisfy \(d_i+d_j\le0\) for every distinct \(i,j\). Furthermore **at most one \(d_i\) can be positive**: otherwise \(y_i>Cv_i\) and \(y_j>Cv_j\) imply \(\|y\|_p>C(v_i^p+v_j^p)^{1/p}\ge1\), contrary to the assumption; the last inequality follows from Hölder's inequality applied to the two-coordinate vector above.

If \(E\) is either sign set, \(\sum_{i\in E}a_i=1\) and \(a_i\ge0\) imply
\[
\sum_{i\in E}d_ia_i^\sigma\le\max_{i\in E}d_i.
\]
Indeed, if all \(d_i\le0\), use \(\sum_i a_i^\sigma\ge1\); if one is positive, its positive contribution is no larger than \(d_i\), while all others are nonpositive. Applying this to \(I_+,I_-\), and using \(d_i+d_j\le0\) for every pair across the two sets, yields
\[
y\cdot g-C(v\cdot g)=\sum_i d_ia_i^\sigma\le0.
\]
Taking the supremum over \(\|y\|_p\le1\) gives \(\|g\|_q\le C(v\cdot g)\). Conversely, for any pair \(i\ne j\) take residuals \(r_i=v_i^{-1/(p-1)}\), \(r_j=-v_j^{-1/(p-1)}\), all other residuals zero. They satisfy the moment condition and give gradient \(g\) supported exactly on the pair with \(g_i=v_i^{q-1}\), \(g_j=v_j^{q-1}\). This realizes derivative norm \(VF_{ij}\). Maximize over pairs to prove the stated equality.

**3. The case \(1<p<2\) and at least three active coordinates.** At all points with nonzero residual coordinates,
\[
\frac{\|g\|_q}{\sum_i v_ig_i}\le\frac{\|g\|_1}{(\min_i v_i)\|g\|_1}\le\frac1{\min_i v_i}.
\]
For a global bound without assuming differentiability at zero residuals, replace \(\varphi(s)=\operatorname{sgn}(s)|s|^{p-1}\) by \(\varphi_\varepsilon(s)=s(s^2+\varepsilon^2)^{(p-2)/2}\). Its derivative is strictly positive. The root \(t_\varepsilon(x)\) of \(\sum_i v_i\varphi_\varepsilon(x_i-t_\varepsilon v_i)=0\) is smooth, and the same positive-gradient inequality shows \(\operatorname{Lip}(x\mapsto t_\varepsilon(x)v)\le V/\min_iv_i\). As \(\varepsilon\downarrow0\), strict monotonicity gives \(t_\varepsilon(x)\to t(x)\) pointwise, so this uniform Lipschitz bound passes to \(P_v\).

For the reverse inequality choose an index \(i\) of minimal \(v_i\) and two other indices \(j,l\). Take residuals away from zero at \(j,l\), of opposite signs, scaled to make their two moment contributions cancel; set all other residuals at fixed nonzero magnitudes and choose one opposite-sign residual to balance the full equation. Now let \(r_i=\varepsilon>0\) and adjust that balancing residual continuously. As \(\varepsilon\downarrow0\), the weight \(g_i=v_i\varepsilon^{p-2}\) diverges, while all other \(g_j\) remain bounded. Thus the derivative norm approaches \(V/v_i\), proving sharpness. All approximating points have nonzero residuals, so the derivative formula applies.

**4. Supports of size one and two.** One active coordinate gives the ordinary contractive coordinate projection. With exactly two active coordinates the residual moment equation has the fixed signed ratio \(|r_i|/|r_j|=(v_j/v_i)^{1/(p-1)}\). Hence \(t(x)\) is linear, and its norm is exactly the two-coordinate value \(VF_{ij}\), for all \(p\ne2\). At \(p=2\) the projection is orthogonal and has norm \(1\).

**5. Contractivity.** A nonzero linear or nonlinear retraction onto a subspace has Lipschitz constant at least \(1\). For \(k\ge3\) and \(p<2\), \(V/\min v_i>1\). For \(k\ge3\) and \(p>2\), Hölder yields \(F_{ij}\ge(v_i^p+v_j^p)^{-1/p}\), so \(VF_{ij}>1\). For \(k=2\), equality in Hölder for the two-coordinate norm holds exactly when \(v_i^{q-1},v_j^{q-1}\) are proportional to \(v_i^{p-1},v_j^{p-1}\). When \(p\ne2\), this requires \(v_i=v_j\); conversely equal magnitudes give \(VF_{ij}=1\). This completes the classification. \(\square\)

## Verification
The standalone program `check_weighted_line.py` checks the predicted formula against normalized residual-gradient ratios for random positive generators, with both signs in the zero-moment constraint. It also tests the two-coordinate tangent witnesses for \(p>2\) and sharp near-vanishing-residual gradients for \(p<2\). Finite numerical checks are diagnostics only; the proof above establishes the assertions for every admissible exponent, dimension, and generator.

## Relationship to prior work
Borodin, Druzhinin and Chesnokova (2017, Theorem 2) established finiteness and quantitative estimates for the Lipschitz constant of a best-line projection supported on finitely many atoms, not an exact all-weight formula. Németh (2025, Theorem 1) gives an abstract qualitative Hilbert-space characterization of linearity of all metric projections, rather than the present quantitative classification. Berens, Finzel, Li, and Xu (1997) established uniform Lipschitz continuity of best finite-dimensional \(\ell_p\) approximations but no corresponding exact all-weight modulus was identified in the available material. A previously published weighted-cross-polytope projection calculation has the same two-coordinate norm factor \(F_{ij}\); that shared planar rank-one expression is not claimed as new. The previously reported sharp formula for the unweighted constant-vector line is recovered as a special case: \(L_p(1,\ldots,1)=n^{1/p}\) for \(1<p<2\), and \((n/2)^{1/p}\) for \(p>2\), provided \(n\ge3\). That unweighted case is not asserted to be new. The nonuniform exact pair-support reduction, full weighted formula, and weighted contractivity classification are the asserted contributions.

## Limitations
The formulas concern finite-dimensional **real** \(\ell_p\) spaces; they are not asserted for complex scalars, arbitrary nonatomic \(L_p\), or infinite-support generators. The proof identifies sharp moduli, not all equality pairs of distinct vectors. Publication priority remains subject to possible older equivalent best-approximation formulations and independent literature review.

## References
1. P. A. Borodin, Yu. Yu. Druzhinin, and K. V. Chesnokova, "Finite-dimensional subspaces of \(L_p\) with Lipschitz metric projection," *Mathematical Notes* **102** (2017), 465–474. DOI: 10.4213/mzm11479 (original Russian text); DOI: 10.1134/S0001434617090188 (English edition). Full source: https://www.mathnet.ru/php/getFT.phtml?jrnid=mzm&option_lang=rus&paperid=11479&what=fullt
2. A. B. Németh, "The metric geometry of subspaces and convex cones of the Banach space revisited," arXiv:2511.19382v1, first posted 2025-11-24. https://arxiv.org/pdf/2511.19382
3. H. Berens, M. Finzel, W. Li, and Y. Xu, "Hoffman's Error Bounds and Uniform Lipschitz Continuity of Best \(\ell_p\)-Approximations," *Journal of Mathematical Analysis and Applications* **213** (1997), 183–201. DOI: 10.1006/jmaa.1997.5521.
