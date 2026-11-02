# A complete two-point distance ordering for the flat Möbius band and its matched cylinder

## Finding

Let \(L,h>0\). Give the rectangular flat Möbius band and the flat cylinder defined below their intrinsic quotient metrics, and sample two points independently from normalized area measure. If \(D_M\) and \(D_C\) denote their distances, then \(D_M\) is strictly smaller than \(D_C\) in the first-order stochastic order, except where the cumulative distributions must agree. More precisely, put \(s=L/2\) and \(R=\sqrt{s^2+4h^2}\). Their distribution functions satisfy

\[
F_M(r)=F_C(r)\quad(r\le s\text{ or }r\ge R),\qquad F_M(r)>F_C(r)\quad(s<r<R).
\]

For each \(r\ge0\), define

\[
a_r(t)=\left[2h-\sqrt{(r^2-t^2)_+}\right]_+,\qquad b_r(t)=\sqrt{(r^2-(2s-t)^2)_+},\qquad j_r(t)=\min\{a_r(t),b_r(t)\},
\]

where \(z_+=\max\{z,0\}\). The **complete excess distribution** is the one-dimensional integral

\[
\boxed{F_M(r)-F_C(r)=\frac1{2h^2s}\int_0^s\left(a_r(t)j_r(t)-\frac12j_r(t)^2\right)\,dt.}
\]

The cylinder distribution itself is

\[
F_C(r)=\frac1s\int_0^s H\!\left(\sqrt{(r^2-t^2)_+}\right)\,dt,
\qquad H(z)=\begin{cases}z/h-z^2/(4h^2),&0\le z\le2h,\\1,&z\ge2h.\end{cases}
\]

Thus both complete laws are determined by single integrals. They have **sharp first-divergence and last-divergence asymptotics**:

\[
\boxed{F_M(s+\varepsilon)-F_C(s+\varepsilon)=\frac{2\sqrt2}{3h\sqrt{s}}\varepsilon^{3/2}+o(\varepsilon^{3/2})}\qquad(\varepsilon\downarrow0),
\]

\[
\boxed{F_M(R-\varepsilon)-F_C(R-\varepsilon)=\frac{R^3}{48h^4s^2}\varepsilon^3+o(\varepsilon^3)}\qquad(\varepsilon\downarrow0).
\]

Under the explicit *matched-coordinate coupling* in the proof, the probability that the Möbius distance is strictly less than the cylinder distance depends only on the aspect ratio \(x=h/s\):

\[
\boxed{\Pr(D_M<D_C)=p(x)=\begin{cases}\dfrac{x^2}{8},&0<x\le1,\\[2pt]\dfrac12-\dfrac{3}{8x^2}-\dfrac{\log x}{2x^2},&x\ge1.\end{cases}}
\]

Here the probability means the specific coupling, **not** an assertion that separately sampled distances can be compared pointwise. The function \(p\) is strictly increasing from \(0\) toward \(1/2\), is twice continuously differentiable at \(x=1\), and has a third-derivative jump there: its left third derivative is \(0\) and its right third derivative is \(-4\).

## Assumptions and scope

Define

\[
M=\big(\mathbb R\times[-h,h]\big)/\langle T\rangle,\quad T(x,y)=(x+L,-y),\qquad
C=(\mathbb R/L\mathbb Z)\times[-h,h].
\]

Both carry the induced intrinsic *flat* Riemannian length metric, not distances through an ambient three-dimensional embedding. Each has area \(2hL\) and total boundary length \(2L\); the Möbius band has one boundary component, the cylinder two. Two area-uniform samples are independent for each surface. All results hold for every real \(L,h>0\), without a thin-strip assumption. Boundary points have sampling probability zero.

## Proof

**1. All relevant lifts and the coupling.** A lift of a point of \(M\) has images \((x'+kL,(-1)^ky')\), where \(k\in\mathbb Z\). The lifted strip is convex; hence a shortest intrinsic geodesic is the straight segment to a suitable deck image. The cylinder has the same images with \(y'\) unreflected. For two random horizontal coordinates, the folded difference \(T_0\) is uniform on \([0,L/2]=[0,s]\). Absorb the parity of the nearest horizontal lift into the sign of the second vertical coordinate (which remains independently uniform by symmetry). Writing \(Y,Y'\) for independent uniforms on \([-h,h]\), the **same probability space** realizes the two distances as

\[
A=\sqrt{T_0^2+(Y-Y')^2},\qquad
B=\sqrt{(2s-T_0)^2+(Y+Y')^2},\qquad
D_C=A,\quad D_M=\min\{A,B\}.
\]

To verify the minimization, note that the closest parity class of deck images has horizontal displacement \(T_0\), the opposite parity class has displacement \(2s-T_0\), and more distant images in either parity class cannot shorten a Euclidean segment. Thus \(D_M\le D_C\) under the coupling, with no assumption about aspect ratio.

**2. Exact distribution.** Put \(u=Y-Y'\) and \(v=Y+Y'\). The pair \((u,v)\) is uniformly distributed with density \(1/(8h^2)\) over the diamond \(|u|+|v|\le2h\). Conditional on \(T_0=t\), the event \(B\le r<A\) consists, in each of the four sign quadrants, of

\[
0\le |v|\le b_r(t),\qquad \sqrt{(r^2-t^2)_+}<|u|\le2h-|v|.
\]

Whenever \(B\le r\), we have \(r\ge2s-t\ge t\), so the square-root interpretation is exact. The area per quadrant is

\[
\int_0^{j_r(t)}\big(a_r(t)-v\big)\,dv=a_r(t)j_r(t)-\frac12j_r(t)^2.
\]

Multiplying by four, by density \(1/(8h^2)\), and integrating \(t\) with density \(1/s\) proves the boxed difference formula. The difference \(Y-Y'\) has triangular density \((2h-|u|)/(4h^2)\) on \([-2h,2h]\), yielding the stated formula for \(F_C\).

**3. Sharp positivity interval.** The alternative length is at least \(s\), so the integrand vanishes if \(r\le s\). The cylinder distance is at most \(R\), so the difference vanishes if \(r\ge R\). If \(s<r<R\), take \(t\) sufficiently close to \(s\), \(v\) close to zero, and \(|u|\) strictly between \(\sqrt{r^2-s^2}\) and \(2h\). This gives an open, positive-measure set of \(B<r<A\), hence strict positivity.

**4. Opening and closing asymptotics.** With \(r=s+\varepsilon\) and \(t=s-w\), the event \(B\le r\) requires \(0\le w\le\varepsilon\). Uniformly in this interval, \(b_r(t)=\sqrt{2s(\varepsilon-w)}+O(\varepsilon^{3/2})\), while \(a_r(t)=2h+O(\sqrt\varepsilon)\). Inserting into the exact integral gives

\[
F_M(s+\varepsilon)-F_C(s+\varepsilon)
=\frac{1}{hs}\int_0^\varepsilon\sqrt{2s(\varepsilon-w)}\,dw+o(\varepsilon^{3/2}),
\]

which is the claimed \(3/2\)-power law. For the upper endpoint, the maximum of \(A\) is \(R\), possible only at \(t=s\) and \(|u|=2h\). At those points \(v=0\) and \(B=s<R\), so compactness and continuity show that \(\max\min(A,B)<R\). Thus near \(R\), the CDF difference equals \(\Pr(A>r)\) exactly. With \(w=s-t\) and \(z=2h-|u|\), the distance deficit satisfies

\[
R-A=\frac{sw+2hz}{R}+O((w+z)^2),
\]

and the \((w,z)\) probability density is \(z/(2h^2s)\). Integrating over the triangle \(sw+2hz<R\varepsilon\) gives

\[
\Pr(A>R-\varepsilon)\sim\frac1{2h^2s}\int_0^{R\varepsilon/s}\int_0^{(R\varepsilon-sw)/(2h)}z\,dz\,dw
=\frac{R^3\varepsilon^3}{48h^4s^2}.
\]

**5. Exact strict-shortcut probability.** Squaring yields

\[
B^2-A^2=4\big(s(s-T_0)+YY'\big).
\]

The signs of \(Y,Y'\) differ with probability \(1/2\). Conditional on this, their absolute magnitudes are independent uniforms on \([0,h]\). If \(U,V\) are independent uniforms on \([0,1]\), then \(\Pr(UV>z)=1-z+z\log z\) for \(0<z<1\). Integrating this with \(z=s(s-T_0)/h^2\), and using its zero extension for \(z\ge1\), gives precisely the two formulas for \(p(h/s)\). For \(x>1\), direct differentiation gives \(p'(x)=(1/4+\log x)/x^3>0\); for \(x<1\), \(p'(x)=x/4>0\). One-sided differentiation through third order at \(x=1\) gives the stated \(C^2\) but non-\(C^3\) transition.

## Verification

The reproducible Python 3 standard-library script `verify_geometry.py` checks exact rational deck distances against direct lift enumeration, Monte Carlo estimates of the CDF excess and coupling shortcut probability against the one-dimensional formula, both asymptotic constants, and the derivative jump. Run `python3 verify_geometry.py` in the extracted artifact directory. The completed run passed 7,203 exact lift comparisons, 750,009 seeded finite comparisons and bookkeeping checks, 12 endpoint checks, and 4 transition checks (757,228 total). Only the complete analytic proof above establishes the all-parameter assertions; simulations are not proofs of stochastic ordering or sharp limits.

## Relationship to prior work

Starostin and van der Heijden (2007) analyze the shape of an elastically embedded Möbius strip; the focus is bending equilibrium, not the intrinsic two-point distance law of a flat rectangular quotient. Sabitov (2007) treats isometric immersions and embeddings of a flat Möbius strip; the full article was not accessible for a decisive full-text comparison, and priority uncertainty is acknowledged. Starostin and van der Heijden (2014) analyze equilibrium of elastic strips. Eyll (2025, first preprint 2025-02-19) studies systolic inequalities and stability for the Möbius strip and Klein bottle, not two-point distance cumulative laws. A prior full intrinsic pair-distance law for the lateral surface of a finite circular cylinder already gives the matched flat cylinder distribution \(F_C\), including its cubic terminal tail coefficient. That law is used as a comparator, not claimed as new; in particular, the terminal constant above is inherited from the cylinder law once the Möbius support is seen to end strictly earlier. Related exact distance comparisons on flat closed Klein bottles concern a surface without boundary and do not imply this theorem for the boundary Möbius strip and matched cylinder. The new assertions are the all-aspect-ratio strict CDF ordering and exact CDF *difference*, the sharp onset behavior at \(s\), the comparison support, and the coupling transition law—not the pre-existing cylinder law or intrinsic diameter and moment formulas for flat Möbius strips.

## Limitations

The model is the intrinsic flat quotient of a Euclidean strip, not a physically embedded developable strip with bending stress, nor a curved metric. The strict-shortcut probability is defined under the displayed coupled sampling and does not compare independent samples pointwise. The theorem concerns area-uniform sampling and all fixed positive geometric dimensions; it does not assert uniform asymptotic errors in a singular limit where \(h/s\) changes with \(\varepsilon\). Some historical primary texts were not available in full, so an unqualified global priority assertion is not made. Independent validation of the new proof has not been performed.

## References

1. E. L. Starostin and G. H. M. van der Heijden, “The shape of a Möbius strip,” *Nature Materials* **6** (2007), 563–567, first public 2007-07-15, doi:10.1038/nmat1929.
2. I. Kh. Sabitov, “Isometric immersions and embeddings of a flat Möbius strip in Euclidean spaces,” *Izvestiya Mathematics* **71** (2007), doi:10.1070/IM2007v071n05ABEH002376. Full text not inspected.
3. E. L. Starostin and G. H. M. van der Heijden, “Equilibrium Shapes with Stress Localisation for Inextensible Elastic Möbius and Other Strips,” *Journal of Elasticity*, first published 2014-08-27, doi:10.1007/s10659-014-9495-0.
4. J. Eyll, “Stability of Systolic Inequalities for the Möbius Strip and Klein Bottle,” *Journal of Geometric Analysis* **35** (2025), article 365, preprint arXiv:2502.13715 (2025-02-19), doi:10.1007/s12220-025-02197-9.
5. D. Granata and V. Carnevale, “Accurate Estimation of the Intrinsic Dimension Using Graph Distances,” *Scientific Reports* **6** (2016), article 31377, doi:10.1038/srep31377.
