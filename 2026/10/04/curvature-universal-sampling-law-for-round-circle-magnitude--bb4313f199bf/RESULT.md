# Curvature-universal sampling law for round-circle magnitude

## Finding

Let \(C_{\ell,\kappa}\) be the round circle metric of circumference \(\ell>0\) and relative curvature \(\kappa\le1\) introduced by Leinster and Willerton. Let \(K^n_{\ell,\kappa}\) be the metric subspace consisting of \(n\) equally spaced points. Write
\[
M_{n,\kappa}=|K^n_{\ell,\kappa}|,
\qquad
M_\kappa=|C_{\ell,\kappa}|,
\]
and use reciprocal magnitudes
\[
Q_{n,\kappa}=M_{n,\kappa}^{-1},
\qquad
Q_\kappa=M_\kappa^{-1}.
\]

For every fixed \(\kappa<1\),
\[
Q_{n,\kappa}
=
Q_\kappa
+
\frac{\ell}{6n^2}
+
\frac{\ell\bigl(\pi^2(1-\kappa)-\ell^2\bigr)}{360n^4}
+
O_{\ell,\kappa}(n^{-6}).
\]
Thus the leading reciprocal-magnitude sampling bias is independent of the ambient relative curvature. Curvature is invisible at order \(n^{-2}\) and first enters at order \(n^{-4}\).

Inverting the expansion gives
\[
M_{n,\kappa}
=
M_\kappa
-
\frac{\ell M_\kappa^2}{6n^2}
+
\left(
\frac{\ell^2M_\kappa^3}{36}
-
\frac{\ell\bigl(\pi^2(1-\kappa)-\ell^2\bigr)M_\kappa^2}{360}
\right)n^{-4}
+
O_{\ell,\kappa}(n^{-6}).
\]
In particular, for every fixed \(\ell>0\) and \(\kappa<1\), sufficiently fine equal-spacing samples have magnitude strictly below the continuum circle magnitude.

The intrinsic endpoint \(\kappa=1\) is different. Put
\[
E=e^{-\ell/2},
\qquad
x=\frac{\ell}{2n}.
\]
Then the reciprocal magnitude is exactly
\[
Q_{n,1}
=
\begin{cases}
\displaystyle \frac{1-E}{n}\coth x,&n\text{ even},\\[3mm]
\displaystyle \frac{\coth x-E\operatorname{csch}x}{n},&n\text{ odd}.
\end{cases}
\]
Consequently,
\[
Q_{n,1}
=
Q_1+
\begin{cases}
\displaystyle \frac{\ell(1-E)}{6n^2}-\frac{\ell^3(1-E)}{360n^4}+O(n^{-6}),&n\text{ even},\\[3mm]
\displaystyle \frac{\ell(2+E)}{12n^2}-\frac{\ell^3(8+7E)}{2880n^4}+O(n^{-6}),&n\text{ odd},
\end{cases}
\]
where
\[
Q_1=\frac{2(1-E)}{\ell}.
\]
The antipodal cusp of the intrinsic distance therefore produces a genuine parity transition in the sampling bias.

## Assumptions and scope

For \(\kappa<1\), the normalized distance profile \(D_\kappa:[0,1]\to\mathbb R\) is the smooth round-metric profile
\[
D_\kappa(s)=
\begin{cases}
\displaystyle \frac{1}{\sqrt\kappa\,\pi}\arcsin\!\bigl(\sqrt\kappa\sin(\pi s)\bigr),&0<\kappa<1,\\[3mm]
\displaystyle \frac{1}{\pi}\sin(\pi s),&\kappa=0,\\[3mm]
\displaystyle \frac{1}{\sqrt{-\kappa}\,\pi}\operatorname{arsinh}\!\bigl(\sqrt{-\kappa}\sin(\pi s)\bigr),&\kappa<0.
\end{cases}
\]
Distances on a circumference-\(\ell\) circle are \(\ell D_\kappa(s)\). The endpoint \(\kappa=1\) is the intrinsic circle, for which
\[
D_1(s)=\min\{s,1-s\}.
\]

The finite spaces are homogeneous, so their magnitude is obtained from the constant weighting. Leinster and Willerton prove that the corresponding continuum magnitude is the limit of these equal-spacing approximants and give
\[
Q_\kappa
=
\int_0^1 e^{-\ell D_\kappa(s)}\,ds.
\]

## Proof

For any \(\kappa\le1\), homogeneity gives
\[
Q_{n,\kappa}
=
\frac1n\sum_{j=0}^{n-1}
\exp\!\left(-\ell D_\kappa(j/n)\right).
\]
For fixed \(\kappa<1\), define
\[
g(s)=e^{-\ell D_\kappa(s)}.
\]
Since \(D_\kappa\) is smooth on \([0,1]\), the sum is the composite trapezoidal rule for \(\int_0^1g(s)\,ds\): the endpoint weights combine because \(g(0)=g(1)=1\).

The local expansion of the round metric at an endpoint is
\[
D_\kappa(s)
=
s+
\frac{\pi^2(\kappa-1)}6s^3
+O(s^5).
\]
Hence
\[
D_\kappa'(0)=1,
\qquad
D_\kappa''(0)=0,
\qquad
D_\kappa'''(0)=\pi^2(\kappa-1).
\]
The symmetry
\[
D_\kappa(1-s)=D_\kappa(s)
\]
gives the corresponding endpoint derivatives at \(1\). Therefore
\[
g'(1)-g'(0)=2\ell
\]
and a direct differentiation gives
\[
g'''(1)-g'''(0)
=
2\ell\bigl(\ell^2+\pi^2(\kappa-1)\bigr).
\]

Euler–Maclaurin for the composite trapezoidal rule yields
\[
Q_{n,\kappa}-Q_\kappa
=
\frac{g'(1)-g'(0)}{12n^2}
-
\frac{g'''(1)-g'''(0)}{720n^4}
+
O_{\ell,\kappa}(n^{-6}).
\]
Substituting the endpoint derivatives gives
\[
Q_{n,\kappa}-Q_\kappa
=
\frac{\ell}{6n^2}
+
\frac{\ell\bigl(\pi^2(1-\kappa)-\ell^2\bigr)}{360n^4}
+
O_{\ell,\kappa}(n^{-6}).
\]
The magnitude expansion follows by applying the reciprocal series to \(M_{n,\kappa}=1/Q_{n,\kappa}\).

At \(\kappa=1\), smooth Euler–Maclaurin across the midpoint is inapplicable because \(D_1\) has an antipodal corner. Instead set
\[
q=e^{-\ell/n}.
\]
For even \(n=2m\), the distance multiset from one sample point gives
\[
Q_{n,1}
=
\frac1n\left(1+2\sum_{j=1}^{m-1}q^j+q^m\right)
=
\frac{1-e^{-\ell/2}}{n}\coth\!\left(\frac{\ell}{2n}\right).
\]
For odd \(n=2m+1\),
\[
Q_{n,1}
=
\frac1n\left(1+2\sum_{j=1}^{m}q^j\right)
=
\frac1n\left[
\coth\!\left(\frac{\ell}{2n}\right)
-e^{-\ell/2}\operatorname{csch}\!\left(\frac{\ell}{2n}\right)
\right].
\]
Expanding \(\coth x\) and \(\operatorname{csch}x\) at \(x=0\) gives the two parity-dependent asymptotic formulas.

## Verification

The accompanying `verify.py` uses only the Python standard library. For several positive circumferences and relative curvatures on both sides of the Euclidean case, it compares direct equal-spacing sums with the two-term smooth expansion and checks sixth-order residual decay when the sample count doubles.

It separately verifies that the \(\kappa=0\) formula is exactly the Euclidean regular-polygon chord sum. At \(\kappa=1\), it compares direct sampling against both exact parity formulas for every sample count in a finite test range and checks the two different leading coefficients on large even and odd samples.

The replay output was:

`VERIFY_OK round-circle magnitude sampling law`

These finite checks are consistency tests. The all-\(n\) asymptotics follow from the displayed Euler–Maclaurin calculation and exact geometric-series identities.

## Relationship to prior work

Kodama and O'Hara's 2024 preprint studies regular polygons and circular metric spaces through magnitude and gives the homogeneous finite-space formula used to compute regular-polygon magnitude. The accessible current revision studies identification and isomer questions; targeted full-text searches found no finite-to-continuum convergence-rate analysis.

Leinster and Willerton introduced the equal-spacing approximation of a Euclidean circle, wrote its finite magnitude as a Riemann sum, and passed to the continuum integral. They then extended the same construction to the one-parameter family of round metrics \(C_{\ell,\kappa}\), noting that all \(D_\kappa\) have the same first and second endpoint derivatives. Their paper establishes convergence and analyzes the separate large-circumference limit, but it does not state a rate in the number of sample points.

The present result quantifies exactly the approximation process that those papers use. It shows that the shared first-order endpoint geometry forces a curvature-universal \(n^{-2}\) term, the third derivative records curvature at \(n^{-4}\), and the intrinsic endpoint leaves the smooth regime and develops an explicit parity split.

## Limitations

The smooth expansion fixes \(\ell>0\) and \(\kappa<1\) before sending \(n\to\infty\). Its remainder is not asserted to be uniform as \(\kappa\uparrow1\), where the midpoint singularity forms. The intrinsic endpoint is instead handled by exact geometric sums.

The result concerns equal-spacing approximants. It does not claim optimality among all \(n\)-point approximations of a circle, nor does it address arbitrary nonhomogeneous circular metric spaces.

The literature comparison was targeted. Euler–Maclaurin theory itself is classical; the originality claim is specifically the curvature-resolved magnitude sampling law and intrinsic parity transition for this geometric family, not the summation formula in isolation.

## References

H. Kodama and J. O'Hara, “Distinguishing regular polygons, cycle graphs, and circular metric spaces by the distance multiset and magnitude,” arXiv:2408.06091. The first public version, posted 2024-08-12, was titled “Identification of circular spaces by magnitude and discrete Riesz energy.”

T. Leinster and S. Willerton, “On the asymptotic magnitude of subsets of Euclidean space,” Geometriae Dedicata 164 (2013), 287–310, DOI 10.1007/s10711-012-9773-6; arXiv:0908.1582.
