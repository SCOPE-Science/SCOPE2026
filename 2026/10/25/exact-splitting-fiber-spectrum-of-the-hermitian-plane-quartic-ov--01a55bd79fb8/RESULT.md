# Exact splitting-fiber spectrum of the Hermitian plane quartic over \(\mathbb F_{729}\)

## Finding
Let \(K=\mathbb F_{3^6}=\mathbb F_{729}\), and let \(C\subset\mathbb P^2_K\) be the smooth Hermitian quartic
\[
C:\quad Y^3Z+YZ^3=X^4.
\]
For each exterior rational center \(P\in\mathbb P^2(K)\setminus C(K)\), the linear projection \(\pi_P:C\to\mathbb P^1_K\) has degree four. Write \(N(P)\) for the number of \(K\)-rational fibers of \(\pi_P\) comprising four **distinct \(K\)-rational points**, or equivalently the number of \(K\)-rational four-secant lines to \(C(K)\) through \(P\).

**Theorem (exact splitting-fiber spectrum).** The set of all \(531279\) exterior \(K\)-rational points has the following complete distribution:

| \(N(P)\) | Number of exterior centers |
| ---: | ---: |
| 25 | 1512 |
| 48 | 36288 |
| 49 | 60480 |
| 50 | 36288 |
| 51 | 12096 |
| 52 | 36288 |
| 53 | 18144 |
| 54 | 67032 |
| 55 | 12096 |
| 56 | 72576 |
| 57 | 36288 |
| 58 | 48384 |
| 59 | 54432 |
| 61 | 12096 |
| 62 | 9072 |
| 65 | 18144 |
| 222 | 63 |
| **Total** | **531279** |

In particular, \(\min_P N(P)=25\), while the exceptional maximum \(N(P)=222\) is attained at precisely the 63 points of
\[
\mathbb P^2(\mathbb F_9)\setminus C(\mathbb F_9).
\]
There are exactly \(39879\) \(K\)-rational four-secant lines. The complete line-character distribution is \(158760\) zero-secants, \(175420\) one-secants, \(158112\) two-secants, and \(39879\) four-secants; no three-secant occurs. This is an exact arithmetic classification of completely split projection fibers, *not* a claim that completeness of the \((892,4)\)-arc was previously unknown.

## Assumptions and scope
All points and lines are rational over \(K=\mathbb F_{729}\); intersections count **distinct rational curve points**, not scheme-theoretic multiplicities. The curve is defined by the displayed homogeneous polynomial, and the projection-center distribution excludes rational points on the curve. The genus is three, as \(C\) is a smooth plane quartic. The polynomial field model for reproduction is \(K=\mathbb F_3[t]/(t^6+t+2)\), with each element encoded by its six base-three coefficients. The defining polynomial is irreducible: the supplied programs verify invertibility of every nonzero encoded element; this finite check proves that the quotient is a field. A subfield \(\mathbb F_9\) is the fixed set under ninth-power Frobenius.

## Proof
**Step 1 (smoothness and size).** The defining partial derivatives are \(-X^3\), \(Z^3\), and \(Y^3\). They never vanish simultaneously at a projective point; hence \(C\) is geometrically smooth and has genus \((4-1)(4-2)/2=3\). Every affine point \((x,y)\) satisfies \(y^3+y=x^4\), and the sole point at infinity is \((0:1:0)\). In the explicit field model the exact point enumeration yields \(891\) affine points, hence \(\#C(K)=892\). The total number of rational projective points and lines is \(729^2+729+1=532171\).

**Step 2 (line enumeration certificate).** Every affine nonvertical line is uniquely \(y=mx+b\), where \(m,b\in K\). Substitution into the curve equation gives the exactly equivalent equation
\[
x^4-m^3x^3-mx=b^3+b.
\]
The number of distinct roots in \(K\) is therefore the exact rational intersection character of the line. Each vertical line \(x=c\) has the point at infinity and the affine solutions of \(y^3+y=c^4\). The line at infinity has exactly one point of \(C(K)\). Enumeration of all \(729^2\) nonvertical, 729 vertical, and one infinity lines gives the line-character counts stated above. An independently implemented second certificate recovers the same counts by enumerating all curve points and rational lines and checking the number of point pairs on each line. The checksum
\[
158112+6\cdot39879=\binom{892}{2}=397386
\]
verifies the pair incidence accounting. These are finite exhaustive computations over the completely specified field, not statistical experiments.

**Step 3 (point spectrum).** For every one of the \(39879\) lines with four rational curve points, increment a counter at each of its \(729+1=730\) rational projective points. Identify each projective point by a unique normalized representative \((x:y:1)\), \((1:y:0)\), or \((0:1:0)\). The exact program exhausts all such points and splits the resulting counts into those on \(C(K)\) and those off it. For the latter it obtains precisely the 17 rows of the table. As an independent check, the root-based implementation above detects four-secant lines without using the point-pair incidence algorithm; it independently increments the counters and reproduces every exterior spectrum row. The total number of line–point incidences is exactly
\[
39879\cdot730=29111670.
\]
On-curve points contribute \(864\cdot175+28\cdot297=159516\) incidences, leaving \(28952154\) incidences at exterior centers. Both computed spectra satisfy these sums.

**Step 4 (geometric exceptional locus).** The ninth-power Frobenius fixed points of \(\mathbb P^2(K)\) are exactly \(\mathbb P^2(\mathbb F_9)\). The explicit enumerator determines that this subplane has 91 points, precisely 28 on \(C\) and 63 exterior; each of its exterior points has \(N(P)=222\). The global table shows that *exactly* 63 exterior points have \(N(P)=222\). Therefore the 63 maximal centers are exactly \(\mathbb P^2(\mathbb F_9)\setminus C(\mathbb F_9)\). This conclusion uses both the inclusion and the global multiplicity equality, not a guess from observed symmetry.

**Step 5 (projection interpretation).** Since \(P\notin C\), the pencil of lines through \(P\) induces a base-point-free degree-four morphism from \(C\) to \(\mathbb P^1_K\). A rational line is a completely split unramified fiber exactly when its intersection with \(C\) comprises four distinct \(K\)-rational points, so the line counts equal the stated \(N(P)\) without multiplicity ambiguity.

## Verification
The two self-contained independent programs `verify.cpp` and `check_direct.cpp` use exact integer representations of \(\mathbb F_{729}\), and each visits **every** rational plane point or line required by its proof. `verify.cpp` builds the curve-point and line-incidence lists, checks all point-pair incidences, generates the full center spectrum, and verifies the exact ninth-Frobenius exceptional locus; its successful terminal assertion is `VERIFY_OK`. `check_direct.cpp` instead obtains intersection characters from the quartic-in-\(x\) equation and independently generates the same full spectrum; its successful terminal assertion is `DIRECT_VERIFY_OK`. Compile either program with a C++17 compiler, e.g. `g++ -O3 -std=c++17 verify.cpp -o verify` and `g++ -O3 -std=c++17 check_direct.cpp -o check_direct`, then run `./verify` and `./check_direct`. No external packages or data files are required. The invariance of the results under the two different enumeration methods provides error detection but is not an independent external mathematical audit.

## Relationship to prior work
Korchmáros, Nagy, and Szőnyi (first publicly posted 2023-02-20, arXiv:2302.10162) establish the Hermitian-arc setting, its restricted line characters and general completeness results; the preprint describes the \(r=3\) Hermitian case as not settled by its main theorem. More decisively, Korchmáros's 2022 Irsee conference slides explicitly report that a Magma computation already confirms *completeness* of the \((892,4)\)-arc in \(\mathrm{PG}(2,3^6)\), and the slides also give a four-secant incidence count for points on the curve. **Thus completeness for \(q=3,r=3\), the cardinality 892, and the on-curve incidence count are prior facts, not novelty claims here.** The present claim is the much finer 17-valued exterior splitting-fiber spectrum, its sharp minimum 25, and the precise 63-point subfield maximum locus, none of which are stated in the inspected slide pages.

Bartoli and Timpanella, *Complete \((k,q+1)\)-arcs in \(\mathrm{PG}(2,\mathbb F_{q^6})\) from the Hermitian curve* (2025, DOI 10.1007/s10801-025-01456-w), prove a completeness theorem for sufficiently large \(q\); its text does not supply the 17-valued \(q=3\) exterior fiber distribution. Thus neither the known small-field binary completeness computation nor the large-field existence theorem implies the exact per-center counts and subfield characterization stated here.

## Limitations
The result concerns exactly this Hermitian quartic over \(\mathbb F_{729}\); it does not give a symbolic formula for all parameters \(q,r\), and the geometric subfield characterization is for this embedded model. Exhaustive finite computations prove these specific finite assertions because their search domains and field arithmetic are completely specified; they do not imply an asymptotic theorem. Published or unindexed exact census tables or unpublished Magma outputs may contain the finer exterior distribution; those remain residual novelty risks. Independent external audit and independent validation have not been performed.

## References
1. G. Korchmáros, G. P. Nagy, T. Szőnyi, *Algebraic approach to the completeness problem for \((k,n)\)-arcs in planes over finite fields*, arXiv:2302.10162, v1 2023-02-20. https://arxiv.org/abs/2302.10162
2. G. Korchmáros, *Plane algebraic curves with many symmetries, and complete \((k,n)\)-arcs*, Sixth Irsee Conference, 2022, presentation pages 176–177 (zero-based indexing); https://osebje.famnit.upr.si/~michel.lavrauw/Irsee6/Slides/Invited/Korchmaros.pdf
3. D. Bartoli, M. Timpanella, *Complete \((k,q+1)\)-arcs in \(\mathrm{PG}(2,\mathbb F_{q^6})\) from the Hermitian curve*, *J. Algebraic Combinatorics* 62, article 21 (2025). DOI 10.1007/s10801-025-01456-w; https://link.springer.com/article/10.1007/s10801-025-01456-w
