# Exact area optimizer on the fixed-angle blunted quarter-disk slice
## Finding
Fix \(m=15/16\), put \(S=\sin m\), \(C=\cos m\),
\[
k=\frac{C^2}{2S^2},\qquad q=\frac{2S}{m+SC},
\]
and for \(0\le \varepsilon\le \varepsilon_*\) define
\[
r_\varepsilon(\theta)=k+\varepsilon\bigl(1-q\cos(\theta-m)\bigr),\qquad 0\le\theta\le 2m,
\]
with the support-function construction of Kominers for the corresponding thickness-one reduced body \(R_\varepsilon\). The sharp endpoint of this nonnegative-curvature slice is
\[
\varepsilon_*=\frac{\tfrac12-k}{1-qC}
=0.7080841391075817500574\ldots .
\]
On the entire interval \(0\le\varepsilon\le\varepsilon_*\), the area is strictly increasing. Hence \(R_{\varepsilon_*}\) is the unique area maximizer on this fixed-\(m\), nonnegative-\(\varepsilon\) slice. Its area is
\[
\operatorname{area}(R_{\varepsilon_*})
=0.7871835266964053731023\ldots,
\]
so in particular
\[
\operatorname{area}(R_{\varepsilon_*})>\frac{\pi}{4}
\]
and it improves the published parameter choice \(\varepsilon=13/20\), whose area is \(0.7862156027191261229868\ldots\), by about \(9.67924\times10^{-4}\).

## Assumptions and scope
The construction is exactly the two-arc, two-segment support-function family in arXiv:2606.28612v1 with \(m\) fixed to \(15/16\), \(k=\tfrac12\cot^2m\), and \(q=2\sin m/(m+\sin m\cos m)\). Only the perturbation amplitude \(\varepsilon\) varies, and this finding restricts to \(\varepsilon\ge0\). The conclusion is an exact optimization on this one-parameter slice. It does not optimize over \(m\), over the full two-parameter family, or over all reduced planar bodies.

At \(\varepsilon=\varepsilon_*\), one of the two curvature-radius functions vanishes only at the two endpoints of an active arc. It is strictly positive in the active interior. Thus the body remains convex, its active support faces are singletons for interior active normals, its thickness is \(1\), and the reducedness argument continues to apply.

## Proof
For \(x=\theta-m\in[-m,m]\), write
\[
r_\varepsilon=k+\varepsilon(1-q\cos x).
\]
For \(m=15/16\), one has \(q>1\) and \(qC<1\). Since \(\cos x\in[C,1]\), for every \(\varepsilon\ge0\),
\[
k+\varepsilon(1-q)\le r_\varepsilon(\theta)\le k+\varepsilon(1-qC).
\]
The right endpoint \(\varepsilon_*=(\tfrac12-k)/(1-qC)\) is therefore exactly where the maximum curvature split first reaches \(r=1/2\). At that parameter,
\[
k+\varepsilon_*(1-q)=0.1705836995749896\ldots>0,
\]
while \(r_{\varepsilon_*}(0)=r_{\varepsilon_*}(2m)=1/2\). Hence for every \(0\le\varepsilon\le\varepsilon_*\),
\[
0<r_\varepsilon(\theta)\le\frac12,
\]
and at the endpoint parameter the equality \(r=1/2\) occurs only at \(\theta=0,2m\). The two curvature radii \(\tfrac12+r_\varepsilon\) and \(\tfrac12-r_\varepsilon\) are therefore nonnegative everywhere and strictly positive for interior active normals. The support measure is nonnegative, the two gap atoms are unchanged and positive, and the thickness identity on active normals remains \(1\). The reducedness proof from the source needs singleton support faces only for interior active normals; those remain singleton, while the four arc endpoints enter by closure. Thus every \(R_\varepsilon\) in this interval, including \(R_{\varepsilon_*}\), is reduced of thickness \(1\).

The source area formula is quadratic in \(\varepsilon\). Define
\[
I_0=2m-\sin 2m,
\]
\[
I_1=2m\cos m-\frac72\sin m+\frac12\sin 3m,
\]
\[
I_2=-\frac12m\cos 2m+\frac14m+\frac14\sin 2m-\frac1{16}\sin 4m.
\]
With \(\alpha=k+\varepsilon\) and \(\beta=q\varepsilon\),
\[
A(\varepsilon)=\alpha^2I_0+\alpha\beta I_1+\beta^2I_2+\frac m2+\frac14\sin 2m.
\]
Equivalently,
\[
A(\varepsilon)=C_0+C_1\varepsilon+C_2\varepsilon^2,
\]
where
\[
C_1=2kI_0+kqI_1,
\qquad
C_2=I_0+qI_1+q^2I_2.
\]
Exact rational interval evaluation of the alternating Taylor bounds for \(\sin(15/16)\) and \(\cos(15/16)\) gives
\[
C_2< -0.0026567<0
\]
and
\[
A'(\varepsilon_*)=C_1+2C_2\varepsilon_*>0.0165098>0.
\]
Because \(C_2<0\), the derivative \(A'\) decreases with \(\varepsilon\). Its minimum on \([0,\varepsilon_*]\) is therefore its positive endpoint value, so \(A\) is strictly increasing on the whole interval. This proves uniqueness of the slice optimizer.

The same exact rational interval calculation gives
\[
0.7871835266964052< A(\varepsilon_*)<0.7871835266964056.
\]
Using Machin's formula and alternating rational bounds for the two arctangent series gives an independent rational upper bound for \(\pi/4\) below this interval, proving the strict excess without floating-point assumptions.

## Verification
Run

`python verify.py`

from the package directory. The script uses only Python's standard library and exact `Fraction` arithmetic. It constructs alternating-series rational enclosures for the needed sine, cosine, and arctangent values; verifies the curvature endpoint, the sign of the quadratic coefficient, positivity of the area derivative at \(\varepsilon_*\), the area interval, the improvement over \(\varepsilon=13/20\), and the comparison with \(\pi/4\). A successful replay prints `VERIFY_OK`.

## Relationship to prior work
arXiv:2606.28612v1 gives the support-function family, proves convexity, thickness one and reducedness for its displayed parameter choice, derives the closed area formula, and explicitly states that the parameters \(m=15/16\) and \(\varepsilon=13/20\) were chosen for convenience rather than area optimization. It further says that the construction closes for every \(m\in(0,\pi/2)\) and every \(\varepsilon\), and identifies optimization over the family as an open direction. The present result carries out that optimization exactly on the natural fixed-angle slice \(m=15/16\), including the boundary case where one curvature radius reaches zero only at the arc endpoints.

The earlier planar reduced-body literature supplies the structural background and the formerly conjectured \(\pi/4\) area bound. It does not contain this 2026 support-function family or the fixed-\(m\) parameter optimization.

## Limitations
This result does not determine the best value of \(m\), the supremum over the full Kominers two-parameter family, or the global maximal area among all reduced planar bodies of thickness \(1\). It also does not assert that the curvature-boundary optimizer is a local maximizer under arbitrary perturbations of the support function. Its exact claim is the unique maximizer on the specified one-parameter slice \(0\le\varepsilon\le\varepsilon_*\).

## References
1. S. D. Kominers, "A reduced planar body with area greater than \(\pi\Delta^2/4\)," arXiv:2606.28612v1, 2026.
2. M. Lassak, "Reduced convex bodies in the plane," Israel Journal of Mathematics 70 (1990), 365-379.
3. M. Lassak, "Area of reduced polygons," Publicationes Mathematicae Debrecen 67 (2005), 349-354.
4. M. Lassak and H. Martini, "Reduced convex bodies in Euclidean space—a survey," Expositiones Mathematicae 29 (2011), 204-219.
