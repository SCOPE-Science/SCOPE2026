# A beta exponent law for Crofton-random affine sections of regular simplices

## Finding

For every integer \(n\ge4\), let \(S_n\) be a regular Euclidean simplex with \(n\) vertices and dimension \(n-1\). Choose an unoriented affine hyperplane according to Euclidean-motion-invariant measure on the affine span, conditioned on intersecting \(S_n\). This *Crofton-conditioned* law includes both a normal direction and a translation; it is not the Haar-uniform law of hyperplanes through the centroid. Let \(J_n\) count the vertices of \(S_n\) strictly on one arbitrarily designated side of the hyperplane, and let \(V_n\) count the vertices of its section.

For independent standard normal variables \(Z_1,\ldots,Z_n\), write \(Z_{(1)}<\cdots<Z_{(n)}\) for their order statistics and \(M_n=Z_{(n)}\). The complete finite-dimensional section law is
\[
\boxed{\Pr(J_n=k)=
\frac{\mathbb E[Z_{(k+1)}-Z_{(k)}]}{2\mathbb E M_n}
=\frac{\binom nk}{2\mathbb E M_n}
\int_{-\infty}^{\infty}\Phi(t)^k(1-\Phi(t))^{n-k}\,dt,\quad1\le k<n,}
\tag{1}
\]
where \(\Phi\) is the standard normal distribution function. The section is combinatorially equivalent to \(\Delta_{k-1}\times\Delta_{n-k-1}\) conditional on \(J_n=k\), so it has exactly
\[
\boxed{V_n=J_n(n-J_n)}
\tag{2}
\]
vertices. Thus (1) determines the entire distribution of the section's combinatorial type and vertex count (with the two orientations \(k,n-k\) identified for unoriented hyperplanes).

Define \(K_n=\min\{J_n,n-J_n\}\). For every fixed \(x\in(0,1)\), there is also the exact finite-\(n\) cumulative identity, valid whenever \(1\le\lfloor n^x\rfloor<n/2\):
\[
\boxed{\Pr\{K_n\le\lfloor n^x\rfloor\}
=1+\frac{\mathbb E Z_{(\lfloor n^x\rfloor+1)}}{\mathbb E M_n}.}
\tag{3}
\]
As \(n\to\infty\), the logarithmic section-complexity exponent has the nondegenerate limit
\[
\boxed{\frac{\log V_n}{\log n}-1\ \Longrightarrow\ B,
\qquad \Pr(B\le x)=1-\sqrt{1-x}\ \ (0\le x\le1).}
\tag{4}
\]
Equivalently, \(B\) has the \(\operatorname{Beta}(1,\tfrac12)\) law. In particular, for every \(0<x<1\),
\[
\lim_{n\to\infty}\Pr\{V_n\le n^{1+x}\}=1-\sqrt{1-x}.
\tag{5}
\]
This does **not** assert convergence of \(V_n/n^2\) to a positive constant; the typical polynomial growth exponent is itself random. The novelty assessed here is the all-dimensional Crofton section law together with (4), not the already-known probability for a regular tetrahedron or the classical Gaussian maximum asymptotics taken separately.

## Assumptions and scope

Use the standard realization \(S_n=\operatorname{conv}\{e_1,\ldots,e_n\}\) in the affine space \(A_n=\{z\in\mathbb R^n:\sum_i z_i=1\}\). Hyperplane normals belong to its parallel linear space \(L_n=\{u:\sum_i u_i=0\}\), and a hyperplane is \(H(u,t)=\{z\in A_n:\langle u,z\rangle=t\}\). The invariant measure is proportional to spherical normal measure \(d\sigma(u)\) times one-dimensional Lebesgue measure \(dt\), identifying \((u,t)\) with \((-u,-t)\). Conditioning on meeting \(S_n\) gives a finite probability measure. To discuss \(J_n\), orient the hyperplane by an independent fair choice of its normal sign. The distribution of \(V_n\) does not depend on that convention.

The exceptional configurations where a hyperplane contains any simplex vertex have zero measure. Every asserted section is therefore a generic, nonempty \((n-2)\)-polytope. No claim is made for a different sampling rule that first chooses the normal uniformly and *then* independently chooses a uniform offset within that normal's admissible interval; that rule lacks the required width bias.

## Proof

**1. Crossed edges and product type.** For a generic \(H(u,t)\), write \(a_i=\langle u,e_i\rangle=u_i\) and order the heights \(a_{(1)}<\cdots<a_{(n)}\). If \(a_{(k)}<t<a_{(k+1)}\), there are \(k\) vertices below and \(n-k\) above. Every pair of simplex vertices is joined by an edge. Precisely the \(k(n-k)\) opposite-side edges meet the hyperplane, and these intersections are precisely the section vertices: in barycentric coordinates, each is supported on exactly two positive entries, and at a generic section vertex the remaining \(n-2\) nonnegativity constraints are active. Different edges have distinct supports, so no crossings coincide.

To identify the whole face lattice, for below-side indices put \(p_i=(t-a_i)z_i\), and for above-side indices put \(q_j=(a_j-t)z_j\). The equation of the hyperplane becomes \(\sum_i p_i=\sum_j q_j=\lambda>0\). Divide both collections by \(\lambda\). They give two independent probability vectors, in simplices \(\Delta_{k-1}\) and \(\Delta_{n-k-1}\); the original barycentric normalization uniquely fixes \(\lambda\) as a positive continuous function of the pair. Coordinate zero sets correspond bijectively. Thus the section has the product face lattice and (2) follows.

**2. Exact Crofton weighting.** For fixed \(u\), the offsets meeting the simplex form exactly \((a_{(1)},a_{(n)})\). Under invariant affine-hyperplane measure, the mass of the subclass \(J_n=k\) is therefore proportional to the spherical average of the \(k\)-th consecutive projected-height gap; the total mass is proportional to the average projected range. Hence
\[
\Pr(J_n=k)=\frac{\mathbb E_{u}[a_{(k+1)}-a_{(k)}]}{\mathbb E_{u}[a_{(n)}-a_{(1)}]}.
\tag{6}
\]
The proportionality constants and the orientation factor cancel. This step is essential: taking a uniform offset *conditional on each normal* without a width bias would give a different law.

**3. Reduction to independent Gaussian spacings.** Let \(G_i=Z_i-\bar Z\), where \(\bar Z=n^{-1}\sum_iZ_i\). The Gaussian vector \(G\) is isotropic on \(L_n\), and its length \(R=\|G\|\) is independent of its direction \(U=G/R\), which is Haar-uniform. Since subtracting \(\bar Z\) does not alter consecutive differences or the range, and \(G_{(k+1)}-G_{(k)}=R(U_{(k+1)}-U_{(k)})\), taking expectations and cancelling \(\mathbb E R>0\) proves the first equality in (1), using \(\mathbb E[Z_{(n)}-Z_{(1)}]=2\mathbb E M_n\) by normal symmetry.

For fixed real \(t\), exactly \(k\) of the independent Gaussian values lie below \(t\) with probability \(\binom nk\Phi(t)^k(1-\Phi(t))^{n-k}\). For every sample with distinct values, the Lebesgue measure of the set of \(t\) with exactly \(k\) entries below it is \(Z_{(k+1)}-Z_{(k)}\). Tonelli's theorem yields the second equality in (1). Every integral is finite and strictly positive.

**4. An exact formula for the logarithmic splitting index.** For integers \(1\le k<n/2\), the events \(K_n\le k\) consist of gaps indexed \(1,\ldots,k\) and \(n-k,\ldots,n-1\). By symmetry, the two blocks have equal Crofton masses. Telescoping those gap lengths in (1) gives
\[
\Pr(K_n\le k)=\frac{2\mathbb E[Z_{(k+1)}-Z_{(1)}]}{2\mathbb E M_n}
=1+\frac{\mathbb E Z_{(k+1)}}{\mathbb E M_n}.
\tag{7}
\]
This is (3).

**5. Gaussian intermediate order statistics.** Fix \(x\in(0,1)\), let \(k_n=\lfloor n^x\rfloor+1\), and choose \(0<\delta<\min\{x,1-x\}\). The standard Gaussian tail estimates imply
\[
n\Phi\bigl(-\sqrt{2(1-x+\delta)\log n}\bigr)=n^{x-\delta+o(1)},\qquad
n\Phi\bigl(-\sqrt{2(1-x-\delta)\log n}\bigr)=n^{x+\delta+o(1)}.
\]
The number of observations below either threshold is binomial with these respective means. Markov's inequality at the more-negative threshold and a Chernoff lower-tail bound at the less-negative threshold show that \(Z_{(k_n)}/\sqrt{2\log n}\to-\sqrt{1-x}\) in probability. The analogous extreme-value estimate gives \(M_n/\sqrt{2\log n}\to1\) in probability. These statements also hold in \(L^1\): the normalized absolute order statistics are dominated by \(\max_i|Z_i|/\sqrt{2\log n}\), whose second moments are uniformly bounded by the elementary Gaussian union bound \(\Pr(\max_i|Z_i|>s)\le2n e^{-s^2/2}\). Consequently,
\[
\frac{\mathbb E Z_{(k_n)}}{\sqrt{2\log n}}\to-\sqrt{1-x},\qquad
\frac{\mathbb E M_n}{\sqrt{2\log n}}\to1.
\tag{8}
\]
Insert (8) into (7). The limiting CDF of \(\log K_n/\log n\) at every \(x\in(0,1)\) is exactly \(1-\sqrt{1-x}\). Because \(1\le K_n\le n/2\) and
\[
\log V_n=\log K_n+\log(n-K_n),\qquad
\log(n-K_n)=\log n+O(1)
\]
uniformly over the possible values of \(K_n\), (4) follows by the continuous mapping/Slutsky argument; (5) follows because the limiting law has no atoms. This completes the proof.

## Verification

The accompanying standalone `verify/check.py` (with dependencies in `verify/requirements.txt`) checks the section-edge combinatorics for all nontrivial vertex splits with \(4\le n\le10\); computes the Gaussian-spacing integrals by quadrature for \(n=4,5,8\); and simulates genuine Crofton affine hyperplanes via uniform spherical normals and independent offsets drawn from a global enclosing interval, conditioned on intersecting the simplex. The largest observed finite-dimensional frequency discrepancy was below \(0.003\) in the recorded run. It also computes a finite-size diagnostic for the logarithmic splitting-index law. The slow approach of the finite-size values toward (4) is expected from extreme-value logarithms. No finite computation substitutes for the all-\(n\) and \(n\to\infty\) arguments in the proof.

For \(n=4\), the quadrilateral-section probability from (1) is \(0.288535543072\ldots\), a known special case of the equifacial-tetrahedron section probability. That numerical special case is not proposed as new.

## Relationship to prior work

Baryshnikov and Vitale [1] derive an affine-equivalence relation between random projections of regular-simplex vertices and Gaussian samples. This is relevant to the Gaussian reduction, but projections are not affine hyperplane *sections*, and their reported theorem does not give Crofton width-biased order spacings or the beta exponent law. Their complete text could not be retrieved; only their abstract and a detailed mathematical review were inspected, leaving an explicit residual priority risk.

Dirksen [2], inspected in full in an accessible HTML representation, studies regular-simplex section **volumes** and extremizers. It neither provides a random section-type distribution nor an intermediate-order asymptotic. Kabluchko, Litvak and Zaporozhets [3], whose full accessible text was compared, develop mean widths of regular polytopes and extremes of Gaussian samples. Their Gaussian maximum controls the denominator in (1), but the interior gap distribution and logarithmic random section type are not their conclusions. De Loera, Lopez-Campos and Torres [4] address maximal vertex counts and attainable section counts for polytopes, without the invariant random-affine-plane probability law.

Published results on Haar-random **central** regular-simplex sections establish chi-square section-face fluctuations and related expected-face formulas [5]. They concern hyperplanes fixed through the centroid, a singularly different sampling scheme; neither their law nor their limiting chi-square distribution implies (1) or (4). The regular-tetrahedron \(n=4\) marginal was already covered by the known equifacial-tetrahedron Crofton calculation [6]. Its inclusion here is only a consistency check. The asserted contribution is the general Gaussian-spacing Crofton law and the beta limit for the section's polynomial complexity exponent.

## Limitations

This result applies to Euclidean-motion-invariant affine hyperplanes conditioned on intersection with a regular simplex. It does not describe volume-weighted sections, centroidal sections, or uniform-offset-given-direction sampling, and its asymptotic statement does not supply a convergence rate or a local limit approximation for individual splitting probabilities. The new finding has undergone only the review described in the accompanying files; no independent mathematical audit is represented. Historical priority remains uncertain where older complete sources are inaccessible.

## References

[1] Y. M. Baryshnikov and R. A. Vitale, *Regular simplices and Gaussian samples*, Discrete Comput. Geom. 11 (1994), 141–147. DOI: https://doi.org/10.1007/BF02574000 ; detailed zbMATH review: https://portal.mardi4nfdi.de/wiki/Item:Q1317873 .

[2] H. Dirksen, *Sections of the regular simplex — Volume formulas and estimates*, first posted September 21, 2015, arXiv:1509.06408. https://arxiv.org/abs/1509.06408 .

[3] Z. Kabluchko, A. E. Litvak and D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, first posted November 26, 2015, arXiv:1511.08479. https://arxiv.org/abs/1511.08479 .

[4] J. A. De Loera, G. Lopez-Campos and A. J. Torres, *On the Number of Vertices in a Hyperplane Section of a Polytope*, first posted December 17, 2024, arXiv:2412.12419. https://arxiv.org/abs/2412.12419 .

[5] *Joint chi-square face-vector fluctuations of random central regular-simplex sections*, public research note (2026), and *Exact mean and chi-square fluctuations of Haar central simplex-section vertex counts*, public research note (2026).

[6] *Sharp affine-plane section probability for every equifacial tetrahedron*, public research note (2026).
