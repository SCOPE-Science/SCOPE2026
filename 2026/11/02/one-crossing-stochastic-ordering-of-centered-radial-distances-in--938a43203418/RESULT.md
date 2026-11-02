# One-crossing stochastic ordering of centered radial distances in equal-area regular polygons

## Finding
Let \(P_n\subset\mathbb R^2\) be a centered regular convex polygon of area one with \(n\ge3\) sides, let \(X_n\) be uniformly distributed by area on \(P_n\), and put \(Z_n=\|X_n\|_2\). For **every pair of integers** \(3\le n<m\), the distributions of \(Z_n\) and \(Z_m\) have a unique positive-density crossing. The density of \(Z_m\) is strictly larger on one interval immediately above the inradius of \(P_n\), and strictly smaller after a unique radius \(t_{n,m}\). Their cumulative distribution functions obey
\[
F_m(t)>F_n(t)\quad\text{for all }\rho_n<t<R_n,
\]
with equality for \(0\le t\le\rho_n\) and \(t\ge R_n\). Thus the entire centered-distance law decreases strictly in first-order stochastic order as the number of polygon sides increases. The total-variation and Kolmogorov distances **coincide** and have an exact unique-maximizer description:
\[
\operatorname{TV}(Z_n,Z_m)=\sup_t|F_m(t)-F_n(t)|=F_m(t_{n,m})-F_n(t_{n,m})>0.
\]
The one-Wasserstein distance is an explicit difference of elementary mean-radius expressions given below. No assertion is made about distances between *two* independently sampled polygon points, nor about nonregular polygons.

## Assumptions and scope
Angles use radians. For each integer \(k\ge3\), define \(\alpha_k=\pi/k\), the inradius \(\rho_k\) and circumradius \(R_k\) by
\[
\rho_k=\left(k\tan\frac\pi k\right)^{-1/2},\qquad
R_k=\frac{\rho_k}{\cos(\pi/k)}=\left(\frac{2}{k\sin(2\pi/k)}\right)^{1/2}.
\]
These are the actual radii of an area-one regular convex polygon. A point is sampled from normalized planar Lebesgue area. \(F_k(t)=\Pr(Z_k\le t)\) and \(f_k\) is its almost-everywhere density. The exact distribution is
\[
F_k(t)=\begin{cases}
0,&t\le0,\\
\pi t^2,&0<t\le\rho_k,\\
\pi t^2-k\left[t^2\arccos(\rho_k/t)-\rho_k\sqrt{t^2-\rho_k^2}\right],&\rho_k<t<R_k,\\
1,&t\ge R_k,
\end{cases}
\]
and, away from its finite set of breakpoints,
\[
f_k(t)=\begin{cases}
2\pi t,&0<t<\rho_k,\\
2t\left[\pi-k\arccos(\rho_k/t)\right],&\rho_k<t<R_k,\\
0,&\text{otherwise.}
\end{cases}
\]
The density has the continuous limiting values at breakpoints. These single-shape formulas are **prior literature**, not the asserted new result.

For \(n<m\), there is a unique \(t_{n,m}\in(\rho_m,R_m)\) satisfying
\[
n\arccos(\rho_n/t_{n,m})=m\arccos(\rho_m/t_{n,m}).
\]
For \(\rho_n<t<t_{n,m}\), one has \(f_m(t)>f_n(t)\); for \(t_{n,m}<t<R_n\), one has \(f_m(t)<f_n(t)\) wherever the densities are defined. Both densities agree on \((0,\rho_n)\), and are zero on \((R_n,\infty)\). Their cumulative gap is positive precisely on \((\rho_n,R_n)\). The sharp total-variation gap simplifies to
\[
\Delta_{n,m}=m\rho_m\sqrt{t_{n,m}^2-\rho_m^2}-n\rho_n\sqrt{t_{n,m}^2-\rho_n^2}>0.
\]
Moreover, with
\[
M(k)=\frac{k\rho_k^3}{3}\left[\sec\left(\frac\pi k\right)\tan\left(\frac\pi k\right)+\log\left(\sec\left(\frac\pi k\right)+\tan\left(\frac\pi k\right)\right)\right],
\]
one has \(\mathbb E Z_k=M(k)\) and \(W_1(Z_n,Z_m)=M(n)-M(m)>0\), using Euclidean distance on the nonnegative real line as the transport cost.

## Proof
**1. Exact fixed-area geometry and single-polygon radial law.** Partition \(P_k\) into \(k\) congruent triangles from its center. Each has angular span \(2\alpha_k\) and radial boundary \(r=\rho_k/\cos\theta\), for \(-\alpha_k\le\theta\le\alpha_k\). Its total area is \(k\rho_k^2\tan\alpha_k=1\). If a concentric disk has radius \(\rho_k<t<R_k\), its exterior segments beyond the \(k\) polygon sides are disjoint except at boundaries of zero area. A segment has area \(t^2\arccos(\rho_k/t)-\rho_k\sqrt{t^2-\rho_k^2}\). Subtraction gives \(F_k\) as displayed, and differentiation gives \(f_k\). Alternatively, integrate \(\min\{t^2,\rho_k^2\sec^2\theta\}\) over the angular sectors. These calculations reproduce the known central-reference-point law.

**2. Three strictly ordered shape parameters.** Put \(x=\pi/k\in(0,\pi/3]\). Then \(\rho_k^2=x/(\pi\tan x)\). Since \(\tan x/x\) is strictly increasing in \(x\in(0,\pi/3]\), \(\rho_k\) increases strictly with \(k\). Also \(R_k^2=(2x)/(\pi\sin2x)\). The function \(\sin y/y\) is strictly decreasing on \((0,\pi)\), hence \(R_k\) decreases strictly with \(k\). Finally
\[
k\rho_k=\left(\frac\pi{x\tan x}\right)^{1/2}
\]
increases strictly with \(k\), because \(x\tan x\) increases strictly with \(x\). Consequently \(\rho_n<\rho_m\), \(R_m<R_n\), and \(n\rho_n<m\rho_m\) whenever \(n<m\). We do not require \(\rho_m<R_m< R_n\) to be ordered relative to \(\rho_n\) beyond the displayed inequalities.

**3. Unique density crossing.** For \(\rho_m\le t\le R_m\), both circular-cap formulas are active (because \(\rho_n<\rho_m\le t\le R_m<R_n\)). Define
\[
h(t)=n\arccos(\rho_n/t)-m\arccos(\rho_m/t).
\]
Then \(f_m(t)-f_n(t)=2t\,h(t)\), and
\[
h'(t)=\frac1t\left[\frac{n\rho_n}{\sqrt{t^2-\rho_n^2}}-\frac{m\rho_m}{\sqrt{t^2-\rho_m^2}}\right]<0
\quad(\rho_m<t<R_m).
\]
The inequality is strict because \(n\rho_n<m\rho_m\) and \(\sqrt{t^2-\rho_m^2}<\sqrt{t^2-\rho_n^2}\). At the left endpoint \(h(\rho_m)=n\arccos(\rho_n/\rho_m)>0\). At the right endpoint \(h(R_m)=n\arccos(\rho_n/R_m)-\pi<0\), since \(R_m<R_n\) implies \(\arccos(\rho_n/R_m)<\arccos(\rho_n/R_n)=\pi/n\). Thus there exists exactly one root \(t_{n,m}\in(\rho_m,R_m)\). On \((\rho_n,\rho_m)\), \(f_m=2\pi t>f_n\). On \((R_m,R_n)\), \(f_m=0<f_n\). Hence this one root is the only positive density crossing, aside from intervals of identical densities.

**4. Stochastic and sharp transport consequences.** The CDF difference \(G=F_m-F_n\) equals zero below \(\rho_n\), increases strictly up to \(t_{n,m}\), decreases strictly afterwards, and equals zero above \(R_n\), because both densities integrate to one. It is therefore strictly positive throughout \((\rho_n,R_n)\). Since the positive and negative parts of \(f_m-f_n\) are separated by exactly one threshold, the supremum CDF gap equals half its \(L^1\) density discrepancy, i.e., both total variation and Kolmogorov distance. Substituting the cap formulas at \(t_{n,m}\), the \(t_{n,m}^2\arccos\) terms cancel by the defining crossing equation, leaving the displayed exact \(\Delta_{n,m}\). First-order stochastic dominance implies the one-dimensional identity \(W_1(Z_n,Z_m)=\int_0^\infty (F_m-F_n)\,dt=\mathbb E Z_n-\mathbb E Z_m\).

To evaluate the expectation, integrate \(r\) against uniform area in each angular sector:
\[
\mathbb E Z_k=\frac{k\rho_k^3}{3}\int_{-\pi/k}^{\pi/k}\sec^3\theta\,d\theta.
\]
The antiderivative \(\tfrac12[\sec\theta\tan\theta+\log(\sec\theta+\tan\theta)]\) gives \(M(k)\). This concludes the proof for every integer \(3\le n<m\), with all endpoint equalities stated explicitly.

## Verification
Run `python3 check.py` with Python 3 (standard library only). The script independently integrates polar-sector areas numerically rather than relying exclusively on the circular-cap expression; it compares the resulting CDFs, bisection crossings, sign-order inequalities, the gap simplification, and mean-distance integrals. Its deterministic test scope covers \(3\le n\le18\), \(n<m\le22\), plus dense radial grids, and it reports a square–hexagon example:
\[
t_{4,6}\approx0.567729021647736,\quad
\Delta_{4,6}\approx0.053443541641648,\quad
W_1(Z_4,Z_6)\approx0.005401122747670.
\]
All numerical checks are finite diagnostics. The argument in the Proof section is the infinite-family certificate, and the quoted decimals are approximations to quantities exactly specified above.

## Relationship to prior work
Dacey (1965) tabulated exact distributions of distances to nearest lattice points, including the square and hexagonal cases. Khalid and Durrani (2012, arXiv:1207.5857, first version) gave a general formula for centered and off-center point-to-point distances within regular polygons; the entire single-polygon CDF above follows from their analysis and is explicitly **not novel here**. Haimovich and Magnanti (1988) established asymptotic hexagonal partition optimality for increasing location penalties; this gives a much broader benchmark in a different facility-location optimization setting and can imply special hexagonal comparisons, but does not furnish the present pairwise order for every pair \(n<m\), its unique density-crossing theorem, or exact pairwise total-variation crossing formula. An existing published calculation of Fraenkel asymmetry for individual regular polygons covers the polygon-to-disk symmetric-difference special case; no claim of novelty is made for that endpoint or its asymptotic. The new assertion is solely the **simultaneous finite pairwise one-crossing classification and its quantitative consequences**, not the known CDF or a rephrased disk asymmetry.

## Limitations
The comparison requires the *same area* and a *centered* reference point. The statement is not about two independently uniform polygon points, arclength-uniform boundary points, arbitrary convex polygons, or arbitrary reference locations. No claim is made that regular polygons minimize distances over all convex bodies of equal area; the equal-area disk is a known global rearrangement benchmark. The criterion \(t_{n,m}\) is given uniquely and exactly by a transcendental equation, not asserted to have an elementary radical formula. The finite numerical comparisons are diagnostics, not substitutes for the all-side-count argument. Complete historical priority is not proven, especially for older facility-location and geometric-probability sources that were not inspected in full.

## References
1. M. F. Dacey, *Measures of Distance from a Randomly Located Point to Neighboring Lattice Points for Rectangular and Hexagonal Point Lattices*, Northwestern University Technical Report No. 3, December 1965, NASA document 19660019945. https://ntrs.nasa.gov/api/citations/19660019945/downloads/19660019945.pdf
2. Z. Khalid and S. Durrani, *Distance Distributions in Regular Polygons*, arXiv:1207.5857, first submitted 25 July 2012. https://arxiv.org/abs/1207.5857 (full-text https://arxiv.org/html/1207.5857v3).
3. M. Haimovich and T. L. Magnanti, *Extremum Properties of Hexagonal Partitioning and the Uniform Distribution in Euclidean Location*, SIAM J. Discrete Math. 1 (1988), 50–64, DOI 10.1137/0401006. https://doi.org/10.1137/0401006
4. *Exact Fraenkel asymmetry of regular polygons*, published mathematical research record, 2026-10-04. https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-fraenkel-asymmetry-of-regular-polygons--de06f1cf64dc
