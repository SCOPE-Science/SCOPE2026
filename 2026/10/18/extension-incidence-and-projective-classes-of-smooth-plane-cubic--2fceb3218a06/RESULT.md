# Extension incidence and projective classes of smooth plane-cubic pencils over \(\mathbf F_2\)

## Finding

Let \(V=\mathbf F_2[X,Y,Z]_3\), and call an \(\mathbf F_2\)-linear subspace **all-smooth** if every nonzero member defines a geometrically smooth plane cubic. For a two-dimensional all-smooth subspace (pencil) \(P\), define \(e(P)\) to be the number of three-dimensional all-smooth subspaces (nets) containing \(P\), and \(b(P)\) the number of common \(\mathbf F_2\)-rational points of its three members.

**Theorem (complete extension-incidence classification).** Among the \(5544\) such pencils, the possible values of \(e(P)\) are **exactly** \(0,1,2,3\), with respective multiplicities \(1680,1848,1848,168\). The pencils form exactly **37** orbits under \(\operatorname{PGL}_3(\mathbf F_2)\), with stabilizer-order distribution \(31\) orbits of order \(1\), one of order \(2\), three of order \(3\), and two of order \(4\). Their complete joint distribution by extension number \(e\) and rational base-point number \(b\) is:

| \(e\) | \(b=0\) | \(b=1\) | \(b=2\) | \(b=3\) | total pencils |
|---:|---:|---:|---:|---:|---:|
| 0 | 504 | 672 | 504 | 0 | 1680 |
| 1 | 840 | 504 | 336 | 168 | 1848 |
| 2 | 672 | 840 | 168 | 168 | 1848 |
| 3 | 0 | 0 | 168 | 0 | 168 |
| **Total** | **2016** | **2016** | **1176** | **336** | **5544** |

In particular, **1680 all-smooth pencils do not extend to any all-smooth net**, while exactly \(168\) extend to three different nets. A pencil extends to at most three such nets, and the three-extension case has precisely two rational base points. The number of projective orbits in each nonempty cell, listed in the same order as the table, is \((3,6,3)\), \((5,5,2,1)\), \((4,5,1,1)\), and \((1)\), respectively. The supplied CSV lists a canonical integer-mask representative of every one of the 37 orbits, along with its orbit size, stabilizer, rational base points, and extension count.

The total of \(5544\) pencils and the total of \(864\) nets were determined in an earlier individual-net census and are **not** asserted here as new. The claimed new classification is the extension multiplicity, its incidence with rational base points, and the full 37-orbit pencil structure.

## Assumptions and scope

All coefficients, subspaces, and transformations are defined over exactly \(\mathbf F_2\). Smoothness is **geometric**, meaning no singular point over the algebraic closure, not just nonsingularity at rational points. Only the three \(\mathbf F_2\)-members of a pencil must be geometrically smooth; members at non-rational parameters may be singular. The transformations form \(\operatorname{PGL}_3(\mathbf F_2)=\operatorname{GL}_3(\mathbf F_2)\), of order \(168\). The orbit classification is for projective plane embeddings and pencils, not for abstract isomorphism classes of elliptic curves.

Fix monomial order \(M=(Z^3,YZ^2,Y^2Z,Y^3,XZ^2,XYZ,XY^2,X^2Z,X^2Y,X^3)\); in formulae the monomials are always typeset mathematically, while executable files use integer encodings. Encode a cubic \(F=\sum_{i=0}^{9}c_iM_i\) by \(m(F)=\sum_{i=0}^{9}c_i2^i\). For two distinct nonzero cubics \(F,G\), the three members of their pencil have masks \(a=m(F)\), \(b=m(G)\), and \(a\mathbin{\mathrm{xor}}b=m(F+G)\). The canonical pencil representation sorts these three integers.

## Proof

**1. Exact geometric smoothness criterion.** Let \(F_X,F_Y,F_Z\) be the three quadratic partial derivatives of a cubic \(F\) over \(\mathbf F_2\). Euler's homogeneous identity gives \(XF_X+YF_Y+ZF_Z=3F=F\), so \(F\) is geometrically singular precisely when its three partials have a common nonzero zero over the algebraic closure. Let \(S=\mathbf F_2[X,Y,Z]\), and consider the degree-four multiplication map
\[
\Phi_F:S_2^{\oplus3}\longrightarrow S_4,\qquad
(A,B,C)\longmapsto AF_X+BF_Y+CF_Z.
\]
If the three quadratic partials have no projective common zero, they generate an ideal of height three, hence form a homogeneous regular sequence in the Cohen–Macaulay ring \(S\). The resulting complete-intersection Hilbert series is \((1+t)^3\), so \((S/(F_X,F_Y,F_Z))_4=0\), and \(\Phi_F\) is surjective. Conversely, if the partials have a common projective zero, evaluation at that point is a nonzero functional on \(S_4\) annihilating their degree-four multiples, so \(\Phi_F\) is not surjective. Therefore
\[
F\text{ is geometrically smooth}\iff\operatorname{rank}_{\mathbf F_2}\Phi_F=\dim_{\mathbf F_2}S_4=15.
\]
The matrix has 15 rows and 18 columns and is evaluated by exact bitwise Gaussian elimination, not by extension-field point sampling. Exhaustively testing all \(1023\) nonzero masks yields exactly \(336\) smooth cubics. An independently written checker obtains the identical smooth-mask set from Gröbner bases of the dehomogenized Jacobian ideal on all three affine charts.

**2. Every pencil, exactly once.** Let \(\mathcal S\) be the set of 336 smooth nonzero masks. Enumerate all ordered pairs \(a<b\) in \(\mathcal S\) such that \(a\mathbin{\mathrm{xor}}b\in\mathcal S\), then canonically sort the triple \(\{a,b,a\mathbin{\mathrm{xor}}b\}\). Each two-dimensional binary subspace has exactly three nonzero elements, so deduplication of these triples counts each pencil exactly once. This gives \(5544\) pencils. Its rational base-point count is calculated at the seven points of \(\mathbf P^2(\mathbf F_2)\) by simultaneous equation evaluation.

**3. Counting extensions without duplicates.** For a pencil \(P=\langle F,G\rangle\), a mask \(h\in\mathcal S\setminus P\) generates an all-smooth net precisely when the three additional forms \(h+F,h+G,h+F+G\) also belong to \(\mathcal S\). Every containing net has exactly four elements outside the pencil, all passing this test, while two masks from different containing nets cannot generate the same three-space. Hence the number of successful masks divided by four is **exactly** \(e(P)\). This computes every entry of the joint table. The incidence identity
\[
\sum_P e(P)=1848+2(1848)+3(168)=6048=7(864)
\]
checks the count against the fact that each three-dimensional binary net contains seven pencils; it is an internal cross-check, not an assumption that proves the distribution.

**4. Complete projective orbit classification.** Enumerate the \(168\) invertible binary \(3\times3\) matrices. For each, substitute the three binary linear forms into the ten cubic monomials, which gives the induced linear transformation of the 10-bit coefficient space. The orbit of each canonical pencil triple is then computed and removed from the unseen set. Every orbit is verified to preserve \(e\) and \(b\). The resulting 37 orbits have stabilizers as stated. An independent Burnside count, using matrix orders, yields:

| Matrix order | Number of matrices | Fixed all-smooth pencils |
|---:|---:|---:|
| 1 | 1 | 5544 |
| 2 | 21 | 8 |
| 3 | 56 | 6 |
| 4 | 42 | 4 |
| 7 | 48 | 0 |

Thus the orbit count is \((5544+21\cdot8+56\cdot6+42\cdot4)/168=37\). The orbit representative CSV provides all 37 individual cases and their group-theoretic multiplicities, rather than relying only on aggregate counts.

## Verification

Run `python3 verify_pencils.py` with the Python standard library to reproduce the full exact census, joint extension/base distribution, 37 orbit representatives, stabilizers, and Burnside check. Its canonical JSON output is included as `census.json`. Run `python3 check_groebner.py` with SymPy version 1.12 or newer for an independently implemented Gröbner-basis smoothness and extension/base classification; its output is `independent.json`. In the completed verification, the two independent algorithms produced identical sets of 336 geometrically smooth masks (SHA-256 of the comma-separated ascending mask list: `60e0382b0c4781b08e42f42af5bf66966645d068899e076a518f714438510374`), matching the extension table in every cell. All 37 orbit representatives are tabulated in `orbit_representatives.csv` using the monomial convention above.

The exact ring-theoretic rank criterion and exhaustive finite algebra underpin the universal assertions; the independent numerical agreement is a cross-check, not a substitute for those arguments.

## Relationship to prior work

Asgarli–Ghioca, *Smoothness in pencils of hypersurfaces over finite fields* (arXiv:2203.07169, first publicly posted 2022-03-14), formulates the all-rational-members-smooth problem and proves existence for sufficiently large fields. Asgarli–Ghioca–Reichstein, *Linear families of smooth hypersurfaces over finitely generated fields* (arXiv:2207.00918), proves a general existence/maximal-dimension theorem; the existence of smooth plane-cubic nets over \(\mathbf F_2\) is not the contribution here. A prior finite plane-cubic **net** census already lists 336 smooth individual cubics, 5544 pencils, 864 nets, and eight net orbits. It neither classifies **all** pencil orbits nor records how many nets extend each pencil: the 1680 nonextendible pencils are invisible from a census restricted to nets.

Asgarli–Ghioca, *Linear system of geometrically irreducible plane cubics over finite fields* (arXiv:2407.18104), addresses the weaker irreducibility condition and larger systems; its Appendix A gives specific examples, not the present extension table. Moschetti–Pirola–Stoppino, *Pencils of plane cubics with one base point* (arXiv:2407.04569), classifies a different characteristic-zero condition involving one **geometric** base point, not this binary rational-base/extension incidence. Targeted literature and mathematical research-record searches did not identify the present exact classification; search failure alone is not a proof of historical priority.

## Limitations

The theorem is confined to degree-three homogeneous forms over the exact field \(\mathbf F_2\), coordinate projective equivalence, and the three rational members of each pencil. The number of common rational base points \(b\) should not be mistaken for the total number of geometric base points or for the scheme-theoretic multiplicities in their degree-nine intersection. Nothing is asserted for all members after extension of the pencil's parameter field. Although the enumeration is exact and complete under the stated hypotheses, an unpublished or unindexed classification with equivalent conclusions may exist. The independent external scientific audit has not been performed.

## References

1. Shamil Asgarli and Dragos Ghioca, *Smoothness in pencils of hypersurfaces over finite fields*, arXiv:2203.07169, 2022-03-14. https://arxiv.org/abs/2203.07169
2. Shamil Asgarli, Dragos Ghioca and Zinovy Reichstein, *Linear families of smooth hypersurfaces over finitely generated fields*, arXiv:2207.00918, 2022. https://arxiv.org/abs/2207.00918
3. Shamil Asgarli and Dragos Ghioca, *Linear system of geometrically irreducible plane cubics over finite fields*, arXiv:2407.18104, 2024. https://arxiv.org/abs/2407.18104
4. R. Moschetti, G. P. Pirola and L. Stoppino, *Pencils of plane cubics with one base point*, arXiv:2407.04569, 2024. https://arxiv.org/abs/2407.04569
