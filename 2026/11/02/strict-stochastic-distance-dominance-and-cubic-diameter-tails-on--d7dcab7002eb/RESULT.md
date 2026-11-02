# Strict stochastic distance dominance and cubic diameter tails on rectangular flat Klein bottles

## Finding

Let \(L,H>0\). Give the flat Klein bottle
\[
K_{L,H}=\mathbb R^2/\langle (x,y)\mapsto(x+L,y),\ (x,y)\mapsto(-x,y+H)\rangle
\]
its quotient Euclidean length metric, and give the equal-area rectangular flat torus
\[
T_{L,H}=\mathbb R^2/(L\mathbb Z\oplus H\mathbb Z)
\]
its intrinsic Euclidean metric. Sample two points independently according to normalized area on each surface, and denote their distances by \(D_K\) and \(D_T\), respectively.

Put \(s=L/2\), \(h=H/2\), \(R=\sqrt{s^2+h^2}\), and
\[
q_t(v)=\min\left\{1,\frac{\sqrt{(t^2-v^2)_+}}{s}\right\},\qquad (z)_+=\max\{z,0\},\quad t,v\geq0.
\]
The **exact difference between the full cumulative distributions** is
\[
\boxed{\Pr(D_K\leq t)-\Pr(D_T\leq t)
 =\frac1h\int_0^h q_t(2h-w)\,[1-q_t(w)]\,dw.}
\]
Consequently,
\[
\boxed{\Pr(D_K\leq t)=\Pr(D_T\leq t)\quad (0\leq t\leq h),}
\]
\[
\boxed{\Pr(D_K\leq t)>\Pr(D_T\leq t)\quad (h<t<R),}
\]
with both cumulative distributions equal to one for \(t\geq R\). Both surfaces have intrinsic diameter \(R\). Thus the Klein-bottle two-point distance is strictly smaller in first-order stochastic order over the indicated interval, for **every** positive aspect ratio, although the two surfaces have identical area and diameter.

The comparison has a sharp nonanalytic onset:
\[
\boxed{\Pr(D_K\leq h+\varepsilon)-\Pr(D_T\leq h+\varepsilon)
 \sim\frac{2\sqrt2}{3s\sqrt h}\,\varepsilon^{3/2}
 \qquad(\varepsilon\downarrow0).}
\]
At their common diameter, the two upper tails have **different exponents**:
\[
\boxed{\Pr(D_T>R-\varepsilon)\sim\frac{R^2}{2h^2s^2}\,\varepsilon^2,\qquad
\Pr(D_K>R-\varepsilon)\sim\frac{2R^3}{3h^2s^4}\,\varepsilon^3.}
\]
For example, when \(L=H=2\), the leading upper-tail constants are \(1\) and \(4\sqrt2/3\), respectively. The strict distributional ordering entails strict inequalities for the expectations of every strictly increasing continuous function of distance for which the expectation is defined.

## Assumptions and scope

Both positive lengths are arbitrary fixed real numbers. Uniform sampling refers to the normalized intrinsic two-dimensional Riemannian area, **not** to an extrinsic embedding. The Klein bottle is represented by the fundamental rectangle \([0,L)\times[0,H)\); its generators are the horizontal translation and a vertical glide reflection. Its area is \(LH\), the same as the comparison torus. All probability formulas use independent sampling of **both** endpoints, with no distinguished base point. Formulas involving \(\varepsilon\) are fixed-aspect-ratio limits; no error uniformity in \(L/H\) is asserted.

## Proof

**1. The two possible deck-transform path types.** Let representatives be \(p=(x,y)\) and \(q=(x',y')\) in the fundamental rectangle. Every even deck transform of \(q\) has the form \((x'+kL,y'+2jH)\); every odd transform has the form \((-x'+kL,y'+(2j+1)H)\). A shortest quotient geodesic is the projection of a Euclidean segment joining \(p\) to a nearest lift of \(q\). Define the folded horizontal distances
\[
u=\operatorname{dist}(x-x',L\mathbb Z),\qquad
v=\operatorname{dist}(x+x',L\mathbb Z),\qquad z=|y-y'|.
\]
Since \(0\leq z<H\), minimizing separately over even and odd lifts gives the **exact** pointwise identity
\[
\boxed{d_K(p,q)^2=\min\{u^2+z^2,\ v^2+(H-z)^2\}.}\tag{1}
\]
No other lift types exist; hence this is an equality, not merely a bound.

**2. Two independent horizontal distances.** For independent uniform \(x,x'\) on the circle of circumference \(L\), the map
\[
(x,x')\longmapsto(x-x',x+x')\pmod L
\]
is a surjective finite covering of the product torus. It pushes normalized Haar measure to normalized Haar measure. Equivalently, for every integer pair \((j,k)\ne(0,0)\), the corresponding Fourier expectation factors into the expectations of nontrivial circle characters with frequencies \(j+k\) and \(k-j\), at least one of which is nonzero. Thus \(u\) and \(v\) in (1) are **independent**, both uniformly distributed over \([0,s]\), and independent of the vertical variables.

**3. Symmetrizing the vertical separation.** If \(y,y'\) are independent uniform on \([0,H)\), then \(z=|y-y'|\) has density \(2(H-z)/H^2\) for \(0<z<H\). For independent identically distributed \(u,v\), the law of the right-hand side of (1) at \(z\) equals its law at \(H-z\), by swapping \(u\) and \(v\). For any bounded measurable function of the resulting distance, averaging the triangular density against this symmetric function is the same as averaging the uniform density \(1/H\) over \([0,H]\). Therefore
\[
D_K\ \stackrel{d}{=}\ \min\{\sqrt{U^2+Z^2},\sqrt{V^2+(H-Z)^2}\},
\]
where \(U,V\) are independent uniform on \([0,s]\) and \(Z\) is an independent uniform on \([0,H]\).

Set \(W=\min\{Z,H-Z\}\). Then \(W\) is uniform on \([0,h]\). Select the horizontal variable paired with the nearer of the two vertical distances and call it \(B\), and call the other horizontal variable \(C\). Conditional on \(W\), \(B,C\) remain independent uniforms on \([0,s]\). Consequently there is an exact joint realization
\[
\boxed{D_K=\min\{\sqrt{B^2+W^2},\sqrt{C^2+(2h-W)^2}\},\qquad
D_T=\sqrt{B^2+W^2}.}\tag{2}
\]
The marginal \(D_T\) is precisely the intrinsic two-point distance on the rectangular flat torus, by its independent uniformly folded coordinate differences. In particular, (2) is a coupling with \(D_K\leq D_T\) almost surely.

**4. Complete cumulative distribution and strictness.** Conditional on \(W=w\), the probability that \(\sqrt{B^2+w^2}\leq t\) is exactly \(q_t(w)\); likewise the other branch has conditional probability \(q_t(2h-w)\). Independence of \(B,C\) yields
\[
F_T(t)=\frac1h\int_0^h q_t(w)\,dw,
\]
\[
F_K(t)=\frac1h\int_0^h\{q_t(w)+q_t(2h-w)-q_t(w)q_t(2h-w)\}\,dw.
\]
However the first expression inside braces has the extra far-branch term, so subtraction yields the boxed difference formula above. If \(0\leq t\leq h\), then \(q_t(2h-w)=0\) for every \(w<h\), proving equality. For \(h<t<R\), the inequalities
\[
2h-w<t,\qquad t<\sqrt{s^2+w^2}
\]
both hold for all \(w\) sufficiently close to \(h\) from below. Hence the gap integrand is strictly positive on a set of positive length. At and above \(R\), \(q_t(w)=1\) for all \(w\in[0,h]\), so both laws are one. This proves the claimed sharp strictness interval.

Formula (2) implies both diameters are at most \(R\). On the torus the opposite half-period pair realizes \(R\). On the Klein bottle choose \(x=L/2\), \(x'=0\), \(y=H/4\), \(y'=3H/4\). Then \(u=v=s\), \(z=h\) in (1), so the distance is \(R\). Both diameter claims follow.

**5. Onset at the vertical half-period.** Let \(t=h+\varepsilon\) and write \(w=h-\varepsilon u\). Only \(0\leq u\leq1\) contributes to the gap integral. Uniformly for \(u\in[0,1]\), as \(\varepsilon\downarrow0\),
\[
q_{h+\varepsilon}(h+\varepsilon u)
=\frac{\sqrt{2h\varepsilon}}s\sqrt{1-u}+o(\sqrt\varepsilon),
\qquad q_{h+\varepsilon}(h-\varepsilon u)=O(\sqrt\varepsilon).
\]
After the change of variable the gap divided by \(\varepsilon^{3/2}\) tends, by dominated convergence, to
\[
\frac{\sqrt{2h}}{hs}\int_0^1\sqrt{1-u}\,du
=\frac{2\sqrt2}{3s\sqrt h}.
\]
This proves the exact leading onset constant.

**6. The two diameter-tail exponents.** Let \(t=R-\varepsilon\), and again write \(w=h-\varepsilon u\). For bounded \(u\geq0\),
\[
1-q_{R-\varepsilon}(h-\varepsilon u)
=\frac\varepsilon{s^2}(R-hu)_++o(\varepsilon),
\]
\[
1-q_{R-\varepsilon}(h+\varepsilon u)
=\frac\varepsilon{s^2}(R+hu)+o(\varepsilon).
\]
The first factor is zero outside \(u\leq R/h+o(1)\), so this rescaling captures the full contribution. From (2),
\[
\Pr(D_T>t)=\frac1h\int_0^h[1-q_t(w)]\,dw,
\]
\[
\Pr(D_K>t)=\frac1h\int_0^h[1-q_t(w)][1-q_t(2h-w)]\,dw.
\]
Dominated convergence on the bounded rescaled support gives
\[
\lim_{\varepsilon\downarrow0}\frac{\Pr(D_T>R-\varepsilon)}{\varepsilon^2}
=\frac1{hs^2}\int_0^{R/h}(R-hu)\,du=\frac{R^2}{2h^2s^2},
\]
\[
\lim_{\varepsilon\downarrow0}\frac{\Pr(D_K>R-\varepsilon)}{\varepsilon^3}
=\frac1{hs^4}\int_0^{R/h}(R^2-h^2u^2)\,du=\frac{2R^3}{3h^2s^4}.
\]
Both constants are positive and finite for all \(L,H>0\). This completes the proof.

## Verification

A standalone standard-library Python checker is included as `VERIFY.py`; run `python3 VERIFY.py`. It verifies the squared-distance lift formula against exact rational deck enumeration for several aspect ratios, checks sum–difference independence on finite cyclic analogues, and numerically checks distribution support, strictness, the onset constant, and both diameter-tail constants. The recorded execution passed 5,656 finite exact checks and 49 numerical checks. These finite checks are **not** proofs for all positive real aspect ratios; all universal quantifiers are covered by the analysis above.

## Relationship to prior work

El Mir and Yassine (first publicly available in 2012) explicitly model flat Klein bottles by glide reflections and study optimal conformal inequalities between systolic lengths and area, rather than random two-point distance laws. Davis and Recio-Mitter (2019) describe shortest geodesics and total cut loci on higher-dimensional Klein bottles; their polyhedral cut-locus structure is relevant background but does not state the distributional comparison or its endpoint exponents. Benedetto and coauthors (2021) compute spectral constants for random assignment problems on flat manifolds, including a Klein bottle, rather than the distance distribution of an unpaired uniform point pair. Previous calculations of squared pairwise geodesic distance on rectangular flat Klein bottles establish a weaker moment-level comparison; no novelty is claimed for that moment formula. The present contribution is the strict all-threshold stochastic ordering, its exact integral gap, and its distinct sharp endpoint exponents. Literature coverage is necessarily incomplete; priority beyond the sources examined is not certified.

## Limitations

The statements apply to the intrinsic quotient metrics defined above, not to extrinsic distances on an immersed Klein bottle. The comparison torus has the **same fundamental rectangle and area**, but is not the orientable double cover of the Klein bottle. The calculations do not address nonflat metrics, higher-dimensional generalizations, or nonuniform sampling. Endpoint constants are pointwise in the aspect ratio. The absence of an equivalent result in searched publications does not constitute a proof of worldwide novelty. No independent mathematical audit has been performed.

## References

1. C. El Mir and Z. Yassine, *Conformal Geometric Inequalities on the Klein bottle*, arXiv:1209.6202v1, publicly posted 27 September 2012, https://arxiv.org/html/1209.6202v1 (full text inspected, especially Sections 1.1–1.2).
2. D. M. Davis and D. Recio-Mitter, *The geodesic complexity of n-dimensional Klein bottles*, arXiv:1912.07411, publicly posted 16 December 2019, https://arxiv.org/abs/1912.07411 (full accessible text inspected, especially Sections 2–3).
3. D. Benedetto, E. Caglioti, S. Caracciolo, M. D’Achille, G. Sicuro and A. Sportiello, *Random Assignment Problems on 2d Manifolds*, Journal of Statistical Physics 183 (2021), article 34, https://doi.org/10.1007/s10955-021-02768-4 (full accessible text inspected, especially Section 5.3.3).
