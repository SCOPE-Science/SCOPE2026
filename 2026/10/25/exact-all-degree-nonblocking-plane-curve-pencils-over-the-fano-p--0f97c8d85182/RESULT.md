# Exact all-degree nonblocking plane-curve pencils over the Fano plane

## Finding
For an integer \(d\geq3\), let \(V_d=H^0(\mathbf P^2_{\mathbf F_2},\mathcal O(d))\), of dimension \(N_d=\binom{d+2}{2}\). A **pencil** is a two-dimensional \(\mathbf F_2\)-linear subspace \(W\subset V_d\). It is **fully nonblocking** if, for each of the three nonzero forms \(F\in W\), there is a rational projective line on which \(F\) is nonzero at all three rational points. No smoothness or irreducibility is assumed here.

The exact number of fully nonblocking degree-\(d\) pencils is
\[
\boxed{287\,2^{2(N_d-7)}}.
\]
Of these, \(147\,2^{2(N_d-7)}\) have no common rational base point and \(140\,2^{2(N_d-7)}\) have exactly one. No such pencil has two common rational base points. Their unordered three-member rational-point-count profiles are exactly

| Profile | Number of pencils |
| --- | ---: |
| \((1,2,4)\) | \(21\,2^{2(N_d-7)}\) |
| \((1,3,3)\) | \(42\,2^{2(N_d-7)}\) |
| \((2,2,3)\) | \(84\,2^{2(N_d-7)}\) |
| \((2,3,4)\) | \(84\,2^{2(N_d-7)}\) |
| \((3,3,3)\) | \(56\,2^{2(N_d-7)}\) |

Consequently, the proportion among all degree-\(d\) pencils tends, as \(d\to\infty\), to \(\boxed{861/8192}\), approximately \(0.10510\). The total number of pencils in \(V_d\) is \((2^{N_d}-1)(2^{N_d}-2)/6\).

For cubics (\(d=3\)), there are **18,368** fully nonblocking pencils; their \(\operatorname{PGL}_3(\mathbf F_2)\)-action has exactly **112 orbits**, with **108 orbits of size 168** and **four of size 56**. Among these pencils, 784 have all three members geometrically smooth, forming six projective orbits (four of size 168 and two of size 56). The complete distribution by number \(s\in\{0,1,2,3\}\) of geometrically smooth members is
\[
\big(\#\{s=0\},\#\{s=1\},\#\{s=2\},\#\{s=3\}\big)
=(4816,9408,3360,784).
\]
These statistics classify embedded linear systems under rational projective coordinate change, not abstract genus-one curves.

## Assumptions and scope
All schemes and sections are defined over \(\mathbf F_2\). A rational projective line is **disjoint from the rational zero locus** of \(F\) precisely when \(F\) takes the value \(1\) on all three points of that line. Since \(\mathbf F_2^*=\{1\}\), evaluations of homogeneous forms at rational projective points are well defined, independent of coordinates. Multiplicities, geometric irreducibility and singularities play no role in the all-degree counting formula. Smoothness is used only for the cubic refinement.

For numerical coefficient masks, the ten cubic monomials are ordered by \((a,b,c)\) lexicographically with \(a+b+c=3\); bit \(j\) corresponds to monomial \(X^{a_j}Y^{b_j}Z^{c_j}\), as specified verbatim in the verification programs.

## Proof
**Evaluation surjectivity.** Write \(E=\mathbf F_2^{\mathbf P^2(\mathbf F_2)}\cong\mathbf F_2^7\). The evaluation map \(\mathrm{ev}_d:V_d\to E\) is onto for every \(d\ge3\). Indeed, for any rational point \(P\), choose three rational lines avoiding \(P\) whose union is the other six rational points. Their linear equations have product a homogeneous cubic evaluating to the indicator of \(P\). Multiplying this cubic by a linear form not vanishing at \(P\), to the power \(d-3\), preserves the indicator at every rational point. The seven indicators span \(E\). Thus \(\dim\ker(\mathrm{ev}_d)=N_d-7\).

**Finite Fano-plane classification.** Let \(\mathscr A\subset E\) consist of the binary point-functions equal to one at all points of at least one rational line. There are exactly 64 such functions. Enumerate the 128 functions on seven points, the seven rational lines, and the three nonzero members of each two-dimensional subspace of \(E\). Exactly 287 subspaces \(U\le E\) of dimension two satisfy \(U\setminus\{0\}\subset\mathscr A\). The complete rational zero-locus profile frequencies are respectively \(21,42,84,84,56\), in the order shown in the Finding table. Their rational common-base-point distribution is 147 with none and 140 with one, and zero with more than one. This is an exhaustive check on a completely enumerated seven-bit space: `scripts/independent_checker.py` constructs all seven rational points and all seven lines directly and verifies the frequencies. The `scripts/orbit_census.py` implementation independently checks all 1023 nonzero cubic coefficient masks and all qualifying pairs.

**Counting lifts.** A fully nonblocking pencil \(W\le V_d\) has \(W\cap\ker(\mathrm{ev}_d)=0\), since a nonzero element in that intersection vanishes everywhere rationally and is blocking. Consequently, \(\mathrm{ev}_d(W)\) is one of the 287 eligible two-spaces \(U\). Conversely, every linear graph \(U\to\ker(\mathrm{ev}_d)\) is a different pencil whose members have those eligible evaluations. There are exactly \(2^{2(N_d-7)}\) graphs for each \(U\). The same argument preserves the profile and common rational base-point count, giving all formulas without extrapolating from numerical experiments.

**Cubic projective orbits.** With \(d=3\), every evaluation vector has eight cubic lifts, so each of the 287 evaluation pencils has 64 lifts, totaling 18,368. `scripts/orbit_census.py` exhausts all 512 binary \(3\times3\) matrices, retains the 168 invertible ones, expands their substitutions on the ten cubic monomials, and computes the complete orbit of every eligible coefficient-mask triple. The 112 disjoint orbit sets have sizes \(168\) (108 times) and \(56\) (four times); their sizes add to 18,368. Explicit canonical representatives and smooth-member annotations are in `data/orbits.json`.

**Geometric smoothness.** For a homogeneous plane cubic in characteristic two, the Euler relation makes the equation follow from its three partial derivatives. Hence it is geometrically smooth if and only if these three homogeneous quadrics have no common point of \(\mathbf P^2_{\overline{\mathbf F}_2}\). This is equivalent to the degree-four Macaulay map from three copies of the six-dimensional space of quadrics into the fifteen-dimensional space of quartics having full rank 15: the quadrics are then a homogeneous regular sequence, with quotient Hilbert series \((1+t)^3\), and conversely degree-four surjectivity excludes every projective common zero. The first program uses this exact binary rank test; the independent program uses Gröbner ideals on all three affine charts with arithmetic modulo two. Both give the smooth-member distribution above and exactly 784 all-smooth fully nonblocking cubic pencils.

## Verification
From the directory containing this document, execute `python scripts/orbit_census.py` and `python scripts/independent_checker.py` (the latter requires SymPy). Compare their output with `data/orbit_census_expected.txt` and `data/independent_checker_expected.txt`. Their numerical enumerations agree exactly. `data/orbits.json` contains all 112 projective orbit representatives and sizes. All loops run over explicitly finite spaces (128 functions on seven points, 1024 cubics, and 512 binary matrices); no probabilistic sampling or unproved extrapolation is used.

## Relationship to prior work
Asgarli–Ghioca–Yip, *Existence of pencils with nonblocking hypersurfaces*, arXiv:2301.09215, Theorem 1.1, proves existence of fully nonblocking pencils in all degrees at least two. Its discussion of efficient pencils concerns sufficient witnessing lines; it does not enumerate all pencils over the binary projective plane or give their projective orbits. Asgarli–Ghioca–Yip, *Proportion of blocking curves in a pencil*, arXiv:2301.06019, Proposition 2.1 and Remark 2.5, show that prescribed rational partitions or compatible point sets can be realized by a pencil at sufficiently high degree. That existence statement and the interpolation construction are compatible with the present argument but do not specify the precise Fano-plane incidence subspaces, their lift multiplicities, or the 112 projective cubic orbits. The enumeration of all-smooth cubic pencils is a distinct prior classification; the number 784 is a filter within the new all-nonblocking census, not claimed in isolation as a new classification of every all-smooth pencil.

## Limitations
The formula counts degree-\(d\) linear pencils whose **rational members** are nonblocking; it does not assert geometric smoothness, irreducibility, or nonblocking of geometric members over extension fields. The 112-orbit result is specific to cubic equations over \(\mathbf F_2\), not an all-degree orbit theorem. Earlier unindexed fixed-field enumerations could anticipate part of the numerical classification; an independent publication-priority review remains warranted.

## References
1. S. Asgarli, D. Ghioca, C. H. Yip, *Existence of pencils with nonblocking hypersurfaces*, arXiv:2301.09215v2 (first public 2023-01-22), especially Theorem 1.1 and Sections 3–4.
2. S. Asgarli, D. Ghioca, C. H. Yip, *Proportion of blocking curves in a pencil*, arXiv:2301.06019v2 (first public 2023-01-15), especially Proposition 2.1, Remark 2.5, and Section 3.
3. S. Asgarli, D. Ghioca, C. H. Yip, *Plane curves giving rise to blocking sets over finite fields*, arXiv:2208.13299 (2022), particularly Section 3.2 on plane cubics.
