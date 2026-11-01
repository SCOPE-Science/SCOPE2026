# Sharp chord-moment ambiguity and stable reconstruction of circular cone sidewalls

## Finding

Let \(S\) be the *lateral surface only* of a finite, nondegenerate right circular cone in Euclidean three-space, with slant length \(s>0\), base radius \(b\), and axial height \(h\), where \(0<b<s\) and \(h=\sqrt{s^2-b^2}\). Choose two independent points uniformly with respect to surface area, and let \(D\) be their **ambient Euclidean chord distance**, not their intrinsic surface distance. Put
\[
\mu=\mathbb E[D^2],\quad \nu=\mathbb E[D^4],\quad \omega=\mathbb E[D^6],\quad
k=b^2/s^2\in(0,1),\quad K=\nu/\mu^2,\quad J=\omega/\mu^3.
\]
Then the precise feasible region for the first two even distance moments is
\[
\boxed{\mu>0,\qquad \frac{1107}{770}\le K<\frac{27}{10}.}
\]
Every feasible pair comes from **exactly two noncongruent cones** when \(1107/770<K<5/3\), and from **exactly one cone** when \(K=1107/770\) or \(5/3\le K<27/10\). The minimum occurs only at \(k=6/29\). Two ambiguous squared shape ratios are exchanged by
\[
\boxed{k\longmapsto \frac{19k+12}{464k-19}}
\]
(only when both ratios are in \((0,1)\)).

By contrast, the three consecutive even moments determine both \(b\) and \(h\) globally. In fact, their dimensionless contrast
\[
T=J-5K=-\frac{27(32760k^3+11207k^2+1668k+40)}{350(1+8k)^3}
\]
is strictly decreasing for \(0<k<1\), with the **sharp global inverse inequality**
\[
\boxed{|k_1-k_2|\le\frac{4725}{281}|T_1-T_2|.}
\]
The constant cannot be reduced over the entire family. Thus three consecutive even distance moments are necessary and sufficient for universal identification of a cone sidewall with unknown scale.

## Assumptions and scope

The cone has a genuine, positive axial height and base radius; the base disk is excluded. The apex and rim have surface-area measure zero. Points are independent and surface-area uniform. All moments are exact population moments. The ambient Euclidean chord metric is essential; the intrinsic geodesic metric on the developed cone produces different formulas. Equality and endpoint statements concern \(k\in(0,1)\), with the collapsed-segment and flat-disk configurations serving only as limiting boundaries.

## Proof

**1. Sampling representation.** Parameterize the sidewall as
\[
X(t,\phi)=s t(\sqrt{k}\cos\phi,\sqrt{k}\sin\phi,\sqrt{1-k}),\qquad 0\le t\le1,\quad0\le\phi<2\pi.
\]
The area element is \(s^2\sqrt{k}\,t\,dt\,d\phi\). Consequently, for a uniform surface point, \(t\) has density \(2t\) on \((0,1)\) and \(\phi\) is independent and uniform on \([0,2\pi)\). For independent points at \((t,\phi)\), \((u,\psi)\),
\[
\frac{D^2}{s^2}=t^2+u^2-2tu\{1-k+k\cos(\phi-\psi)\}.
\]
In particular \(\mathbb E[t^m]=2/(m+2)\), while odd cosine moments vanish and \(\mathbb E[\cos^{2j}(\phi-\psi)]={2j\choose j}/4^j\). Expanding the first three powers, integrating term by term, and collecting coefficients gives the exact identities
\[
\boxed{\frac{\mu}{s^2}=\frac{1+8k}{9},\qquad
\frac{\nu}{s^4}=\frac{1+4k+45k^2}{30},\qquad
\frac{\omega}{s^6}=\frac{5+16k+84k^2+1120k^3}{350}.}
\]
The polynomial integration can also be checked by the independent finite expansion in the accompanying verifier.

**2. The complete two-moment fiber.** From the preceding identities,
\[
K(k)=\frac{27(1+4k+45k^2)}{10(1+8k)^2},\qquad
K'(k)=\frac{27(29k-6)}{5(1+8k)^3}.
\]
Hence \(K\) strictly decreases on \((0,6/29)\), strictly increases on \((6/29,1)\), and takes the values
\[
K(6/29)=1107/770,\qquad \lim_{k\downarrow0}K(k)=27/10,\qquad\lim_{k\uparrow1}K(k)=5/3.
\]
All stated feasibility and multiplicity conclusions follow by continuity and the strict branch monotonicities, because for fixed \(\mu>0\) the scale is uniquely fixed by \(s^2=9\mu/(1+8k)\). In more detail, the exact difference factorization
\[
K(k)-K(y)=\frac{27(k-y)\{464ky-19k-19y-12\}}{10(1+8k)^2(1+8y)^2}
\]
shows that any unequal ratios with the same normalized fourth moment satisfy \(y=(19k+12)/(464k-19)\). Both ratios are in \((0,1)\) precisely for the participating branch parameters \(31/445<k<1\). At the unique fixed point \(k=6/29\) the two branches meet. For example, setting \(\mu=1\), the two cones with \((b^2,h^2)=(1/2,9/2)\) and \((b^2,h^2)=(139/154,135/154)\) have respective squared shape ratios \(k=1/10\) and \(y=139/274\). Both give exactly \((\mu,\nu)=(1,37/24)\), yet they are noncongruent.

**3. Strict third-moment inverse.** Set \(T=J-5K\). Substitution and reduction give
\[
T(k)=-\frac{27(32760k^3+11207k^2+1668k+40)}{350(1+8k)^3},\qquad
T'(k)=-\frac{27(4312k^2-2137k+354)}{175(1+8k)^4}.
\]
The numerator quadratic has negative discriminant \(-1539023\) and positive leading coefficient, so \(T'<0\) for every real \(k\ge0\). The exact image of \((0,1)\) is \((-29/6,-108/35)\). Thus the measured \(T\) uniquely identifies \(k\), after which
\[
\boxed{s^2=\frac{9\mu}{1+8k},\qquad b=s\sqrt{k},\qquad h=s\sqrt{1-k}}
\]
reconstructs the geometric cone. Since \(K\) has a genuine two-element fiber, a third even moment is necessary for a universal inverse. Because \(T\) is strictly monotone, it distinguishes the elements of every such fiber without any genericity assumption.

**4. Optimal uniform inverse constant.** Let \(P(k)=4312k^2-2137k+354\). Differentiation gives
\[
\frac{d}{dk}\left(\frac{P(k)}{(1+8k)^4}\right)
=-\frac{68992k^2-59912k+13465}{(1+8k)^5}.
\]
The numerator on the right has negative discriminant \(-126461376\) and positive leading coefficient. Therefore \(P(k)/(1+8k)^4\) strictly decreases on \([0,1]\). As a result,
\[
-T'(k)\ge \frac{27}{175}\frac{P(1)}{9^4}=\frac{281}{4725},\qquad0<k<1.
\]
The mean value theorem proves the claimed Lipschitz inverse inequality. For two distinct parameters approaching \(1\), their difference quotient \(|k_1-k_2|/|T(k_1)-T(k_2)|\) tends to \(4725/281\), so the constant is sharp though not attained by a positive-height cone.

## Verification

The standalone `verify_cone.py` uses only Python's standard library. Its exact rational polynomial expansion reconstructs the three moment polynomials; it checks the derivative identities, discriminants, endpoint constants, several exact ambiguity pairs, and an independent ambient-distance quadrature over 15 moment/shape combinations. Run with `python3 verify_cone.py`. The actual execution returned `VERIFY_OK exact_polynomial_and_rational_checks= 38 independent_quadratures=15 max_absolute_quadrature_error= 7.29849565e-05`. The finite checks corroborate but do not replace the general algebraic proof above.

## Relationship to prior work

Tu and Fischbach (2002) develop forward two-point Euclidean distance distributions for spherical objects with general densities, and their Sec. V calculates moments for spherical balls. This framework concerns forward distributions and does not state the present inverse phase diagram for a conical lateral surface. García-Pelayo (2011) establishes a general reduction of even distance moments to density moments; this is relevant background for the first proof step, not by itself an implication of the shape-fiber classification or sharp stability constant. Only an abstract could be accessed for this latter paper. Independent geometric investigations of a cone's intrinsic surface distances or of projection widths concern different measurements, not the same Euclidean pair-chord moments. Historical priority is therefore provisional; the accessible source comparisons are not an exhaustive novelty certificate.

## Limitations

The result does not cover solid cones (with volume sampling), cone surfaces including base-disk area, frusta, oblique cones, unequal or dependent sampling laws, intrinsic cone geodesic distances, or finite-sample statistical reconstruction. The inverse uses exact moments, and the sharp Lipschitz estimate controls the dimensionless squared radius ratio \(k\), not absolute scale measurement error or the angle \(\arcsin\sqrt{k}\) uniformly near degenerate endpoints. The full text of García-Pelayo (2011) remained inaccessible, so the priority assessment carries a specific source-access risk. No independent mathematical audit is asserted.

## References

1. S.-J. Tu and E. Fischbach, *Random Distance Distribution for Spherical Objects: General Theory and Applications to n-Dimensional Physics*, arXiv:math-ph/0201046v1, first posted 22 January 2002; Journal of Physics A 35 (2002), 6557–6570. https://arxiv.org/abs/math-ph/0201046 .
2. R. García-Pelayo, *Moments of the distribution of distance*, Journal of Mathematical Physics 52 (2011), 033505. https://doi.org/10.1063/1.3559719 . Abstract and publication information inspected; complete full text unavailable.
3. R. García-Pelayo, *Distribution of distance in the spheroid*, Journal of Physics A: Mathematical and General 38 (2005), 3475–3482. https://doi.org/10.1088/0305-4470/38/16/001 . Abstract inspected for the forward-distance comparison.
