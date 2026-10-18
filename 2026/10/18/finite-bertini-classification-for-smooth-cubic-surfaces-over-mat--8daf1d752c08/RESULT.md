# Finite Bertini classification for smooth cubic surfaces over \(\mathbf F_2\)

## Finding
Let \(S\subset\mathbf P^3_{\mathbf F_2}\) be a geometrically smooth cubic surface and let \(h(S)\) be the number of \(\mathbf F_2\)-rational hyperplanes \(H\) for which the plane cubic \(S\cap H\) is geometrically smooth. Among all \(322{,}560\) geometrically smooth cubic equations there are exactly \(36\) projective equivalence classes. Their complete distribution is:

| \(h(S)\) | Equations | \(\operatorname{PGL}_4(\mathbf F_2)\)-orbits |
|---:|---:|---:|
| 0 | 1,708 | 2 |
| 4 | 11,340 | 2 |
| 6 | 68,320 | 8 |
| 7 | 10,080 | 1 |
| 8 | 94,500 | 10 |
| 9 | 60,480 | 3 |
| 10 | 64,512 | 7 |
| 11 | 10,080 | 1 |
| 12 | 1,540 | 2 |
| **Total** | **322,560** | **36** |

In particular, \(h(S)=0\) if and only if \(\#S(\mathbf F_2)\in\{13,15\}\). Thus there are precisely two projective types of smooth cubic surfaces for which no rational hyperplane has smooth geometric intersection. Representatives in coordinates \((X,Y,Z,W)\) are
\[
X^2W+XW^2+Y^2Z+YZ^2=0,
\qquad
X^2W+XW^2+Y^2Z+YZ^2+XYZ=0.
\]
They have, respectively, \(15\) and \(13\) rational points and projective orbit sizes \(28\) and \(1680\). The attainable values of \(h(S)\) are exactly \(\{0,4,6,7,8,9,10,11,12\}\); in particular, no geometrically smooth cubic surface has \(1,2,3,5,13,14\), or \(15\) smooth rational hyperplane sections.

The two examples are minimal in degree among geometrically smooth projective surfaces in \(\mathbf P^3_{\mathbf F_2}\) with no smooth rational hyperplane section: every smooth linear plane and smooth quadric surface admits a smooth rational hyperplane section.

## Assumptions and scope
An equation is a nonzero homogeneous form of degree three in four variables with coefficients in \(\mathbf F_2\). Scalar multiples cause no duplication because the field has one nonzero scalar. Projective equivalence is by \(\operatorname{PGL}_4(\mathbf F_2)\) acting on homogeneous forms, not abstract surface isomorphism. Smoothness is geometric, i.e. over an algebraic closure. There are exactly \(15\) rational hyperplanes. The table counts equations with projective orbit-size weights, and projective orbits separately.

## Proof
Enumerate the \(2^{20}-1\) nonzero cubic forms. Three coordinate transformations (a swap, a four-cycle and a transvection) generate \(\operatorname{GL}_4(\mathbf F_2)\), of order \(20160\); orbit propagation partitions the coefficient vectors into exactly \(141\) projective equivalence classes. For a homogeneous cubic \(F\), form the degree-five multiplication map
\[
\bigoplus_{j=0}^{3} S_3\longrightarrow S_5,\qquad
(A_0,A_1,A_2,A_3)\longmapsto\sum_{j=0}^{3}A_j\,\partial_{X_j}F.
\]
Here \(S_d\) denotes homogeneous polynomials of degree \(d\) in four variables, and the target has dimension \(56\). Its rank is \(56\) exactly when the four quadratic partials have no common projective zero over the algebraic closure: in that case they form a regular sequence, with quotient Hilbert series \((1+t)^4\), which vanishes in degree five. Conversely, a common projective zero yields nonzero homogeneous quotient pieces in every degree, including five. By Euler's homogeneous identity in characteristic two, a common zero of the partials lies on \(F=0\) because the degree is odd. Thus full rank is equivalent to geometric smoothness. Exact binary elimination leaves \(36\) smooth orbits, totaling \(322{,}560\) coefficient vectors.

For every nonzero rational dual vector \(\lambda\in\mathbf F_2^4\), select a basis of the three-dimensional kernel of \(\lambda\). Substitution of those basis vectors into \(F\) yields a homogeneous ternary cubic \(F_\lambda\). Its three quadratic partials determine the map \(\bigoplus_{i=0}^{2}T_2\to T_4\), whose target has dimension \(15\). By the identical regular-sequence argument, rank \(15\) is equivalent to geometric smoothness of the plane cubic. Test all \(15\) dual vectors for each of the \(36\) smooth orbit representatives. Because projective transformations permute hyperplanes, \(h\) is constant on an orbit. Summing the exact orbit sizes gives the table and the indicated equivalence with the surface rational-point counts. The two masks \(10760\) and \(10792\) correspond to the displayed equations and generate the two exceptional orbits; the coefficient conventions and all representatives are fixed by the standalone scripts.

For minimality, a degree-one smooth surface is a rational plane, admitting a transverse rational plane section. Let \(Q\) be a smooth quadric in \(\mathbf P^3_{\mathbf F_2}\). Its polar bilinear form \(B_Q\) is nondegenerate alternating. Some rational vector \(v\) satisfies \(Q(v)=1\): otherwise the quadratic polynomial vanishes on every one of the \(16\) affine vectors and is the zero polynomial function, which contradicts nondegeneracy of \(B_Q\). On the rational hyperplane \(v^\perp\), the restricted bilinear form has radical precisely \(\langle v\rangle\), while \(Q(v)=1\), so no nonzero vector is simultaneously in that radical and on the quadric. Hence \(Q\cap\mathbf P(v^\perp)\) is a geometrically smooth conic.

## Verification
Run `python verify_census.py` in the extracted artifact directory to reproduce all \(141\) orbit representatives, exact rank tests, all \(36\) smooth classes, and the distribution, and compare with `census_output.json` and `orbit_representatives.tsv`. Then run `python verify_groebner.py` (SymPy required) to reconstruct all \(141\) geometric surface-smoothness decisions using affine-chart Gröbner unit ideals and independently test all \(540\) rational hyperplane sections of the \(36\) smooth representatives. The latter outputs `groebner_output.txt`. The independent symbolic checker found zero discrepancies. All computations are over exact \(\mathbf F_2\) arithmetic, never finite-extension sampling.

## Relationship to prior work
Karaoğlu (2021) already classifies all \(36\) smooth projective cubic-surface classes over \(\mathbf F_2\), with detailed rational-point and geometric statistics. The number \(36\), total \(322{,}560\), and existing representative classification are not new. Kadyrsizova and collaborators (2020) study cubic surfaces in characteristic two, including Frobenius properties. Asgarli, Duan, and Lai (2020) investigate existence of rational transverse linear subspaces over finite fields. The claim here is the complete geometric smooth-rational-hyperplane-section incidence spectrum, its exact failure locus among the projective classes, and the minimal-degree finite-field Bertini examples, which were not located as stated in the inspected prior texts.

## Limitations
The claim concerns only smooth cubic **surfaces** over the exact field \(\mathbf F_2\) in the given projective embedding, and projective rather than abstract equivalence. The enumeration is finite and exhaustive only for this coefficient space. The section spectrum is computable from previously published representatives, so an implicit or unindexed earlier tabulation is a residual priority risk; absence in searches is not proof of absolute novelty. It does not classify hyperplanes over extension fields or higher-degree hypersurfaces. No independent external review has been carried out.

## References
- Kadyrsizova et al., *Cubic Surfaces of Characteristic Two*, arXiv:2007.12018, first posted 2020-07-23, https://arxiv.org/abs/2007.12018.
- Asgarli, Duan, Lai, *Transverse linear subspaces to hypersurfaces over finite fields*, arXiv:2008.11306, first posted 2020-08-25, https://arxiv.org/abs/2008.11306.
- Karaoğlu, *Non-Singular Cubic Surfaces over F_{2^k}*, Turkish Journal of Mathematics 45 (2021), https://doi.org/10.3906/mat-2102-10.
- Asgarli, Ghioca, *Smoothness in pencils of hypersurfaces over finite fields*, arXiv:2203.07169, 2022, https://arxiv.org/abs/2203.07169.
