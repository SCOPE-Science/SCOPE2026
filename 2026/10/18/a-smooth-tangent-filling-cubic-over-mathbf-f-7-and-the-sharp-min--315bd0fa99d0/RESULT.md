# A smooth tangent-filling cubic over \(\mathbf F_7\) and the sharp minimal degree

## Finding
A plane curve over a finite field is tangent-filling if the tangent lines at all of its smooth rational points cover every rational point of its ambient projective plane. Among all nonzero plane curves over \(\mathbf F_7\), including singular and reducible curves, the minimum tangent-filling degree is exactly \(3\). The bound is realized by the geometrically smooth cubic
\[
C:\quad X^3+XYZ+Y^3+YZ^2-Z^3=0.
\]
Its \(12\) rational points have \(12\) distinct rational tangent lines covering all \(57\) points of \(\mathbf P^2(\mathbf F_7)\). The rational tangent arrangement has incidence multiplicity distribution \(36\) points of multiplicity \(1\), \(9\) of multiplicity \(2\), \(9\) of multiplicity \(3\), and \(3\) of multiplicity \(5\). The three fivefold centers are noncollinear, and the \(12\) dual points form a minimal nontrivial blocking set in the dual plane (using the classical size lower bound).

## Assumptions and scope
All curves, points, and tangents are over \(k=\mathbf F_7\) unless expressly qualified. Geometric smoothness is taken over an algebraic closure; rational points mean \(k\)-points. The minimum allows any projective plane curve over \(k\), including nonreduced and reducible plane schemes; tangent lines at non-smooth rational points are not counted. Distinct tangent lines are regarded projectively. The dual blocking set assertion is about the Gauss image, not the cubic's own rational-point set.

## Proof
**Geometric smoothness.** Put \(F=X^3+XYZ+Y^3+YZ^2-Z^3\). Modulo \(7\),
\[
F_X=3X^2+YZ,\quad F_Y=XZ+3Y^2+Z^2,\quad F_Z=XY+2YZ-3Z^2.
\]
If a common zero of the three partial derivatives had \(X=0\), then \(YZ=0\), while \(F(0,Y,Z)=Y^3+YZ^2-Z^3\) excludes every projective point with \(YZ=0\). If \(X\ne0\), scale \(X=1\). The first derivative gives \(YZ=4\); hence \(Y\ne0\) and \(Z=4/Y\). Multiplying the remaining two equations by suitable nonzero powers of \(Y\) gives
\[
A(Y)=3Y^4+4Y+2=0,\qquad B(Y)=Y^3+Y^2+1=0.
\]
These cannot vanish simultaneously, since the following identity holds modulo \(7\):
\[
(-2Y^2+Y+3)A(Y)+(-Y^3-2Y^2+2)B(Y)=1.
\]
Thus the projective plane cubic has no geometric singularities. In particular it is geometrically integral.

**Exact rational tangent coverage.** Projective representatives of its \(12\) rational points and the normalized coefficients of their tangent lines \((F_X,F_Y,F_Z)\), respectively, are the rows of the following table:

| Rational point \([X:Y:Z]\) | Tangent \([a:b:c]\), equation \(aX+bY+cZ=0\) |
|---|---|
| \([1:0:1]\) | \([1:3:6]\) |
| \([1:0:2]\) | \([1:2:3]\) |
| \([1:0:4]\) | \([1:2:5]\) |
| \([1:1:2]\) | \([1:6:0]\) |
| \([1:1:4]\) | \([0:1:5]\) |
| \([1:2:5]\) | \([1:0:4]\) |
| \([1:3:0]\) | \([1:2:1]\) |
| \([1:3:5]\) | \([1:2:0]\) |
| \([1:5:0]\) | \([1:4:4]\) |
| \([1:6:0]\) | \([1:1:2]\) |
| \([1:6:2]\) | \([1:2:4]\) |
| \([1:6:4]\) | \([1:5:1]\) |

These are all the rational points: substitution in \(F\) over the \(49\) affine representatives \([1:y:z]\) and the \(8\) infinity representatives \([0:1:z]\), \([0:0:1]\) produces exactly these rows. Tangent vectors are pairwise distinct and perpendicular to their corresponding points. Exhaustive exact incidence arithmetic on the \(57\) rational projective representatives gives
\[
\#\{P:m(P)=j\}=\begin{cases}36&j=1,\\9&j=2,\\9&j=3,\\3&j=5,\\0&\text{otherwise},\end{cases}
\]
where \(m(P)\) is the number of listed tangent lines through \(P\). In particular \(m(P)\ge1\) everywhere. All three fivefold intersection points are \([1:1:4]\), \([1:3:0]\), and \([1:3:5]\), and their determinant is \(3\ne0\) modulo \(7\), so they are noncollinear. These finite calculations are fully reproduced by the accompanying standard-library Python program, which enumerates all projective points, not a sample. The tangent arrangement is a nontrivial blocking set in the dual plane since it contains no complete dual line: the maximum number of tangents through any point is \(5<8\). Its size \(12\) attains the classical nontrivial blocking-set lower bound \(3(7+1)/2=12\).

**Minimum degree.** A line has only itself as a smooth rational tangent, so degree one does not suffice. A geometrically smooth conic over \(\mathbf F_7\) has exactly \(8\) rational points and \(8\) distinct rational tangent lines. In odd characteristic no three distinct tangent lines to a smooth conic are concurrent (equivalently, a point has at most two conic tangents), so their union contains \(8\cdot8-\binom82=36<57\) rational points. For a non-smooth conic, every smooth rational point lies on a geometrically reduced line component, whose tangent is that line; the at most two geometric line components yield at most two rational tangent lines. Nonreduced components have no smooth points. Thus no conic is tangent-filling. The smooth cubic above proves the exact minimum \(3\).

## Verification
Execute `python3 verify_tangent.py` using Python's standard library. It verifies the explicit Bézout polynomial identity, enumerates the \(57\) canonical rational projective points, checks the \(12\) cubic points and corresponding tangent vectors, and establishes exact multiplicities \((36,9,9,3)\). Successful completion prints `VERIFY_OK`. Smoothness over an algebraic closure follows from the symbolic identity, not from the finite enumeration. The conic lower bound is the geometric polarity argument above.

## Relationship to prior work
Asgarli–Ghioca, *Tangent-filling plane curves over finite fields* (2023, arXiv:2302.13420v1), posed the minimal-degree question and gave degree \(q-1\) examples for \(q\ge11\) in characteristic greater than \(3\). Their observation that their particular degree-six construction fails at \(q=7\) does not address this different smooth cubic. The earlier Asgarli–Ghioca–Yip paper (arXiv:2208.13299v1) concerns when the rational point set of a plane curve is a blocking set, a different object from the dual Gauss image of its tangents. The lower bound \(12\) for a nontrivial dual blocking set is classical and is not claimed to be new; the new point is its realization by tangents to an explicit smooth cubic, together with the sharp degree-three minimum.

## Limitations
The theorem is specific to the field with seven elements. It does not assert uniqueness up to projective equivalence, classify all tangent-filling cubics, or extend to other fields. The tangent-incidence census is exhaustive for this specified cubic, not an exhaustive search over cubic equations. An independently published or unindexed equivalent example may exist; the literature comparison does not prove uniqueness of discovery. Independent audit has not been performed.

## References
1. S. Asgarli and D. Ghioca, *Tangent-filling plane curves over finite fields*, first public arXiv version February 26, 2023, arXiv:2302.13420v1, https://arxiv.org/abs/2302.13420.
2. S. Asgarli, D. Ghioca and C. H. Yip, *Plane curves giving rise to blocking sets over finite fields*, first public arXiv version August 28, 2022, arXiv:2208.13299v1, https://arxiv.org/abs/2208.13299.
3. A. Blokhuis, *On the size of a blocking set in \(\mathrm{PG}(2,p)\)*, Combinatorica 14 (1994), 111–114 (classical size bound; invoked only for sharpness as a dual blocking set).
