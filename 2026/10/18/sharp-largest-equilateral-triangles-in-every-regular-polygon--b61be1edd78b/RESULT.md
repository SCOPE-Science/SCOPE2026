# Sharp largest equilateral triangles in every regular polygon

## Finding

For every integer \(m\ge3\), let
\[
P_m=\operatorname{conv}\{(\cos(2\pi j/m),\sin(2\pi j/m)):j=0,\ldots,m-1\}.
\]
Let \(R_m\) be the greatest circumradius of an equilateral triangle \(T\subseteq P_m\), allowing arbitrary translations, rotations, and points of contact. Then
\[
R_m=\begin{cases}
1,&3\mid m,\\[3pt]
\displaystyle\frac{\cos(\pi/m)-\cos((2q+1)\pi/m)}{\cos(\pi/(3m))-\cos((2q+1)\pi/m)},&3\nmid m,\ q=\lfloor(m-1)/3\rfloor.
\end{cases}
\]
When \(3\nmid m\), equality holds for exactly \(m\) geometric triangles, forming one orbit under the rotational symmetries of \(P_m\). Representatives are
\[
T_0=\operatorname{conv}\{(1,0),\ (1-3R_m/2,\sqrt3 R_m/2),\ (1-3R_m/2,-\sqrt3 R_m/2)\}.
\]
When \(3\mid m\), equality holds for exactly \(m/3\) geometric triangles, each formed by three vertices spaced \(m/3\) steps apart. Accordingly the sharp area is \(3\sqrt3 R_m^2/4\) in every case. Equivalently, the least circumradius of a regular \(m\)-gon (freely placed) containing an equilateral triangle of circumradius one is \(1/R_m\).

## Assumptions and scope

All polygons and triangles are ordinary closed Euclidean convex sets in the plane. The integer \(m\) is arbitrary at least three. The containing polygon has circumradius one, and the inscribed triangle is required to be equilateral but is otherwise unconstrained; degenerate triangles are irrelevant. Similarity gives the formulas for other circumradii. The classification counts subsets of the plane, not ordered vertex labels or orientations.

Set \(\alpha=\pi/m\), \(\delta=\alpha/3\), \(a=\cos\alpha\). When \(3\nmid m\), set
\[
q=\lfloor(m-1)/3\rfloor,\quad \beta=(2q+1)\alpha=2\pi/3+s\delta,\quad
s=\begin{cases}1,&m\equiv1\pmod3,\\-1,&m\equiv2\pmod3.\end{cases}
\]
Thus \(m\ge4\), \(\beta\in[3\pi/5,3\pi/4]\) and \(\cos\beta<0\). Write \(r=(a-\cos\beta)/(\cos\delta-\cos\beta)\), \(c=1-r=(\cos\delta-a)/(\cos\delta-\cos\beta)\). Both \(r\) and \(c\) are positive, with \(r<1\).

## Proof

**Case \(3\mid m\).** An equilateral triangle with center \(z\), circumradius \(\rho\), and unit vertex rays \(v_0,v_1,v_2\) has \(\sum_jv_j=0\), hence
\[
\frac13\sum_{j=0}^2\lVert z+\rho v_j\rVert^2=\lVert z\rVert^2+\rho^2.
\]
Since \(P_m\) lies in the unit disk, \(\rho\le1\). Equality forces \(z=0\) and all vertices on the unit circle; the only such points of \(P_m\) are its polygon vertices. Exactly \(m/3\) vertex triples have the required angular separations.

**Reduction to an orientation interval for \(3\nmid m\).** Write a candidate as \(\operatorname{conv}\{z+\rho v_j(\theta):j=0,1,2\}\), where \(v_j(\theta)=(\cos(\theta+2\pi j/3),\sin(\theta+2\pi j/3))\). Because rotating \(P_m\) by \(2\pi/m\) and cyclically relabeling triangle vertices preserves the optimization, and \(\gcd(m,3)=1\), orientation is defined modulo \(2\pi/(3m)=2\delta\); polygon reflection maps \(\theta\) to \(-\theta\). It therefore suffices to study \(0\le\theta\le\delta\).

The polygon is the intersection of the halfplanes with outward unit normals \(u_k=(\cos((2k+1)\alpha),\sin((2k+1)\alpha))\) and support value \(a\). If \(H_k(\theta)=\max_j u_k\cdot v_j(\theta)\), then containment is exactly
\[
u_k\cdot z+\rho H_k(\theta)\le a\qquad(k=0,\ldots,m-1).
\]
Within the reduced orientation interval, the four normals at angles \(\pm\alpha\) and \(\pm\beta\) have triangle support values respectively \(\cos(\alpha\mp\theta)\) and \(\cos(s\delta\mp\theta)\). These identities hold at the interval endpoints as well.

**A balanced-normal upper certificate.** Define
\[
L=-\frac{\cos\alpha}{\cos\beta}>0,\quad
D=-\frac{\sin\alpha}{\sin\beta}<0,\quad
\lambda_+=(L+D)/2,\quad\lambda_-=(L-D)/2.
\]
Since \(\alpha+\beta\le\pi\), \(L\ge|D|\); thus both \(\lambda_\pm\ge0\), and direct trigonometry gives
\[
u(\alpha)+\lambda_+u(\beta)+\lambda_-u(-\beta)=0,
\]
where \(u(\psi)=(\cos\psi,\sin\psi)\). Weighting the corresponding containment inequalities eliminates the free center \(z\). Reflection gives another such certificate, and together they imply
\[
\rho\,[A\cos\theta+B\sin\theta]\le a(1+L),\qquad 0\le\theta\le\delta,
\]
with
\[
A=\cos\alpha+L\cos\delta>0,
\qquad B=\sin\alpha+sD\sin\delta
=\sin\alpha\left(1-s\frac{\sin\delta}{\sin\beta}\right)>0.
\]
For clarity, the nonreflected weighted sum is \(A\cos\theta+B\sin\theta\), while its reflection is \(A\cos\theta-B\sin\theta\); their maximum gives the displayed bound.

We prove the strict inequality \(B>A\tan(\delta/2)\), uniformly over all admissible integers. The elementary estimate \(\tan(\delta/2)<(51/100)\delta\) holds for \(\delta\le\pi/12\): use \(\sin t\le t\), \(\cos t\ge1-t^2/2\), and \(\pi<22/7\). If \(s=1\), then \(m\ge4\), \(\beta\in(2\pi/3,3\pi/4]\), \(L\le2\), and \(A\le3\). Further,
\[
1-\frac{\sin\delta}{\sin\beta}>\frac58,
\qquad\sin3\delta>\frac83\delta,
\]
from \(\delta\le\pi/12\), \(\sin\beta\ge\sqrt2/2\), and monotonicity of \(\sin t/t\). Therefore \(B>5\delta/3>3(51/100)\delta>A\tan(\delta/2)\). If \(s=-1\), then \(m\ge5\), \(\delta\le\pi/15\), \(L\le1+\sqrt5\), \(A\le2+\sqrt5\), and
\[
B>\sin3\delta\ge\frac{15\sin(\pi/5)}\pi\delta>\frac{14}5\delta
>(2+\sqrt5)\frac{51}{100}\delta>A\tan(\delta/2).
\]
The last strict numerical-free comparisons follow directly from \(\sin(\pi/5)=\sqrt{10-2\sqrt5}/4\) and \(\pi<22/7\).

Consequently, for every \(0<\theta\le\delta\),
\[
A\cos\theta+B\sin\theta-A
=2\sin(\theta/2)[B\cos(\theta/2)-A\sin(\theta/2)]>0.
\]
The upper bound is strictly below its \(\theta=0\) value whenever the orientation is noncanonical. At \(\theta=0\), the bound is
\[
\rho\le\frac{a(1+L)}A
=\frac{a-\cos\beta}{\cos\delta-\cos\beta}=r.
\]

**Construction attaining the bound.** Take center \(z=(c,0)\), triangle circumradius \(r\), and orientation \(\theta=0\). For a unit normal at any angle \(\psi\in[0,\pi/3]\), the triangle support plus center contribution equals \((c+r)\cos\psi=\cos\psi\). Every polygon normal in this sector satisfies \(\psi\ge\alpha\), so its support does not exceed \(a\).

For \(\psi\in[\pi/3,\pi]\), the corresponding expression is
\[
f(\psi)=c\cos\psi+r\cos(\psi-2\pi/3).
\]
This sinusoid has its unique peak in the sector at some angle \(\psi_*\) satisfying
\[
2\pi/3-2\delta<\psi_*<2\pi/3.
\]
Indeed, \(f'(2\pi/3)=-c\sin(2\pi/3)<0\), while \(f'(2\pi/3-2\delta)>0\) is equivalent to
\[
2\sin\delta\sin(2\pi/3-2\delta)<a-\cos\beta.
\]
The left side is at most \(2\sin(\pi/12)<1\); the right is at least \(\cos(\pi/4)-\cos(3\pi/5)>1\). The polygon normals are spaced by \(2\alpha=6\delta\). If \(s=1\), the midpoint of the two normals adjacent to \(\beta=2\pi/3+\delta\) on its preceding side is \(2\pi/3-2\delta\); if \(s=-1\), the midpoint on its following side is \(2\pi/3+2\delta\). Hence \(\beta\) is the unique polygon-normal angle closest to \(\psi_*\) in this sector. Because \(f(\psi)=\lVert (c,0)+r v_1(0)\rVert\cos(\psi-\psi_*)\), its maximum over the sector's discrete polygon normals occurs at \(\beta\). At that normal, \(f(\beta)=c\cos\beta+r\cos\delta=a\) by definition of \(r\). Reflection about the horizontal axis covers negative normal angles. This proves \(T_0\subseteq P_m\) with sharp circumradius \(r\).

**All equality cases.** Strictness of the angular certificate forces every maximizer, after a symmetry of \(P_m\), to have \(\theta=0\) and radius \(r\). Write its center as \((x,y)\). The two constraints at \(\pm\alpha\) yield \(x\le c-|y|\tan\alpha\). The two constraints at \(\pm\beta\), since \(\cos\beta<0\), yield \(x\ge c+|y|\sin\beta/|\cos\beta|\). Thus \(y=0\) and \(x=c\), so its triangle is exactly \(T_0\). The rotational orbit contains precisely \(m\) distinct triangles: if a nontrivial polygon rotation stabilizes an equilateral triangle, it must be a rotation by \(2\pi/3\) or \(4\pi/3\), impossible for \(3\nmid m\). This proves the classification and both area and inverse-circumscription statements.

## Verification

The included standalone `verify.py` uses only the Python standard library. Execute `python verify.py` from a directory containing that extracted file. It tests witness containment and strict angular dual inequalities for every integer from \(4\) through \(300\) not divisible by three; it separately solves independent three-variable linear-programming vertices at 80 small-polygon/orientation instances. Expected output:

`VERIFY_OK analytic_witness_cases=198 independent_LP_orientations=80`

The finite checks are diagnostics only: the result for all integers and all triangle placements is established by the analytical inequalities above, not by extrapolation from sampled instances.

## Relationship to prior work

Mathar's *Tightly Circumscribed Regular Polygons* (arXiv:1301.6293v1, first public January 26, 2013) computes concentric packing ratios, allows concentric rotations, and, in Section IV, exhibits small translated-center examples for triangle–quadrilateral and triangle–pentagon placements; it explicitly leaves comprehensive joint translation-and-rotation treatment aside. In contrast, this result gives one sharp arbitrary-placement formula and exact equality count for every number of sides. The triangle–square and triangle–pentagon numerical optima are not claimed as new standalone cases.

DePano, Ke, and O'Rourke (1987) give a general algorithm for largest inscribed equilateral triangles in arbitrary polygons; such an algorithm establishes computability, but the accessible bibliographic evidence does not give this exact uniform regular-polygon expression or its classification. Their full text was not available for inspection, so an equivalent result therein is a genuine historical-priority risk. A 2017 online discussion proposes a geometric construction for regular polygons without presenting an all-side-count theorem or rigorous global optimality argument; it remains a further comparison risk. General optimization algorithms, special configurations, and this complete explicit theorem are different levels of mathematical coverage.

## Limitations

The statement is Euclidean and only treats equilateral triangles and regular containing polygons, not other equiangular/affine classes or arbitrary convex polygons. The closed form is a sharp universal theorem, not a claim of an independently audited or externally certified result. The most relevant 1987 algorithm paper could not be inspected in full, and a 2017 construction claim creates residual historical-priority uncertainty; originality is therefore assessed provisionally on inspected material.

## References

1. R. J. Mathar, *Tightly Circumscribed Regular Polygons*, arXiv:1301.6293v1 (first public January 26, 2013), https://arxiv.org/html/1301.6293v1, especially Sections II–IV.
2. A. DePano, Y. Ke, and J. O'Rourke, *Finding Largest Inscribed Equilateral Triangles and Squares*, Proc. 25th Allerton Conference on Communication, Control and Computing (1987), 869–878. Cited via https://math.stackexchange.com/questions/883050/largest-equilateral-triangle-in-a-polygon and later computational-geometry bibliographies; primary full text unavailable for inspection.
3. *Largest Equilateral Triangle in a Polygon*, Mathematics Stack Exchange discussion, posted 2014; a purported regular-polygon construction posted August 12, 2017, https://math.stackexchange.com/questions/883050/largest-equilateral-triangle-in-a-polygon.
