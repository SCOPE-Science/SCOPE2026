# Planar collapse and chi-square fluctuations of spherical Gram triangles

## Finding

Fix integers \(d\ge 2\) and \(n\ge3\). Let \(U_1,\ldots,U_n\) be independent, uniform unit vectors on the Euclidean sphere \(S^{d-1}\). For distinct indices, put \(R_{ij}=\langle U_i,U_j\rangle\), and define the signed Gram-triangle statistic
\[
T_{n,d}=\sum_{1\le i<j<k\le n}R_{ij}R_{ik}R_{jk}.
\]
Then \(\mathbb E T_{n,d}=\binom n3/d^2\), and its exact finite-sample variance is
\[
\operatorname{Var}(T_{n,d})
=\binom n3\frac{(d-1)(d^2+8d+4)}{d^4(d+2)^2}
+4\binom n2\binom{n-2}2\frac{d-1}{d^4(d+2)}.
\]
There is an exact second-/third-order orthogonal decomposition. Writing
\[
P_{n,d}=\sum_{i<j}(R_{ij}^2-1/d),\qquad
T_{n,d}-\mathbb ET_{n,d}=\frac{n-2}{d}P_{n,d}+Q_{n,d},
\]
its third-order remainder has
\[
\operatorname{Var}(Q_{n,d})=
\binom n3\frac{(d-2)(d-1)(d+4)}{d^4(d+2)^2}.
\]
Thus **the entire genuine third-order component vanishes precisely in dimension \(d=2\)**, while it is nonzero for every \(d\ge3\). In the plane, the cancellation is pointwise for any three unit vectors:
\[
\langle u,v\rangle\langle u,w\rangle\langle v,w\rangle
=\frac{\langle u,v\rangle^2+\langle u,w\rangle^2+\langle v,w\rangle^2-1}{2}.
\]
For each fixed \(d\ge2\), put \(m=(d-1)(d+2)/2\). As \(n\to\infty\),
\[
\frac{T_{n,d}-\mathbb E T_{n,d}}{n^2}
\ \xrightarrow{\ \mathrm d\ }\ 
\frac{\chi_m^2-m}{d^2(d+2)}.
\]
In particular, the limiting law is non-Gaussian in **every** fixed dimension, and
\[
\operatorname{Var}(T_{n,d})\sim
\frac{d-1}{d^4(d+2)}n^4.
\]

## Assumptions and scope

The dimension \(d\) is fixed while \(n\to\infty\); dimensions and sample sizes are integers with \(d\ge2,n\ge3\). Inner products are ordinary real Euclidean inner products. Each \(U_i\) is uniform with respect to normalized rotation-invariant surface measure, and the vectors are independent. The Gram matrix may be singular when \(n>d\): positive definiteness or an LKJ density is **not** assumed. The chi-square variable has \(m\) degrees of freedom. No asymptotic statement is asserted for growing \(d\).

## Proof

**Spherical moments.** For \(U\) uniform on \(S^{d-1}\), rotational symmetry and the unit-norm condition give
\[
\mathbb E[UU^\top]=I_d/d,\qquad
\mathbb E[(U\cdot a)^2(U\cdot b)^2]
=\frac{\|a\|^2\|b\|^2+2(a\cdot b)^2}{d(d+2)}.
\]
The fourth-order identity follows, for example, by orthogonal invariance of the fourth tensor and its contraction \(\mathbb E\|U\|^4=1\); its diagonal coefficient is \(3/[d(d+2)]\). For two independent uniform vectors with inner product \(r\), these formulas imply \(\mathbb Er^2=1/d\) and \(\mathbb Er^4=3/[d(d+2)]\).

**Projections.** On three independent sphere points \(u,v,w\), let \(h(u,v,w)=(u\cdot v)(u\cdot w)(v\cdot w)\). Conditioning on \(u,v\) yields
\[
\mathbb E[h(U_1,U_2,U_3)\mid U_1=u,U_2=v]=(u\cdot v)^2/d,
\]
and conditioning on a single vector yields the constant \(1/d^2\). Consequently the first Hoeffding projection is zero; the second is
\[
p_2(u,v)=\frac{(u\cdot v)^2-1/d}{d}.
\]
The remainder
\[
g_3(u,v,w)=h(u,v,w)-d^{-2}-p_2(u,v)-p_2(u,w)-p_2(v,w)
\]
has zero conditional expectation given any one or any two of its variables. Summing the projections over all unordered triples proves the decomposition in the finding, with \(Q_{n,d}=\sum_{i<j<k}g_3(U_i,U_j,U_k)\). Distinct pair projections are orthogonal (even when sharing a single vertex); all distinct third-order remainder terms are orthogonal and are orthogonal to all pair terms.

**Exact second moments and planar boundary.** Writing \(r=U_1\cdot U_2\), condition first on \(U_1,U_2\) and apply the fourth spherical moment to \(U_3\):
\[
\mathbb Eh^2
=\frac{\mathbb E[r^2(1+2r^2)]}{d(d+2)}
=\frac{d+8}{d^2(d+2)^2}.
\]
Thus
\[
\operatorname{Var}(h)
=\frac{(d-1)(d^2+8d+4)}{d^4(d+2)^2},\qquad
\operatorname{Var}(p_2)=\frac{2(d-1)}{d^4(d+2)}.
\]
Orthogonality gives \(\operatorname{Var}(g_3)=\operatorname{Var}(h)-3\operatorname{Var}(p_2)=(d-2)(d-1)(d+4)/[d^4(d+2)^2]\). This is zero exactly when \(d=2\), and strictly positive for \(d\ge3\). In dimension two, \(g_3\) vanishes almost surely; the displayed planar identity is in fact pointwise. To see this directly, write \(u=(\cos a,\sin a)\), \(v=(\cos b,\sin b)\), \(w=(\cos c,\sin c)\), and expand the cosine double-angle addition formula. Equivalently, the \(3\times3\) Gram matrix has determinant zero, yielding \(1+2h-[(u\cdot v)^2+(u\cdot w)^2+(v\cdot w)^2]=0\).

For two distinct unordered triples sharing exactly one edge, their covariance is \(\operatorname{Var}(p_2)\). For triples sharing at most one vertex, their covariance vanishes by conditioning. There are \(\binom n2\binom{n-2}2\) unordered pairs of different triangles with a common edge. Expanding the variance (with a factor two for off-diagonal pairs) gives the finite variance formula. Alternatively, orthogonality in the Hoeffding decomposition gives
\[
\operatorname{Var}(T_{n,d})=
\frac{(n-2)^2}{d^2}\binom n2\operatorname{Var}(R_{12}^2)
+\binom n3\operatorname{Var}(g_3),
\]
which simplifies to the same expression.

**Fixed-dimension limit.** Define the \(d\times d\) matrix \(W_n=\sum_{i=1}^nU_iU_i^\top\) and its centered fluctuation \(Z_n=n^{-1/2}(W_n-nI_d/d)\). These matrices have trace zero. Since \(\operatorname{tr}(W_n^2)=n^2/d+n\operatorname{tr}(Z_n^2)\), one gets the exact pair identity
\[
P_{n,d}=\frac n2\left(\operatorname{tr}(Z_n^2)-\frac{d-1}{d}\right).
\]
The ordinary multivariate central limit theorem, applied to the entries of \(U_iU_i^\top-I_d/d\), gives convergence of \(Z_n\) to a centered Gaussian element \(Z\) of the \(m\)-dimensional Euclidean space of real symmetric traceless \(d\times d\) matrices. For any traceless symmetric matrices \(A,B\),
\[
\mathbb E[\operatorname{tr}((UU^\top-I_d/d)A)\operatorname{tr}((UU^\top-I_d/d)B)]
=\frac{2\operatorname{tr}(AB)}{d(d+2)}.
\]
Therefore \(\operatorname{tr}(Z^2)\) has law \(2\chi_m^2/[d(d+2)]\), with mean \((d-1)/d\). Finally, the third-order remainder has variance \(O_d(n^3)\); thus \(Q_{n,d}/n^2\to0\) in \(L^2\). Combining these facts and the continuous mapping theorem yields the stated centered chi-square law. Its variance equals \(2m/[d^4(d+2)^2]=(d-1)/[d^4(d+2)]\), matching the leading coefficient of the exact finite variance.

## Verification

The accompanying standalone `verify.py` reproduces exact rational identities for \(23\) dimensions and \(12\) sample sizes each, and verifies the planar identity on all \(8^3\) combinations of octagonal directions using exact arithmetic in \(\mathbb Q(\sqrt2)\). It also checks exact octagonal second and overlapping-triangle fourth moments. A twelve-direction icosahedral quadrature checks the corresponding three-dimensional moments after validating the requisite second- and fourth-order tensor identities. An independently seeded simulation checks the predicted planar asymptotic variance at a finite sample size. The simulation is diagnostic only; the infinite-sample conclusion comes from the analytical proof.

Run `python3 verify.py` with Python 3.10 or later and no third-party packages.

## Relationship to prior work

Archakov, Hansen, and Luo (2022) review random Gram constructions of correlation matrices and discuss their marginal correlation laws; their model section does not give this signed Gram-triangle variance, the planar collapse, or the fixed-dimensional chi-square fluctuation law. Bubeck, Ding, Eldan, and Rácz (2015/2016) study signed triangles in *thresholded* random geometric adjacency matrices in a high-dimensional testing regime; thresholded indicators are different from the unthresholded inner-product products studied here. A published result on triangular third moments of LKJ correlation matrices establishes a related single-triangle expectation for a nonsingular correlation-matrix ensemble but does not provide the all-\(n\) fixed-ambient-dimension variance or non-Gaussian limit; the regime \(n>d\) here has singular Gram matrices. Standard Hoeffding and Gaussian limit theory supplies general tools but not the explicit special-dimensional cancellation or its exact coefficients.

## Limitations

The result assumes iid uniform spherical directions and fixed \(d\). It does not cover unequal directional laws, thresholded geometric graphs, or jointly growing \(d,n\). Its claimed originality is assessed against inspected works, not independently certified against all historical literature. The verification examples are finite checks and cannot replace the all-parameter proof. The law is non-Gaussian at each fixed \(d\); no inference about high-dimensional normality is implied.

## References

1. I. Archakov, P. R. Hansen, and Y. Luo, *A New Method for Generating Random Correlation Matrices*, arXiv:2210.08147 (initial posting October 15, 2022), https://arxiv.org/abs/2210.08147. See the Random Gram Methods section.
2. S. Bubeck, J. Ding, R. Eldan, and M. Z. Rácz, *Testing for high-dimensional geometry in random graphs*, arXiv:1411.5713 (2015), https://arxiv.org/abs/1411.5713, especially Sections 1 and 3.
3. *Exact triangle cumulants reveal the first hidden dependence in LKJ correlation matrices* (public scientific record, 2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-triangle-cumulants-reveal-the-first-hidden-dependence-in-l--955e3ffe3131. Only its accessible indexed scientific summary was compared; the complete record was not retrievable.
