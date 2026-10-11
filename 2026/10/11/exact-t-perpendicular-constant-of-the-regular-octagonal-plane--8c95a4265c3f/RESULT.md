# Exact T-perpendicular constant of the regular octagonal plane
## Finding
Let \(X_8=(\mathbb R^2,N)\), where
\[
N(s,t)=\max\left\{|s|,|t|,\frac{|s|+|t|}{\sqrt2}\right\}.
\]
For Birkhoff orthogonality \(x\perp_B y\), Ahmad, Xie and Li define
\[
T_{\perp}(X)
=
\sup\left\{
\sqrt{\|x+y\|\,\|2x-y\|}:
 x,y\in S_X,\ x\perp_B y
\right\}.
\]
For the regular octagonal plane,
\[
T_{\perp}(X_8)=\sqrt{\frac{12+11\sqrt2}{8}}.
\]
Numerically, this is approximately \(1.855948180381932\).

One maximizing pair is
\[
x=(1,\sqrt2-1),
\qquad
y=\left(-\frac{\sqrt2-1}{2},1\right).
\]

## Assumptions and scope
All scalars are real. Put
\[
a=\sqrt2-1.
\]
The unit sphere of \(X_8\) is the regular octagon with vertices
\[
(1,a),\ (a,1),\ (-a,1),\ (-1,a),\ (-1,-a),\ (-a,-1),\ (a,-1),\ (1,-a).
\]
The proof uses the standard support-functional characterization of Birkhoff orthogonality: \(x\perp_B y\) if and only if some norming functional for \(x\) annihilates \(y\).

## Proof
The dihedral isometry group of the regular octagon reduces the first unit vector \(x\) to two types: an interior point of the vertical edge joining \((1,-a)\) to \((1,a)\), or the vertex \((1,a)\).

First suppose
\[
x=(1,t),\qquad -a<t<a.
\]
The unique norming functional is \((s,t)\mapsto s\), so \(x\perp_B y\) forces
\[
y=(0,1)\quad\text{or}\quad y=(0,-1).
\]
For \(y=(0,1)\), direct evaluation of the octagonal norm gives
\[
N(x+y)=\frac{t+2}{\sqrt2},
\]
and
\[
N(2x-y)=
\begin{cases}
\dfrac{3-2t}{\sqrt2},&-a\le t\le \dfrac{3-2\sqrt2}{2},\\[4pt]
2,&\dfrac{3-2\sqrt2}{2}\le t\le a.
\end{cases}
\]
Hence the squared objective is respectively
\[
\frac{(t+2)(3-2t)}2
\quad\text{or}\quad
\sqrt2(t+2).
\]
Their maxima on the indicated intervals are \(49/16\) and \(2+\sqrt2\). The case \(y=(0,-1)\) is the reflected calculation and has the same two maxima. Thus every edge-interior case satisfies
\[
N(x+y)N(2x-y)\le 2+\sqrt2.
\]

Now take the vertex
\[
x=(1,a).
\]
Its norming functionals form the segment joining
\[
f_0(s,t)=s,
\qquad
f_1(s,t)=\frac{s+t}{\sqrt2}.
\]
Therefore \(x\perp_B y\) is equivalent to
\[
y_1(y_1+y_2)\le0.
\]
On the octagonal unit sphere this condition is exactly the union of four line segments. They admit the following parametrizations, together with the corresponding squared objectives \(P=N(x+y)N(2x-y)\):
\[
\begin{array}{c|c|c}
\text{segment for }y&\text{parameter range}&P\\ \hline
(-u,1)&0\le u\le a&\dfrac{(2+u)(1+\sqrt2-u)}{\sqrt2}\\[6pt]
(u,-1)&0\le u\le a&\dfrac{(3+u-\sqrt2)(1+2\sqrt2-u)}2\\[6pt]
(-u,\sqrt2-u)&a\le u\le1/\sqrt2&(2+u)(2\sqrt2-1-u)\\[4pt]
(u,-\sqrt2+u)&a\le u\le1/\sqrt2&(1+u)(3-\sqrt2 u).
\end{array}
\]
The first quadratic has its unique maximum at
\[
u=\frac a2,
\]
and the fourth has its unique maximum at
\[
u=\frac{3-\sqrt2}{2\sqrt2}.
\]
Both maxima are
\[
\frac{12+11\sqrt2}{8}.
\]
The second quadratic is increasing on its interval, while the third is decreasing; each has maximum \(2+\sqrt2\). Finally,
\[
\frac{12+11\sqrt2}{8}-(2+\sqrt2)=\frac{3\sqrt2-4}{8}>0,
\]
and it also exceeds \(49/16\). Therefore
\[
N(x+y)N(2x-y)\le\frac{12+11\sqrt2}{8}
\]
for every Birkhoff-orthogonal unit pair.

At
\[
x=(1,a),
\qquad
y=\left(-\frac a2,1\right),
\]
the two adjacent norming functionals of \(x\) take opposite signs on \(y\), so a convex combination annihilates \(y\) and hence \(x\perp_B y\). The first vertex branch attains
\[
N(x+y)N(2x-y)=\frac{12+11\sqrt2}{8}.
\]
Taking square roots proves the claimed value.

## Verification
The bundled `verify.py` checks, in exact symbolic arithmetic, all one-variable branch formulas used after the dihedral/support-functional reduction. It verifies the edge thresholds and maxima, the two vertex critical points, the common sharp value, and the strict comparison with all subsidiary branch maxima. The continuum reduction itself is analytical: the octagonal boundary has only the edge-interior and vertex support types described in the proof.

## Relationship to prior work
Ahmad, Xie and Li introduced \(T_{\perp}\), proved the universal bounds
\[
\sqrt2\le T_{\perp}(X)\le\sqrt6,
\]
computed the square-plane endpoint \(\sqrt6\), and obtained the Hilbert-space value \(10^{1/4}\). Their concluding discussion explicitly notes that values on further specific spaces remained to be investigated. Their paper does not compute the regular octagonal plane.

The closest exact public computations found in the same geometric-constant literature are the value of the distinct constant \(T_G\) on the regular octagonal plane and the value of \(T_{\perp}\) on the smooth plane \(\ell_3^2\). The first changes the admissibility condition from Birkhoff orthogonality to unit separation, while the second changes the underlying norm, so neither statement implies the present formula.

Several exact constants are already known for this regular octagonal norm, including James-type, von Neumann--Jordan-type, P-angle, Ptolemy, and equilateral-triangle quantities. None of those objectives determines the asymmetric product \(N(x+y)N(2x-y)\) under Birkhoff orthogonality.

## Limitations
The result is an exact benchmark for one canonical polyhedral plane. It does not classify \(T_{\perp}\) for all regular polygonal norms or all symmetric Minkowski planes. The literature search cannot prove absolute novelty, and a differently named equivalent calculation could exist outside the checked sources.

## References
1. A. Ahmad, H. Xie and Y. Li, “Some new geometric constants in Banach spaces,” Advances in Fixed Point Theory 12 (2022), Article 9, doi:10.28919/afpt/7588. Primary classification 46B20.
2. G. Birkhoff, “Orthogonality in linear metric spaces,” Duke Mathematical Journal 1 (1935), 169–172.
