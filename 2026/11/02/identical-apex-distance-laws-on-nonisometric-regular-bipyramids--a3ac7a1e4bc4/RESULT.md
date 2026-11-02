# Identical apex-distance laws on nonisometric regular bipyramids

## Finding

**Theorem.** Fix an integer \(n\ge3\), a slant edge length \(s>0\), and a face half-apex angle \(0<\beta<\pi/n\). Form the nondegenerate *symmetric regular \(n\)-gonal bipyramid* with a regular equatorial \(n\)-gon of side \(2s\sin\beta\) and two mirror-image apices, each at distance \(s\) from every equatorial vertex. Equip its complete boundary \(M_{n,s,\beta}\) with intrinsic path distance \(d\) and normalized surface area. Let \(N\) be the upper apex, and let \(X\) be area-uniform on the whole boundary.

Then \(D=d(N,X)\) has exactly the distribution of the Euclidean distance from the origin to a uniform point of the single planar rhombus
\[
Q_{s,\beta}=\operatorname{conv}\left\{(0,0),\ (s\cos\beta,s\sin\beta),\ (2s\cos\beta,0),\ (s\cos\beta,-s\sin\beta)\right\}.
\]
In particular its law depends only on \(s,\beta\), **not** on \(n\). For every integer \(K\ge3\), choosing \(0<\beta<\pi/K\) gives \(K-2\) pairwise nonisometric convex polyhedral surfaces \(M_{n,s,\beta}\), \(3\le n\le K\), with exactly the same apex-distance distribution. There are therefore arbitrarily large finite families of nonisometric pointed polyhedral surfaces indistinguishable by the entire normalized radial distance distribution.

Put \(q=\sin(2\beta)\), \(R_*=2s\cos\beta\), and \(F(r)=\mathbb P(D\le r)\). For \(0<r<R_*\), a complete exact one-variable formula is
\[
 F(r)=\frac{1}{s^2q}\int_0^\beta
 \min\left\{r^2,\frac{s^2q^2}{\sin^2(\beta+\theta)}\right\}\,d\theta,
\]
with \(F(r)=0\) for \(r\le0\) and \(F(r)=1\) for \(r\ge R_*\). The integral is elementary, as follows. Set
\[
 r_0=\begin{cases}s,&\beta\le\pi/4,\\sq,&\beta>\pi/4.\end{cases}
\qquad \alpha(r)=\arcsin(sq/r).
\]
For \(0\le r\le r_0\),
\[
 F(r)=\frac{\beta r^2}{s^2q}.
\]
If \(\beta>\pi/4\) and \(sq<r<s\),
\[
 F(r)=\frac{r^2(\beta-\pi+2\alpha(r))
   +2s^2q^2\cot\alpha(r)}{s^2q}.
\]
For \(s<r<R_*\), independently of which angular regime holds,
\[
 F(r)=\frac{r^2(\alpha(r)-\beta)
   +s^2q^2\bigl(\cot\alpha(r)-\cot(2\beta)\bigr)}{s^2q}.
\]
At the shared boundary values these expressions agree continuously. The support endpoint \(R_*\) is attained only at the opposite apex.

For every integer \(k\ge0\), all even moments are the finite exact sum
\[
\mathbb E[D^{2k}]=s^{2k}\sum_{i+j+\ell=k}
 \frac{k!\,(2\cos 2\beta)^\ell}{i!j!\ell!\,(2i+\ell+1)(2j+\ell+1)}.
\]
In particular,
\[
 \mathbb E[D^2]=s^2\left(\frac23+\frac12\cos2\beta\right),
 \qquad
 \mathbb E[D^4]=s^4\left(\frac{28}{45}+\cos2\beta
                      +\frac49\cos^2 2\beta\right).
\]

**Sharp wavefront transitions.** The first departure from the flat vertex-cone law \(\beta r^2/(s^2q)\) occurs at \(r=r_0\). For fixed \(\beta<\pi/4\), as \(r\downarrow s\) from above,
\[
 \frac{\beta r^2}{s^2q}-F(r)
 \sim\frac{(r-s)^2}{s^2\cos2\beta}.
\]
At \(\beta=\pi/4\), the corresponding difference is asymptotic to
\[
 \frac{4\sqrt2}{3}\left(\frac{r-s}{s}\right)^{3/2}.
\]
For \(\beta>\pi/4\), as \(r\downarrow sq\) from above, the difference is asymptotic to
\[
 \frac{8\sqrt2}{3\sqrt q}\left(\frac{r-sq}{s}\right)^{3/2}.
\]
Finally, for every admissible angle,
\[
1-F(r)\sim \frac{(R_*-r)^2}{2s^2\cos^2\beta}
\quad\text{as }r\uparrow R_*.
\]
All limits here are one-sided, with \(\beta,s\) held fixed. For \(\beta>\pi/4\) there is also a secondary wavefront regime change at \(r=s\); the exact piecewise formula above covers it.

## Assumptions and scope

This is the **intrinsic** (on-surface) geodesic distance, not ambient Euclidean chord distance and not graph distance along edges. Sampling uses the complete two-dimensional surface area (both pyramid halves), normalized to mass one. The equatorial polygon has circumradius \(s\sin\beta/\sin(\pi/n)\); the strict condition \(\beta<\pi/n\) makes the Euclidean height of each apex positive and the bipyramid convex and nondegenerate. For \(n\ge4\) necessarily \(\beta<\pi/4\); the two other first-contact regimes arise only for triangular bipyramids.

The main conclusion concerns *one fixed apex as source* and a uniform random target. It does not assert equality of pairwise-distance distributions between two uniform random surface points, equality of total surface areas, or metric-measure isomorphism. The number of conical singular vertices is \(n+2\), which distinguishes the surfaces with different \(n\).

## Proof

**1. Rhombus partition.** Let \(E_0,\ldots,E_{n-1}\) be the cyclic equatorial vertices and \(S\) the opposite apex. For every equatorial side \(E_jE_{j+1}\), take the two triangular faces \(NE_jE_{j+1}\) and \(SE_jE_{j+1}\), joined along that side. Develop the pair isometrically into the plane. Both faces are congruent isosceles triangles with side lengths \(s,s,2s\sin\beta\) and altitude \(s\cos\beta\). Their development is exactly \(Q_{s,\beta}\), with \(N\) mapped to its origin and \(S\) to the opposite vertex. These \(n\) rhombi partition the surface up to a finite collection of zero-area seams.

**2. Exact global shortest paths, not merely candidate paths.** On each developed rhombus define \(f(P)\) to be the planar distance from its origin. This definition is consistent on the common upper seams \(NE_j\), where both values equal the arclength from \(N\). It is also consistent on the common lower seams \(SE_j\): on either incident rhombus the value at the point \(P=E_j+t(S-E_j)\), \(0\le t\le1\), is
\[
 f(P)^2=s^2\bigl(\cos^2\beta(1+t)^2
                         +\sin^2\beta(1-t)^2\bigr),
\]
which does not depend on the choice of rhombus. Hence \(f\) is globally continuous. It has Euclidean gradient of norm one on each planar face away from the origin. Subdividing any polygonal surface path at face crossings gives \(|f(P)-f(Q)|\le\operatorname{length}(\gamma)\), and approximation gives the same bound for any rectifiable surface path. Thus \(d(N,P)\ge f(P)\), since \(f(N)=0\).

Every rhombus is convex. The straight segment from its developed origin to the developed \(P\) lies inside that rhombus and pulls back to a surface path of length exactly \(f(P)\). Therefore \(d(N,P)\le f(P)\), establishing the exact equality \(d(N,P)=f(P)\) at every surface point, including seams.

**3. Distribution and its invariance.** Each developed rhombus has area \(s^2\sin2\beta\). The entire boundary has \(n\) times this area. Uniform area therefore selects each congruent rhombus with probability \(1/n\), and conditional on that rhombus the developed target is uniform. The distribution of \(D=f(X)\) consequently equals the single-rhombus radial law. The dependence on \(n\) cancels exactly, proving the asserted non-identifiability. Different \(n\) give different numbers \(n+2\) of positive-curvature conical vertices, so the surfaces are pairwise nonisometric.

**4. Distribution formulas.** Use polar coordinates about the rhombus origin. At polar angle \(\theta\in[0,\beta]\), the far rhombus boundary is the line joining \((s\cos\beta,s\sin\beta)\) to \((2s\cos\beta,0)\), so its radial coordinate is
\[
 \rho(\theta)=\frac{s\sin2\beta}{\sin(\beta+\theta)}.
\]
The other half is its reflection. Integrating radial area \(\tfrac12\min(r^2,\rho^2)\) over both halves yields the stated exact integral. The clipping set is determined by \(\sin(\beta+\theta)>sq/r\). If \(\beta\le\pi/4\), clipping starts at the angular endpoint \(\theta=\beta\), when \(r=s\). If \(\beta>\pi/4\), it starts at the interior normal direction \(\theta=\pi/2-\beta\), when \(r=sq\), and reaches the endpoint at \(r=s\). Writing \(\alpha=\arcsin(sq/r)\), the clipped angular intervals are respectively \([\alpha-\beta,\beta]\) and, for the intermediate obtuse-angle regime, \([\alpha-\beta,\pi-\alpha-\beta]\). Integration uses \(\int\csc^2 u\,du=-\cot u\) and gives every displayed closed form. The maximum radius among the vertices of the convex rhombus is \(2s\cos\beta>s\), since \(\beta<\pi/3\).

**5. Moments and sharp endpoints.** Map independent \(U,V\sim\operatorname{Unif}[0,1]\) to the rhombus by
\[
 (x,y)=s\bigl(\cos\beta(U+V),\sin\beta(U-V)\bigr).
\]
The affine map has constant Jacobian, so the image is uniform and
\[
 D^2=s^2(U^2+V^2+2UV\cos2\beta).
\]
Multinomial expansion and \(\mathbb E[U^j]=1/(j+1)\) give the stated finite formula for every even moment.

For \(\beta<\pi/4\), the radial boundary meets the first-contact ray transversely, so the lost area is a triangle to leading order, of area \((r-s)^2/\cot2\beta\). For \(\beta=\pi/4\), it meets tangentially at an angular endpoint; expanding \(\sin(\pi/2-u)^{-1}=1+u^2/2+O(u^4)\) and integrating over a one-sided interval of angular width \(\sqrt{2(r-s)/s}\) gives the \(3/2\) coefficient above. When \(\beta>\pi/4\), the same tangency occurs at an interior angle and contributes twice that one-sided leading integral, with threshold \(sq\). Finally \(\rho(0)=2s\cos\beta\) and \(\rho'(0)=-2s\cos^2\beta/\sin\beta\); expansion of the small remaining angular cap gives the asserted quadratic upper-tail coefficient. These derivations use fixed positive \(s\) and strict admissibility \(\beta<\pi/n\).

## Verification

The standalone file `verify.py` implements the elementary closed CDF, independently integrates the radial-area formula, simulates uniform rhombus points, compares the exact second and fourth moments, and checks asymptotic coefficients at three angle regimes using arbitrary precision. Deterministic runs covered admissible side counts \(n=3,4,5,7,15\). The largest CDF discrepancy against independent quadrature was \(4.91\times10^{-12}\); the largest simulation-to-CDF absolute discrepancy among the sampled thresholds was \(0.00303\). The largest empirical relative discrepancy for the second and fourth moments was below \(0.006\). These numerical checks are corroboration, not a proof of the continuum results.

A separate direct proof of shortest-path optimality appears in Step 2 and does not rely on enumeration, simulation, or a numerical optimizer.

## Relationship to prior work

Source unfolding and cut-locus theory for convex polyhedral boundaries are developed in Aronov and O'Rourke (1992) and in Miller and Pak (first public arXiv version 2003-12-12). Those works provide general structural tools, not the parameterized normalized apex-distance law or the cross-side-count equality established here. O'Rourke and Vîlcu (first public arXiv version 2023) explicitly discuss skeletal cut loci on regular octahedra and dipyramids, so skeletal cut-locus geometry alone is **not asserted to be new**. Their partially accessible text does not state the full normalized law or its phase changes, but historical priority remains uncertain because the full relevant text could not be inspected. Dantsin and Wolpert (2020) study radial-distance comparisons for rooted metric-measure spaces; the present family is an explicit geometric non-identifiability construction in that broader setting, not a refutation of their results.

## Limitations

This is a claim about the full **single-source** radial distribution, not the joint distances of multiple random points. The construction needs congruent upper and lower pyramids and regular equatorial geometry; no analogous invariance is claimed for asymmetric bipyramids. Historical priority has not been independently certified. The relevant 2023 skeletal-cut-locus preprint was accessible only as abstracts and selected indexed excerpts during source comparison, leaving a specific residual risk; no conclusion about every result in that unavailable complete text is asserted. The classification is restricted to the exact nondegenerate parameter range; the flat limiting case \(\beta=\pi/n\) is excluded.

## References

1. Boris Aronov and Joseph O'Rourke, *Nonoverlap of the star unfolding*, Discrete & Computational Geometry **8** (1992), 219–250, DOI: 10.1007/BF02293047. Abstract and introductory material compared.
2. Ezra Miller and Igor Pak, *Metric combinatorics of convex polyhedra: cut loci and nonoverlapping unfoldings*, arXiv:math/0312253v1, first posted **2003-12-12**; sections on geodesics, source unfolding, and Theorem 3.5 compared. https://arxiv.org/abs/math/0312253
3. Evgeny Dantsin and Alexander Wolpert, *Similarity Between Points in Metric Measure Spaces*, arXiv:2011.00616v1, **2020-11-01**. Introduction and radial-distribution method compared. https://arxiv.org/abs/2011.00616
4. Joseph O'Rourke and Costin Vîlcu, *Skeletal Cut Loci on Convex Polyhedra*, arXiv:2312.01534v1, **2023-12-03**. Accessible abstract and indexed passages on the octahedron and suitable dipyramids compared; complete text not obtained. https://arxiv.org/abs/2312.01534
