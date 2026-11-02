# A four-region first-instability chart for an antisymmetric two-site clipped logistic map

## Finding

Fix \(0<s<1\) and \(r>0\). On \([0,1]^2\) define the two-site clipped logistic map
\[
\mathcal F_{r,s}(x,y)=\big(H(rx(1-x+sy)),\ H(ry(1-y-sx))\big),\qquad H(u)=\min\{1,\max\{0,u\}\}.
\]
Set \(d=1+s^2\), \(a=(1+s)/d\), \(b=(1-s)/d\), and \(r_c=1+\sqrt6\). For \(3<r<r_c\), put
\[
 z_\pm=\frac{r+1\pm\sqrt{(r-3)(r+1)}}{2r},\qquad P_\pm=(az_\pm,bz_\pm).
\]
The points \(P_+,P_-\) form an interior prime-period-two orbit precisely when \(3<r<\min\{r_c,r_{\rm clip}(s)\}\), where
\[
 r_{\rm clip}(s)=\frac{1+s}{2d}\left(1+\sqrt{1+\frac{4d}{s(1-s)}}\right).
\]
Its two (full two-dimensional) return multipliers are
\[
 \nu_\parallel=4+2r-r^2,\qquad
 \nu_\perp=r^2-\frac{2r(r+1)}d+\frac{4(r+1)}{d^2}.
\]
The unique transverse \(-1\) parameter is
\[
 r_\perp(s)=\frac{1+\sqrt{(d^3+3d+2)/(2-d)}}d.
\]
Let \(s_1\in(0,1)\) be the unique root of \(s^3+s^2+3s-1=0\), let \(s_2\in(0,1)\) be the unique root of \(s^3+s^2+s-1=0\), and put \(s_3=\sqrt{(2\sqrt6-3)/5}\). They satisfy
\[
 0<s_1\approx0.2955977425<s_2\approx0.5436890127<s_3\approx0.6162758288<1.
\]
As \(r\) increases from \(3\), the **first loss of a smooth interior exponentially attracting prime-two orbit** is exactly as follows:

| Coupling range | First event | Exact parameter |
|---|---|---|
| \(0<s<s_1\) | transverse return multiplier reaches \(-1\) | \(r_\perp(s)\) |
| \(s_1<s<s_2\) | the larger orbit point first reaches the clipping face \(x=1\) | \(r_{\rm clip}(s)\) |
| \(s_2<s<s_3\) | transverse return multiplier reaches \(-1\) | \(r_\perp(s)\) |
| \(s_3<s<1\) | tangent return multiplier reaches \(-1\) | \(r_c\) |

At \(s=s_1,s_2\), clipping contact coincides with the formal polynomial transverse \(-1\) threshold; the clipped map is nonsmooth at the boundary event. At \(s=s_3\), the two return multipliers are both \(-1\) at an interior orbit. For every \(0<s<1\), the interior period-two orbit is exponentially attracting for
\[
 3<r<\min\{r_\perp(s),r_{\rm clip}(s),r_c\}.
\]
There is no assertion here that any bifurcation generates a particular subsequent periodic orbit.

## Assumptions and scope

Both coupling signs and magnitudes are fixed as the pair \((s,-s)\); both growth parameters equal \(r\); each coordinate is clipped to \([0,1]\) after its polynomial update. Stability means local exponential attraction of the period-two orbit within the two-dimensional physical square. At the first clipping contact, the orbit itself still has a point on the square's boundary, but the smooth-interior classification no longer applies; the un-clipped polynomial continuation is not asserted to be a physical orbit beyond that contact. The parameter \(r\) is studied only from just above the logistic flip at \(r=3\) to its first event. The limiting couplings \(s=0,1\) are excluded.

## Proof

**1. Exact invariant ray and scalar dynamics.** For the un-clipped polynomial update \(F\), the identities \(a-sb=b+sa=1\) give
\[
 F(az,bz)=(a\,r z(1-z),b\,r z(1-z)).
\]
The polynomial ray therefore carries the familiar scalar logistic map. Solving its two-step fixed-point equation gives exactly \(z_+,z_-\) above, with \(0<z_-<z_+<1\) for \(3<r<r_c\). As long as \(az_+<1\), both orbit points are strictly inside \([0,1]^2\), and the clipping is inactive at and near them. Because \(b<a\), this is the only possible positive clipping contact. Direct differentiation gives \(z_+'(r)>0\): if \(\Delta=\sqrt{(r-3)(r+1)}\), then \(z_+'(r)=[(r+3)/\Delta-1]/(2r^2)>0\). Hence the contact is unique. Substituting \(z_+=1/a\) in the scalar period-two quadratic, and taking its unique root greater than \(3\), yields the stated \(r_{\rm clip}(s)\); also \(r_{\rm clip}(s)>3\).

**2. Exact return spectrum.** Along the ray, the Jacobian of the polynomial map has the fixed tangent eigenvector \((a,b)^\top\) with eigenvalue \(r(1-2z)\). Since its trace equals \(r(2-2z-2z/d)\), its quotient eigenvalue is \(r(1-2z/d)\). The tangent line is the same at both period-two points, so multiplication of the two triangular forms gives
\[
 \nu_\parallel=r^2(1-2z_+)(1-2z_-),\quad
 \nu_\perp=r^2(1-2z_+/d)(1-2z_-/d).
\]
The identities \(z_++z_-=(r+1)/r\) and \(z_+z_-=(r+1)/r^2\) give the displayed formulas. For \(3<r<r_c\), one has \(-1<\nu_\parallel<1\). Furthermore
\[
 \nu_\perp(3)=\left(3-\frac4d\right)^2<1,\qquad
 \nu_\perp-1=\frac{(d-2)(r+1)(dr-d-2)}{d^2}<0,
\]
for \(1<d<2\) and \(r>3\), and
\[
 \frac{\partial\nu_\perp}{\partial r}=\frac{2(d-2)(dr-1)}{d^2}<0.
\]
Thus the transverse multiplier reaches \(-1\) exactly once as a function of \(r>3\), at the positive solution \(r_\perp(s)\). No transverse \(+1\) crossing precedes it.

**3. Exact phase thresholds.** Write the transverse-\(-1\) equation as \(K=d^2(\nu_\perp+1)=0\). The clipping-contact condition, after clearing positive denominators, is
\[
 R=r s(1-s)[rd-(1+s)]-(1+s)^2=0.
\]
An exact polynomial resultant in \(r\) factors as
\[
 \operatorname{Res}_r(K,R)=(s-1)^4d^3(s^3+s^2+s-1)(s^3+s^2+3s-1).
\]
Both cubics are strictly increasing for \(s>0\); each has exactly one root in \((0,1)\), namely \(s_2,s_1\). The penultimate subresultant is a positive factor times \(r(s^3-s)+(s^4+s^3+2s^2-s+1)\). At either cubic root its common solution is therefore \[\n r=\frac{s^4+s^3+2s^2-s+1}{s(1-s^2)}>0,\n\]\n because the numerator is positive for \(0<s<1\). Each of \(K\) and \(R\) has exactly one positive real root, and both positive roots exceed \(3\); hence this common root is precisely \(r_\perp=r_{\rm clip}>3\). There are no other positive crossings. Evaluating the continuous thresholds at \(s=1/4\), \(2/5\) and \(3/5\) establishes their alternating order across the intervals separated by \(s_1,s_2\).

To compare the transverse threshold with the tangential threshold, substitute \(r_c=1+\sqrt6\):
\[
 d^2[\nu_\perp(r_c)+1]=2(d-1)[(4+\sqrt6)d-(4+2\sqrt6)].
\]
Its unique zero for \(s\in(0,1)\) is \(s_3=\sqrt{(2\sqrt6-3)/5}\); the transverse threshold lies below \(r_c\) for \(s<s_3\), and above it for \(s>s_3\). Since \(s_2<s_3\), the ordering from the previous paragraph also excludes an earlier clipping contact when \(s>s_3\). These comparisons prove exactly the four rows of the chart and its three boundary cases. Strict inequalities for both multipliers plus absence of clipping give the asserted local exponential attraction.

## Verification

`CHECK.py` (Python 3 with SymPy) tests the ray identities, tangent and quotient eigenvalues, both return multipliers, the elimination resultant, and the second threshold factorization as exact symbolic equalities. It additionally compares independently evaluated polynomial orbit steps and four representative parameter regimes. Execute `python CHECK.py`. The exact algebraic identities and the preceding analytic sign arguments, not the finite numerical examples, support the universal theorem.

## Relationship to prior work

Baron and Galla (2026) define the clipped interacting logistic-map class and develop large-system disordered fixed-point and fluctuation theory; their accessible supplemental sections S1–S6 cover the parent model and scalar two-cycle but not this finite, deterministic, antisymmetric two-site first-event chart. Satoh and Aihara (1990) studied the **same un-clipped two-variable polynomial specialization** in a numerical predator–prey setting, so their work is a direct and important antecedent, not a merely similar title. Their accessible abstract describes numerical attractor phase diagrams, not the present algebraic four-region ordering; the complete journal article could not be inspected and prior coverage remains a genuine risk. Al-Kaff et al. (2024) analyze general coupled-logistic predator–prey fixed-point bifurcations, but the accessible published sections do not state an interior period-two transverse/contact comparison with explicit cubic thresholds. This comparison is limited to material actually inspected; it is not a proof of absolute historical novelty.

## Limitations

The assertion is for the single antisymmetric, equal-growth two-site slice \(0<s<1\), not for generic random couplings or large networks. The chart concerns the **first event on a specified exact two-cycle branch**; it does not classify every attractor, the fate of other initial conditions, the post-contact clipped dynamics, or the nonlinear dynamics beyond a transverse or double flip. Results at equality are threshold descriptions and do not assert exponential stability. The inaccessible full text of the directly related 1990 numerical study is a substantive historical-priority uncertainty. Independent validation has not been performed.

## References

1. J. W. Baron and T. Galla, *The disordered logistic map*, arXiv:2609.24402v1 (public 2026-09-21), https://arxiv.org/abs/2609.24402 (including accessible supplemental material).
2. K. Satoh and T. Aihara, *Numerical Study on a Coupled-Logistic Map as a Simple Model for a Predator-Prey System*, Journal of the Physical Society of Japan **59** (1990), 1184–1198, DOI:10.1143/JPSJ.59.1184.
3. K. Satoh and T. Aihara, *Self-Similar Structures in Phase Diagram of a Coupled-Logistic Map*, Journal of the Physical Society of Japan **59** (1990), 1123–1126, DOI:10.1143/JPSJ.59.1123.
4. M. O. Al-Kaff, H. A. El-Metwally, A.-E. A. Elsadany and E. M. Elabbasy, *Exploring chaos and bifurcation in a discrete prey–predator based on coupled logistic map*, Scientific Reports **14** (2024), 16118, DOI:10.1038/s41598-024-62439-8.
