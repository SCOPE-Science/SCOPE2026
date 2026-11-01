# The three-phase Löwner ellipsoid of an axially spiked cube

## Finding

Fix an integer \(d\ge2\) and a real parameter \(a\ge1\). Let
\[
K_{d,a}=\operatorname{conv}\bigl([-1,1]^d\cup\{a e_1\}\bigr)\subset\mathbb R^d.
\]
For a center \(c e_1\) and positive axial/transverse semiaxes \(b,r\), write
\[
E(c;b,r)=\left\{(x_1,x_\perp):\frac{(x_1-c)^2}{b^2}+\frac{\|x_\perp\|_2^2}{r^2}\le1\right\}.
\]
The **unique minimum-volume enclosing Euclidean ellipsoid** (Löwner ellipsoid) of \(K_{d,a}\) is \(E(c;b,r)\) with the following exact parameters:
\[
\boxed{\begin{array}{c|ccc}
\text{range}&c&b&r\\ \hline
1\le a\le\sqrt d&0&\sqrt d&\sqrt d\\[3pt]
\sqrt d\le a\le d&0&a&a\sqrt{\dfrac{d-1}{a^2-1}}\\[7pt]
a\ge d&\dfrac{a-d}{d+1}&\dfrac{d(a+1)}{d+1}&\dfrac d{\sqrt{d+1}}
\end{array}}
\]
The formulas coincide at both thresholds. Denoting the volume of the Euclidean unit ball by \(\kappa_d\), the normalized minimum volume is
\[
\boxed{\frac{\operatorname{vol}_d E(c;b,r)}{\kappa_d}=br^{d-1}=
\begin{cases}
d^{d/2}, &1\le a\le\sqrt d,\\
a^d\bigl((d-1)/(a^2-1)\bigr)^{(d-1)/2}, &\sqrt d\le a\le d,\\
d^d(a+1)/(d+1)^{(d+1)/2},&a\ge d.
\end{cases}}
\]
The volume profile is continuously differentiable but not twice continuously differentiable at either \(a=\sqrt d\) or \(a=d\). For \(a>d\), the cone apex \(a e_1\) and every vertex of the negative facet \(\{-1\}\times\{-1,1\}^{d-1}\) contact the ellipsoid, whereas **every vertex of the positive facet is strictly interior to it**. This screening happens even though all original cube vertices remain vertices of \(K_{d,a}\). At \(a=d\) the positive facet vertices also contact; throughout \(\sqrt d\le a\le d\), all cube vertices contact. For \(a<\sqrt d\), only the cube vertices contact among this set of generators, and the apex lies inside the circumball.

## Assumptions and scope

The ambient metric and volume are the standard Euclidean ones; a zero-volume limiting ellipsoid is inadmissible. The convex body is the full-dimensional convex hull of an axis-aligned cube and the additional point \(a e_1\), not a truncation of the cube or a body obtained by perturbing every vertex. No assumption of axial symmetry is imposed on alternative enclosing ellipsoids. The parameter includes both transition values and \(a=1\), where the extra point belongs to the original cube. Uniqueness is uniqueness among **all** positive definite enclosing ellipsoids.

## Proof

**Step 1: A global Löwner contact criterion.** Suppose \(X\subset B_2^d\) and a probability measure on \(X\cap\partial B_2^d\) has mean zero and covariance \(I_d/d\). For any ellipsoid \(F=\{z:(z-v)^\top Q^{-1}(z-v)\le1\}\) containing \(X\), averaging the defining inequality gives
\[
\frac1d\operatorname{tr}(Q^{-1})+v^\top Q^{-1}v\le1.
\]
The arithmetic--geometric mean inequality on the eigenvalues of \(Q^{-1}\) now gives \(\det Q\ge1\), with equality only for \(Q=I_d\) and \(v=0\). Thus the ball is the unique minimum-volume enclosing ellipsoid of \(X\). Affine transformation proves the analogous criterion for any proposed \(E(c;b,r)\); it suffices to exhibit a probability measure supported on **actual touching generators** of the proposed ellipsoid whose transformed mean is zero and covariance is \(I_d/d\). Since an ellipsoid is convex, inclusion of all the cube vertices and apex proves inclusion of \(K_{d,a}\).

**Step 2: Small spike.** If \(1\le a\le\sqrt d\), the ball \(\sqrt d B_2^d\) contains all cube vertices (at distance \(\sqrt d\)) and the apex (at distance \(a\)). Put uniform mass on the \(2^d\) cube vertices. Under normalization by \(\sqrt d\), this measure has mean zero and covariance \(I_d/d\). Step 1 proves the first formula. The apex first touches at \(a=\sqrt d\).

**Step 3: Centered anisotropic phase.** Suppose \(\sqrt d\le a\le d\) and take \(c=0\), \(b=a\), \(r=a\sqrt{(d-1)/(a^2-1)}\). Each cube vertex satisfies
\[
\frac1{a^2}+\frac{d-1}{r^2}=1,
\]
and the apex satisfies \(a^2/b^2=1\), so all generators are on the ellipsoid. Put
\[
p=\frac{a^2-d}{d(a^2-1)},\qquad q=\frac{(d-1)a^2}{d(a^2-1)},\qquad m=-\frac{a^2-d}{a(d-1)}.
\]
These satisfy \(p+q=1\), \(p,q\ge0\), and \(-1\le m\le0\) exactly within the specified range. Give probability \(p\) to the apex; with probability \(q\), choose a cube vertex whose first sign \(\sigma\in\{-1,+1\}\) has mean \(m\), while the remaining \(d-1\) signs are independent unbiased Rademacher variables. Under the affine normalization \((x_1,x_\perp)\mapsto(x_1/a,x_\perp/r)\), the mean vanishes because \(p+qm/a=0\). The axial and transverse second moments are, respectively,
\[
p+\frac q{a^2}=\frac1d,\qquad\frac q{r^2}=\frac1d.
\]
All cross-moments vanish by independence and symmetry. The normalized contact covariance is therefore exactly \(I_d/d\), and Step 1 proves optimality and uniqueness without restricting competitors to rotationally symmetric ellipsoids. At \(a=\sqrt d\), \(p=0\); at \(a=d\), \(m=-1\), so only the negative facet receives cube-vertex mass. Both endpoints are covered.

**Step 4: Translated phase and exact screening.** For \(a\ge d\), choose
\[
c=\frac{a-d}{d+1},\qquad b=\frac{d(a+1)}{d+1},\qquad r=\frac d{\sqrt{d+1}}.
\]
After transforming by \((x_1,x_\perp)\mapsto((x_1-c)/b,x_\perp/r)\), the apex has axial coordinate \(+1\). Every vertex of the negative cube facet has axial coordinate \(-1/d\), transverse coordinates \(\pm\sqrt{d+1}/d\), and squared norm
\[
\frac1{d^2}+(d-1)\frac{d+1}{d^2}=1.
\]
Give probability \(1/(d+1)\) to the apex and distribute the remaining \(d/(d+1)\) uniformly over negative-facet cube vertices. Its normalized axial mean is \(\frac1{d+1}-\frac d{d+1}\frac1d=0\); its axial second moment equals \(1/(d+1)+1/[d(d+1)]=1/d\); each transverse second moment is \([d/(d+1)]\cdot[(d+1)/d^2]=1/d\), with zero cross-moments. Step 1 proves global minimality. For a positive-facet vertex the axial coordinate is \((1-c)/b\), while for negative-facet vertices it is \((-1-c)/b=-1/d\). As \(c>0\) when \(a>d\), one has \(|1-c|<1+c\). Hence every positive-facet vertex has strictly smaller ellipsoidal norm than one and lies strictly inside. At \(a=d\), \(c=0\), so they also touch. This verifies the complete generator-contact classification.

**Step 5: Volume and sharp differentiability.** The shape matrix has determinant \(b^2r^{2d-2}\), so the displayed volume is exactly \(\kappa_dbr^{d-1}\). Elementary substitution shows continuity at both thresholds, and differentiation shows the logarithmic volume has matching first derivatives. On the middle branch, writing \(L=\log(br^{d-1})\),
\[
L'(a)=\frac{a^2-d}{a(a^2-1)}.
\]
On the lower and upper branches these derivatives are \(0\) and \(1/(a+1)\), respectively. Their values agree at \(a=\sqrt d\) and \(a=d\). But the second-derivative jumps are
\[
L''(\sqrt d+)-L''(\sqrt d-)=\frac2{d-1}>0,
\quad L''(d-)-L''(d+)=\frac1{d(d^2-1)}>0.
\]
Because the volume is positive and its first derivative is continuous, its second derivative also has a genuine jump at each threshold. This completes the proof.

## Verification

The standalone `verify.py` reproduces the three formulas, exact contact probabilities, normalizations, and covariance identities numerically for 989 dimension--spike configurations, then performs 70 independently initialized numerical convex-optimization comparisons over enclosing axially symmetric ellipsoids. The recorded maximum logarithmic volume discrepancy was \(8.82\times10^{-12}\). The test is run with `python3 verify.py` and requires Python, NumPy and SciPy. These finite tests verify implementation consistency only. The **infinite-parameter correctness and unrestricted ellipsoid optimality** follow from the explicit Step 1 contact certificates and direct algebra in Steps 2--5, not the numerical solver.

## Relationship to prior work

The Löwner--John contact theorem is classical; Martin Henk's survey supplies an affine-invariant proof framework and the cube's unspiked circumball. Sun and Freund study optimization algorithms for general minimum-volume covering ellipsoids, but the inspected general formulation and examples do not give the present closed three-phase cube-with-one-exterior-point classification. Published related geometric calculations include the John ellipsoid of the diagonally capped cube \([0,1]^d\cap\{\sum x_i\le\tau\}\), the enclosing ellipsoid of rank-selected Boolean polytopes, and John/Löwner ellipsoids of isocanted cubes. Their bodies are different: a diagonal **intersection** is not an axial exterior-point **hull**, and an isocanted cube has coordinated difference constraints rather than an extra axial vertex. In particular, the rank-selected Boolean polytopes are hulls of subsets of binary cube vertices, whereas \(K_{d,a}\) has \(2^d+1\) vertices whenever \(a>1\). Those prior results do not algebraically imply the new ellipsoid, thresholds or screening. The origin-polar of the spiked cube is a one-sided coordinate-clipped crosspolytope, but polar duality for **translated** ellipsoids does not by itself give the stated Löwner minimization or the contact transition. The intrinsic general theory plus generic optimization algorithms are not the present exact evaluation.

## Limitations

Only the Euclidean coordinate-axis spike of a Euclidean cube is treated, not an arbitrary spike direction, an offset noncentral box, arbitrary polytopes or John inscribed ellipsoids. No extension to non-Euclidean metrics is claimed. The literature investigation identifies no matching full classification in the inspected sources or relevant mathematical research records, but cannot rule out an earlier result under different terminology or in unindexed optimal-design tables. The numerical checks are noncertifying corroboration. Independent scholarly historical-priority and proof review have not been performed.

## References

1. Martin Henk, *Löwner--John ellipsoids*, Documenta Mathematica, Extra Volume ISMP (2012), Theorem 2.1, available at https://ems.press/books/dms/251/4926. Survey of global contact certificates and the cube example.
2. Peng Sun and Robert M. Freund, *Computation of Minimum Volume Covering Ellipsoids*, Optimization Online, first public 2002-07-31; https://optimization-online.org/2002/07/516/. General optimization algorithms and examples, not an exact parameter classification of the above family.
3. *Three-phase John ellipsoid of a capped hypercube*, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-three-phase-john-ellipsoid-of-a-capped-hypercube--9b8726b32127. Different diagonal-truncation body.
4. *Exact Löwner ellipsoids of arbitrary rank-selected Boolean polytopes*, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-l-wner-ellipsoids-of-arbitrary-rank-selected-boolean-polyt--3c04f47dc8c3. Different binary-vertex families.
5. *Parity-sharp Löwner contact transitions and pole avoidance for isocanted cubes*, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-parity-sharp-l-wner-contact-transitions-and-pole-avoidance-for-i--c0498570052b. Related but different difference-constrained cubes.
