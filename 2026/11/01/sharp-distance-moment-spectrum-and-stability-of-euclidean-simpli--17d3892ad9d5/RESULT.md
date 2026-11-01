# Sharp distance-moment spectrum and stability of Euclidean simplices

## Finding

For every integer \(d\ge3\), put \(n=d+1\). Let \(\Delta\subset\mathbb R^d\) be any nondegenerate Euclidean \(d\)-simplex. Independently choose \(X,Y\) uniformly by \(d\)-dimensional volume in \(\Delta\), and set
\[
\mathcal K(\Delta)=\frac{\mathbb E\|X-Y\|_2^4}{(\mathbb E\|X-Y\|_2^2)^2}.
\]
Its **complete sharp range** is
\[
\boxed{\quad \kappa_n:=\frac{n(n+1)(n+6)}{(n-1)(n+2)(n+3)}\le\mathcal K(\Delta)<U_n:=\frac{6n^3}{(n-1)(n+2)(n+3)}.\quad} \tag{1}
\]
Every value in this half-open interval is attained by a nondegenerate simplex. In dimension three, the sharp range is \(100/63\le\mathcal K<64/21\). The lower equality holds exactly for regular simplices. The upper endpoint is unattainable in full dimension; the only normalized limiting configurations attaining it have a single vertex separated from \(n-1\) coincident vertices, up to vertex relabeling and Euclidean congruence.

The theorem also supplies an exact rigidity identity. Let \(v_1,\ldots,v_n\) be the simplex vertices, \(c=n^{-1}\sum_i v_i\), and put
\[
G_{ij}=\langle v_i-c,v_j-c\rangle,\quad S=\operatorname{tr}G>0,\quad J=I_n-\frac{\mathbf1\mathbf1^{\mathsf T}}{n},\quad E=G-\frac S{n-1}J.
\]
Then
\[
\boxed{\mathcal K(\Delta)-\kappa_n
=A_n\frac{\|E\|_{\mathrm F}^2}{S^2}
+B_n\frac{\sum_{i=1}^n E_{ii}^2}{S^2},}\qquad
A_n=\frac{2(n^2+3n+3)}{(n+2)(n+3)},\quad
B_n=\frac{3n(n+1)}{(n+2)(n+3)}. \tag{2}
\]
Both terms are nonnegative. Writing \(e=\frac{1}{\binom{n}{2}}\sum_{i<j}\|v_i-v_j\|_2^2=2S/(n-1)\), one consequently has the quantitative edge-shape estimate
\[
\boxed{\max_{i<j}\left|\frac{\|v_i-v_j\|_2^2}{e}-1\right|
\le (n-1)\sqrt{\frac{(n+2)(n+3)}{2(n^2+3n+3)}\bigl(\mathcal K(\Delta)-\kappa_n\bigr)}.} \tag{3}
\]
The exponent \(1/2\) in this estimate is optimal among uniform power-law bounds, although the numerical prefactor in (3) is not asserted to be optimal.

## Assumptions and scope

The simplex is full-dimensional and has exactly \(n=d+1\) affinely independent vertices; \(d\ge3\). The distribution is independent uniform *interior volume sampling*, rather than sampling on edges, facets, vertices, or isotropic random lines. Distances are ordinary Euclidean distances. The ratio \(\mathcal K\) is invariant under translation, rotation, reflection and positive homothety. Statements about degenerate configurations refer only to limits in the fixed-scale closure, not to applying a full-dimensional probability law to a degenerate body. A known planar-triangle moment interval is not presented as new; the result concerns dimensions at least three.

## Proof

**1. Exact pairwise moment formula.** Translate so \(c=0\). Write \(X=\sum_{i=1}^n\lambda_i v_i\) for a uniformly Dirichlet-distributed barycentric vector \(\lambda\sim\operatorname{Dirichlet}(1,\ldots,1)\). Its mixed integer moments are
\[
\mathbb E\prod_i\lambda_i^{a_i}=\frac{(n-1)!\prod_i a_i!}{(n-1+\sum_i a_i)!}. \tag{4}
\]
Since \(\sum_i v_i=0\), we get \(\mathbb EX=0\) and
\[
\mathbb E[XX^{\mathsf T}]=\frac M{n(n+1)},\quad \mathbb E\|X\|_2^2=\frac S{n(n+1)},\qquad M=\sum_i v_i v_i^{\mathsf T}. \tag{5}
\]
Put \(T=\operatorname{tr}(M^2)=\operatorname{tr}(G^2)\), and \(H=\sum_i\|v_i\|_2^4=\sum_iG_{ii}^2\). The generating identity for complete homogeneous symmetric polynomials, applied to \(p_1=\sum_i\langle t,v_i\rangle=0\), gives
\[
\mathbb E\langle t,X\rangle^4
=\frac{3(\sum_i\langle t,v_i\rangle^2)^2+6\sum_i\langle t,v_i\rangle^4}
{n(n+1)(n+2)(n+3)}. \tag{6}
\]
Averaging (6) over an independent standard Gaussian \(t\in\mathbb R^d\) uses
\(\mathbb E_t\langle t,x\rangle^4=3\|x\|_2^4\),
\(\mathbb E_t(\sum_i\langle t,v_i\rangle^2)^2=S^2+2T\), and
\(\mathbb E_t\sum_i\langle t,v_i\rangle^4=3H\).
Thus
\[
\mathbb E\|X\|_2^4=\frac{S^2+2T+6H}{n(n+1)(n+2)(n+3)}. \tag{7}
\]
For an independent copy \(Y\), expanding \(\|X-Y\|_2^4\) and using \(\mathbb EX=0\) yields
\[
\begin{aligned}
\mu&:=\mathbb E\|X-Y\|_2^2=\frac{2S}{n(n+1)},\\
\nu&:=\mathbb E\|X-Y\|_2^4
=\frac{2(S^2+2T+6H)}{n(n+1)(n+2)(n+3)}
+\frac{2S^2+4T}{n^2(n+1)^2}.
\end{aligned} \tag{8}
\]
Equations (7)--(8) are valid at rank-deficient limiting vertex configurations as algebraic identities, although the original uniform-volume interpretation requires nondegeneracy.

**2. Lower bound and exact rigidity.** The nonzero eigenvalues of the centered Gram matrix \(G\) are positive and number \(n-1\). Hence
\(T\ge S^2/(n-1)\). Also \(H\ge S^2/n\) by Cauchy--Schwarz on its diagonal. Subtracting the value of (8) at these lower bounds and dividing by \(\mu^2\) gives
\[
\frac\nu{\mu^2}-\kappa_n
=A_n\frac{T-S^2/(n-1)}{S^2}
+B_n\frac{H-S^2/n}{S^2}. \tag{9}
\]
Because \(G\mathbf1=0\), \(\operatorname{tr}E=0\), and \(J\) is the orthogonal projector onto \(\mathbf1^\perp\), one has
\(T-S^2/(n-1)=\|E\|_{\mathrm F}^2\) and
\(H-S^2/n=\sum_iE_{ii}^2\). This proves (2). Equality forces \(G=(S/(n-1))J\), which is precisely the Gram matrix of a regular simplex, since every squared edge length then equals \(2S/(n-1)\).

**3. A sharp centered quartic lemma.** For \(n\ge4\) and real numbers \(a_1,\ldots,a_n\) with \(\sum_i a_i=0\),
\[
\sum_i a_i^4\le \frac{n^2-3n+3}{n(n-1)}\left(\sum_i a_i^2\right)^2. \tag{10}
\]
Equality for nonzero vectors holds exactly when, up to permutation and common sign/scale, one entry is \(n-1\) and the others are \(-1\).

Here is a proof, including the nonstandard equality claim. Normalize \(\sum_i a_i^2=1\). At a maximum of \(\sum_i a_i^4\) subject to both constraints, Lagrange multipliers show that every coordinate solves one cubic \(4z^3-2\lambda z-\eta=0\). If three distinct real roots \(\alpha<\beta<\gamma\) occur, the two extreme roots have positive cubic derivative. A root occurring twice admits the tangent perturbation \((1,-1)\) on its equal-coordinate pair, and the constrained second variation is then positive, contradicting maximality. Thus each extreme root occurs once and the middle root occurs \(n-2\) times. The three roots sum to zero (the cubic has no quadratic coefficient), whereas the coordinates sum to zero, so \((n-3)\beta=0\). Since \(n\ge4\), \(\beta=0\) and \(\gamma=-\alpha\), giving fourth-to-second ratio \(1/2\). But the two-level vector \((n-1,-1,\ldots,-1)\) has strictly larger ratio \((n^2-3n+3)/(n(n-1))>1/2\). Consequently a global maximizer has exactly two coordinate values. If their multiplicities are \(k,n-k\), normalization and centering give the fourth-power sum
\(n/[k(n-k)]-3/n\); this is largest exactly for \(k=1\) or \(n-1\), proving (10) and uniqueness. Multipliers apply because the two gradients of the constraints are independent on the nonzero centered unit sphere.

**4. Matrix quartic bound and sharp upper endpoint.** The centered positive semidefinite Gram matrix, after division by \(S\), is a convex combination of rank-one matrices \(aa^{\mathsf T}\) with \(\sum_i a_i=0\) and \(\sum_i a_i^2=1\). Convexity of the squared diagonal norm, followed by (10), shows
\[
H\le\frac{n^2-3n+3}{n(n-1)}S^2. \tag{11}
\]
Equality for \(n\ge4\) forces \(G\) to be a rank-one Gram matrix supported on the unique spike direction from (10): strict convexity of the squared diagonal norm and the distinct spike-coordinate profiles exclude nontrivial mixtures. Independently, positive semidefiniteness gives \(T\le S^2\), with equality exactly for rank one. Both bounds are met by the same spike matrix \(G=Saa^{\mathsf T}\). Substitution into (8) proves the upper value \(U_n\) in (1), and the unique normalized limiting shape. Every full-dimensional simplex has \(\operatorname{rank}G=n-1\ge3\), so its upper inequality is strict.

**5. Every interior value occurs.** Fix \(S=n(n-1)\), put \(w=(n-1,-1,\ldots,-1)^{\mathsf T}\), and consider
\[
G_t=(1-t)nJ+tww^{\mathsf T},\quad 0\le t<1. \tag{12}
\]
It is centered, positive definite on \(\mathbf1^\perp\), and has trace \(S\), so it is the centered Gram matrix of a nondegenerate \((n-1)\)-simplex. At \(t=0\) it is regular; at \(t=1\) it is the spike Gram matrix. As the deviations in (2) are quadratic in \(G-G_0\),
\[
\mathcal K(G_t)=\kappa_n+t^2(U_n-\kappa_n). \tag{13}
\]
This covers precisely the entire half-open interval (1).

**6. Stability and optimal exponent.** For each edge, with \(a=e_i-e_j\),
\[
\|v_i-v_j\|_2^2-\frac{2S}{n-1}=a^{\mathsf T}Ea,
\quad |a^{\mathsf T}Ea|\le2\|E\|_{\mathrm F}.
\]
Using (2) and the mean edge-square value gives (3). To see that a power larger than \(1/2\) is impossible uniformly, choose any nonzero symmetric matrix \(F\) satisfying \(F\mathbf1=0\) and \(\operatorname{tr}F=0\), and deform the regular Gram matrix by \(G_\varepsilon=\frac S{n-1}J+\varepsilon F\). For sufficiently small real \(\varepsilon\) it remains a full-rank centered Gram matrix. Every such nonzero \(F\) changes at least one squared edge to first order: if all \((e_i-e_j)^{\mathsf T}F(e_i-e_j)\) vanished, the elementary double-centering identity would imply \(F=0\). The left side of (3) is therefore of order \(|\varepsilon|\), whereas (2) shows that the moment excess is of order \(\varepsilon^2\). This proves sharpness of the exponent.

## Verification

Run `python3 verify.py` with Python 3 and its standard library. The program independently enumerates degree-four Dirichlet moments from the factorial definition, compares them with (7)--(9) for rational simplex configurations, checks rational instances of the whole spectrum and Gram interpolation for orders four through ten, checks (3) on independently generated shapes, and compares two cases with seeded direct barycentric-pair sampling. The executed result was `VERIFY_OK 591 exact identities and seeded pair-distance tests`.

The infinite-dimensional-parameter and universal inequalities are proved above; finitely many computations cannot certify them. In particular, the variational proof of (10) and the rank-one equality argument in step 4 are necessary analytic components, not consequences of numerical tests.

## Relationship to prior work

Anderson, Goyal and Rademacher derive general directional moments of the uniform simplex through homogeneous symmetric polynomials; that established technique supplies (4) and (6), not the range or extremal geometry of the normalized Euclidean **pairwise distance** statistic in (1). Nikolov and Rafailov investigate sums of powered distances from one moving observation point to fixed regular-polytope vertices, a different object and optimization variable. Reichenwallner supplies general chord-moment formulas in a **planar triangle**, not a higher-dimensional shape optimization; the planar specialization is excluded from the new-dimensional claim. A known stochastic bound for **difference-body gauge distances** concerns an affine-invariant metric dependent on the convex body, rather than Euclidean distances, and has no consequence for the Euclidean shape-dependent two-moment ratio. A separate parallelogram result compares sampling from the boundary and interior, not the all-interior simplex spectrum.

The contribution here is the combined full-dimensional interval, equality classification at both ends of its closure, exact positive Gram-defect decomposition and sharp square-root rigidity for all \(d\ge3\), not the foundational barycentric moment formula.

## Limitations

The range is for simplices, not arbitrary convex bodies. The sampling is uniform interior volume and independent. The stability prefactor is explicit but is not claimed to be the best possible one. The upper endpoint occurs only as a degeneration; a literal uniform volume measure on the limiting lower-dimensional configuration is not used. No claim is made about all higher moments, finite-sample statistical estimation, or full shape reconstruction from two moments. Historical priority is provisional, and no independent mathematical audit has been performed.

## References

1. J. Anderson, N. Goyal and L. Rademacher, *Efficient Learning of Simplices*, arXiv:1211.2227v1, first publicly posted 2012-11-09, https://arxiv.org/abs/1211.2227; Section 3 of the public HTML version discusses simplex moments.
2. N. Nikolov and R. Rafailov, *On extremums of sums of powered distances to a finite set of points*, arXiv:1211.2975v1, first publicly posted 2012-11-13, https://arxiv.org/abs/1211.2975.
3. B. Reichenwallner, *Moments of volumes of lower-dimensional random simplices are not monotone*, Monatshefte für Mathematik 186 (2018), 481--501; published online 2017-06-21, https://doi.org/10.1007/s00605-017-1077-3; Section 3 studies two-point chord moments in planar triangles.
