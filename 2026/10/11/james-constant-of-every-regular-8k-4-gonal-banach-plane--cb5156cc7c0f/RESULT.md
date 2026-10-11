# James constant of every regular \((8k+4)\)-gonal Banach plane
## Finding
For every integer \(k\ge0\), let \(X_{8k+4}\) be the real two-dimensional Banach space whose unit ball is a Euclidean regular \((8k+4)\)-gon, up to linear isometry. Then
\[
J(X_{8k+4})
=
\sqrt2\,\sec\!\left(\frac{\pi}{8k+4}\right).
\]
Thus the residue class \(4\pmod 8\) gives an infinite family in which the elementary Euclidean comparison bound for the James constant is attained exactly.

For the first nonsquare case,
\[
J(X_{12})
=
\sqrt2\,\sec\!\left(\frac{\pi}{12}\right)
=
2(\sqrt3-1).
\]

## Assumptions and scope
All spaces are real and two-dimensional. The James constant is
\[
J(X)=
\sup_{x,y\in S_X}
\min\{\|x+y\|,\|x-y\|\}.
\]

Fix
\[
N=8k+4
\]
and normalize the regular \(N\)-gon so that its Euclidean inradius is \(1\). Write
\[
u_j=
\left(
\cos\frac{2\pi j}{N},
\sin\frac{2\pi j}{N}
\right),
\qquad
0\le j<N,
\]
for the unit outward facet normals, and define
\[
\|z\|_N=\max_{0\le j<N}\langle u_j,z\rangle .
\]
The unit ball is then
\[
B_N=\bigcap_{j=0}^{N-1}\{z:\langle u_j,z\rangle\le1\}.
\]
Its vertices have Euclidean radius
\[
R_N=\sec\!\left(\frac{\pi}{N}\right)
\]
and directions
\[
\frac{(2j+1)\pi}{N}.
\]

## Proof
For every vector \(z\),
\[
\|z\|_N\le \|z\|_2,
\]
because every \(u_j\) is a Euclidean unit vector. Conversely, every point of \(B_N\) has Euclidean norm at most the circumradius
\[
R_N=\sec\!\left(\frac{\pi}{N}\right).
\]
Hence every \(x\in S_{X_N}\) satisfies
\[
\|x\|_2\le R_N.
\]

Take arbitrary \(x,y\in S_{X_N}\), and put
\[
A=\|x+y\|_N,
\qquad
B=\|x-y\|_N.
\]
Then
\[
A^2+B^2
\le
\|x+y\|_2^2+\|x-y\|_2^2.
\]
The Euclidean parallelogram identity gives
\[
\|x+y\|_2^2+\|x-y\|_2^2
=
2\|x\|_2^2+2\|y\|_2^2
\le
4R_N^2.
\]
Therefore
\[
\min\{A,B\}^2
\le
\frac{A^2+B^2}{2}
\le
2R_N^2,
\]
so
\[
J(X_N)\le \sqrt2\,R_N
=
\sqrt2\,\sec\!\left(\frac{\pi}{N}\right).
\tag{1}
\]

It remains to attain (1). Because
\[
N=8k+4=4(2k+1),
\]
the direction \(\pi/4\) is a vertex direction:
\[
\frac{(2k+1)\pi}{N}=\frac{\pi}{4}.
\]
Choose the two unit-ball vertices
\[
x=
R_N
\left(
\cos\frac{\pi}{4},
\sin\frac{\pi}{4}
\right),
\qquad
y=
R_N
\left(
\cos\frac{3\pi}{4},
\sin\frac{3\pi}{4}
\right).
\]
They are separated by a Euclidean right angle. Their sum and difference are
\[
x+y=
\sqrt2\,R_N(0,1),
\qquad
x-y=
\sqrt2\,R_N(1,0).
\]
Since \(N\) is divisible by \(4\), both coordinate directions are facet-normal directions. Along a facet-normal ray the polygonal norm equals the Euclidean norm. Consequently
\[
\|x+y\|_N
=
\|x-y\|_N
=
\sqrt2\,R_N.
\]
This gives the reverse inequality in (1), proving
\[
J(X_{8k+4})
=
\sqrt2\,\sec\!\left(\frac{\pi}{8k+4}\right).
\]

For \(N=12\),
\[
\sqrt2\,\sec\!\left(\frac{\pi}{12}\right)
=
2(\sqrt3-1),
\]
which yields the stated dodecagonal value.

## Verification
The proof is analytic and does not depend on finite enumeration. Its critical steps are the exact inclusion of the Euclidean unit disk in the inradius-one regular polygon, the circumradius identity
\[
R_N=\sec\!\left(\frac{\pi}{N}\right),
\]
the Euclidean parallelogram identity, and the residue-class identity
\[
\frac{(2k+1)\pi}{8k+4}=\frac{\pi}{4}.
\]

The bundled `verify.py` checks the integer index identities exactly, numerically reconstructs the regular polygon norm for the first several values \(N=4,12,20,\ldots\), and verifies that the explicit right-angle vertex pair attains
\[
\sqrt2\,\sec\!\left(\frac{\pi}{N}\right)
\]
to high precision. This computation is a reproducibility check only; the infinite-family statement is proved by the preceding symbolic argument.

## Relationship to prior work
Sain, Ghosh and Paul study the James constant through isosceles orthogonality. Their paper proves that every attaining pair for \(J(X)\) is isosceles-orthogonal and that, in a two-dimensional polyhedral Banach space, a maximizing configuration may be chosen with one vector at a vertex of the unit ball. They explicitly compute the regular-octagonal example, where
\[
J(X_8)=\sqrt2,
\]
and also work out an irregular hexagonal example. The inspected full text does not contain a regular dodecagon or an all-regular-polygon formula.

The present result uses the same polyhedral-geometric motivation but a different sharp mechanism: a Euclidean upper envelope combined with a residue-class alignment of polygon vertices and facet normals. The regular-octagonal value from the source does not imply this result; indeed \(8\) lies in the other divisible-by-\(4\) residue class, where the upper envelope is not attained by the same right-angle construction.

Targeted bibliographic searches under the classical James notation, regular-polygon aliases, the residue class \(8k+4\), and the candidate secant formula found no prior statement covering the theorem. Publicly indexed exact results on regular polygons encountered in the comparison concern different invariants.

## Limitations
The theorem treats regular polygons with
\[
N\equiv4\pmod8.
\]
It does not claim the same formula for regular polygons with
\[
N\equiv0\pmod8,
\]
and the regular-octagonal example already shows that such an extension would be false.

The argument determines the global James constant but does not classify all maximizing pairs. Bibliographic searches cannot prove absolute novelty; an equivalent formula under a different regular-polygon normalization or notation remains a residual literature risk.

## References
1. D. Sain, S. Ghosh and K. Paul, “On isosceles orthogonality and some geometric constants in a normed space,” Aequationes Mathematicae 97 (2023), 147–160, doi:10.1007/s00010-022-00909-y. Published online 1 September 2022. Primary MSC 46B20.
2. J. Gao and K.-S. Lau, “On the geometry of spheres in normed linear spaces,” Journal of the Australian Mathematical Society, Series A 48 (1990), 101–112.
