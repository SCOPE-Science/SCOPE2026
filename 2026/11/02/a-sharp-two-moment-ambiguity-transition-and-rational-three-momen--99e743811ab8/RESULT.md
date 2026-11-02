# A sharp two-moment ambiguity transition and rational three-moment inverse for cylinder sidewalls

## Finding

For a finite right circular cylinder's **lateral surface only**, the first two even Euclidean point-pair distance moments have a complete sharp feasibility and multiplicity classification. Exactly three consecutive even moments recover the radius and height globally, by a rational formula. The two shapes in every ambiguous two-moment pair are separated strictly—and quantitatively—by the sixth distance moment.

Specifically, let \(R,h>0\), let \(P,Q\) be independent points uniformly sampled by area on
\[
S_{R,h}=\{(R\cos\theta,R\sin\theta,z):0\leq\theta<2\pi,\ 0\leq z\leq h\},
\]
and set \(D=\|P-Q\|_2\), \(\mu=\mathbb E[D^2]\), \(\nu=\mathbb E[D^4]\), and \(\omega=\mathbb E[D^6]\). Put \(\kappa=\nu/\mu^2\). The exact first-two-moment feasible region is
\[
\boxed{\mu>0,\qquad \frac{26}{19}\leq\kappa<\frac{12}{5}.}
\]
Every feasible pair comes from exactly two noncongruent finite cylinder sidewalls when \(26/19<\kappa<3/2\), and from exactly one when \(\kappa=26/19\) or \(3/2\leq\kappa<12/5\). The lower bound is attained only for \(h^2/R^2=30/7\), and the upper bound is unattained but approached in the limit \(h/R\to\infty\).

The inverse from three even moments is
\[
\boxed{h^2=\frac{7581\omega+23082\mu^3-28023\mu\nu}{1672\nu-1628\mu^2},\qquad R^2=\frac12\left(\mu-\frac{h^2}{6}\right).}
\]
The denominator is at least \(660\mu^2>0\) on the feasible first-two-moment region.

When two distinct sidewalls share \((\mu,\nu)\), write \(y_1=h_1^2\), \(y_2=h_2^2\). Then \(y_1+y_2=60\mu/19\), and the **exact sixth-moment separation** is
\[
\boxed{\omega_1-\omega_2=\frac{11}{945}(y_1^3-y_2^3).}
\]
In particular,
\[
|\omega_1-\omega_2|\geq\frac{220}{2527}\,\mu^2|y_1-y_2|.
\]
The latter constant is sharp in the limit when the two branches coalesce at \(\kappa=26/19\).

## Assumptions and scope

All expectations are exact population moments of **Euclidean straight-line distances in ambient \(\mathbb R^3\)**. The cylinder has finite positive radius and height. Its end disks are excluded; the two boundary circles have zero area, hence do not affect sampling. This is not an intrinsic shortest-path problem, an invariant-line random-chord problem, or sampling in the solid cylinder. Surface-area measure is normalized to probability measure. A cylinder sidewall is considered up to ambient Euclidean congruence, hence its parameters are \((R,h)\) with both positive.

## Proof

**1. Exact pair-distance moments.** For independent uniform \(\Theta_1,\Theta_2\in[0,2\pi)\) and independent uniform \(Z_1,Z_2\in[0,h]\), angular and axial differences are independent, and
\[
D^2=A+B,\qquad A=2R^2(1-\cos(\Theta_1-\Theta_2)),\qquad B=(Z_1-Z_2)^2.
\]
The angular difference is uniform modulo \(2\pi\), and \(|Z_1-Z_2|\) has triangular density \(2(h-s)/h^2\) on \([0,h]\). For every integer \(j\geq0\),
\[
\mathbb E[A^j]=\binom{2j}{j}R^{2j},\qquad
\mathbb E[B^j]=\frac{2h^{2j}}{(2j+1)(2j+2)}.
\]
(The first identity is the elementary circle average of \((4\sin^2(\Theta/2))^j\).) By independence,
\[
\mathbb E[D^{2k}]=\sum_{j=0}^{k}\binom{k}{j}\binom{2j}{j}R^{2j}\,
\frac{2h^{2(k-j)}}{[2(k-j)+1][2(k-j)+2]}.
\]
For \(x=R^2>0\) and \(y=h^2>0\), the first three terms are
\[
\begin{aligned}
\mu&=2x+\frac y6,\\
\nu&=6x^2+\frac23xy+\frac{y^2}{15},\\
\omega&=20x^3+3x^2y+\frac25xy^2+\frac{y^3}{28}.
\end{aligned}
\]

**2. Feasibility and sharp two-moment ambiguity.** Fix \(\mu=m>0\), and define \(u=y/m\). The constraint \(x=(m-y/6)/2>0\) is equivalent to \(0<u<6\). Substituting into \(\nu\) gives
\[
\kappa=\frac{\nu}{m^2}=\frac{540-60u+19u^2}{360},\quad 0<u<6.
\]
This is a strictly convex quadratic with its unique minimum at \(u=30/19\) and value \(26/19\). Its left endpoint limit is \(3/2\), its right endpoint limit is \(12/5\), and the latter is strictly larger. Therefore its image is \([26/19,12/5)\); two admissible preimages occur precisely for \(26/19<\kappa<3/2\), and one otherwise. Explicitly, the candidate normalized heights are
\[
u_{\pm}=\frac{30\pm\sqrt{6840\kappa-9360}}{19};
\]
retain only roots in \((0,6)\), then \(h^2=m u\) and \(R^2=m(1-u/6)/2\). At the minimizing ratio, \(y/x=h^2/R^2=30/7\). For \(\kappa>26/19\) in the two-root regime, the roots satisfy \(u_++u_-=60/19\). In the alternative squared aspect ratio \(t=h^2/R^2\), the nontrivial ambiguity partner is the involution
\[
\boxed{t\longmapsto\frac{9(40-3t)}{7t+27}},\qquad 0<t<40/3,
\]
with its sole fixed point \(t=30/7\).

For an exact example at \(\mu=1\), two noncongruent sidewalls with
\[
(R_1^2,h_1^2)=\left(\frac6{13},\frac6{13}\right),\quad
(R_2^2,h_2^2)=\left(\frac{68}{247},\frac{666}{247}\right)
\]
share \(\nu=1212/845\), but not their sixth moments.

**3. Rational three-moment inverse.** With \(m=\mu\) fixed, the exact polynomials become
\[
360\nu=540m^2-60my+19y^2,
\]
\[
7560\omega=18900m^3-3780m^2y+1197my^2+88y^3.
\]
Eliminating \(y^2\) and \(y^3\) using the first identity gives
\[
(1672\nu-1628m^2)y=7581\omega+23082m^3-28023m\nu.
\]
Since \(\nu/m^2\geq26/19\), the left coefficient is at least \([1672(26/19)-1628]m^2=660m^2>0\). Thus \(y=h^2\) is uniquely recovered, and then \(x=R^2\) is uniquely recovered from \(\mu\). Two moments are globally insufficient by Step 2, so **three consecutive even moments are the sharp cutoff for global injectivity**.

**4. Exact and sharp branch separation.** Suppose distinct \(y_1,y_2\) yield the same positive \(m\) and \(\nu\). The quadratic in Step 3 gives \(y_1+y_2=60m/19\). Dividing the difference of the cubic expressions for \(\omega\) by \(y_1-y_2\), and using this sum relation, cancels the linear and quadratic contributions and yields
\[
\omega_1-\omega_2=\frac{11}{945}(y_1-y_2)(y_1^2+y_1y_2+y_2^2).
\]
For any real \(y_1,y_2\) with fixed sum \(s>0\), \(y_1^2+y_1y_2+y_2^2\geq3s^2/4\). Taking \(s=60m/19\) gives the stated separation lower bound with constant \(220/2527\). At \(\kappa\downarrow26/19\), the two distinct admissible branches converge to \(y_1=y_2=30m/19\), so the ratio between the left side and \(m^2|y_1-y_2|\) tends to precisely \(220/2527\). This proves sharpness without asserting attainment for two distinct cylinders.

## Verification

Run `python verify.py` with Python 3, SymPy and SciPy installed. The script independently verifies the binomial moment expansion through degree six, the fixed-mean quadratic, the rational inverse, the ambiguity involution, the exact sixth-moment difference, five exact rational ambiguous-cylinder pairs, and 48 independently integrated angular/axial moment comparisons. Its success message is:

`VERIFY_OK: exact moment/inversion/involution identities, 48 independent quadratures, 5 exact noncongruent moment pairs`

All universal statements are proved analytically above. Finite computations check their implementation and do not replace the inequalities or quantifier arguments.

## Relationship to prior work

Tu and Fischbach (arXiv:math-ph/0201046v1, first public January 22, 2002) develop random Euclidean distance laws for spherical interiors and related moments, not the surface-area point-pair law on a finite cylinder sidewall. Kellerer (1971) treats cylinder chords generated by isotropic **lines**, explicitly distinguishing several chord-sampling models; this does not imply a two-independent-surface-point moment inverse. García-Pelayo (2011) establishes general polynomial expressions for even distance moments of probability densities, as stated in its accessible abstract; the full paper was unavailable for direct comparison, and any implicit special case remains a historical-priority risk. Lellouche and Souris (2019) develop a broad convolution approach to random distances in compact volume regions, with examples including segments, rectangles, balls, and cubes. Neither accessible description supplies the two-moment multiplicity threshold or the rational three-moment inverse for a cylinder sidewall.

An earlier geometric study of the **intrinsic** random distance law on this same lateral surface has different distances and different data: its full shortest-path distribution does not imply the above exact statements about only two or three ambient straight-line distance moments. Neither its metric model nor invariant-line chord results are identified with the present sampling model. Searches of named scientific-result records and the relevant research literature identified no equivalent statement; this is evidence about the sources searched, not a proof of global historical uniqueness.

## Limitations

The result requires known sample construction (uniform lateral-area sampling), Euclidean ambient distance, and exact population moments. It does not treat the solid cylinder, included end disks, nonuniform sampling, noisy finite-sample estimation, intrinsic geodesic distance, or truncated moment observations. The branch-separation estimate is sharp for a fixed moment pair near the branch merger but is not claimed as a minimax statistical rate. Historical priority requires independent literature review, particularly for unindexed results on inverse chord moments.

## References

1. S.-J. Tu and E. Fischbach, *Random Distance Distribution for Spherical Objects: General Theory and Applications to n-Dimensional Physics*, arXiv:math-ph/0201046v1 (January 22, 2002), https://arxiv.org/abs/math-ph/0201046.
2. A. M. Kellerer, *Considerations on the Random Traversal of Convex Bodies and Solutions for General Cylinders*, Radiation Research **47** (1971), 359–376, https://doi.org/10.2307/3573243.
3. R. García-Pelayo, *Moments of the distribution of distance*, Journal of Mathematical Physics **52** (2011), 033505, https://doi.org/10.1063/1.3559719 (full text inaccessible for this comparison).
4. S. Lellouche and M. Souris, *Distribution of Distances between Elements in a Compact Set*, Stats **3** (2019), 1–15, https://doi.org/10.3390/stats3010001.
