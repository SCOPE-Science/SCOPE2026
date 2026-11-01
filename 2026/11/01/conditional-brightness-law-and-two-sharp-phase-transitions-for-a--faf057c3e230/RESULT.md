# Conditional brightness law and two sharp phase transitions for a regular octahedron

## Finding
Let \(O=\operatorname{conv}\{\pm e_1,\pm e_2,\pm e_3\}\subset\mathbb R^3\), let \(U\) be Haar-uniform on the unit sphere, and let \(B\) be the area of the orthogonal projection of \(O\) onto \(U^\perp\). Set \(M=\max_{1\le i\le3}|U_i|\). The following gives the **complete conditional law of projected area given nearest-axis alignment**, not merely an unconditional mean or silhouette count.

For \(1/\sqrt3<a<1\), set
\[
r=\sqrt{1-a^2},\qquad
q(a)=\begin{cases}
\pi/4-\arccos(a/r),&a<1/\sqrt2,\\
\pi/4,&a\ge1/\sqrt2.
\end{cases}
\]
Then a regular conditional distribution is
\[
\boxed{\displaystyle B\mid(M=a)\ \overset{d}=\ 2a+\bigl(\sqrt2\,r\cos\Psi-a\bigr)_+,\qquad
\Psi\sim\operatorname{Unif}[0,q(a)].}
\tag{1}
\]
Here \(x_+=\max(x,0)\). The two sharp transition values are \(a=1/\sqrt2\) and \(a=\sqrt{2/3}\):

* For \(1/\sqrt3<a\le1/\sqrt2\), the conditional law is purely continuous and is supported on the exact interval
\[
\left[2a+\sqrt{1-2a^2},\ a+\sqrt{2(1-a^2)}\right].
\tag{2}
\]
* For \(1/\sqrt2<a<\sqrt{2/3}\), its support is \([2a,\ a+\sqrt{2(1-a^2)}]\), with a **positive atom at \(2a\)** of mass
\[
\boxed{\displaystyle 1-\frac{\arccos\left(a/\sqrt{2(1-a^2)}\right)}{\pi/4}.}
\tag{3}
\]
* For \(\sqrt{2/3}\le a<1\), the law is exactly the point mass at \(2a\).

For precision, define \(T=\sqrt2 r\) and let \(q=q(a)\). On the interior of the non-atomic portion, the conditional density is
\[
\boxed{\displaystyle f_{B\mid M=a}(z)=\frac{1}{q\sqrt{T^2-(z-a)^2}}.}
\tag{4}
\]
The interval is \((2a+\sqrt{1-2a^2},a+T)\) in the first regime, and \((2a,a+T)\) in the middle regime. There is no continuous component in the last regime. The endpoint alignments \(a=1/\sqrt3\) and \(a=1\) are interpreted by continuous limits, yielding point masses at \(\sqrt3\) and \(2\), respectively; these conditioning events have probability zero under Haar measure.

An exact first conditional moment follows from the same law: if
\[
\psi_*(a)=\begin{cases}
q(a),&a\le1/\sqrt2,\\
\arccos\!\left(a/\sqrt{2(1-a^2)}\right),&1/\sqrt2<a<\sqrt{2/3},\\
0,&a\ge\sqrt{2/3},
\end{cases}
\]
then
\[
\boxed{\displaystyle\mathbb E[B\mid M=a]
=2a+\frac{\sqrt{2(1-a^2)}\sin\psi_*(a)-a\psi_*(a)}{q(a)}.}
\tag{5}
\]
The phase boundaries are necessary: the support changes geometry at the first, while the atom increases continuously from zero to one across the intermediate regime.

## Assumptions and scope
All projections are orthogonal in the Euclidean metric and \(O\) has vertices at the six signed coordinate unit vectors, hence edge length \(\sqrt2\). The conditioning variable \(M\) takes values in \([1/\sqrt3,1]\). Equation (1) is a version of the regular conditional distribution for almost every interior \(a\), as is standard for continuously distributed conditioning variables. The ambient random direction is uniformly distributed on \(S^2\); changing the direction to its negative does not alter the projection.

## Proof
**1. An exact facet formula.** Each of the eight triangular facets has area \(\sqrt3/2\) and a unit outer normal of the form \((\pm1,\pm1,\pm1)/\sqrt3\). Cauchy's projection formula therefore yields, writing \((a,b,c)\) for the sorted absolute coordinates of a unit direction,
\[
B=\frac14\sum_{\epsilon\in\{-1,1\}^3}|\epsilon_1a+\epsilon_2b+\epsilon_3c|
=\boxed{\max\{2a,a+b+c\}},\qquad a\ge b\ge c\ge0.
\tag{6}
\]
For the equality, group the eight terms into opposite pairs and use \(a+b-c\ge0\), \(a-b+c\ge0\): their sum is \(2(3a+b+c+|b+c-a|)\). In particular, the four-vertex projection region \(a\ge b+c\) is the region with brightness \(2a\), and the six-vertex region has brightness \(a+b+c\).

**2. Conditional Haar disintegration.** By signed permutations we may select the chamber \(a=|U_1|\ge b=|U_2|\ge c=|U_3|\ge0\). Fix \(a\in(1/\sqrt3,1)\) and write \(r=\sqrt{1-a^2}\). The circle at latitude \(a\) is parameterized by
\[
(b,c)=(r\cos\phi,r\sin\phi),\qquad \phi\in[0,\pi/4].
\]
The further constraint \(b\le a\) forces \(\phi\ge\arccos(a/r)\) when \(a<1/\sqrt2\), and imposes no constraint otherwise. Thus \(\phi\in[\phi_0,\pi/4]\), with \(\phi_0=\arccos(a/r)\) in the first regime and \(\phi_0=0\) in the second. The spherical-area element in coordinates \((a,\phi)\) is simply \(da\,d\phi\). Each signed-permutation chamber has the same area factor; therefore conditional on \(M=a\) the azimuth \(\phi\) is uniform on this interval. Hence \(\Psi=\pi/4-\phi\) is uniform on \([0,q]\) and
\[
b+c=\sqrt2\,r\cos\Psi.
\]
Substitution into (6) proves (1) for the entire conditional distribution.

**3. Support, atom, and density.** The sum \(b+c\) decreases continuously as \(\Psi\) increases. Its maximum is \(T=\sqrt2 r\); its minimum is \(a+\sqrt{1-2a^2}\) if \(a<1/\sqrt2\), and \(r\) otherwise. Comparison of these endpoints with \(a\) proves the three regimes and their support intervals. In the middle regime the condition \(B=2a\) is \(\Psi\ge\arccos(a/T)\), so uniformity gives the mass (3). For \(a\ge\sqrt{2/3}\) even \(T\le a\), whence determinism. On the strictly increasing branch of \(B=a+T\cos\Psi\), the inverse Jacobian is \(|d\Psi/dz|=1/\sqrt{T^2-(z-a)^2}\); division by \(q\) proves (4). The density integrates to one minus the stated atom, and endpoint limits follow directly.

**4. Exact conditional mean.** The positive part in (1) is nonzero precisely for \(0\le\Psi<\psi_*\). Integrating it against \(d\Psi/q\) gives
\[
\mathbb E[(T\cos\Psi-a)_+\mid M=a]
=\frac1q\int_0^{\psi_*}(T\cos\psi-a)\,d\psi
=\frac{T\sin\psi_*-a\psi_*}{q},
\]
proving (5).

## Verification
Run `python3 verify.py` using only the Python standard library. It evaluates \(360{,}000\) deterministic angular instances across twelve values of \(a\), computing projection areas independently from all eight facet normals and from (1). It verifies the sharp support bounds and checks the atom fractions and conditional expectations against deterministic angular quadrature. The program prints `VERIFY_OK` on success. These finite tests are cross-checks; the continuum classification follows from the preceding proof.

## Relationship to prior work
Cauchy's projection formula and the facet-normal representation of brightness are classical. Finch (2012) and Böröczky--Henk (1999) study projection geometry and regular-octahedron face-count probabilities. Abas (2026) develops unconditional random width and brightness laws and their spherical co-area framework; the later *Random Width and Brightness* paper includes a tetrahedral brightness law, which is related by projection-body equivalence to the octahedron's **unconditional** brightness distribution. The independently accessible *Exact orientation-variance spectrum of Platonic shadow areas* evaluates the octahedron's unconditional second moment, while *Axial rigidity of six-vertex shadows of octahedra* obtains its unconditional four/six-vertex probability and deformation behavior. None of those cited **accessible full-result statements** supplies the joint conditioning by the largest absolute viewing coordinate, including its nontrivial intermediate atom and sharp three-regime support envelope. An unread full manuscript could nevertheless contain an equivalent conditional formulation; no claim of exhaustive negative historical priority is made.

## Limitations
The law holds for the stated regular octahedron and **Haar viewing directions**, conditioned on the nearest coordinate axis; it is not a formula for general affine octahedra or for other conditioning statistics. A conditional atom does not imply any atom in the unconditioned brightness law. The full text of Abas's broader 2026 random-brightness manuscript was not accessible in the available open text routes, so possible equivalent material there is a residual priority risk. No independent external audit has been performed.

## References
1. O. Abas, *Width Laws and Spectral Geometry*, arXiv:2608.06348v1, first public 2026-08-06, https://arxiv.org/abs/2608.06348.
2. O. Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability*, arXiv:2609.26202, https://arxiv.org/abs/2609.26202 (abstract accessible; full text not inspected).
3. S. R. Finch, *Planar Projections and Second Intrinsic Volume*, arXiv:1203.2464v1, https://arxiv.org/abs/1203.2464.
4. K. Böröczky Jr. and M. Henk, *Random Projections of Regular Polytopes*, *Archiv der Mathematik* 73 (1999), 465–473, DOI:10.1007/s000130050424.
5. *Exact orientation-variance spectrum of Platonic shadow areas*, publicly available complete research text, 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-orientation-variance-spectrum-of-platonic-shadow-areas--76ed33fc3859.
6. *Axial rigidity of six-vertex shadows of octahedra*, publicly available complete research text, 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-axial-rigidity-of-six-vertex-shadows-of-octahedra--ddf3a826ab64.
7. E. W. Weisstein, *Cauchy's Projection Formula*, MathWorld, https://mathworld.wolfram.com/CauchysProjectionFormula.html.
