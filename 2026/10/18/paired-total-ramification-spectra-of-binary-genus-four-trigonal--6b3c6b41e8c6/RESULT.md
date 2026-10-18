# Paired total-ramification spectra of binary genus-four trigonal curves on the split quadric

## Finding

Let \(C\) be a geometrically smooth divisor of bidegree \((3,3)\) on \(Q=\mathbf P^1_{\mathbf F_2}\times\mathbf P^1_{\mathbf F_2}\). Its two projections \(\pi_1,\pi_2:C\to\mathbf P^1\) are degree-three morphisms. Write \(t_i(C)\) for the number of rational base points of \(\pi_i\) whose scheme-theoretic fibre is \(3P\) for a rational point \(P\). Up to interchange of the two projections, **exactly six pairs** \((t_1,t_2)\) occur:

| Unordered pair \((t_1,t_2)\) | Smooth defining equations | \(\mathbf F_2\)-isomorphism classes |
|:--:|--:|--:|
| \((0,0)\) | 5856 | 103 |
| \((0,1)\) | 6912 | 96 |
| \((0,2)\) | 1224 | 19 |
| \((0,3)\) | 48 | 2 |
| \((1,1)\) | 1620 | 27 |
| \((1,2)\) | 360 | 5 |
| **Total** | **16020** | **252** |

In particular \(t_1(C)+t_2(C)\le3\), sharply. In this fixed genus-four family the two trigonal structures cannot each have two rational totally ramified fibres. The pair is not determined by the Weil polynomial: the smooth sections with coefficient masks \(6335\) and \(10685\) have respective pairs \((0,2)\) and \((0,0)\), yet their point counts over \(\mathbf F_{2^n}\) for \(n=1,2,3,4\) are simultaneously \((2,8,17,20)\). Their common Weil numerator is
\[
1-T+2T^2+T^3+2T^5+8T^6-8T^7+16T^8.
\]

## Assumptions and scope

Sections are homogeneous bihomogeneous polynomials \(F\in H^0(Q,\mathcal O_Q(3,3))\) over \(\mathbf F_2\); nonzero sections are identified with their defining coefficient vectors (the field has only one nonzero scalar). Smoothness always means smoothness over an algebraic closure. A fibre counted by \(t_i\) is supported at a *single rational geometric point of multiplicity three*, not merely a fibre with a repeated point. Since the residual degree-three factor is uniquely supported and Galois stable, a rational base fibre with a geometric triple point has that point rational. Such ramification is tame, as its index three is prime to the characteristic.

We count only curves lying on the **split** quadric. Their arithmetic genus equals \((3-1)(3-1)=4\). For a smooth curve, adjunction identifies its canonical line bundle with \(\mathcal O_Q(1,1)|_C\), so its Segre embedding is canonical. Its containing quadric is unique: the ideal of a canonical genus-four curve of this type is generated in degrees two and three by the containing quadric and a cubic. Thus the full automorphism group \((\operatorname{PGL}_2(\mathbf F_2)\times\operatorname{PGL}_2(\mathbf F_2))\rtimes C_2\) has order \(72\), and its orbits on the smooth forms are exactly the abstract \(\mathbf F_2\)-isomorphism classes of this family. No claim is made about nonsplit quadrics, singular quadrics, other base fields or arbitrary genus-four curves.

For reproducibility, encode a section by a positive integer \(m\in\{1,\dots,65535\}\) via
\[
F_m=\sum_{0\le i,j\le3}c_{ij}X_0^{3-i}X_1^iY_0^{3-j}Y_1^j,\qquad m=\sum_{0\le i,j\le3}c_{ij}2^{4j+i},\quad c_{ij}\in\mathbf F_2.
\]

## Proof

**1. Exact total-fibre criterion.** At each of the three rational points \([1:0],[1:1],[0:1]\) of the first base line, restrict \(F_m\) to obtain a binary cubic in \((Y_0,Y_1)\). In the coefficient encoding \(\sum_{j=0}^3 a_jY_0^{3-j}Y_1^j\mapsto\sum_j a_j2^j\), it is the cube of a rational linear form if and only if its four-bit mask is one of \(1,8,15\). Indeed these are \(Y_0^3,Y_1^3,(Y_0+Y_1)^3\) in characteristic two. The analogous criterion holds for the second projection. Counting these restrictions produces \(t_1,t_2\) exactly, including fibres at infinity.

**2. A direct sharp-bound obstruction.** Independently of any smooth-curve census, apply the criterion of step 1 to all \(65535\) nonzero coefficient masks. Exactly \(1128\) sections have \(t_1+t_2\ge4\). Of these, \(1110\) are singular at one of the nine rational points, as direct evaluation of the equation and both affine partial derivatives shows. The other \(18\) are one orbit under the \(72\)-element quadric automorphism group, represented by mask \(6854\). On its standard affine chart its equation is
\[
 f(x,y)=x+x^2+x^2y+x^3y+xy^2+x^3y^2+y^3.
\]
Let \(\alpha\in\mathbf F_4\) satisfy \(\alpha^2+\alpha+1=0\). Direct substitution gives
\[
f(\alpha,\alpha+1)=f_x(\alpha,\alpha+1)=f_y(\alpha,\alpha+1)=0.
\]
Thus this final orbit is geometrically singular as well, proving the universal inequality. The bound is attained by the smooth forms of masks \(6289\) (pair \((0,3)\)) and \(6150\) (pair \((1,2)\)), whose smoothness is included in step 3.

**3. Complete census with exact positive/negative certificates.** The \(65535\) nonzero coefficient vectors are examined over finite extensions \(\mathbf F_{2^d}\), \(1\le d\le6\). At each geometric test point on the quadric, the equations \(F=F_x=F_y=0\) give binary linear conditions on the sixteen coefficients. Gaussian elimination enumerates the complete nullspace of these conditions. This constructs explicit singular-point witnesses for exactly \(49515\) nonzero vectors. A separate polynomial-field evaluator rechecks every one of those witnesses. This test alone **does not establish** smoothness of the remaining \(16020\) vectors.

The \(16020\) survivors are partitioned using all \(72\) explicit substitutions of the two \(\operatorname{PGL}_2(\mathbf F_2)\) factors and their swap. Exactly \(252\) orbits result. For every one of the \(252\) representative equations, on each of the four affine charts, the Gröbner basis of \((f,f_x,f_y)\subset\mathbf F_2[x,y]\) is \(\{1\}\). These \(1008\) exact unit-ideal checks establish geometric smoothness on each chart and hence on the entire projective curve. Group invariance then proves that **every** survivor is smooth; with the negative certificates, this is an exhaustive classification, not an inference from a bounded search.

**4. Ramification and orbit tabulation.** For each representative, the three restrictions along each projection are classified by step 1. Each orbit has one unordered pair \(\{t_1,t_2\}\), because the group either preserves the two rulings or swaps them. Summing orbit sizes gives the second column of the table; counting orbits gives its third column. Independently classifying all \(16020\) smooth coefficient masks reproduces the orbit-weighted totals. The orbit list, all representatives and their sizes appear in `data/census.json`.

**5. Same zeta, different ramification.** The four rational-extension point counts for masks \(6335\) and \(10685\) are independently enumerated directly on \(\mathbf P^1(\mathbf F_{2^d})^2\), \(1\le d\le4\), and equal \((2,8,17,20)\). The first four Frobenius power sums determine the first four coefficients of the genus-four Weil numerator by Newton identities; the functional equation determines the remaining four. The resulting numerator is the polynomial displayed above. Yet step 1 gives distinct paired total-ramification spectra, so the zeta function does not imply the new invariant.

## Verification

The self-contained computational package contains `code/count_singular.cpp`, `code/verify_negative.py`, `code/group_orbits.py`, `code/branch_census.py`, `code/verify_positive.py`, `code/verify_sharp_bound.py`, `code/verify_zeta_collision.py`, and `run_checks.sh`. The source files and all data files are embedded together; no previously computed curve-census table is needed. From the package root, execute `./run_checks.sh` with a C++17 compiler and Python 3 with SymPy installed. The command regenerates `data/smooth_bitset.bin`, `data/witness.bin`, and `data/census.json`; the independent negative witness check and the positive Gröbner certificates then run. The exact output of this replay appears in `data/run_report.txt`.

The irreducible moduli used for \(\mathbf F_{2^d}\), for \(d=1,\ldots,6\), are respectively \(z+1\), \(z^2+z+1\), \(z^3+z+1\), \(z^4+z+1\), \(z^5+z^2+1\), and \(z^6+z+1\); irreducibility is directly checkable over \(\mathbf F_2\). The finite-point enumerator is used only to **exclude** singular equations by explicit witnesses; geometric smoothness is established separately by exact ideal computations. All counts in this theorem are exhaustive over the stated \(2^{16}-1\) coefficient vectors.

## Relationship to prior work

Xarles's 2020 census of all genus-four curves over \(\mathbf F_2\) supplies a pre-existing classification of curves and extension-field point counts. Its paper, including its computational method and tabulated results, does not state the two-ruling total-ramification spectrum. The accompanying public Magma program calculates smooth curves and the numbers of extension-field points, not the paired rational triple-fibre distribution. The present result is **not** a new census of abstract genus-four curves; the new theorem is the exact six-stratum paired ramification classification, its sharp obstruction and the equal-zeta distinction.

Looijenga's 2022 study of genus-four curves with a degree-three pencil explains the two natural trigonal morphisms and discriminant geometry in characteristic zero, but it does not compute the arithmetic double-ramification statistics over \(\mathbf F_2\). This result concerns a characteristic-two finite-field specialization and is not a corollary of that complex-analytic classification. Existing classifications of individual curve point counts or Cartier strata are logically weaker than the present paired ramification distribution; an explicit equal-zeta pair illustrates the insufficiency of zeta data.

## Limitations

The conclusion is restricted to the fixed split-quadric family and to *rational* totally ramified fibres. No assertion is made about geometric total ramification away from the rational base points, the full discriminant polynomial, wild simple ramification in characteristic two, or all genus-four curves. The numerical classification is computer-assisted but has exact finite and Gröbner certificates. It is not an independent external audit. An unindexed historical computation or unpublished postprocessing of existing genus-four census files could contain equivalent numbers; this priority risk remains despite the cited source comparisons.

## References

1. X. Xarles, *A census of all genus 4 curves over the field with 2 elements*, arXiv:2007.07822, first posted 2020-07-15, https://arxiv.org/abs/2007.07822 .
2. E. Looijenga, *A ball quotient parametrizing trigonal genus 4 curves*, arXiv:2211.09941, first posted 2022-11-17, https://arxiv.org/abs/2211.09941 .
3. X. Xarles, *Censusforgenus4curvesoverF2* (public computational repository), https://github.com/XavierXarles/Censusforgenus4curvesoverF2 .
