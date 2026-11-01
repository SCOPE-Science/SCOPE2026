# Two even Euclidean chord moments identify spherical caps, with optimal inverse exponents

## Finding

Let \(R>0\), \(-1\le z<1\), and let \(C(R,z)\) be the spherical-surface cap
\[
C(R,z)=\{x\in\mathbb R^3:\|x\|_2=R,\ x_3\ge Rz\}.
\]
The endpoint \(z=-1\) means the complete sphere; \(z=1\) is excluded because the cap has zero area. Let \(X,Y\) be **independent and uniformly distributed by spherical surface area** on \(C(R,z)\), and let \(D=\|X-Y\|_2\) be the ambient **Euclidean chord distance**, not intrinsic surface distance. Set
\[
\mu=\mathbb E[D^2],\qquad \nu=\mathbb E[D^4],\qquad
\kappa=\frac{\nu}{\mu^2}.
\]
Then
\[
\mu=\frac{R^2(1-z)(z+3)}2,\qquad
\nu=\frac{2R^4(1-z)^2(z^2+4z+5)}3,
\]
and the normalized fourth moment has the factorization
\[
\boxed{\kappa=\frac43\left(1+\left(\frac{z+1}{z+3}\right)^2\right).}
\]
Consequently, the complete feasible set of pairs of even moments is exactly
\[
\boxed{\mu>0,\qquad \frac43\mu^2\le\nu<\frac53\mu^2.}
\]
Every such pair determines one and only one spherical cap up to Euclidean isometry. Explicitly, put
\[
t=\sqrt{\frac{3\nu}{4\mu^2}-1}\quad(0\le t<\tfrac12).
\]
Then
\[
\boxed{z=\frac{3t-1}{1-t},\qquad R^2=\frac{\mu(1-t)^2}{2(1-2t)}.}
\]
The boundary \(\nu=4\mu^2/3\) corresponds only to the complete sphere. The upper boundary \(\nu=5\mu^2/3\) is sharp but is not attained by a positive-area cap: it is approached when \(z\uparrow1\). One moment \(\mu\) alone never identifies both the radius and the cap opening.

The inverse map has sharp stability statements. For any two caps, writing their normalized moment ratios \(\kappa_1,\kappa_2\) and normalized cut heights \(z_1,z_2\),
\[
\boxed{|z_1-z_2|\le 2\sqrt3\,|\kappa_1-\kappa_2|^{1/2}.}
\]
Both the constant \(2\sqrt3\) and the exponent \(1/2\) are globally sharp (the constant as a limiting supremum). In terms of the cap angular opening \(\alpha=\arccos z\in(0,\pi]\),
\[
|\alpha_1-\alpha_2|\le\pi 3^{1/4}|\kappa_1-\kappa_2|^{1/4}.
\]
Here \(1/4\) is the optimal uniform Hölder exponent, even if the first squared-distance moment is held fixed. More precisely, as \(\alpha\uparrow\pi\),
\[
\boxed{\kappa-\frac43\sim\frac{(\pi-\alpha)^4}{12}.}
\]
The constant in the angular-opening inequality is not asserted optimal.

## Assumptions and scope

The underlying sphere is a two-dimensional surface embedded in three-dimensional Euclidean space. Caps may be smaller or larger than a hemisphere. The circular boundary has zero sampling probability. Sampling is *by surface area* (not from volume or from lines), and each pair consists of independent points. All parameter and equality statements are for exact population moments; no sampling-noise model is assumed. Position and orientation of the cap are immaterial under Euclidean congruence.

## Proof

**Step 1: the axial and azimuthal law.** Divide \(X\) by \(R\) to obtain \(U\) on the unit sphere. In spherical coordinates \(u=U_3=\cos\theta\) and azimuth \(\varphi\), the area element is \(R^2\,\mathrm d\varphi\,\mathrm du\). Thus \(u\) is uniform on \([z,1]\) and \(\varphi\) is independent and uniform on \([0,2\pi)\). Its mean and second moment are
\[
m=\mathbb E[u]=\frac{1+z}{2},\qquad
q=\mathbb E[u^2]=\frac{1+z+z^2}{3}.
\]
By axial symmetry,
\[
\mathbb EU=(0,0,m),\qquad
M:=\mathbb E[UU^{\mathsf T}]
=\operatorname{diag}\left(\frac{1-q}{2},\frac{1-q}{2},q\right).
\]
For an independent copy \(V\), define \(H=U\cdot V\). Independence gives
\[
\mathbb EH=m^2,\qquad
\mathbb EH^2=\sum_{i,j}(\mathbb E U_iU_j)^2
=\operatorname{tr}(M^2)=q^2+\frac{(1-q)^2}{2}.
\]
Since \(D^2=2R^2(1-H)\),
\[
\mu=2R^2(1-m^2),\qquad
\nu=4R^4\left(1-2m^2+q^2+\frac{(1-q)^2}{2}\right).
\]
Substituting \(m,q\) and collecting polynomial terms yields exactly the two moment formulas in the finding. This derivation remains valid for \(z=-1\), \(z=0\), and \(z<0\), without a convexity assumption on the spherical cap.

**Step 2: complete inversion and feasible range.** Cancelling \(R\) from \(\nu/\mu^2\) gives
\[
\kappa=\frac{8(z^2+4z+5)}{3(z+3)^2}
=\frac43\left(1+\frac{(z+1)^2}{(z+3)^2}\right).
\]
The coordinate \(t=(z+1)/(z+3)\) increases strictly from \(0\) to the unattained endpoint \(1/2\) as \(z\) ranges over \([-1,1)\). Hence \(\kappa\) increases strictly from \(4/3\) toward \(5/3\). Solving \(t=(z+1)/(z+3)\) gives \(z=(3t-1)/(1-t)\). Substitution into the expression for \(\mu\) gives
\[
\mu=2R^2\frac{1-2t}{(1-t)^2},
\]
which proves the inverse formulas. Conversely, for every \(\mu>0\) and \(\kappa\in[4/3,5/3)\), these formulas produce a unique \(R>0\) and \(z\in[-1,1)\), proving sufficiency as well as necessity. Holding \(\mu\) fixed while varying \(t\) in this interval shows that one moment is not enough.

**Step 3: sharp global stability of the cut height.** For \(0\le s<t<1/2\), let \(z(t)=(3t-1)/(1-t)\), \(k(t)=4(1+t^2)/3\). Direct subtraction yields
\[
\frac{z(t)-z(s)}{\sqrt{k(t)-k(s)}}
=\frac{\sqrt3}{(1-t)(1-s)}\sqrt{\frac{t-s}{t+s}}.
\]
Since \(s+t<1\),
\[
(t+s)(1-s)^2-(t-s)
=s\bigl(2(1-t-s)+s(t+s)\bigr)\ge0.
\]
Therefore the square-root factor is at most \(1-s\), and the displayed quotient is bounded by \(\sqrt3/(1-t)\le2\sqrt3\). Exchanging the two caps if needed gives the asserted bound. Setting \(s=0\) and taking \(t\uparrow1/2\) makes the quotient tend to \(2\sqrt3\), so the constant is the best possible. With \(s=0\) and \(t\downarrow0\), \(z(t)-z(0)\) is linear in \(t\) but \(k(t)-k(0)\) is quadratic, forbidding every larger Hölder exponent.

**Step 4: optimal quarter-power angular stability.** For \(0\le\beta\le\alpha\le\pi\), elementary trigonometry gives
\[
|\cos\alpha-\cos\beta|\ge 1-\cos(\alpha-\beta)
=2\sin^2\left(\frac{\alpha-\beta}{2}\right)
\ge\frac{2(\alpha-\beta)^2}{\pi^2}.
\]
(The cosine difference is smallest, for fixed angular separation, when an endpoint is a pole.) Thus \(|\alpha_1-\alpha_2|\le\pi\sqrt{|z_1-z_2|/2}\), which combined with Step 3 gives the asserted quarter-power bound. Finally put \(\alpha=\pi-\varepsilon\). Then \(z=-\cos\varepsilon=-1+\varepsilon^2/2+O(\varepsilon^4)\), so
\[
t=\frac{z+1}{z+3}=\frac{\varepsilon^2}{4}+O(\varepsilon^4),\qquad
\kappa-\frac43=\frac43t^2=\frac{\varepsilon^4}{12}+O(\varepsilon^6).
\]
The opening angle changes by \(\varepsilon\) while the normalized moment ratio changes only to fourth order. By choosing \(R\) using the inversion formula at a common prescribed \(\mu\), this counterfamily also has an identical first squared-distance moment. Hence no exponent greater than \(1/4\) can hold uniformly for the opening angle as a function of the first two even moments. This completes the proof.

## Verification

The standalone `verify_cap.py` uses only Python's standard library. Run `python3 verify_cap.py` in the same directory as this document. It checks 2,206 exact rational moment, inverse, and stability comparisons, and independently integrates the original four-variable pair-distance integrand on deterministic surface grids for five nondegenerate or complete caps. It checks 10 direct numerical quadrature comparisons and additionally checks the quarter-power expansion at four angular deficits. A successful run prints `VERIFY_OK`. These tests do not prove universal statements; Steps 1–4 do.

## Relationship to prior work

Sidiropoulos (arXiv:1411.5639v1, November 20, 2014) develops the full-sphere random-chord law in arbitrary ambient dimension, including full-sphere moment formulas. The endpoint \(z=-1\) here is therefore previously available forward information, not an originality claim. The full text, including Sections II–IV and Propositions III.2–III.3, was checked.

Moseeva, Tarasov and Zaporozhets (arXiv:2007.07297v1, July 14, 2020) develop a forward law for geodesic distances of two uniform points in a spherically convex body; their spherical-cap corollary treats angular caps of radius below \(\pi/2\). Their result is richer forward distributional information for a prescribed cap, and Euclidean chord distance is a monotone transformation of spherical distance. It does not state the present two-even-moment inverse classification, its sharp feasible moment wedge, or its two optimal inverse exponents. Sections 1–3, including the cap corollary and its proof discussion, were inspected. An unrecognized earlier inverse deduction remains a historical-priority risk.

## Limitations

This is a two-dimensional spherical-surface cap theorem. It is not an inverse theorem for arbitrary spherical patches, higher-dimensional sphere caps, uniform *solid* caps, or intrinsic geodesic distance moments. Radius recovery from noisy data is not uniformly well-conditioned when the cap shrinks to zero area; no statistical confidence bounds are established. The global constant for the angular quarter-power inequality is not proved optimal. Historical novelty has only a literature comparison, not independent certification.

## References

1. P. Sidiropoulos, *N-sphere chord length distribution*, arXiv:1411.5639v1 (first posted 2014-11-20). https://arxiv.org/abs/1411.5639
2. T. Moseeva, A. Tarasov and D. Zaporozhets, *Random sections of spherical convex bodies*, arXiv:2007.07297v1 (first posted 2020-07-14). https://arxiv.org/abs/2007.07297
