# Exact splitting-fiber stratification of projections of a Hermitian elliptic cubic over \(\mathbb F_{64}\)

## Finding
Let \(k=\mathbb F_{64}\), and let \(E\subset\mathbb P^2_k\) be the smooth cubic
\[
E:\quad Y^2Z+YZ^2=X^3.
\]
For each \(P\in\mathbb P^2(k)\setminus E(k)\), projection from \(P\) defines a degree-three morphism \(\pi_P:E\to\mathbb P^1\). Let \(N(P)\) denote the number of \(k\)-rational fibers of \(\pi_P\) consisting of three **distinct \(k\)-rational geometric points**. Equivalently, \(N(P)\) counts the \(k\)-lines through \(P\) containing exactly three distinct points of \(E(k)\).

The complete distribution among all \(4080\) exterior rational centers is

| \(N(P)\) | Number of exterior centers |
|---:|---:|
| \(11\) | \(72\) |
| \(14\) | \(648\) |
| \(16\) | \(2052\) |
| \(17\) | \(864\) |
| \(18\) | \(432\) |
| \(26\) | \(12\) |

Furthermore, the twelve centers with \(N(P)=26\) are **exactly** the points in \(\mathbb P^2(\mathbb F_4)\setminus E(\mathbb F_4)\), under the standard subfield embedding \(\mathbb F_4\subset\mathbb F_{64}\). In particular, every exterior projection has a completely split unramified rational fiber; the coarse completeness statement is prior work, not claimed as new.

## Assumptions and scope
All counts refer to **marked centers of projection** in the fixed plane model, not to equivalence classes of morphisms or curves. The base field is exactly \(\mathbb F_{64}\); no statement is asserted for other extensions. The field representation used for exact verification is \(\mathbb F_2[u]/(u^6+u+1)\), with the unique subfield of four elements selected by \(a^4=a\). The cubic is nonsingular since the homogeneous partial derivatives of \(Y^2Z+YZ^2+X^3\) are \(X^2,Z^2,Y^2\), with no common projective zero. It has genus one. Because \(P\notin E\), its pencil of lines has no base points on \(E\), giving a finite morphism of degree three.

## Proof
The result has a finite exhaustive certificate supplied as `verify.py`; all field operations and incidence tests are exact, and the two enumeration methods reconstruct each \(N(P)\) independently.

First verify that \(u^6+u+1\) has no divisor of degrees one, two, or three over \(\mathbb F_2\). Thus its quotient is the field of \(64\) elements. Enumerate the \(64^2+64+1=4161\) distinct projective points in the two disjoint charts \((a:b:1)\), \((1:b:0)\) together with \((0:1:0)\). Evaluate the cubic exactly at every point, obtaining \(\#E(k)=81\).

**First incidence computation.** For each of the \(\binom{81}{2}=3240\) unordered pairs of distinct rational curve points, calculate the projective line via the nonzero cross product. Group all pairs by their resulting line, and collect the distinct curve points on it. Bézout's theorem bounds the number of distinct points of \(E\) on a line by three. The grouped lines have multiplicity profile: \(1056\) lines with three rational curve points, and \(72\) lines with two. This accounts for all \(3240\) unordered pairs because \(1056\binom32+72\binom22=3240\). For each of the \(4161\) centers, count its incidence with the \(1056\) three-point lines. Restricting to the \(4080\) exterior centers yields precisely the six-row distribution in the Finding section.

**Independent splitting-fiber computation.** Every nonvertical affine line is \(Y=mX+c\), where \((m,c)\) independently ranges over \(k^2\). Its intersection with \(E\) consists of the roots of
\[
X^3+(mX+c)^2+(mX+c)=0.
\]
Evaluate this polynomial at each of the \(64\) field elements and count its distinct roots. The resulting \(4096\) affine lines have counts \(1080,1928,72,1016\), respectively, of lines with \(0,1,2,3\) distinct affine intersections. In addition, among the \(64\) vertical lines, exactly \(40\) have three rational curve points (the remaining \(24\) have one), while the line at infinity has one rational curve point. For each affine center \((a:b:1)\), the split lines of slope \(m\) passing through it have intercept \(c=b+ma\); add the vertical contribution. The corresponding formulas for points at infinity use their fixed slope or the vertical direction. **Each of the 4161 independently recomputed per-center values agrees with the first calculation.** This completely determines the claimed histogram, rather than only checking totals.

To identify the maximizers, enumerate the \(21\) rational points of the embedded subplane by the condition \(x^4=x\) in each homogeneous coordinate. Exactly \(9\) of them are on \(E\), and the set of the remaining \(12\) is exactly the enumerated set of the \(12\) centers with \(N(P)=26\). Thus both inclusions, not merely the cardinalities, are certified.

As a consistency check, each three-point line has \(65\) rational plane points, three on \(E\). Therefore the claimed exterior distribution must obey
\[
\sum_{P\notin E(k)}N(P)=1056(65-3)=65472,
\]
which it does. The corresponding on-curve distribution has \(N(P)=39\) at \(72\) points and \(N(P)=40\) at \(9\) points, giving total \(3168=1056\cdot3\). Independently all \(4161\) rational lines have section-character counts \(1080,1953,72,1056\) for intersection cardinalities \(0,1,2,3\), respectively. These checks also follow from the second enumeration.

## Verification
Run `python3 verify.py` from the directory containing the standalone file, using Python 3 and no third-party packages. Its exact required output includes:

```
EXTERIOR_SPLIT_PROFILE {11: 72, 14: 648, 16: 2052, 17: 864, 18: 432, 26: 12}
ON_CURVE_SPLIT_PROFILE {39: 72, 40: 9}
LINE_SECTION_PROFILE {0: 1080, 1: 1953, 2: 72, 3: 1056}
F4_OUTSIDE_EXTREMALS 12
VERIFY_OK
```

The certificate uses exhaustive enumeration of complete **finite** sets, not sampling or an asymptotic argument. Both methods are independently implemented in the same standalone program. All calculations are within the specified finite field and exact projective plane.

## Relationship to prior work
Korchmáros, Nagy, and Szőnyi (2023) investigate Hermitian-curve point sets and the complete-splitting of projective line sections by algebraic and Galois methods. Bartoli, Marcugini, and Pambianco (2015) explicitly determine completeness for cubic curves in projective planes of order at most \(81\); their table covering the \(81\)-point cubic over \(\mathbb F_{64}\) establishes **zero uncovered exterior points**. Hence the present finding does **not** assert first proof of completeness. Standard line-section character counts similarly do not determine how the \(1056\) three-secant lines distribute among *individual* exterior centers. The exact six-valued splitting-fiber distribution and the identification of all twelve maximal centers with the excluded \(\mathbb F_4\)-subplane points are the asserted additions. Bartoli and Timpanella (2025) treat general Hermitian arcs over sixth-degree extensions and do not supply this particular \(\mathbb F_{64}\) splitting-fiber census.

## Limitations
This is an exact finite-field arithmetic/incidence result, not a universal formula in \(q\). The counts distinguish center coordinates, not conjugacy classes under the automorphism group. No structural abstract characterization of the other five strata is provided. Prior work already establishes the coarser completeness property, and the possibility of an unindexed earlier refined center-incidence census cannot be entirely excluded. The standalone arithmetic script supplies a finite proof, but independent audit has not been performed.

## References
1. G. Korchmáros, G. P. Nagy, and T. Szőnyi, *Algebraic approach to the completeness problem for \((k,n)\)-arcs in planes over finite fields*, arXiv:2302.10162, first posted 2023-02-20. https://arxiv.org/abs/2302.10162
2. D. Bartoli, S. Marcugini, and F. Pambianco, *Completeness of cubic curves in PG(2, q), q <= 81*, arXiv:1510.08375, 2015, particularly its tabulation of the 81-point nonsingular cubic. https://arxiv.org/abs/1510.08375
3. D. Bartoli and M. Timpanella, *Complete \((k,q+1)\)-arcs in \(\mathrm{PG}(2,\mathbb F_{q^6})\) from the Hermitian curve*, Journal of Algebraic Combinatorics 62 (2025), article 21. https://doi.org/10.1007/s10801-025-01456-w
