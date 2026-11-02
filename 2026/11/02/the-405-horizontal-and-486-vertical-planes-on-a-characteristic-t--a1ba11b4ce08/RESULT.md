# The 405 horizontal and 486 vertical planes on a characteristic-two Fermat cubic fourfold

## Finding

Let \(R=\mathbb Z_2[\zeta]/(\zeta^2+\zeta+1)\), the complete unramified quadratic extension of \(\mathbb Z_2\), with residue field \(k=\mathbb F_4\). Define the smooth relative cubic fourfold
\[
 X=V(x_0^3+x_1^3+x_2^3+x_3^3+x_4^3+x_5^3)
 \subset\mathbb P^5_R,
\]
and let \(\mathcal F=\operatorname{Fano}_2(X/R)\) be the scheme of projective planes contained in its fibers, as a closed subscheme of \(\operatorname{Gr}_R(3,6)\). There is an isomorphism of \(R\)-schemes
\[
 \boxed{\mathcal F\cong\coprod_{405}\operatorname{Spec}R\ \sqcup\ \coprod_{486}\operatorname{Spec}k.}
\]
Thus the geometric generic fiber consists of \(405\) reduced planes, while the geometric special fiber consists of \(891\) reduced \(\mathbb F_4\)-rational planes. Exactly the \(405\) coordinate-pairing planes lift to mixed characteristic, and each of the other \(486\) planes is obstructed already over \(R/4R\). Consequently \(\mathcal F\to\operatorname{Spec}R\) is finite and nonflat, despite the smoothness of \(X/R\).

The \(891\) planes split into two orbits under coordinate permutations and coordinatewise multiplication by cubic roots of unity: the \(405\) pairing planes and the \(486\) planes represented by the \(\mathbb F_4\)-linear hexacode. For a plane of each type, the numbers of planes of either type meeting it in a point, line, or not at all are:

| Reference plane | Other type | Disjoint | Meet at a point | Meet along a line | Same plane |
| --- | --- | ---: | ---: | ---: | ---: |
| Pairing | Pairing | 224 | 156 | 24 | 1 |
| Pairing | Hexacode | 288 | 180 | 18 | 0 |
| Hexacode | Pairing | 240 | 150 | 15 | 0 |
| Hexacode | Hexacode | 272 | 186 | 27 | 1 |

The baseline numbers \(405\), \(891\), and the unpartitioned geometric incidence graph are known; the principal conclusion here is the **complete mixed-characteristic scheme structure and exact lifting obstruction**. The orbit-refined table describes the degeneration relative to the horizontal component.

## Assumptions and scope

The base is exactly the displayed \(2\)-adic unramified quadratic ring \(R\); its uniformizer is \(2\). The statement concerns the relative Hilbert/Fano **scheme of linear projective two-planes**, not the four-dimensional Fano variety of lines. The word "lift" means a point of \(\mathcal F(R/4R)\) or \(\mathcal F(R)\) reducing to the specified \(k\)-point. A plane represented by a three-dimensional vector subspace \(L\subset k^6\) is written using its row-space generator matrix. Projective intersections of two such planes have dimensions \(-1,0,1,2\), corresponding to vector-space intersection dimensions \(0,1,2,3\).

Write \(\omega=\overline\zeta\in k\), so \(\omega^2+\omega+1=0\). The standard hexacode plane is the image of
\[
 (u,v,w)\longmapsto
 (u,v,w,u+v+w,u+\omega v+\omega^2w,u+\omega^2v+\omega w).
\]
The classical pairing planes have one independent pair of proportional coordinate variables for each of the three pairs of a perfect matching of the six coordinates.

## Proof

**1. Smoothness and the generic fiber.** The six partial derivatives of the defining cubic are \(3x_i^2\). Since \(3\) is a unit in \(R\), they have no common projective zero, so \(X/R\) is smooth. In characteristic zero the Fermat cubic fourfold has exactly \(405\) planes, given by \(15\) perfect matchings of the coordinates and \(3^3\) choices of cube roots of \(-1\), as established in [2]. Every such plane is defined over \(R\): on paired coordinates one imposes \(x_j=-\zeta^a x_i\), where \(a\in\{0,1,2\}\). All of these planes are reduced points of the generic Fano scheme: at any pairing plane, the first-order normal variations multiply independent squares of three coordinate linear forms, giving a rank-nine map from the nine-dimensional Grassmannian tangent space. Thus the generic fiber has \(405\) reduced points.

**2. All characteristic-two planes are Hermitian and rational over \(\mathbb F_4\).** For a linear subspace \(L\subset\overline k^6\), the vanishing of \(\sum x_i^3\) on \(L\) implies, by comparing the mixed cubic coefficients on every pair of vectors \(v,w\in L\),
\[
 \sum_i v_i^2w_i=0.
\]
Therefore \(L^{[2]}\subset L^\perp\) for the ordinary dot-product orthogonal complement. If \(\dim L=3\), equality holds. Taking coordinatewise Frobenius again yields \(L^{[4]}=L\). Such a subspace descends to \(k=\mathbb F_4\). Over \(k\), the form \(h(v,w)=\sum v_i^2w_i\) is nondegenerate Hermitian, and the planes are exactly its maximal totally isotropic three-subspaces.

In \(k^6\), a nonzero vector is isotropic precisely when its Hamming weight is even, because each nonzero field element has cube \(1\). There are \(693\) isotropic projective points in six dimensions. The four-dimensional nondegenerate Hermitian quotient of an isotropic point has \(45\) isotropic projective points, so there are \(693\cdot45/5=6237\) totally isotropic vector two-subspaces. Each is contained in \(3\) maximal isotropic three-subspaces, and each maximal subspace has \(21\) two-subspaces. Double counting gives
\[
 \#\mathcal F(\overline k)=\frac{6237\cdot3}{21}=891.
\]
These numbers follow directly from counting even-weight vectors in lengths six and four, and from the Hermitian quotients of dimensions four and two.

**3. The two monomial classes.** Let \(L\subset k^6\) be one of the isotropic three-subspaces. If \(L\) contains a weight-two vector, Hermitian orthogonality splits off its two-coordinate support, leaving a length-four Hermitian self-dual code of dimension two. Every nonzero vector of this residual code has even weight; the Singleton bound excludes minimum weight four, so another weight-two vector exists. Repeating gives a direct sum of three disjoint weight-two vectors. Conversely every such split code is isotropic. Its three weight-two supports uniquely determine a perfect matching, and each support allows three nonzero phase ratios: precisely \(15\cdot3^3=405\) pairing planes.

A remaining isotropic \(L\) has minimum weight four and is a \([6,3,4]\) maximum-distance-separable quaternary linear code. After permuting coordinates, any three columns form an information set, so a generator has shape \([I_3\mid A]\). Every entry of \(A\) is nonzero. Row and column scalings normalize the first row and first column of \(A\) to ones. Hermitian row orthogonality then forces the remaining two rows of \(A\), up to the last two column permutations, to be
\[
 A=\begin{pmatrix}1&1&1\\1&\omega&\omega^2\\1&\omega^2&\omega\end{pmatrix}.
\]
This is the displayed hexacode representative; hence the remaining \(891-405=486\) planes form one orbit under the specified monomial group. The uniqueness of this classical length-six code is not claimed as new.

**4. Reducedness of the special Fano scheme.** At either type of plane choose a coordinate grouping and a Grassmannian chart in which its row generator is \([I_3\mid A]\) with \(A\) invertible. For the hexacode this follows from the MDS property, and for the pairing type choose one coordinate from each pair. Write the last three restricted coordinate functions as \(\ell_1,\ell_2,\ell_3\). They form a basis of the three-variable linear forms. The differential of the ten cubic-coefficient equations on the nine Grassmannian parameters maps variations \(\delta\ell_j\) to
\[
 \sum_{j=1}^3\ell_j^2\delta\ell_j.
\]
Because the squares form a basis of the Frobenius-square linear forms, the nine images span exactly the nine distinct cubic monomials other than \(uvw\). Hence the differential has rank nine. Every special-fiber Fano point has zero tangent space; the finite special scheme with \(891\) geometric points is therefore reduced.

**5. A first-order mixed-characteristic obstruction.** Lift the standard hexacode generator to \(R\) by replacing \(\omega\) with \(\zeta\), retaining the indicated plus signs. Direct expansion using \(\zeta^2+\zeta+1=0\) gives the *integral identity*
\[
 \sum_{i=0}^5x_i^3\big|_{\mathrm{lifted\ hexacode}}
 =4(u^3+v^3+w^3)+18uvw.
\]
The restriction vanishes modulo two but has \(uvw\) coefficient \(18\equiv2\pmod4\). Any other \(R/4R\)-plane reducing to this hexacode plane lies in the same normalized Grassmannian chart and differs by \(2\delta\ell_j\). Its change in the cubic restriction modulo four is a linear combination of the nine monomials \(u^3,v^3,w^3,u^2v,u^2w,v^2u,v^2w,w^2u,w^2v\), and therefore cannot change the coefficient of \(uvw\). No lift over \(R/4R\) exists. Coordinate permutations and multiplication by cube roots of unity act on the integral cubic over \(R\) and transitively on the \(486\) hexacode planes, so every one of them has the same obstruction.

**6. Complete local rings and global decomposition.** At every special Fano point nine of the ten cubic equations have invertible Jacobian with respect to the nine Grassmannian parameters. The formal implicit-function theorem over complete \(R\) eliminates these nine equations, leaving completed local ring \(R/(g)\) for some \(g\in2R\). At a pairing plane, the explicit \(R\)-valued section proves \(g=0\). At a hexacode plane, the nonzero obstruction modulo four proves \(g\in2R\setminus4R\), hence \(R/(g)\cong R/(2)=k\). Since both geometric fibers are finite, \(\mathcal F\) is proper and quasi-finite over \(R\), thus finite. The complete Henselian ring \(R\) splits the finite scheme into its individual \(891\) rational-residue local factors, yielding the displayed decomposition.

**7. Refined intersection counts.** For a fixed maximal Hermitian isotropic three-space, there are \(42\) other maximal spaces meeting it in a vector two-space: each of its \(21\) two-spaces lies on two other generators. There are \(336\) meeting it in a vector line: for each of its \(21\) points, the four-dimensional Hermitian quotient supplies \(16\) complementary isotropic lines. The remaining \(512\) are disjoint. For a fixed pairing plane, classify the other perfect matchings as identical (one), sharing exactly one pair (six), or sharing no pairs (eight). The corresponding phase-choice distributions for vector intersection dimensions \((0,1,2,3)\) per matching are respectively \((8,12,6,1)\), \((12,12,3,0)\), and \((18,9,0,0)\). This gives \((224,156,24,1)\) within the pairing class. Subtract from the all-plane counts to obtain the pairing-to-hexacode row. Double counting the incidences between the \(405\) and \(486\) classes gives the reverse row, and subtraction from the all-plane counts gives the remaining hexacode-to-hexacode row.

## Verification

The accompanying self-contained Python program `verify_fermat.py` uses exact arithmetic in \(\mathbb F_4\) and \(\mathbb Z[\zeta]/(\zeta^2+\zeta+1)\). It independently enumerates the \(405\) pairing planes, the \(486\) monomial images of the hexacode, their disjointness and isotropy, and the four complete refined intersection rows. It checks the rank-nine tangent matrices at the two standard representatives, the exact ten cubic coefficients in the lifted hexacode identity, and the Hermitian point counts \(693\) and \(45\). Run `python3 verify_fermat.py`; successful completion prints `FERMAT_CUBIC_FOURFOLD_HEXACODE_405_486_MOD4_AND_INCIDENCE_EXACT_PASS`.

The finite-field enumeration is not substituted for the arguments establishing completeness over the algebraic closure, generic-fiber exhaustiveness, the formal local rings, or the global finite-scheme decomposition; these follow from Steps 1–6. The program uses only the Python standard library.

## Relationship to prior work

Shimada [1] explicitly studies all \(891\) characteristic-two planes and their geometric incidence graph via Edge's correspondence and the Leech lattice. Thus neither \(891\) nor the unrefined incidence graph is a new enumeration. Degtyarev, Itenberg and Ottem [2] establish that the characteristic-zero Fermat cubic fourfold realizes the maximal total of \(405\) planes. The classical quaternary hexacode and its monomial classification are likewise established coding-theoretic objects. Auel, Kulkarni, Petok and Weinbaum [4] count planes on cubic fourfolds over \(\mathbb F_2\), including the Fermat fourfold, but their finite-field census does not determine the complete \(\mathbb F_4\)-geometric plane scheme or its deformation to the dyadic integers. The new structural assertion concerns the **relative Fano scheme over the unramified dyadic ring**, namely the product decomposition into \(405\) horizontal sections and \(486\) reduced vertical points, with a uniform explicit obstruction modulo four. The incidence table identifies those two arithmetically different classes within the known characteristic-two configuration.

## Limitations

Only the specified Fermat equation and complete ring \(R\) are treated; the conclusion is not asserted for arbitrary integral models or deformations of cubic fourfolds. The degeneration occurs in the plane Hilbert scheme although the ambient hypersurface remains smooth. The local-algebra claim concerns geometric special points, not an unsupported global classification of every possible coefficient ring. Historical priority is not guaranteed: a calculation of the same relative scheme might appear in literature not identified by the inspected sources. No independent external validation of the proof has been performed.

## References

[1] Ichiro Shimada, *On Edge's correspondence associated with \(\cdot 222\)*, arXiv:1708.06054 (first public version, 2017-08-21), https://arxiv.org/abs/1708.06054.

[2] Alex Degtyarev, Ilia Itenberg, John Christian Ottem, *Planes in cubic fourfolds*, arXiv:2105.13951 (first public version, 2021-05-28), *Algebraic Geometry* 10 (2023), 228–258, https://arxiv.org/abs/2105.13951.

[3] Frank Gounelas and Alexis Kouvidakis, *The Fermat cubic and monodromy of lines*, arXiv:2302.09562 (2023), https://arxiv.org/abs/2302.09562. Used only as contextual comparison for line loci, not for the plane count.

[4] Asher Auel, Avinash Kulkarni, Jack Petok, Jonah Weinbaum, *A census of cubic fourfolds over \(\mathbb F_2\)*, preprint dated 2023-08-15, https://math.dartmouth.edu/~auel/papers/docs/AKPW_cubic_fourfold_census.pdf. Relevant comparison: Remark 3.6 and §3.4.
