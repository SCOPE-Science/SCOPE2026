# All-smooth pencils of binary cubic surfaces and their rational base loci

## Finding
Let \(V=\mathbf F_2[x_0,x_1,x_2,x_3]_3\) be the \(20\)-dimensional coefficient space of cubic forms. A pencil is a two-dimensional vector subspace \(P\subset V\), and it is **all-smooth** if every one of its three nonzero members defines a geometrically smooth cubic surface in \(\mathbf P^3\). Put \(b(P)=\#\bigcap_{F\in P\setminus\{0\}}V(F)(\mathbf F_2)\).

There are exactly \(5,002,905,600\) all-smooth pencils. The complete distribution of \(b(P)\), as pairs \((b(P),\#P)\), is:

| \(b(P)\) | Pencils |
|---:|---:|
| 0 | 164,589,376 |
| 1 | 635,685,120 |
| 2 | 1,171,931,040 |
| 3 | 1,292,537,400 |
| 4 | 956,743,200 |
| 5 | 504,716,688 |
| 6 | 198,190,720 |
| 7 | 59,318,280 |
| 8 | 15,402,240 |
| 9 | 3,113,600 |
| 10 | 493,920 |
| 11 | 148,680 |
| 12 | 30,240 |
| 13 | 5,040 |
| 14 | 0 |
| 15 | 56 |

In particular, \(b(P)=14\) is impossible. The \(56\) extremal pencils with \(b(P)=15\) form a single orbit under \(\operatorname{PGL}_4(\mathbf F_2)\), each with stabilizer order \(360\). Each contains precisely five common \(\mathbf F_2\)-rational lines, which are pairwise skew and partition the \(15\) rational points of the ambient projective space.

## Assumptions and scope
All coefficients and projective transformations are over \(\mathbf F_2\). Geometric smoothness means absence of singular points after extension to an algebraic closure. The three nonzero equations, not merely their rational-point loci, must all define smooth cubic hypersurfaces. The base-point statistic counts only \(\mathbf F_2\)-rational points; no assertion is made that the scheme-theoretic intersection curve is smooth. Two forms over \(\mathbf F_2\) determine a unique hypersurface without a nontrivial scalar ambiguity.

## Proof
Write \(S=\mathbf F_2[x_0,x_1,x_2,x_3]\). For a cubic \(F\), the four derivatives \(F_{x_i}\) are quadrics. The corresponding linear map
\[
\Phi_F:S_3^{\oplus 4}\longrightarrow S_5,\qquad (A_i)_i\longmapsto\sum_{i=0}^3 A_iF_{x_i}
\]
is surjective exactly when the derivatives have no common projective zero over the algebraic closure. Indeed, if they have no common projective zero they form a homogeneous regular sequence of four quadrics in four variables. Its Artinian quotient has Hilbert series \((1+t)^4\), so the degree-five quotient vanishes. Conversely, surjectivity forces every quintic into the gradient ideal and prevents a common nonzero projective zero. Euler's identity gives \(\sum x_iF_{x_i}=3F=F\) in characteristic two, so a common derivative zero is precisely a singular point of \(V(F)\). Hence geometric smoothness is equivalent to \(\operatorname{rank}(\Phi_F)=\dim S_5=56\).

Enumerate all \(2^{20}-1\) nonzero cubic forms by their monomial coefficient vectors, using the monomial order implemented in `cubic_surface.cpp`. Adjacent variable swaps and the shear \(x_0\mapsto x_0+x_1\) generate \(\operatorname{GL}_4(\mathbf F_2)\), of order \(20,160\). Breadth-first enumeration under these four generators gives \(141\) coefficient orbits, of which exactly \(36\) pass the exact \(56\)-rank test. The total size of these smooth orbits is \(322,560\). Orbit invariance makes the check exhaustive, not a sample.

Let \(\mathcal S\subset V\) be the resulting set of smooth forms, and for each of its \(36\) representatives \(F_i\) let \(w_i\) be its orbit size. Define \(Z(F)\subset\mathbf P^3(\mathbf F_2)\) as the zero set of \(F\) on the \(15\) rational points. For \(0\le k\le15\) compute, by exact binary evaluation,
\[
H_k=\frac16\sum_{i=1}^{36}w_i\cdot\#\{G\in\mathcal S:F_i+G\in\mathcal S,\ |Z(F_i)\cap Z(G)|=k\}.
\]
The denominator is six because a two-dimensional \(\mathbf F_2\)-space has exactly six ordered bases \((F,G)\), all giving the same three nonzero members. This formula produces the displayed histogram and its sum \(5,002,905,600\). An independent Walsh-transform calculation gives the total ordered-basis count
\[
2^{-20}\sum_{\chi\in\widehat V}\bigl(\sum_{F\in\mathcal S}\chi(F)\bigr)^3
=30,017,433,600.
\]
The orbit-weighted point-histogram calculation is independently reproduced using a separate implementation.

The absence of \(14\) common rational points also has a direct explanation. Summing the value of any cubic monomial over \(\mathbf F_2^4\) gives zero: its support involves at most three distinct variables, leaving a freely varying fourth coordinate. Therefore every cubic form has an even number of nonzeros among the \(15\) nonzero vectors. If two forms vanished simultaneously at \(14\) projective points, each would have to vanish at the fifteenth. Thus a pencil cannot have exactly \(14\) base points.

For the extremal case, the subspace of cubics vanishing on every rational point consists precisely of
\[
F_A=\sum_{0\le i<j\le3}a_{ij}(x_i^2x_j+x_ix_j^2),
\]
where \(A=(a_{ij})\) is an alternating \(4\times4\) matrix. Its gradient is \(A\,(x_0^2,x_1^2,x_2^2,x_3^2)^T\), hence it is smooth exactly when \(A\) is nonsingular. There are \(\lvert\operatorname{GL}_4(\mathbf F_2)\rvert/\lvert\operatorname{Sp}_4(\mathbf F_2)\rvert=28\) nonsingular alternating forms. Each admits exactly \(12\) other nonsingular partners whose sum is nonsingular, yielding \(28\cdot12/6=56\) all-smooth pencils with fifteen rational base points. A complete enumeration of these \(56\) pencils under the same four projective generators gives one orbit, so each stabilizer has size \(20,160/56=360\). Restriction to the \(35\) rational projective lines establishes that any two members have exactly five common lines, with pairwise empty intersections; five triples of rational points consequently partition the \(15\) points.

## Verification
Run `g++ -O3 -std=c++17 cubic_surface.cpp -o cubic_surface && ./cubic_surface` to regenerate `cubic_surface_smooth.bin`, `cubic_surface_orbits.tsv`, and the initial orbit census. Run `g++ -O3 -std=c++17 pencil_surface_census.cpp -o pencil_surface_census && ./pencil_surface_census` to regenerate the full histogram. The independent checks are `python verify_surface_groebner.py`, `python verify_surface_pencils.py` (requires NumPy), and `python maxbase_geometry.py`. All paths are relative to the working directory containing these files. The first independent checker confirms \(144\) Gröbner unit ideals for the \(36\) orbit representatives on four affine charts; the second checks the total by a Walsh transform and all \(16\) rational-base bins by separately coded evaluation. The third rederives the \(56\)-pencil extremal orbit and the five skew common rational lines. The embedded outputs are the expected exact outputs, not substitutes for the executable checks.

## Relationship to prior work
Asgarli–Ghioca study the existence of smooth members throughout finite-field pencils, including low-degree examples, but do not supply this exact cubic-surface-pencil census. Karaoğlu's classification, building on Dickson and Cooley, establishes the \(36\) smooth projective equivalence classes of **individual** binary cubic surfaces (and related point, line and Eckardt data); those individual-surface figures are inputs and checks here, not the asserted new conclusion. Kadyrsizova–Kenkel–Page–Singh–Smith–Vraciu–Witt classify characteristic-two cubic surfaces by Frobenius splitting, but not the additive compatibility of three independent smooth equations. This theorem instead counts \(\mathbf F_2\)-lines wholly contained in the complement of the discriminant in the parameter space, with a complete rational base-point refinement and an extremal spread geometry.

## Limitations
These results are restricted to \(\mathbf F_2\), four homogeneous variables and cubic degree. The count is exact computational enumeration with independently checked mathematical criteria, not a closed formula for general finite fields. No claim is made that the common intersection of two generators is geometrically reduced, irreducible, or smooth. The orbit statement concerns only the \(56\) maximal rational-base pencils, not all five billion pencils. Existing individual-cubic classifications and bounds are not claimed as new. Literature searches cannot exclude unindexed earlier pencil enumerations; no independent external audit has been performed.

## References
- S. Asgarli and D. Ghioca, *Smoothness in pencils of hypersurfaces over finite fields*, arXiv:2203.07169 (initial posting 2022-03-14), https://arxiv.org/abs/2203.07169.
- F. Karaoğlu, *Non-Singular Cubic Surfaces over* \(\mathbf F_{2^k}\), Turkish Journal of Mathematics **45** (2021), 2492–2510, DOI:10.3906/mat-2102-10, https://journals.tubitak.gov.tr/math/vol45/iss6/11/.
- Z. Kadyrsizova et al., *Cubic Surfaces of Characteristic Two*, arXiv:2007.12018 (initial posting 2020-07-23), https://arxiv.org/abs/2007.12018.
