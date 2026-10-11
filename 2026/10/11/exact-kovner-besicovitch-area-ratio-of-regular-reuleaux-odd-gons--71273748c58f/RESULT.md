# Exact Kovner–Besicovitch area ratio of regular Reuleaux odd-gons

## Finding
For each odd integer \(n\ge3\), write
\[r_n=\frac{1}{2\cos(\pi/(2n))},\qquad v_j=r_n(\cos(2\pi j/n),\sin(2\pi j/n)),\quad 0\le j<n,\]
and let \(K_n=\bigcap_{j=0}^{n-1}B(v_j,1)\) be the regular Reuleaux \(n\)-gon of width one, centered at the origin. The Kovner–Besicovitch area ratio is
\[\beta(K)=\frac{1}{\operatorname{area}(K)}\sup\{\operatorname{area}(C):C\subseteq K,\ C\text{ a centrally symmetric convex body}\}.\]
For each integer \(k\ge3\) and \(0<r<1\), define
\[F(k,r)=k\left[\frac\pi k+\frac{r^2}{2}\sin\frac{2\pi}k-r\sin\frac\pi k\sqrt{1-r^2\sin^2\frac\pi k}-\arcsin\left(r\sin\frac\pi k\right)\right].\]
Then
\[\boxed{\beta(K_n)=\frac{F(2n,r_n)}{F(n,r_n)}}\]
for every odd \(n\ge3\). The maximum is attained by the centered reflected intersection \(K_n\cap(-K_n)\), which is the intersection of \(2n\) equally spaced unit disks. Furthermore \(\beta(K_n)<1\) and
\[\boxed{\beta(K_n)=1-\frac{\pi^2}{8n^2}-\frac{25\pi^4}{1536n^4}+O(n^{-6})}\]
as odd \(n\to\infty\). Numerically, the ratio is about \(0.840342603\) at \(n=3\) and \(0.947986295\) at \(n=5\).

## Assumptions and scope
The disks are closed Euclidean unit disks; the generating vertices have circumradius \(r_n\), so the farthest pair of generating vertices is at distance one. This is the standard constant-width-one regular Reuleaux polygon. Its exact area is positive, and the area ratio does not change under a common positive scaling. The theorem applies to every odd \(n\ge3\) without limiting assumptions on its size. It makes no uniqueness claim about the center of a largest centrally symmetric subset, nor any extremality claim among irregular Reuleaux polygons.

## Proof
**1. A maximizing center can be placed at the dihedral center.** Let \(K\) be any planar convex body, and put \(C_c=K\cap(2c-K)\) for \(c\in K\). Any centrally symmetric convex subset of \(K\) with center \(c\) lies in \(C_c\). For \(c,d\in K\) and \(0\le t\le1\), convexity of \(K\) gives
\[tC_c+(1-t)C_d\subseteq C_{tc+(1-t)d}.\]
The planar Brunn–Minkowski inequality therefore makes \(c\mapsto\operatorname{area}(C_c)^{1/2}\) concave on \(K\). For \(K_n\), rotation by \(2\pi/n\) preserves this function. Average the orbit of any center over all \(n\) rotations: its barycenter is the origin. Concavity implies \(\operatorname{area}(C_0)\ge\operatorname{area}(C_c)\), so \(K_n\cap(-K_n)\) maximizes area. Compactness of \(K_n\) ensures a maximum also exists, though the inequality already identifies one.

**2. The symmetric kernel is an equally spaced disk intersection.** Reflection negates each generating circle center. Since \(n\) is odd, the \(2n\) centers \(\{v_j,-v_j\}\) are all distinct and uniformly spaced on the circle of radius \(r_n\). Thus
\[K_n\cap(-K_n)=\bigcap_{j=0}^{2n-1}B\left(r_n(\cos(\pi j/n),\sin(\pi j/n)),1\right).\]
Define \(D_{k,r}\) as the intersection of unit disks whose \(k\) centers are equally spaced on the circle of radius \(r<1\). For a ray at an angular displacement \(\delta\) from the antipode of the farthest disk center, where \(|\delta|\le\pi/k\), the active disk constraint is
\[s^2+r^2+2rs\cos\delta\le1.\]
Indeed its center has the least scalar product with the ray, hence gives the greatest distance at each \(s\ge0\). Solving the quadratic yields the boundary radius
\[s(\delta)=-r\cos\delta+\sqrt{1-r^2\sin^2\delta}.\]
Integrate in \(k\) equal angular sectors:
\[\operatorname{area}(D_{k,r})=k\int_0^{\pi/k}s(\delta)^2\,d\delta=F(k,r).\]
To evaluate the integral, expand \(s^2=1+r^2\cos(2\delta)-2r\cos\delta\sqrt{1-r^2\sin^2\delta}\), then substitute \(u=r\sin\delta\) in the last term. Taking \((k,r)=(n,r_n)\) and \((2n,r_n)\) proves the quotient.

**3. Strictness and asymptotics.** Since \(r_n>1/2\), each generating vertex \(v_j\) belongs to \(K_n\) but violates the additional reflected disk \(B(-v_j,1)\), because \(2r_n>1\). Thus the centered kernel is a proper convex subset with strictly smaller area. For asymptotics, put \(z=\pi/(2n)\) and \(r_n=1/(2\cos z)\). Taylor expansion of the exact elementary formula gives
\[F(n,r_n)=\frac\pi4-\frac{\pi}{12}z^2-\frac\pi{30}z^4+O(z^6),\]
\[F(2n,r_n)=\frac\pi4-\frac{5\pi}{24}z^2-\frac{109\pi}{1920}z^4+O(z^6).\]
Both admit even convergent local Taylor expansions because all radical and inverse-sine arguments remain inside their domains near \(z=0\). Their quotient is
\[1-\frac12z^2-\frac{25}{96}z^4+O(z^6),\]
which is the claimed formula after replacing \(z\).

## Verification
The standalone standard-library script `verify.py` independently computes intersection areas by sampling rays and, on each ray, enforcing **all** disk inequalities rather than assuming which disk is active. It checks the analytic area formula at odd orders \(3,5,7,11\), independently evaluates displaced reflected overlaps, verifies the Reuleaux-triangle area benchmark, and tests the predicted asymptotic on larger orders. Running `python3 verify.py` produces `VERIFY_OK`. The proof above does not rely on finite numerical samples, and a finite integration mesh alone is not an exhaustive proof.

## Relationship to prior work
Harrell's 2000 direct proof of the Blaschke–Lebesgue theorem studies minimizing area among planar constant-width bodies and discusses regular Reuleaux odd-gons, not the maximizing centrally symmetric **subset** area. The classical Kovner–Besicovitch measure is precisely the largest centrally symmetric inner-area fraction; the Reuleaux-triangle extremal case is known and is not claimed here as original. Groemer and Wallen's 2001 diameter-bisection ratio and Jin and Guo's 2011 Minkowski dilation measure are distinct notions of asymmetry. In particular, neither their area-split bound nor their Minkowski scaling coefficient determines the present inner-area fraction. An earlier exact Kovner–Besicovitch formula for straight-edged regular polygons likewise does not cover the circular-arc disk intersections here. A 1951 Besicovitch article on constant-width asymmetry remains inaccessible and historically relevant. Guo and Jin (2017, introduction and reference 10) explicitly identify Jin (2016) as studying the different Lu–Pan boundary-perimeter asymmetry, although the 2016 primary full text was not directly accessible.

## Limitations
The theorem is for **regular** Euclidean Reuleaux odd-gons. It does not rank irregular Reuleaux polygons by this measure or establish monotonicity in polygon order. The three-sided case is included to reproduce a known benchmark rather than to claim historical priority. The proof is an analytic derivation and has undergone only same-model review, not independent validation. The full 1951 Besicovitch paper and the 2016 Jin primary text were unavailable; a later coauthored primary paper identifies the latter's measure as Lu–Pan perimeter asymmetry. Such indirect comparison and search absence cannot establish historical priority.

## References
1. Evans M. Harrell II, *A direct proof of a theorem of Blaschke and Lebesgue*, arXiv:math/0009137, first posted 14 September 2000, https://arxiv.org/abs/math/0009137.
2. A. S. Besicovitch, *Measure of Asymmetry of Convex Curves (II): Curves of Constant Width*, J. London Math. Soc. 26 (1951), 81–93, https://doi.org/10.1112/jlms/s1-26.2.81. Full text not inspected.
3. H. Groemer and L. J. Wallen, *A Measure of Asymmetry for Domains of Constant Width*, Beiträge zur Algebra und Geometrie 42 (2001), 517–521, https://eudml.org/doc/230091.
4. Hailin Jin and Qi Guo, *On a measure of asymmetry for Reuleaux polygons*, J. Geom. 102 (2011), 73–79, https://doi.org/10.1007/s00022-011-0096-9.
5. Hailin Jin, *Asymmetry of Reuleaux polygons*, Beiträge zur Algebra und Geometrie 58 (2017), 311–317, first published 14 September 2016, https://doi.org/10.1007/s13366-016-0318-2. Only title and abstract inspected.
6. PengZhan Guo and HaiLin Jin, *Groemer–Wallen measure of asymmetry for Reuleaux polygons*, Journal of Geometry 108 (2017), 879–884, https://doi.org/10.1007/s00022-017-0382-2. Full author-supplied text inspected; its introduction identifies Jin (2016) as addressing the Lu–Pan measure.
