# Regular-polygon sweep polytopes are regular exactly in odd order
## Finding
Let
\[
n\ge3
\]
and let
\[
a_j=
\left(
\cos\frac{2\pi j}{n},
\sin\frac{2\pi j}{n}
\right)
\qquad
(0\le j<n)
\tag{1}
\]
be the vertices of the unit-circumradius regular \(n\)-gon.

For the sweep-polytope normalization of Padrol and Philippe, define
\[
Z_n
=
\operatorname{SP}(a_0,\ldots,a_{n-1})
=
\sum_{0\le i<j<n}
\left[
-\frac{a_i-a_j}{2},
\frac{a_i-a_j}{2}
\right].
\tag{2}
\]

Then \(Z_n\) is a centrally symmetric equiangular \(2n\)-gon, and its Euclidean shape has an exact parity dichotomy.

If \(n\) is odd, then
\[
\boxed{
Z_n\text{ is a regular }2n\text{-gon}.
}
\tag{3}
\]
Its side length is
\[
\boxed{
\ell_n=\cot\frac{\pi}{2n},
}
\tag{4}
\]
its perimeter is
\[
\boxed{
\operatorname{Per}(Z_n)
=
2n\cot\frac{\pi}{2n},
}
\tag{5}
\]
and its area is
\[
\boxed{
\operatorname{Area}(Z_n)
=
\frac n2\cot^3\frac{\pi}{2n}.
}
\tag{6}
\]
The output isometry group is the full dihedral group of the regular \(2n\)-gon, of order \(4n\). Thus the sweep construction doubles the order of the input regular \(n\)-gon's Euclidean symmetry group.

If \(n\) is even, put
\[
y=\frac{\pi}{n}.
\tag{7}
\]
Then \(Z_n\) is cyclic and nonregular. Its \(2n\) side lengths alternate between
\[
\boxed{
2\cot y
\quad\text{and}\quad
2\csc y,
}
\tag{8}
\]
with exactly \(n\) sides of each length. Hence
\[
\boxed{
\operatorname{Per}(Z_n)
=
2n\left(\cot y+\csc y\right).
}
\tag{9}
\]
Its area is
\[
\boxed{
\operatorname{Area}(Z_n)
=
n\,
\frac{\cos y\left(3+\cos^2 y\right)}
{\sin^3 y}.
}
\tag{10}
\]
Because the two alternating lengths are unequal, the full Euclidean symmetry group has order exactly \(2n\), equal to the order inherited from the input regular \(n\)-gon.

Therefore
\[
\boxed{
Z_n\text{ is regular if and only if }n\text{ is odd}.
}
\tag{11}
\]

## Assumptions and scope
The result uses the centered sweep-polytope normalization in (2), exactly as in the primary source.

The input regular polygon has circumradius \(1\). Scaling the input by a factor \(t>0\) scales every sweep-polytope length by \(t\) and the area by \(t^2\).

All geometry is ordinary Euclidean geometry in \(\mathbb R^2\).

The theorem concerns the metric shape of the sweep polytope, not only its normal fan or combinatorial type. In particular, the odd/even distinction is invisible from the statement that every generic planar sweep polytope is a centrally symmetric polygon with one edge pair for each slope class.

## Proof
Identify \(\mathbb R^2\) with the complex plane and write
\[
a_j=e^{2\pi i j/n}.
\]
For \(i\ne j\),
\[
a_i-a_j
=
2i\,
e^{\pi i(i+j)/n}
\sin\frac{\pi(i-j)}n.
\tag{12}
\]
Therefore the unoriented direction of the chord \(a_i-a_j\) depends only on
\[
i+j\pmod n.
\tag{13}
\]
There are exactly \(n\) such direction classes, equally spaced by angle
\[
\frac{\pi}{n}.
\]
A planar zonotope has one opposite edge pair for every generator direction class. Hence \(Z_n\) is a centrally symmetric equiangular \(2n\)-gon.

For one generator direction class, the corresponding edge of a zonotope is the Minkowski sum of all generator segments parallel to that direction. Because the generators in (2) are half-chords, the edge length is exactly the sum of the lengths of the original chords in that class.

Suppose first that
\[
n=2m+1
\]
is odd. Rotation of the input polygon by one vertex sends the class indexed by \(k\) to the class indexed by \(k+2\). Since \(2\) is invertible modulo \(n\), all \(n\) classes form one orbit and have the same edge length.

For the class
\[
i+j\equiv0\pmod n,
\]
the unordered chord separations are exactly
\[
1,2,\ldots,m.
\]
Therefore every edge length is
\[
\ell_n
=
2\sum_{d=1}^{m}\sin\frac{\pi d}{n}.
\tag{14}
\]
The standard finite sine sum gives
\[
\sum_{d=1}^{m}\sin\frac{\pi d}{n}
=
\frac12\cot\frac{\pi}{2n},
\]
so (4) follows.

An equiangular equilateral convex polygon is regular. Thus \(Z_n\) is the regular \(2n\)-gon of side length (4). The standard regular-polygon formulas give (5) and (6).

Now suppose
\[
n=2m
\]
is even. Rotation by one input vertex sends a direction class \(k\) to \(k+2\), so the classes split into an even orbit and an odd orbit.

For the even class \(k=0\), the admissible unordered pairs are
\[
\{i,-i\},
\qquad
1\le i\le m-1.
\]
Their chord lengths sum to
\[
2\sum_{i=1}^{m-1}\sin\frac{i\pi}{m}
=
2\cot\frac{\pi}{2m}
=
2\cot y.
\tag{15}
\]

For the odd class \(k=1\), there are \(m\) unordered pairs. Their difference residues are the odd residues modulo \(2m\), up to sign. Hence the chord lengths sum to
\[
2\sum_{r=0}^{m-1}
\sin\frac{(2r+1)\pi}{2m}
=
2\csc\frac{\pi}{2m}
=
2\csc y.
\tag{16}
\]
This proves the alternating side lengths (8).

It remains to show the cyclicity and area formula. Let
\[
u_k=
\left(
\cos ky,\sin ky
\right)
\]
be the successive outward-normal directions. By the inherited rotation symmetry, the support numbers of the even-normal edges have one common value \(p\), and those of the odd-normal edges have one common value \(q\).

Write
\[
c=\cos y,
\qquad
s=\sin y.
\]
The edge with normal \(u_0\) is cut out between the two adjacent odd-normal support lines. Its length is
\[
\frac{2(q-pc)}s.
\]
By (15),
\[
q-pc=c.
\tag{17}
\]
Similarly, the edge with normal \(u_1\) has length
\[
\frac{2(p-qc)}s,
\]
and (16) gives
\[
p-qc=1.
\tag{18}
\]
Solving (17)--(18) yields
\[
p=\frac{1+c^2}{s^2},
\qquad
q=\frac{2c}{s^2}.
\tag{19}
\]

A vertex at the intersection of the support lines with normals \(u_0\) and \(u_1\) is
\[
\left(
p,\frac{q-pc}{s}
\right)
=
\left(
p,\cot y
\right).
\tag{20}
\]
Every other vertex is obtained from one of the two adjacent parity types by the inherited rotations and reflections. Equation (20), together with (17)--(19), shows that every vertex has the same distance from the origin. Thus the even-\(n\) sweep polygon is cyclic.

Since the two side lengths in (8) are unequal for
\[
0<y\le\frac{\pi}{4},
\]
the polygon is not regular.

The perimeter formula (9) follows by adding the \(n\) edges of each length.

For the area, join the origin to every edge. A polygon with support distance \(h\) and edge length \(L\) contributes triangle area \(hL/2\). Therefore
\[
\operatorname{Area}(Z_n)
=
\frac n2
\left(
p\cdot2\cot y
+
q\cdot2\csc y
\right).
\tag{21}
\]
Substitution from (19) simplifies (21) to (10).

Finally, for odd \(n\), regularity gives the full dihedral group of order \(4n\). For even \(n\), the alternating unequal side lengths force every Euclidean symmetry to preserve the two edge-length classes. Thus rotations can shift by only an even number of edges, giving at most \(n\) rotations, and there are at most \(n\) compatible reflections. The input dihedral symmetries already realize all \(2n\) of these symmetries, so the full output group has order exactly \(2n\).

## Verification
The proof is symbolic for every \(n\ge3\).

The primary full text was inspected at the Euclidean point-configuration setup, Definition 2.1 of the sweep polytope, Proposition 2.2 identifying its normal fan with the sweep arrangement, and Proposition 2.3 identifying sweep polytopes with centered permutahedral projections. A full-text search found no regular-polygon specialization.

The accompanying `verify.py` reconstructs the sweep zonotope directly from all
\[
\binom n2
\]
half-chord generators for
\[
3\le n\le60.
\]
It groups generators by their actual direction class, evaluates the support function from the raw generators, reconstructs all \(2n\) vertices from consecutive support lines, and checks the side-length, perimeter, area, cyclicity, and parity formulas numerically. The computation is corroborative only.

## Relationship to prior work
Padrol and Philippe place sweep polytopes at the intersection of allowable sequences, zonotopes, permutahedral shadows, and monotone path polytopes. Their paper develops the construction, normal fans, projections, and oriented-matroid framework, but does not specialize the metric geometry to regular polygons.

The earlier shellotope terminology goes back to Gritzmann and Sturmfels in their work on Minkowski sums. That source is relevant to the general construction, but the accessible material inspected here was not sufficient to support a whole-document noncoverage claim; it remains a residual historical indexing risk.

General planar zonotope formulas explain how to recover an edge from the sum of parallel generators. They do not, by themselves, give the parity split in the chord multiplicities of a regular \(n\)-gon. The key object-specific step is that the chord-direction classes are indexed by
\[
i+j\pmod n,
\]
so multiplication by \(2\) is transitive exactly in odd order and splits into two parity classes exactly in even order.

This arithmetic produces an actual Euclidean symmetry jump: the odd family becomes regular and acquires twice as many isometries, while the even family retains two distinct alternating metric edge orbits.

## Limitations
The formulas use the canonical centered sweep-polytope normalization and unit-circumradius input.

The theorem treats regular planar point configurations. It does not classify sweep polytopes of arbitrary cyclic, equiangular, or affinely regular point sets.

The result gives side lengths, perimeter, area, cyclicity, and exact symmetry order. It does not address higher-dimensional regular point configurations.

A classical treatment of the same regular-polygon shellotope under older terminology could still exist; targeted searches did not locate one, and the older shellotope source was not available in sufficiently detailed full text to eliminate that residual risk.

## References
1. Arnau Padrol and Eva Philippe, *Sweeps, Polytopes, Oriented Matroids, and Allowable Graphs of Permutations*, arXiv:2102.06134, first public version 2021-02-11; *Combinatorica* 44 (2024), 63--123, DOI 10.1007/s00493-023-00062-3.
2. Peter Gritzmann and Bernd Sturmfels, *Minkowski Addition of Polytopes: Computational Complexity and Applications to Gröbner Bases*, *SIAM Journal on Discrete Mathematics* 6 (1993), 246--269, DOI 10.1137/0406019.
