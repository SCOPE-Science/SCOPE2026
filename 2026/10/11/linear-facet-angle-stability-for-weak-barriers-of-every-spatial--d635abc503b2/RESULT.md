# Linear facet-angle stability for weak barriers of every spatial convex polytope

## Finding
Let \(K\subset\mathbb R^3\) be a full-dimensional convex polytope. Choose one unit vector \(v_i\) on each of its \(m\) distinct unoriented facet-normal lines. Put
\[
\Delta=\min_{i\ne j}\arccos|\langle v_i,v_j\rangle|>0,\qquad
\rho(u)^2=\min_{1\le i\le m}\bigl(1-\langle u,v_i\rangle^2\bigr).
\]
Define the explicit positive constants
\[
L_0=2\pi,\quad L_k=\frac{4\pi(2k-2)!}{4^k(k-1)!(k+1)!}\ (k\ge1),\quad
H_m=\sum_{k=0}^m\frac{4k+1}{L_k},\quad
\varepsilon_m=\frac{1}{4\pi(1+H_m)}.
\]
For every two-dimensional rectifiable weak barrier \(B\) for \(K\), with normal-orientation measure \(\mu=S^*(B,\cdot)\) and Jones deficit \(\delta=S(B)-S(\partial K)/2\),
\[
\boxed{\int_{S^2}\rho(u)^2\,d\mu(u)\ \le\
\frac{2\delta}{\varepsilon_m\sin^{2m-2}(\Delta/2)}.}
\]
In particular, for every \(0<\beta\le\pi/2\) and
\(J_\beta=\{u\in S^2:\arccos\max_i|\langle u,v_i\rangle|>\beta\}\),
\[
\boxed{\mu(J_\beta)\le\frac{2\delta}{\varepsilon_m\sin^{2m-2}(\Delta/2)\sin^2\beta}.}
\]
The exponent \(2\) of the small-angle denominator is optimal for the class of rectifiable *weak* barriers, for every fixed polytope \(K\).

## Assumptions and scope
Here \(S(B)=\mathcal H^2(B)\); rectifiability allows almost-everywhere unit normals \(n_B\), and
\[
S^*(B,E)=\int_B\bigl(\mathbf1_E(n_B(x))+\mathbf1_E(-n_B(x))\bigr)\,d\mathcal H^2(x).
\]
Thus \(\mu(S^2)=2S(B)\). A weak barrier means that the **total orthogonal projected area with multiplicity** of \(B\), in each direction, is at least the area of the corresponding projection of \(K\). Every rectifiable opaque barrier satisfies this weaker requirement, but the converse need not hold. The theorem asserts no existence of barriers approaching Jones' bound and no estimate on physical positions of barrier pieces. Repeated opposite facet normals are represented once as an unoriented line. Distinct such lines ensure \(\Delta>0\).

## Proof
**1. Projection domination.** Write \(\nu=\tfrac12(S_K+S_{-K})\), the even surface-area measure of \(K\)'s Blaschke symmetral. Its total mass is \(\nu(S^2)=S(\partial K)\), and its support is contained in \(\{\pm v_i\}\). Cauchy's projection formula and the weak-barrier condition give, for every \(z\in S^2\),
\[
\int_{S^2}|\langle z,u\rangle|\,d\mu(u)
\ge\int_{S^2}|\langle z,u\rangle|\,d\nu(u).
\tag{1}
\]

**2. A strictly positive dual density.** On \(S^2\) let
\[
g(u)=\prod_{i=1}^{m}\bigl(1-\langle u,v_i\rangle^2\bigr).
\]
It is an even spherical polynomial of degree at most \(2m\), with \(0\le g\le1\), vanishing on \(\operatorname{supp}\nu\). Let \(\sigma\) be ordinary surface area on \(S^2\), with total mass \(4\pi\), and define the cosine transform \(Tf(u)=\int_{S^2}|\langle u,z\rangle|f(z)\,d\sigma(z)\). Funk--Hecke diagonalizes \(T\) on real spherical harmonics: for degree \(0\) the eigenvalue is \(\lambda_0=2\pi\), while at every positive even degree \(2k\),
\[
\lambda_{2k}=4\pi\int_0^1 tP_{2k}(t)\,dt
=(-1)^{k+1}\frac{4\pi(2k-2)!}{4^k(k-1)!(k+1)!}\ne0.
\tag{2}
\]
For instance, the integral is \(-P_{2k}(0)/((2k-1)(2k+2))\); this follows from the Legendre recurrence and integration, with \(P_{2k}(0)=(-1)^k(2k)!/[4^k(k!)^2]\). Let \(\mathcal P_{2k}\) be the orthogonal projector onto degree-\(2k\) spherical harmonics. Because \(g\) is even and polynomial of degree at most \(2m\),
\(g=\sum_{k=0}^m\mathcal P_{2k}g\). Define
\[
q=\sum_{k=0}^m\frac{\mathcal P_{2k}g}{\lambda_{2k}}.
\]
Then \(Tq=g\). The spherical addition formula gives
\[
(\mathcal P_{2k}g)(u)=\frac{4k+1}{4\pi}\int_{S^2}g(z)P_{2k}(\langle u,z\rangle)\,d\sigma(z).
\]
Since \(|P_{2k}(t)|\le1\) on \([-1,1]\) and \(0\le g\le1\),
\[
\|q\|_\infty\le\sum_{k=0}^m\frac{4k+1}{|\lambda_{2k}|}=H_m.
\]
The density \(r(z)=1/(2\pi)-\varepsilon_m q(z)\) is everywhere positive, since \(r\ge1/(2\pi)-H_m/[4\pi(1+H_m)]>0\), and obeys
\[
Tr=1-\varepsilon_m g.\tag{3}
\]
Here \(T(1/(2\pi))=1\), by rotational invariance and direct integration.

**3. Deficit controls polynomial angular error.** Multiply the pointwise inequalities (1), indexed by \(z\), by \(r(z)\,d\sigma(z)\), integrate, and exchange the nonnegative kernels by Fubini. Using (3) and \(g|_{\operatorname{supp}\nu}=0\) yields
\[
2S(B)-\varepsilon_m\int g\,d\mu
\ge S(\partial K),\qquad
\varepsilon_m\int g\,d\mu\le2\delta.\tag{4}
\]
This also recovers \(\delta\ge0\).

**4. Convert to squared angular distance.** For \(u\in S^2\), choose \(i\) attaining its minimum projective angle \(\theta=\arcsin\rho(u)\). For every \(j\ne i\), the projective spherical triangle inequality and the minimality of \(\theta\) give
\[
\arccos|\langle u,v_j\rangle|\ge\max\{\theta,\Delta-\theta\}\ge\Delta/2.
\]
Consequently
\[
g(u)\ge \rho(u)^2\sin^{2m-2}(\Delta/2).
\tag{5}
\]
Combine (4)--(5) to obtain the first boxed inequality. On \(J_\beta\), \(\rho(u)^2>\sin^2\beta\), which yields the second.

**5. Sharpness of the angular power.** Fix one facet-normal line \(\pm v\) carrying \(\nu\)-mass \(a>0\) at each pole, and choose \(t\perp v\) unit. The even atomic measure \(\nu\) is the orientation measure of a finite union of planar patches with total area \(S(\partial K)/2\); such patches can be placed in disjoint planes. Replace the area-\(a\) patch with normal \(v\) by two disjoint patches, each of area \(a/(2\cos\theta)\), with normals \(w_\pm=\cos\theta\,v\pm\sin\theta\,t\), for small \(\theta>0\). For every \(z\),
\[
\frac{|\langle z,w_+\rangle|+|\langle z,w_-\rangle|}{\cos\theta}
\ge2|\langle z,v\rangle|,
\]
so the modified patches still form a weak barrier for \(K\). Its Jones deficit is \(\delta_\theta=a(\sec\theta-1)\sim a\theta^2/2\), whereas the moved orientation mass is \(2a\sec\theta\), all at angle \(\theta\) from the nearest normal for sufficiently small \(\theta\). Taking \(\beta=\theta/2\) shows that no bound of form \(\mu(J_\beta)\le C_K\delta_\theta/\sin^p\beta\) can hold uniformly for all weak barriers with any \(p<2\). In fact, \(\int\rho^2\,d\mu_\theta/\delta_\theta=2(1+\cos\theta)\to4\).

## Verification
The accompanying reproducible standard-library-only script `artifacts/verify.py` exactly checks the first 13 Legendre eigenvalue integrals, tests the pointwise product inequality on deterministic spherical grids for a cube and tetrahedron, and tests the projected-area domination and asymptotic angular normalization for tilted facet patches. Run `python3 artifacts/verify.py`; expected output begins with `VERIFY_OK`. The infinite-dimensionality of the assertions is handled by the analytic Funk--Hecke identity and (1)--(5), not by finite tests.

## Relationship to prior work
Kiderlen's 2026 general weak-barrier theory supplies projection domination and a polytope off-facet estimate with Jones-deficit exponent strictly below one (Corollary 1.4). The theorem above obtains exponent exactly one for **every** full-dimensional three-dimensional polytope, together with a squared-angular integral estimate, using a finite harmonic inverse-cosine certificate. A published result titled *Linear off-axis orientation stability for weak barriers of the unit cube* proves linear behavior for the cube in all dimensions by a different, specialized Rademacher argument; it does not imply a general-polytope assertion. Steinerberger's 2025 work establishes related opaque-set stability in the plane, including a linear square-specific bound, not the spatial result here.

## Limitations
The constant is deliberately conservative and typically much larger than the best possible shape-specific coefficient; only the angular exponent, not the coefficient, is sharp. The claim is three-dimensional because the nonzero cosine-transform spectrum is written explicitly with Legendre polynomials, although related higher-dimensional methods may exist. Optimality is within the class of weak barriers; the split patches need not be opaque barriers, so no sharpness claim is made for genuinely opaque barriers. The theorem does not improve an actual lower bound for the shortest opaque barrier or control the spatial arrangement of patches. Searches do not eliminate the possibility of unindexed equivalent techniques.

## References
1. M. Kiderlen, *Stability for barriers of n-dimensional convex bodies with surface area close to Jones' bound*, arXiv:2605.13449 (first public version 2026-05-13), notably Theorem 1.2, Theorem 1.3 and Corollary 1.4.
2. S. Steinerberger, *A Stability Version of the Jones Opaque Set Inequality*, arXiv:2501.01004 (2025), theorem and square proposition.
3. *Linear off-axis orientation stability for weak barriers of the unit cube* (2026), published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-linear-off-axis-orientation-stability-for-weak-barriers-of-the-u--621361578458.
4. Standard Funk--Hecke formula and addition formula for the spherical harmonics of \(S^2\), with eigenvalue computation reproduced in the proof.
