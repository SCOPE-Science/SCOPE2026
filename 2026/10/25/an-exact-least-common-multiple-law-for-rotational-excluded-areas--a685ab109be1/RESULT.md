# An exact least-common-multiple law for rotational excluded areas of regular polygons

## Finding

Let \(n,m\geq3\), let \(r,s>0\), and write \(P_n(r)\) and \(P_m(s)\) for regular polygons with circumradii \(r,s\), centered at the origin, whose first vertices lie on the positive horizontal axis. For an orientation \(\theta\in\mathbb R\), the excluded area for the two differently oriented polygonal particles is
\[
E_{n,m}(\theta)=\operatorname{area}\bigl(P_n(r)+(-R_\theta P_m(s))\bigr).
\]
Set \(g=\gcd(n,m)\), \(L=\operatorname{lcm}(n,m)=nm/g\), and
\[
A_n=\frac{nr^2}{2}\sin\frac{2\pi}{n},\qquad
A_m=\frac{ms^2}{2}\sin\frac{2\pi}{m},\qquad
B_{n,m}=\frac{2grs\sin(\pi/n)\sin(\pi/m)}{\sin(\pi/L)}.
\]
Define
\[
\tau=\begin{cases}0,&n/g\text{ odd},\\ \pi/L,&n/g\text{ even},\end{cases}
\quad
\theta_{\max}=\frac\pi n-\pi-\tau,
\quad
d(\theta)=\min_{k\in\mathbb Z}\left|\theta-\theta_{\max}-\frac{2\pi k}{L}\right|.
\]
Then \(0\le d(\theta)\le\pi/L\), and the **complete exact rotational law** is
\[
\boxed{E_{n,m}(\theta)=A_n+A_m+B_{n,m}\cos d(\theta)}.
\]
There are exactly \(L\) strict global maximizing orientations modulo \(2\pi\), namely \(\theta=\theta_{\max}+2\pi k/L\), and exactly \(L\) strict global minimizing orientations, displaced by \(\pi/L\). Their respective values are
\[
E_{\max}=A_n+A_m+B_{n,m},\qquad
E_{\min}=A_n+A_m+B_{n,m}\cos\frac\pi L.
\]
In particular, the exact rotational amplitude is \(B_{n,m}(1-\cos(\pi/L))\). At a minimizing orientation the graph has a genuine V-shaped cusp; at each maximizer it is smooth with negative second derivative \(-B_{n,m}\).

If \(\Theta\) is uniformly distributed on \([0,2\pi)\), the entire excluded-area distribution is known. For \(z\) between the two extremal values,
\[
\boxed{\Pr(E_{n,m}(\Theta)\le z)
=1-\frac{L}{\pi}\arccos\frac{z-A_n-A_m}{B_{n,m}}}.
\]
The distribution function is zero below \(E_{\min}\) and one at or above \(E_{\max}\); moreover
\[
\mathbb E E_{n,m}(\Theta)=A_n+A_m+\frac{p_np_m}{2\pi},\qquad
p_n=2nr\sin\frac\pi n,\quad p_m=2ms\sin\frac\pi m.
\]

## Assumptions and scope

The polygons are nondegenerate Euclidean regular polygons with integer side counts at least three. The orientation is a real angle modulo \(2\pi\); minus denotes point reflection, and \(R_\theta\) denotes counterclockwise planar rotation. The formula holds for arbitrary positive circumradii, without an equal-area assumption or restriction to particular parities. Area means planar Lebesgue measure. Overlaps of polygonal boundaries have area zero. The probability law assumes only a uniformly distributed relative angle, not an actual random adsorption process.

## Proof

**Mixed-area reduction.** For full-dimensional planar convex polygons \(K,H\), the polygonal first variation of area (equivalently, planar Minkowski mixed area) gives
\[
\operatorname{area}(K+H)=\operatorname{area}(K)+\operatorname{area}(H)
+\sum_{e\subset\partial K}|e|\,h_H(\nu_e),
\]
where \(\nu_e\) is the outward unit normal of an edge and \(h_H\) is the support function. This identity follows by differentiating the quadratic polynomial \(\operatorname{area}(K+tH)\) at zero; moving edge \(e\) outward with normal velocity \(h_H(\nu_e)\) changes area at rate \(|e|h_H(\nu_e)\). For the first polygon all \(n\) edge lengths equal \(2r\sin(\pi/n)\), and their normal angles are \(\pi/n+2\pi j/n\), for \(j=0,\ldots,n-1\).

**Support samples.** The reflected and rotated second polygon has vertex angles \(\theta+\pi+2\pi k/m\). For a unit direction at angle \(\alpha\), its support function is
\[
h_H(\alpha)=s\cos\operatorname{dist}\!\left(\alpha-\theta-\pi,
\frac{2\pi}{m}\mathbb Z\right),
\]
where \(\operatorname{dist}\) is the ordinary real distance to the nearest point of the indicated lattice and lies in \([0,\pi/m]\). Put \(N=n/g\), \(M=m/g\), \(\Delta=2\pi/L\), and \(t=\pi/n-\theta-\pi\). Because \(2\pi/n=M\Delta\), \(2\pi/m=N\Delta\), and \(\gcd(M,N)=1\), the \(n\) support arguments are exactly \(g\) copies of \(N\) distinct classes \(t+k\Delta\) modulo \(N\Delta\). Thus the mixed term is
\[
2grs\sin\frac\pi n\,S_N(t),\qquad
S_N(t)=\sum_{k=0}^{N-1}\cos\operatorname{dist}\!\left(t+k\Delta,N\Delta\mathbb Z\right).
\]

**Finite cosine-sum lemma.** The function \(S_N\) is \(\Delta\)-periodic. If \(N=2q+1\), choose \(-\Delta/2\le t\le\Delta/2\); representatives of the summands are \(t+k\Delta\) with \(-q\le k\le q\), all inside \([-N\Delta/2,N\Delta/2]\). Summing the symmetric cosine progression gives
\[
S_N(t)=\frac{\sin(N\Delta/2)}{\sin(\Delta/2)}\cos t.
\]
If \(N=2q\), choose \(0\le t\le\Delta\); representatives with \(-q\le k\le q-1\) lie in the same interval, and the cosine progression instead gives
\[
S_N(t)=\frac{\sin(N\Delta/2)}{\sin(\Delta/2)}
\cos(t-\Delta/2).
\]
At endpoints where two nearest representatives tie, their cosines coincide, so both calculations remain valid. As \(N\Delta/2=\pi/m\), extension by \(\Delta\)-periodicity yields, in both parities,
\[
S_N(t)=\frac{\sin(\pi/m)}{\sin(\pi/L)}
\cos\operatorname{dist}(t-\tau,\Delta\mathbb Z),
\quad \tau=0\text{ or }\Delta/2
\]
according as \(N\) is odd or even. Substituting into the mixed-area identity gives precisely the stated coefficient and profile, since the distance to the lattice is even and \(t-\tau=\theta_{\max}-\theta\).

**Extrema and probability.** On \([0,\pi/L]\) cosine decreases strictly, and \(B_{n,m}>0\), yielding all equality directions. Near a maximizing lattice point the profile is \(B_{n,m}\cos\delta\); near a midpoint the lattice distance is \(\pi/L-|\delta|\), giving the strictly positive one-sided slope \(B_{n,m}\sin(\pi/L)\) on either side of the minimum. Under uniform \(\Theta\), the nearest-lattice distance \(d(\Theta)\) is uniform on \([0,\pi/L]\). Inverting cosine gives the distribution. Integrating cosine gives mean \(A_n+A_m+B_{n,m}(L/\pi)\sin(\pi/L)\), equal to the perimeter-product form using \(gL=nm\).

## Verification

The standalone `verify_orientation.py` computes excluded area independently as the area of the convex hull of all \(nm\) pairwise vertex sums, without invoking the mixed-area derivation. It checks thirteen side-count pairs with all parity/gcd combinations, using forty deterministic pseudorandom relative angles spanning two full turns plus each predicted maximum, minimum, and repeated maximum. All 559 comparisons passed, with maximum absolute discrepancy \(7.105\times10^{-15}\) at radii \(r=0.7\), \(s=1.3\). A separate numerical orientation integral for every pair agrees with the classical perimeter-product mean to within \(3\times10^{-6}\). Execute `python verify_orientation.py` after installing dependencies from `requirements.txt`. These finite checks are corroboration, not proof for arbitrary side counts.

## Relationship to prior work

The mixed-area identity and kinematic orientation-averaging formula are classical; neither is claimed as new. Abbasi Moud (2026) studies binary mixtures of fixed-orientation regular polygons and relates their adsorption behavior to Minkowski-sum excluded areas. It computes selected mixtures and same-species formulas but does not provide the all-orders, all-angles least-common-multiple profile and distribution stated here. Geigenfeind and de las Heras (2019) study excluded areas of planar hard particles, including numerical orientation profiles and specific regular shapes; their work does not state the arbitrary mixed-order formula. The present claim is the complete mixed-polygon orientation classification, its sharp extrema and its induced probability law, rather than the general fact that an excluded area is a Minkowski-sum area.

## Limitations

The theorem concerns convex **regular** polygons and their excluded area, not adsorption saturation density. It does not claim an exact excluded-area profile for arbitrary irregular polygons, nor a result about physical random-packing correlations. The proof uses standard mixed-area theory. Some older specialized mixed-polygon computations may exist outside the indexed literature considered here; novelty relative to every historical source is not mathematically certifiable from a finite search. No independent audit is claimed.

## References

1. Aref Abbasi Moud, *Saturation Coverage in Binary Mixtures of Oriented Regular Polygons via Random Sequential Adsorption*, arXiv:2606.21812 (first public version June 20, 2026), https://arxiv.org/abs/2606.21812.
2. Thomas Geigenfeind and Daniel de las Heras, *The excluded area of two-dimensional hard particles*, arXiv:1902.05961 (2019), https://arxiv.org/abs/1902.05961.
3. Rolf Schneider, *Convex Bodies: The Brunn–Minkowski Theory*, second expanded ed., Cambridge University Press, 2014 (background planar mixed-area theory).
