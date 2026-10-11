# A sharp Steiner-area phase diagram for regular disk triangles

## Finding
Fix a minimal width \(w>0\). For each \(r\ge w\), let \(T_{w,r}\) be the regular \(r\)-disk triangle of minimal Euclidean width \(w\), i.e. the intersection of three congruent closed radius-\(r\) disks whose centers form an equilateral triangle. Let \(B\) be the Euclidean unit disk, and let \(t\ge0\). We determine the unique optimizer, or nonattained infimum, of
\[
\mathcal S_t(r)=\operatorname{area}(T_{w,r}+tB),\qquad r\in[w,\infty).
\]
Set
\[
\tau_- =\frac13,\qquad
\tau_+=\frac{3+2\sqrt3-2\pi}{2\pi-6}=0.6388619161\ldots.
\]
The complete sharp phase diagram is:

1. When \(0\le t/w\le\tau_-\), \(\mathcal S_t(r)\) is strictly decreasing in \(r\); its infimum is approached by the equilateral triangle of altitude \(w\) as \(r\to\infty\), and is not attained by finite \(r\).
2. When \(\tau_-<t/w<\tau_+\), there is exactly one optimal finite parameter \(r_*>w\). Its regular disk triangle strictly beats both the Reuleaux triangle at \(r=w\) and the limiting equilateral triangle for the area of the radius-\(t\) outer parallel set.
3. When \(t/w\ge\tau_+\), \(\mathcal S_t(r)\) has the unique minimizer \(r=w\), the Reuleaux triangle.

For the intermediate regime the parameter is uniquely determined by the explicit scalar equation
\[
\frac{t}{w}=U(\beta_*),\qquad
r_* =\frac{w}{1-\cos\beta_*+\sqrt3\sin\beta_*},
\qquad 0<\beta_*<\frac\pi6,
\]
where \(U\) is defined in the proof. In particular, the two transition constants are not numerical guesses but exact, sharp analytic thresholds.

## Assumptions and scope
All distances, areas, and Minkowski sums are Euclidean and planar. The optimization is **over the canonical family of regular disk triangles**, not over all convex bodies or all \(r\)-ball convex bodies at once. For each fixed \(r\), the initiating isominwidth theorem explains the significance of this family as a fixed-width area extremizer. No claim is made that the same body minimizes the outer-parallel area among *all* convex bodies satisfying those constraints. A limiting equilateral triangle at \(r=\infty\) is a comparison limit, not an admissible finite-radius member.

## Proof
**1. One-to-one angle coordinate.** Let \(\rho\) be the inradius and \(d=w-\rho\) the distance from the common symmetry center to a vertex. Let \(\beta\) be half of the angle subtended by any side arc at its supporting radius-\(r\) disk center. Elementary right triangles give
\[
 d=\frac{2r}{\sqrt3}\sin\beta,\quad
 \rho=r\left(1-\cos\beta+\frac{\sin\beta}{\sqrt3}\right),\quad
 w=rF(\beta),\quad
 F(\beta)=1-\cos\beta+\sqrt3\sin\beta.
\]
Here \(0<\beta\le\pi/6\); the endpoint \(\beta=\pi/6\) is \(r=w\), and \(\beta\downarrow0\) corresponds to \(r\to\infty\). Since \(F'(\beta)=\sin\beta+\sqrt3\cos\beta>0\), this is a bijective decreasing parametrization of the finite \(r\)-range.

**2. Two geometric measures.** The three vertices form an equilateral triangle of side \(2r\sin\beta\). Each of its three outward circular segments has area \(r^2(\beta-\sin\beta\cos\beta)\). Therefore, with
\[
G(\beta)=\sqrt3\sin^2\beta+3(\beta-\sin\beta\cos\beta),
\]
one has the exact area and perimeter identities
\[
\operatorname{area}(T_{w,r})=w^2\frac{G(\beta)}{F(\beta)^2},\qquad
\operatorname{per}(T_{w,r})=w\frac{6\beta}{F(\beta)}.
\]
Steiner's planar parallel-body formula, valid also at the cornered limiting bodies, now yields
\[
\frac{\mathcal S_t(r)}{w^2}=a(\beta)+\tau p(\beta)+\pi\tau^2,
\quad \tau=t/w,\quad
 a=G/F^2,\quad p=6\beta/F.
\]
These expressions include the endpoint values by continuous extension: \(a(0)=1/\sqrt3\), \(p(0)=2\sqrt3\), \(a(\pi/6)=(\pi-\sqrt3)/2\), and \(p(\pi/6)=\pi\).

**3. A strict area-perimeter curvature inequality.** Define
\[
U(\beta)=-\frac{a'(\beta)}{p'(\beta)},\qquad 0<\beta\le\pi/6.
\]
For completeness we prove \(U'(\beta)>0\), rather than assuming a graph shape from plots. Since
\(F''(\beta)=\cos\beta-\sqrt3\sin\beta\ge0\) on \([0,\pi/6]\), with strict inequality in the interior and \(F(0)=0\),
\[
F(\beta)-\beta F'(\beta)=-\int_0^\beta vF''(v)\,dv<0.
\]
Thus \(p'=6(F-\beta F')/F^2<0\). Put
\[
J=G'F-2GF',\quad H_0=F(F-\beta F'),\quad
\mathcal H=JH_0'-J'H_0.
\]
Then \(U=-J/(6H_0)\) and
\[
U'(\beta)=\frac{\mathcal H(\beta)}{6H_0(\beta)^2}.
\]
The following explicit **analytic sign certificate** proves \(\mathcal H>0\) throughout the interval. Expansion of the displayed elementary trigonometric formula gives a finite Fourier polynomial
\[
\mathcal H(\beta)=\sum_{j=0}^{2}\beta^j\sum_{|k|\le4}c_{j,k}e^{ik\beta}
\]
with exact absolute coefficient sums
\[
\sum_k|c_{0,k}|=14\sqrt3+6\sqrt7+2\sqrt{291}+4\sqrt{111}<117,\quad
\sum_k|c_{1,k}|=114,\quad \sum_k|c_{2,k}|=48.
\]
Let \(Q_{20}\) be its degree-20 Maclaurin polynomial. Direct exact expansion, fully reproduced by `verify.py`, gives \(Q_{20}(\beta)=\beta^6\sum_{j=0}^{14}q_j\beta^j\), whose first coefficients are
\[
q_0=\sqrt3/4,\quad q_1=12/5,\quad q_2=-51\sqrt3/80,\quad
q_3=-137/168.
\]
Among the coefficients with \(j\ge4\), the total absolute mass of negative coefficients is strictly below \(6/100\); all other coefficients are nonnegative. Hence for \(0<\beta\le\pi/6<3/5\),
\[
\frac{Q_{20}(\beta)}{\beta^6}
>\frac25+\frac{12}{5}\beta-\frac{111}{100}\beta^2
 -\frac{82}{100}\beta^3-\frac6{100}\beta^6
>\frac25.
\]
For the entire real interval, the Taylor integral remainder for each Fourier exponential gives
\[
\left|\mathcal H(\beta)-Q_{20}(\beta)\right|
\le \beta^{21}\left(\frac{117\cdot4^{21}}{21!}
+\frac{114\cdot4^{20}}{20!}+\frac{48\cdot4^{19}}{19!}\right)
<\frac{\beta^{21}}{5000}<\frac{\beta^6}{5000}.
\]
Consequently \(\mathcal H(\beta)>\beta^6(2/5-1/5000)>0\). This is a continuous-domain bound, not an inference from sampled values. In particular \(U\) is strictly increasing.

**4. Endpoints and minimization.** Direct differentiation (also checked symbolically in `verify.py`) gives
\[
\lim_{\beta\downarrow0} a'(\beta)=\frac13,\qquad
\lim_{\beta\downarrow0}p'(\beta)=-1,\qquad
 a'(\pi/6)=3+2\sqrt3-2\pi,\quad
 p'(\pi/6)=6-2\pi.
\]
Thus \(U(0+)=\tau_-\) and \(U(\pi/6)=\tau_+\). Because
\[
\frac{d}{d\beta}\left[a(\beta)+\tau p(\beta)\right]
=p'(\beta)(\tau-U(\beta)),
\]
and \(p'<0\), monotonicity of \(U\) shows: for \(\tau\le\tau_-\), the expression strictly increases with \(\beta\); for \(\tau\ge\tau_+\), it strictly decreases; and for the intermediate \(\tau\), it strictly decreases before and increases after the **unique** point \(U(\beta)=\tau\). The three statements follow, including endpoint uniqueness, nonattainment, and strict improvement over both endpoint shapes.

## Verification
Run `python verify.py` from the extracted directory, with Python 3 and SymPy installed. The checker reconstructs the Fourier polynomial for \(\mathcal H\) from the formulas, checks all 15 exact Taylor coefficients through degree 20, the frequency bound, the three coefficient norms, the global Taylor remainder inequality, the sign-coefficient bounds, and the four endpoint derivative identities. The expected output is `PARALLEL_DISK_TRIANGLE_PHASE_CERTIFICATE_OK`.

These symbolic computations validate a finite algebraic certificate for the analytic inequality on the entire parameter interval. They are **not** claims of computer-independent formalization or independent audit. The geometry and calculus arguments in this document supply the proof structure; the code exposes every nontrivial coefficient identity used.

## Relationship to prior work
Fodor, Robock, and Sagmeister (2026, arXiv:2602.19300), Theorem 1.1, show that the regular disk triangle minimizes area for **fixed** disk radius and minimal width in the relevant ball-convex class. This paper's Lemma 3.4 supplies its inradius formula. M. Bezdek (2009, arXiv:0903.5361), Remark 1.4, gives area and perimeter formulas for regular disk triangles under a **different fixed center-distance parameter** and states area inequalities for disk-polygons; its Problems 1.7 and 1.14 concern perimeter inequalities for all disk-polygons. Fodor and Sagmeister (2026, arXiv:2606.02882) develop stability at fixed parameters. These studies provide geometric motivation and some scalar ingredients but do not establish the strict curvature inequality \(U'>0\), the sharp outer-parallel optimization thresholds, or the unique interior phase of the varying-radius extremizer family. The present statement is **not** a solution of Bezdek's fixed-parameter perimeter problems.

## Limitations
The result applies only to two-dimensional Euclidean regular disk triangles of prescribed minimal width, with Euclidean circular outer offsets. The limiting triangle is excluded from finite-radius attainment. There is no minimization claim over arbitrary disk-polygons, arbitrary convex bodies, or hyperbolic/spherical bodies. The area and perimeter input functions have appeared in older literature; the new content is the exact global optimization and unique-phase theorem for their Steiner combination. Unindexed prior treatment of this particular optimization is a residual originality risk. The proof uses an exact finite Taylor/Fourier coefficient certificate that can be checked with the included code; independent verification remains outstanding.

## References
1. F. Fodor, N. Robock, Á. Sagmeister, *Pál's isominwidth inequality for ball convex bodies in planes of constant curvature*, arXiv:2602.19300, first submitted 2026-02-22. https://arxiv.org/abs/2602.19300
2. M. Bezdek, *On a generalization of the Blaschke-Lebesgue theorem for disk-polygons*, arXiv:0903.5361, first submitted 2009-03-31. https://arxiv.org/abs/0903.5361
3. F. Fodor, Á. Sagmeister, *Optimal stability of Pál's isominwidth inequality for ball convex bodies in planes of constant curvature*, arXiv:2606.02882, first submitted 2026-06-01. https://arxiv.org/abs/2606.02882
4. Classical planar Steiner parallel-body formula: \(A(K+tB)=A(K)+tP(K)+\pi t^2\) for compact planar convex \(K\), \(t\ge0\).
