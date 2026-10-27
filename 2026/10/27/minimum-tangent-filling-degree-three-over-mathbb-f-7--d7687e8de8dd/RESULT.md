# Minimum tangent-filling degree three over \(\mathbb F_7\)

## Finding

Let \(k=\mathbb F_7\). Define the geometrically smooth plane cubic
\[
 C:\quad X^2Y+XZ^2+2Y^2Z=0\quad\subset\mathbb P^2_k.
\]
Its twelve rational tangent lines are exactly
\[
 X=0,\qquad Y=0,\qquad Z=0,
 \qquad X-hY=0,\quad X-hZ=0,\quad Y-hZ=0
 \quad(h\in\{1,2,4\}).
\]
They cover all \(57\) points of \(\mathbb P^2(k)\). Conversely, no plane curve of degree at most two over \(k\), whether reducible or irreducible, is tangent-filling. Hence the minimum degree of an irreducible tangent-filling plane curve over \(\mathbb F_7\) is **exactly three**, and it is attained by a smooth genus-one curve. The distribution of the number of rational tangent lines through each ambient rational point is
\[
 \#\{P\colon m(P)=1,2,3,5\}=(36,9,9,3).
\]
Here \(m(P)\) denotes the number of distinct lines in the displayed tangent family passing through \(P\).

## Assumptions and scope

The base field is exactly \(\mathbb F_7\); homogeneous coordinates are \([X:Y:Z]\) and all equations and derivatives are interpreted modulo seven. A curve is *tangent-filling* when the tangent lines at its **smooth \(k\)-rational points** jointly cover \(\mathbb P^2(k)\). Smoothness of \(C\) means smoothness over an algebraic closure, not merely absence of rational singularities. The lower bound covers all degree-one and degree-two plane schemes defined by nonzero homogeneous forms; the minimum-degree statement applies, in particular, to geometrically irreducible curves.

## Proof

**1. Geometric smoothness.** Let \(F=X^2Y+XZ^2+2Y^2Z\). Its derivatives are
\[
 F_X=2XY+Z^2,\quad F_Y=X^2+4YZ,\quad F_Z=2XZ+2Y^2.
\]
If these all vanish at a nonzero geometric point with \(X=0\), the first forces \(Z=0\), and the third forces \(Y=0\), contradiction. If \(X\ne0\), set \(X=1\). The first equation gives \(Y=3Z^2\). The second then gives \(1+5Z^3=0\), hence \(Z^3=4\). In particular \(Z\ne0\). The third gives \(2Z+4Z^4=0\), hence \(1+2Z^3=0\), or \(Z^3=3\), contradiction. Thus no projective geometric singularity exists. A smooth plane cubic is geometrically connected and has genus one.

**2. Rational points and tangent lines.** Exhausting the \(49\) normalized points \([x:y:1]\), the seven points \([x:1:0]\), and \([1:0:0]\) gives this full table. Every right-hand side is the tangent obtained by evaluating \((F_X,F_Y,F_Z)\) on the left-hand side:

| \(P\in C(k)\) | \(T_PC\) |
|---|---|
| \([0:0:1]\) | \(X=0\) |
| \([1:5:1]\) | \(X-Z=0\) |
| \([2:6:1]\) | \(X-2Z=0\) |
| \([3:1:1]\) | \(Y-Z=0\) |
| \([3:5:1]\) | \(X-2Y=0\) |
| \([4:3:1]\) | \(X-4Z=0\) |
| \([5:2:1]\) | \(Y-2Z=0\) |
| \([5:3:1]\) | \(X-4Y=0\) |
| \([6:4:1]\) | \(Y-4Z=0\) |
| \([6:6:1]\) | \(X-Y=0\) |
| \([0:1:0]\) | \(Z=0\) |
| \([1:0:0]\) | \(Y=0\) |

The twelve lines are pairwise distinct. With \(H=\{1,2,4\}\), the order-three subgroup of \(k^\times\), their product is, up to a nonzero scalar,
\[
 XYZ(X^3-Y^3)(X^3-Z^3)(Y^3-Z^3).
\]
At a point where any coordinate is zero, a coordinate tangent contains the point. Otherwise the three nonzero cubes \(X^3,Y^3,Z^3\) all lie in \(\{1,-1\}\); two must be equal. Thus one of \(X^3-Y^3\), \(X^3-Z^3\), \(Y^3-Z^3\) vanishes and one of the nine remaining rational tangents contains the point. This proves tangent-filling for **all** rational plane points without relying on a sampled cover computation. Directly counting the number of displayed lines incident with each of the \(57\) normalized rational points gives multiplicity distribution \((1:36,2:9,3:9,5:3)\), also checked in `verify.py`.

**3. Minimality.** A line supplies only its own tangent line and covers eight rational points. For a geometrically smooth conic, there are exactly \(8\) rational points and hence eight distinct rational tangents. No three of those tangent lines are concurrent: otherwise the corresponding three points of the nonsingular *dual conic* would be collinear, contradicting that a line meets a nonsingular conic in at most two distinct points. Therefore the union of the eight tangents has exactly \(8\cdot8-\binom82=36<57\) rational points. A singular conic over an algebraic closure consists of two lines, possibly coincident; at its smooth rational points, any tangent is one of the at most two component lines (or there are no such points if components are conjugate). Such tangents cover at most \(15\) rational points. Thus no degree-one or degree-two plane curve is tangent-filling. Together with the displayed cubic, the minimum is three.

## Verification

Run `python3 verify.py` with Python 3. It uses only the standard library; it checks all \(57\) normalized projective points, the complete twelve-point rational curve locus, the twelve distinct gradient tangents, equality with the Fermat line arrangement, complete coverage, and the multiplicity counts. The exact output ends in `VERIFY_OK`. The geometric smoothness argument and conic lower bound above are symbolic proofs rather than computer extrapolations. The exploratory enumeration of other cubics is not part of the proof or its dependencies.

## Relationship to prior work

Asgarli and Ghioca [1] introduce tangent-filling plane curves and explicitly ask for the minimum degree in Question 1.5. Their Theorem 1.3 constructs degree-\(q-1\) curves for \(q\ge11\) of characteristic above three; their Remark 3.7 says that the particular degree-six equation **fails** to be tangent-filling when \(q=7\). That statement concerns their special curve, not a nonexistence theorem for cubics. Their Hermitian example applies when \(q\) is a square, unlike seven. The present theorem supplies a degree-three smooth example and matching elementary lower bound at this previously unresolved small prime field.

Asgarli, Ghioca and Yip [2, Theorem 1.3] show that a geometrically irreducible cubic over \(\mathbb F_q\) with \(q\ge5\) cannot have its *own rational point set* form a blocking set. This is not contradicted: here the **rational tangent lines**, equivalently the corresponding point set of the dual plane, form a blocking set. Their discussion of projective triangles supplies context for the well-known minimal twelve-point blocking configuration; novelty is not claimed for that line arrangement by itself, but for its realization by the tangents of this particular smooth cubic and the resulting sharp minimum.

## Limitations

The statement is restricted to \(\mathbb F_7\), not all nonsquare or prime finite fields. The argument does not classify all tangent-filling cubics or projective equivalence classes over seven. Novelty is assessed relative to accessible indexed research and materially inspected primary literature; prior unindexed configurations of elliptic-curve tangents or stronger general results remain a residual risk. No independent mathematical audit has been conducted.

## References

1. S. Asgarli and D. Ghioca, *Tangent-filling plane curves over finite fields*, arXiv:2302.13420 (first posted 2023-02-26); *Bulletin of the Australian Mathematical Society* **109** (2024), 301–315. https://arxiv.org/abs/2302.13420
2. S. Asgarli, D. Ghioca and C. H. Yip, *Plane curves giving rise to blocking sets over finite fields*, arXiv:2208.13299 (first posted 2022). https://arxiv.org/abs/2208.13299
