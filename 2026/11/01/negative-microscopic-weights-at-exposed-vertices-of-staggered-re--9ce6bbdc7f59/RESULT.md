# Negative microscopic weights at exposed vertices of staggered regular polygons

## Finding

For each integer \(n\ge4\), let \(X_{n,r}\subset\mathbb R^2\) comprise the two concentric, staggered regular \(n\)-gons
\[
A_j=r(\cos(2\pi j/n),\sin(2\pi j/n)),\qquad B_j=(\cos((2j+1)\pi/n),\sin((2j+1)\pi/n)),
\quad j=0,\ldots,n-1,
\]
where \(0<r\le1\). Set
\[
S_n=2\cot\frac{\pi}{2n},\qquad
C_n(r)=\sum_{j=0}^{n-1}\sqrt{1+r^2-2r\cos((2j+1)\pi/n)},\qquad
\Delta_n(r)=(1+r)S_n-2C_n(r).
\]
The microscopic weighting assigns the same mass to each vertex in either orbit, namely
\[
\boxed{u_n(r)=\frac{S_n-C_n(r)}{n\Delta_n(r)},\qquad
v_n(r)=\frac{rS_n-C_n(r)}{n\Delta_n(r)}}.
\]
For all \(0<r\le1\), \(\Delta_n(r)<0\) and \(v_n(r)>0\). There is exactly one \(r_n\in(\cos(\pi/n),1)\) such that \(C_n(r_n)=S_n\), and
\[
u_n(r)<0\quad (0<r<r_n),\qquad
u_n(r_n)=0,\qquad
u_n(r)>0\quad (r_n<r\le1).
\]
For \(\cos(\pi/n)<r<r_n\), **all** \(2n\) points are exposed vertices of their convex hull, yet every \(A_j\) has a negative microscopic mass. The negative-mass interval within convex position has the sharp asymptotics
\[
\boxed{r_n=1-\frac{\pi^2}{4n^2}+O\!\left(\frac{\log n}{n^4}\right),\qquad
r_n-\cos\frac{\pi}{n}=\frac{\pi^2}{4n^2}+O\!\left(\frac{\log n}{n^4}\right).}
\]
For example, \(n=4\) and \(r=3/4\) produce eight exposed vertices with four negative microscopic masses; here \(r_4\approx0.834207951426\).

## Assumptions and scope

All distances are ordinary Euclidean chord distances. All points are distinct because \(r>0\). For any such finite metric space \(X=\{p_1,\ldots,p_m\}\), write \(D_{ij}=\|p_i-p_j\|_2\) and \(Z_s=(e^{-sD_{ij}})\), \(s>0\). Its magnitude weighting is \(w(s)=Z_s^{-1}{\bf1}\). The **microscopic weighting** is \(\lim_{s\downarrow0}w(s)/(\sum_iw_i(s))\), whenever the limit exists. Thus the mass is normalized to one, not to \(m\). For the configurations above it exists uniquely; the weights are signed, and no positivity is assumed. The term “exposed vertex” means that a linear functional has that point as its unique maximizer on the finite set.

## Proof

**1. Existence and uniqueness of the microscopic weighting.** Euclidean distance has strict negative type on distinct points. One direct proof uses
\[
\|x-y\|_2=\frac{1}{2\sqrt\pi}\int_0^\infty
\left(1-e^{-t\|x-y\|_2^2}\right)t^{-3/2}\,dt.
\]
For any nonzero \(z\in\mathbb R^m\) with \(\sum_i z_i=0\), this yields
\[
z^TDz=-\frac{1}{2\sqrt\pi}\int_0^\infty
z^T(e^{-t\|p_i-p_j\|_2^2})_{ij}z\,t^{-3/2}\,dt<0,
\]
because each Gaussian Gram matrix is strictly positive definite for distinct points (by its positive Fourier density). In particular, the energy \(q\mapsto q^TDq\) has a unique maximizer on the affine hyperplane \(\sum_iq_i=1\), characterized by \(Dq=\lambda{\bf1}\). To connect this maximizer to the microscopic limit, let \(P\) denote the orthogonal projection onto \(\{z:\sum_i z_i=0\}\). The expansion \(Z_s={\bf1}{\bf1}^T-sD+O(s^2)\) shows that the projected equation \(PZ_sq=0\) on \(\sum_iq_i=1\), after division by \(s\), has a uniquely solvable limit \(PDq=0\): its derivative on the zero-sum hyperplane is invertible by strict negative type. Hence for small positive \(s\) a unique normalized vector \(q_s\) depends continuously on \(s\) and tends to the energy maximizer. The scalar \(\lambda_s\) defined by \(Z_sq_s=\lambda_s{\bf1}\) tends to one; therefore the original weighting equals \(q_s/\lambda_s\), and its normalized limit is \(q_0\).

**2. Two-orbit reduction.** Invariance under rotation through \(2\pi/n\), combined with uniqueness, makes the weights constant on the two vertex orbits; denote them \(u,v\). The sum of distances from any point to the other vertices of its own regular \(n\)-gon is \(2R\cot(\pi/(2n))\) for radius \(R\), while the sum of its distances to the opposite ring is \(C_n(r)\). The energy stationarity conditions and total mass are
\[
rS_nu+C_n(r)v=C_n(r)u+S_nv,\qquad n(u+v)=1.
\]
They yield the displayed expressions. Strict negative type applied to the zero-sum vector with entries \(+1/n\) on the inner ring and \(-1/n\) on the outer ring gives \(\Delta_n(r)<0\).

**3. Signs and the unique threshold.** Differentiating each cross-chord length gives
\[
C_n'(0)=-\sum_{j=0}^{n-1}\cos((2j+1)\pi/n)=0,
\quad C_n''(r)=\sum_{j=0}^{n-1}
\frac{\sin^2((2j+1)\pi/n)}{[1+r^2-2r\cos((2j+1)\pi/n)]^{3/2}}>0.
\]
Consequently \(C_n\) is strictly increasing for \(r>0\). The endpoint identities are
\[
C_n(0)=n<S_n,\qquad C_n(1)=2\csc\frac{\pi}{2n}>S_n,
\quad C_n'(1)=\csc\frac{\pi}{2n}.
\]
The first strict inequality follows from \(\sin x\le x\), \(\cos x\ge\sqrt3/2\) on \(0\le x\le\pi/6\): for \(n\ge3\), \(S_n\ge(2\sqrt3/\pi)n>n\). This proves a unique root in \((0,1)\). Moreover \(C_n(r)=rC_n(1/r)\) and strict increase imply \(C_n(r)>rS_n\) on \((0,1]\); since \(\Delta_n(r)<0\), the outer weight \(v\) is positive. The inner sign follows from the strict increase of \(C_n\).

**4. Every negative-weight point can nevertheless be exposed.** Put \(r_0=\cos(\pi/n)\). The point \(A_j\) at this radius is the midpoint of the edge joining the adjacent outer vertices \(B_{j-1},B_j\). For every outer-ring vertex \(B_k\), the triangle inequality gives
\[
\|A_j-B_k\|_2\le\frac12(\|B_{j-1}-B_k\|_2+\|B_j-B_k\|_2).
\]
At least one inequality is strict, and summing over \(k\) gives \(C_n(r_0)<S_n\). Hence \(r_n>r_0\). Whenever \(r>r_0\), the radial direction through each \(A_j\) uniquely exposes \(A_j\): its radial support value \(r\) exceeds the support values of every outer vertex (at most \(r_0\)) and every other inner vertex. Similarly, the radial direction through each \(B_j\) uniquely exposes \(B_j\), because \(1>r\cos(\pi/n)\). Thus all \(2n\) points are exposed simultaneously for \(r_0<r\le1\), including the negative-weight interval \((r_0,r_n)\).

**5. Sharp asymptotics.** Put \(\epsilon=\pi/(2n)\). The exact endpoint identities give
\[
\frac{C_n(1)-S_n}{C_n'(1)}=2(1-\cos\epsilon)
=\frac{\pi^2}{4n^2}+O(n^{-4}).
\]
Uniformly for \(1/2\le r\le1\), the second-derivative formula yields
\[
0\le C_n''(r)\le K\sum_{j=0}^{n-1}
\frac{1}{|\sin((2j+1)\pi/(2n))|}=O(n\log n)
\]
for an absolute constant \(K\). Taylor's theorem at one now shows \(C_n(1-4/n^2)<S_n\) for sufficiently large \(n\), because the linear decrement is asymptotic to \(8/(\pi n)\), exceeding the endpoint excess \(\pi/(2n)\), while the remainder is \(O((\log n)/n^3)\). Therefore \(1-r_n=O(n^{-2})\). A second Taylor expansion at \(r_n\), divided by \(C_n'(1)\asymp n\), gives
\[
1-r_n=2(1-\cos\epsilon)+O((\log n)/n^4).
\]
Subtracting the elementary expansion of \(\cos(\pi/n)\) gives the claimed convex-position interval width. All limits are along integers \(n\to\infty\).

## Verification

The self-contained source file `verify.py` uses Python 3 with NumPy, SciPy, and mpmath; run `python verify.py`. It performs 275 checks spanning Euclidean row sums, the exact two-orbit formulas, independent full distance-matrix solves, direct small-scale zeta-matrix limits, convex-hull vertex counts, threshold signs, high-precision root calculations, and the asymptotic scale. It reports \(r_4=0.834207951426\) and \(\lim_{n\to\infty}n^2(1-r_n)=\pi^2/4\). These finite checks corroborate but do not establish the universal theorem; all universal steps are proved above.

## Relationship to prior work

Roff and Willerton introduced microscopic weighting, its strict-negative-type existence criterion, and the distance-energy interpretation [1]. Those general principles are credited; the result here concerns the new exact staggered Euclidean \(2n\)-gon formulas, the negative-mass transition **while every point remains exposed**, and its sharp asymptotic window. Their full preprint was not available for line-by-line comparison; this leaves a historical-priority risk that cannot be ruled out from its abstract. Kamiyama's full accessible text [2, Definition 2.6] studies cyclic two-chunk metrics with **one common nonzero distance within each chunk**. For \(n\ge4\), a Euclidean regular \(n\)-gon has at least two distinct nonzero within-chunk chord distances, so the construction here is not a special case of that prescribed metric family. The exceptional triangular analogue is not claimed as new. Roff and Yoshinaga [3] investigate magnitude's small-scale one-point property, rather than the present signed probability on exposed vertices.

## Limitations

The construction is planar and uses exactly two staggered regular orbits. It does not classify signs for arbitrary finite Euclidean point sets, all cyclic configurations, or higher-dimensional polytopes. The asymptotic error term is not asserted sharp beyond the stated order. Numerical checks are finite. Historical priority is provisional because [1] was available only as an abstract; independent validation has not been performed.

## References

[1] E. Roff and S. Willerton, *The microscopic weighting on a metric space*, arXiv:2607.05349, first posted July 6, 2026. https://arxiv.org/abs/2607.05349

[2] T. Kamiyama, *Small-Scale Magnitude Below One for Cyclic Two-Chunk Finite Metric Spaces*, arXiv:2606.00707, first posted May 30, 2026, especially Definition 2.6. https://arxiv.org/abs/2606.00707

[3] E. Roff and M. Yoshinaga, *The small-scale limit of magnitude and the one-point property*, Bulletin of the London Mathematical Society 57 (2025), 1841–1855. https://doi.org/10.1112/blms.70064
