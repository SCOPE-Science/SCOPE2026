# Cubic clipping threshold and angular rigidity for random distances in spatial parallelotopes

## Finding

Let \(A\in\mathbb R^{3\times3}\) be invertible, let \(K=x_0+A[0,1]^3\) have volume \(V=|\det A|\), and let \(X,Y\) be independent uniform points of \(K\). Put \(B=A^{-1}\), denote its row vectors by \(b_1,b_2,b_3\), and set
\[
s_i=\|b_i\|_2,\quad \gamma_{ij}=\frac{b_i\cdot b_j}{s_is_j},\quad r_0=\frac1{\max_i s_i},\quad D(r)=\Pr(\|X-Y\|_2\le r).
\]
Define
\[
f(t)=\sqrt{1-t^2}+t\arcsin t\quad(-1\le t\le1),\qquad C_5=\frac8{15}\sum_{i<j}s_is_jf(\gamma_{ij}),
\]
and the strictly positive integral
\[
H_6=\int_{\|z\|_2\le1}|b_1\cdot z|\,|b_2\cdot z|\,|b_3\cdot z|\,dz.
\]
Then for **every** \(0\le r\le r_0\), the *exact* random-pair distance law is the degree-six polynomial
\[
\boxed{VD(r)=P(r):=\frac{4\pi}3r^3-\frac\pi2\Big(\sum_{i=1}^3s_i\Big)r^4+C_5r^5-H_6r^6.}
\]
At fixed face-to-face altitudes \(1/s_i\), put \(C_{5,\mathrm{rect}}=\frac8{15}\sum_{i<j}s_is_j\) and \(\Delta=\sum_{i<j}s_is_j\gamma_{ij}^2\). There are **globally sharp** angular-stability bounds
\[
\boxed{\frac4{15}\Delta\ \le\ C_5-C_{5,\mathrm{rect}}\ \le\ \frac8{15}\Big(\frac\pi2-1\Big)\Delta.}
\]
The difference vanishes exactly for rectangular boxes. Both constants are optimal for nonsingular parallelotopes; the lower constant is approached by almost orthogonal face normals and the upper constant by almost parallel face normals.

The short-distance polynomial ceases to be valid at exactly \(r_0\). To quantify its first departure, let \(s_* = \max_i s_i\), \(I=\{i:s_i=s_*\}\), and
\[
Q_i=\prod_{j\ne i}\left(1-\frac{|b_j\cdot b_i|}{s_i^2}\right)>0 \qquad (i\in I).
\]
As \(r\downarrow r_0\) **from above**,
\[
\boxed{VD(r)-P(r)=\frac{2\pi}3\Big(\sum_{i\in I}Q_i\Big)(r-r_0)^3+o((r-r_0)^3).}
\]
In particular, \(r_0\) is the precise positive endpoint of the initial polynomial branch. This last statement is local to the first threshold; no formula for all larger distances is asserted.

## Assumptions and scope

The matrix is any invertible real \(3\times3\) matrix (orientation arbitrary), \(K\) may be translated, all three row norms are strictly positive, and \(|\gamma_{ij}|<1\) for distinct indices by linear independence. The metric is ordinary **Euclidean distance**, not the parallelotope's affine gauge. Probability is with respect to independent normalized three-dimensional Lebesgue measure on \(K\), including its interior; the boundary has measure zero. The parameters \(1/s_i\) are the Euclidean distances between opposite supporting face planes in each of the three pairs. The radial variable \(r\) has the same length units as \(K\).

The polynomial \(P(r)\) is the particular algebraic expression displayed above, formally extended to values exceeding \(r_0\). The one-sided expansion is a comparison of the *true probability law* with this fixed continuation; it is not an extrapolation assumption. The integral defining \(H_6\) is part of the exact answer and may be numerically evaluated; no elementary closed formula for it is asserted.

## Proof

**1. Covariogram normalization and the exact short-distance branch.** For a translation \(z\), apply the inverse affine map to both copies of \(K\). The intersection is a Cartesian product of three intervals whose normalized overlap lengths are \((1-|b_i\cdot z|)_+\). Consequently the exact covariogram is
\[
\operatorname{vol}_3(K\cap(K+z))=V\prod_{i=1}^3(1-|b_i\cdot z|)_+.
\]
Convolution of the two independent uniform densities gives, for all \(r\ge0\),
\[
VD(r)=\int_{\|z\|_2\le r}\prod_{i=1}^3(1-|b_i\cdot z|)_+\,dz.
\]
If \(r\le r_0\) then \(|b_i\cdot z|\le s_i r\le1\) for every integration point, so all positive parts may be removed exactly. Expand the three factors as a polynomial in the absolute linear forms, and rescale \(z=ru\). The constant term integrates to \(4\pi r^3/3\). Rotational symmetry gives
\[
\int_{\|u\|_2\le1}|b_i\cdot u|\,du=\frac\pi2s_i.
\]

**2. The nonorthogonal pair integral.** For two nonzero vectors \(v,w\), let \(\rho=(v\cdot w)/(\|v\|_2\|w\|_2)\). If \(G\) is standard Gaussian in \(\mathbb R^3\) and \(U=G/\|G\|_2\) is uniform on the sphere independently of \(\|G\|_2\), then \(\mathbb E\|G\|_2^2=3\). A centered unit-variance bivariate normal pair with correlation \(\rho\) obeys
\[
\mathbb E|G_1G_2|=\frac2\pi\big(\sqrt{1-\rho^2}+\rho\arcsin\rho\big).
\]
For completeness, differentiation of the Gaussian density with respect to \(\rho\) and integration by parts gives the derivative \(\mathbb E[\operatorname{sgn}G_1\operatorname{sgn}G_2]=2\arcsin\rho/\pi\). The value at \(\rho=0\) is \(2/\pi\), so integration in \(\rho\) gives the displayed identity. Radial integration of a homogeneous degree-two integrand over the unit ball contributes \(1/5\) times its spherical integral. Combining these facts gives
\[
\int_{\|u\|_2\le1}|v\cdot u|\,|w\cdot u|\,du
=\frac8{15}\|v\|_2\|w\|_2 f(\rho).
\]
The cubic product of the three absolute forms integrates to the positive number \(H_6\). Substitution proves the exact displayed degree-six expression over the whole interval \([0,r_0]\).

**3. Globally sharp angular rigidity.** The function \(f\) is even, \(f(0)=1\), and \(f''(t)=(1-t^2)^{-1/2}\) for \(|t|<1\). Twice integrating from zero gives
\[
\frac{f(t)-1}{t^2}=\int_0^1\frac{1-u}{\sqrt{1-t^2u^2}}\,du,\qquad 0<|t|<1.
\]
The right side is strictly increasing in \(|t|\), with endpoint values \(1/2\) and \(\pi/2-1\). Multiply the resulting two-sided quadratic inequality by \(\frac8{15}s_is_j\) and sum over the three unordered pairs. This proves both stability bounds. The deficit vanishes only when all pairwise cosines vanish, precisely the rectangular-box case. For the sharp lower constant, choose row vectors with prescribed lengths and correlations tending to zero, but not all zero. For the sharp upper constant choose three linearly independent unit directions that tend to a common line, multiplied by any prescribed lengths \(s_i\). Their pairwise correlations tend in absolute value to one, giving the upper constant as a strict, nonsingular limiting supremum. Thus neither bound's coefficient can be improved, even when all three face separations are prescribed.

**4. Exact first clipping scale and positive cubic correction.** Write \(\delta=r-r_0>0\). Subtract the untruncated integrand that defines \(P(r)\) from the true integrand. For sufficiently small \(\delta\), the only points in \(\|z\|_2\le r\) where any factor \(1-|b_i\cdot z|\) becomes negative belong to small spherical caps around the two points \(\pm r_0 b_i/s_i\) with \(i\in I\). They are disjoint for distinct \(i\), because the row vectors are pairwise nonparallel. For \(j\ne i\), at either cap tip the unaffected factor is
\[
1-\frac{|b_j\cdot b_i|}{s_i^2}>0.
\]
Strict positivity follows from \(s_j\le s_i\) and the strict Cauchy–Schwarz inequality for distinct independent rows. The product of the unaffected factors converges **uniformly throughout each shrinking cap** to \(Q_i\). On the cap \(b_i\cdot z>s_i r_0=1\), put \(t=z\cdot b_i/s_i\). The excess replacing the negative factor by zero equals \(s_i(t-r_0)\) times the unaffected product. The cross section of the ball at signed coordinate \(t\) has Euclidean area \(\pi(r^2-t^2)\). Therefore the contribution of one cap is
\[
Q_i s_i\int_{r_0}^{r_0+\delta}(t-r_0)\pi\big((r_0+\delta)^2-t^2\big)\,dt+o(\delta^3)
=\frac\pi3 Q_i\delta^3+o(\delta^3),
\]
using \(s_i r_0=1\). There are two opposite caps per active index. Summation gives the positive claimed coefficient and proves the exact first-polynomial cutoff. The remainder is one-sided as stated.

## Verification

The standalone standard-library script `checker.py` reconstructs \(s_i\), pairwise angles, the \(C_5\) coefficient, the sharp quadratic angular bounds, and the first-cutoff coefficient for four independent full-rank examples. A separate spherical cubature numerically checks the integrated fourth-, fifth-, and sixth-degree terms, and independent disk-slice integration checks the cubic clipping coefficient for small positive \(\delta\). Run `python3 checker.py` beside this file. The expected terminal marker is `PROFILE_AND_CUBIC_ONSET_CHECK_OK 4 profiles`.

The script is a **finite numerical consistency check**, not a proof of the universal assertions. The universal assertions follow from Steps 1–4. The special unit cube has \(r_0=1\), \(C_5=8/5\), \(H_6=1/6\), and clipping coefficient \(2\pi\), which are also used as independent normalization checks. No source-specific numerical table is required for the proof.

## Relationship to prior work

Wang (2026, first posted 2026-10-01) develops general Brunn–Minkowski phenomena for random-pair distances in convex bodies and their covariograms; the inspected accessible primary paper gives general relations and leading boundary corrections but not the present complete angularly resolved short-distance polynomial for arbitrary skew spatial parallelotopes or its explicit positive cubic cutoff term. Ohanyan and Adamyan (2019) study a **right parallelepiped with square base**; Ohanyan and Khalatyan (2022) relate covariograms and distance distributions, giving explicit examples for a disk, ball and triangle. Those general identities and special cases are prior art. Published computations of the regular cube's pair-distance law and a previous all-dimensional orthotope short-distance polynomial already contain the perpendicular-normal special case; neither special case is claimed as new.

The mathematical increment is the explicit dependence on three arbitrary, nonorthogonal face-normal angles, a sharp *two-sided quadratic stability law* at fixed altitudes, and a formula for the first nonanalytic clipping amplitude at the exact least-altitude threshold. This includes a comparison to wider covariogram identities rather than merely to matching titles or dimension parameters.

## Limitations

The result is specific to **three-dimensional parallelotopes** and independent volume-uniform sampling with the Euclidean metric. The sixth-degree coefficient is given as a convergent intrinsic integral, not a claimed elementary closed form. The correction at \(r_0\) is an asymptotic law, not a complete distance distribution for larger \(r\), and does not assert a global shape optimizer for the distance law. The upper angular-stability constant is approached in a degenerating geometry, not attained by any nonrectangular nonsingular parallelotope. Older unindexed exact calculations for skew parallelotopes could affect historical priority; independent literature review has not been performed.

## References

1. S. Wang, *A Brunn–Minkowski Theory for the Distribution of Random Pairs of Points in Convex Bodies*, arXiv:2610.01916, first posted 2026-10-01, https://arxiv.org/abs/2610.01916.
2. V. K. Ohanyan and G. L. Adamyan, *Covariogram of a Right Parallelepiped*, Proceedings of the Yerevan State University A, 2019, DOI:10.46991/PYSU:A/2019.53.2.101.
3. V. K. Ohanyan and V. H. Khalatyan, *Relation between the Covariogram and Distribution Function of the Distance Between Two Uniform and Independent Points*, Proceedings of the Yerevan State University A 56 (2022), 33–42, DOI:10.46991/PYSU:A/2022.56.1.033.
4. A. M. Mathai, P. G. Moschopoulos and A. Pederzoli, *Distance between random points in a cube*, Statistica 59 (1999) (historical cube special case; complete primary text not inspected).
