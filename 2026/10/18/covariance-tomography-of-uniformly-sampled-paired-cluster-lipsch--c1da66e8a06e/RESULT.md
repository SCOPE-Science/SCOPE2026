# Covariance tomography of uniformly sampled paired-cluster Lipschitz potentials

## Finding

Fix an integer \(m\geq2\) and \(0<t\leq1\). Let \(M\) consist of \(m\) labeled pairs \(\{a_i,b_i\}\), where \(d(a_i,b_i)=t\), and every distance between different pairs equals \(1\). Let \(H=\{z\in\mathbb R^{2m}:\sum_v z_v=0\}\), with the Euclidean inner product inherited from labeled vertex coordinates. Let \(Z\) be uniform in the image in \(H\) of the unit ball of the real Lipschitz space on \(M\) modulo constants.

Write \(P=I-\mathbf 1\mathbf 1^{\mathsf T}/(2m)\) and
\[
U=\frac12\sum_{i=1}^{m}(e_{a_i}-e_{b_i})(e_{a_i}-e_{b_i})^{\mathsf T}.
\]
Both \(U\) and \(P-U\) are mutually orthogonal projections; their ranks are \(m\) and \(m-1\). The **complete covariance operator** is
\[
\boxed{\operatorname{Cov}(Z)=\lambda_{\mathrm{inter}}(P-U)+\lambda_{\mathrm{intra}}U,}
\]
where
\[
\boxed{\lambda_{\mathrm{intra}}=\frac{t^2(4m-3mt+t)}{12m(2-t)},\qquad
\lambda_{\mathrm{inter}}=\frac{m(t^2-2t+2)+(t-2)^2}{12m}.}
\]
For \(0<t<1\), the gap is strictly positive:
\[
\boxed{\Delta=\lambda_{\mathrm{inter}}-\lambda_{\mathrm{intra}}=
\frac{(1-t)\big[m(1-t)(t+2)+(1-t)^2+3\big]}{6m(2-t)}>0.}
\]
Consequently the orthogonal projector of \(\operatorname{Cov}(Z)\) onto its **smallest eigenspace** equals \(U\); its negative off-diagonal entries are exactly \(U_{a_i b_i}=U_{b_i a_i}=-1/2\), with all other off-diagonal entries zero. Thus **the uniform covariance determines the entire unknown matching** on the labeled vertices, provided \(t<1\). In fact the covariance off-diagonal entries for paired vertices exceed those for unpaired vertices by precisely \(\Delta/2\). Moreover \(\lambda_{\mathrm{intra}}\) is strictly increasing in \(t\), so the covariance determines the common within-pair distance as well.

For fixed \(0<t<1\), \(\Delta\to(1-t)^2(t+2)/[6(2-t)]\) as \(m\to\infty\). In the near-equilateral boundary layer \(t=1-c/m\), with fixed \(c>0\), one has
\[
\boxed{\lim_{m\to\infty}m^2\Delta=\frac{c(c+1)}2.}
\]
At \(t=1\), both eigenvalues equal \((m+1)/(12m)\); the covariance is isotropic on \(H\) and necessarily contains no information about the arbitrary pairing. The formula does not assert a recovery result at that endpoint.

## Assumptions and scope

All spaces and functions are real. The uniform law means normalized Lebesgue measure in any anchored \((2m-1)\)-coordinate realization of the Lipschitz unit ball, carried to the mean-zero hyperplane \(H\). This law is independent of the anchor: all changes of anchor are volume-preserving integer linear maps, and subtracting the mean identifies potential vectors modulo constants. The covariance matrix is expressed in the fixed, canonical labeled Euclidean coordinates of \(H\); it is not asserted to be invariant under arbitrary changes of basis. Every \(m\ge2\) and every real \(0<t\le1\) are covered. The pairing is unspecified but fixed, and all pair distances are identical.

The previously known exact volume for this two-level clustered family,
\[\operatorname{vol}_{2m-1}(Q)=2m\,t\,(2t-t^2)^{m-1},\]
is used only to normalize the probability law. This volume identity is not presented as new. The new contribution is the exact second-moment operator, its strict two-eigenspace separation and consequent inverse reconstruction, including the transition scale at the equilateral boundary.

## Proof

**1. Range description.** A potential \(x=(x_v)_{v\in M}\) has Lipschitz seminorm at most one exactly when all differences between different pairs have magnitude at most one and \(|x_{a_i}-x_{b_i}|\le t\). These conditions are equivalent to
\[\max_v x_v-\min_v x_v\le1,\qquad |x_{a_i}-x_{b_i}|\le t\quad(1\le i\le m).\]
Indeed the global extrema, if in different pairs, differ by at most one; if in the same pair, by at most \(t\le1\). The reverse implication is immediate.

**2. Dissection at a unique minimum.** The set of potentials with a tied minimum has zero volume. On the chamber whose unique minimum is at a prescribed vertex, translate all coordinates so that this minimum is zero. This is a determinant-\(\pm1\) transformation between anchor coordinate systems, so it preserves Lebesgue measure. If the minimum is \(a_1\), the other member \(b_1\) lies in \([0,t]\), while every other pair \((x_{a_i},x_{b_i})\), \(i\ge2\), lies independently in
\[B_t=\{(u,v)\in[0,1]^2:|u-v|\le t\}.\]
The band has area \(A_t=2t-t^2\). Every minimum chamber therefore has volume \(t A_t^{m-1}\), and exchangeability makes its minimum vertex uniform among \(2m\) labels. Conditioned on that vertex, the special coordinate is uniform on \([0,t]\), and the remaining pairs are independent and uniform on \(B_t\). Subtracting the global mean afterward does not change the coordinate differences used below. This dissection proves the displayed volume normalization and completely specifies the probability law.

**3. Exact band moments.** For independent \((V,W)\) uniformly distributed on \(B_t\), symmetry gives \(\mathbb E[(V+W)/2]=1/2\). The difference \(D=V-W\) has density \((1-|d|)/A_t\) for \(|d|\le t\). Therefore
\[q_t=\mathbb E[D^2]=\frac{2}{A_t}\int_0^t d^2(1-d)\,\mathrm{d}d
=\frac{t^2(4-3t)}{6(2-t)}.\]
Conditional on \(D=d\), the midpoint \(S=(V+W)/2\) is uniform on \([|d|/2,1-|d|/2]\). Its conditional mean is always \(1/2\), and hence
\[s_t=\operatorname{Var}(S)=\frac{2}{12A_t}\int_0^t(1-d)^3\,\mathrm{d}d
=\frac{4-6t+4t^2-t^3}{24(2-t)}.\]
For the exceptional pair, its midpoint is \(Y/2\) with \(Y\) uniform on \([0,t]\), so its mean is \(t/4\), its variance is \(t^2/48\), and its squared difference is \(Y^2\) of mean \(t^2/3\).

**4. Covariance eigenspaces.** Let \(w_i=(e_{a_i}-e_{b_i})/\sqrt2\). Independent within-pair swaps and pair permutations leave the distribution invariant. Thus the contrast directions \(w_i\) have zero mixed covariances and equal variances, and their span (projection \(U\)) is a covariance eigenspace. The complementary mean-zero pair-constant subspace (projection \(P-U\)) is also invariant, and permutation exchangeability makes its covariance scalar. Global sign symmetry makes \(\mathbb E Z=0\).

For a fixed pair, the chance of being special is \(1/m\). Consequently
\[\operatorname{Var}\langle Z,w_i\rangle
=\frac{1}{2m}\left(\frac{t^2}{3}+(m-1)q_t\right)
=\frac{t^2(4m-3mt+t)}{12m(2-t)}=\lambda_{\mathrm{intra}}.\]
For two distinct pairs, their normalized pair-mean contrast is
\[u_{ij}=\frac{e_{a_i}+e_{b_i}-e_{a_j}-e_{b_j}}{2},\qquad\|u_{ij}\|_2=1.\]
With probability \((m-2)/m\), neither pair contains the global minimum, and \(\mathbb E\langle Z,u_{ij}\rangle^2=2s_t\). Otherwise, with probability \(2/m\), one of these pairs is special, giving
\[\mathbb E\langle Z,u_{ij}\rangle^2=s_t+\frac{t^2}{48}+\left(\frac12-\frac t4\right)^2.\]
Thus
\[\lambda_{\mathrm{inter}}=\frac{2(m-1)}m s_t+
\frac2m\left[\frac{t^2}{48}+\frac{(2-t)^2}{16}\right]
=\frac{m(t^2-2t+2)+(t-2)^2}{12m}.\]
Since the orthogonal eigenspaces span \(H\), this proves the entire covariance formula without unaccounted directions.

**5. Strict gap and reconstruction.** Subtracting the two rational formulas yields the positive factorization for \(\Delta\) displayed above. Both factors \(m(1-t)(t+2)\) and \((1-t)^2+3\) are nonnegative, the latter strictly positive, so \(\Delta>0\) when \(t<1\). Therefore the smallest-eigenvalue spectral projector is exactly \(U\), which records all paired labels. Equivalently, for distinct vertices \(v,w\),
\[\operatorname{Cov}(Z)_{vw}=
-\frac{\lambda_{\mathrm{inter}}}{2m}
+\begin{cases}\Delta/2,&\{v,w\}\text{ is a pair},\\0,&\text{otherwise}.
\end{cases}\]
The expression for \(\lambda_{\mathrm{intra}}\) is strictly increasing with \(t\): the term \(t^2/3\) is strictly increasing and \(q_t=\mathbb E[D^2\mid |D|\le t]\) is nondecreasing as \(t\) expands the truncation of the fixed triangular density \(1-|d|\) on \([-1,1]\). Thus the bottom eigenvalue uniquely identifies \(t\) for known \(m\).

**6. Asymptotic boundary.** In the exact expression for \(\Delta\), let \(m\to\infty\) with fixed \(t<1\), to obtain the positive quadratic-in-\(1-t\) limit. Next set \(t=1-c/m\), with fixed \(c>0\) and \(m>c\); multiplication by \(m^2\) gives \(c(c+1)/2+o(1)\) directly. Finally at \(t=1\), substitution gives \(\lambda_{\mathrm{intra}}=\lambda_{\mathrm{inter}}=(m+1)/(12m)\), as required by full permutation symmetry of the equilateral metric. This completes the proof.

## Verification

The attached `enumerate_lattice.cpp` enumerates integer potential vectors in a dilated anchored Lipschitz ball independently of the minimum-chamber sampling argument. For \(t=a/b\) in lowest terms and integer \(k\ge0\), it counts lattice points in the \(bk\)-dilate and exactly accumulates quadratic sums of one within-pair contrast and one between-pair contrast. Because the \(b\)-dilate has integral vertices (the constraints are difference inequalities with integer right sides), weighted Ehrhart theory makes these sequences polynomials in \(k\) of degrees at most \(2m-1\) and \(2m+1\). Exact finite differences yield their leading coefficients, whose ratios give the two uniform quadratic moments. The companion `verify.py` checks five independent configurations with exact integers and rational arithmetic:

- \((m,t)=(2,1/2)\): \((\lambda_{\mathrm{intra}},\lambda_{\mathrm{inter}})=(11/288,19/96)\).
- \((2,1)\): \((1/8,1/8)\).
- \((2,2/3)\): \((7/108,1/6)\).
- \((3,1/2)\): \((1/27,1/6)\).
- \((3,1)\): \((1/9,1/9)\).

All five passed using `python3 verify.py` and `g++` with C++17 support. These finite checks are independent corroboration, not a substitute for the exact argument covering arbitrary \(m\) and \(t\).

## Relationship to prior work

The finite-dimensional Lipschitz-free and dual-ball framework is standard; the canonical molecular description and extremal Banach-space context are established in the cited papers. The existing equilateral volume law and the clustered-metric volume dissection are credited, not claimed. Published research on finite-metric volume products analyzes different functionals of the body and, in its equilateral case, the same unit Lipschitz polytope, but does not state its paired-cluster covariance operator or labeled-pair reconstruction. Work on extreme molecules addresses vertices of the polar unit ball rather than second moments of the uniform measure on the Lipschitz unit ball. Related published findings on shortened-pair facet enumeration and clustered projection constants give, respectively, a face census and an operator norm, not the second-moment spectrum. The question here is inverse recovery from the full **interior** covariance, not recovery from a supplied metric or facet list.

## Limitations

Recovery requires the canonical labeled Euclidean coordinate system and the full population covariance, not an unspecified linearly transformed covariance nor a finite empirical covariance estimate. When \(t=1\), the pairing is metrically invisible and covariance reconstruction is impossible. No finite-sample stability guarantee is asserted; the gap formula quantifies a population spectral separation only. The two-distance, equal-pair-size, common-within-pair-length assumptions are essential to the stated formulas. The theorem says nothing about heterogeneous within-pair lengths or general ultrametrics. An equivalent theorem indexed under different terminology cannot be excluded solely by the completed literature search.

## References

1. Ramón J. Aliaga, *Extreme points in Lipschitz-free spaces over compact metric spaces*, arXiv:2102.01219 (first public version 1 February 2021), especially the introduction and Theorem 1. Primary MSC2020: 46B20. https://arxiv.org/abs/2102.01219
2. Matthew Alexander, Matthieu Fradelizi, Luis C. García-Lirola, Artem Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642 (first public version 24 November 2019), especially Sections 1 and 5.2. https://arxiv.org/abs/1911.10642
3. Sofiya Ostrovska and Mikhail I. Ostrovskii, *Isometric structure of transportation cost spaces on finite metric spaces*, arXiv:2112.02689 (first public version 5 December 2021). https://arxiv.org/abs/2112.02689
