# Complete maximal smooth genus-two nets on the binary split quadric

## Finding
Let \(S=\mathbf P^1_{\mathbf F_2}\times\mathbf P^1_{\mathbf F_2}\), and let \(V=H^0(S,\mathcal O_S(2,3))\), a vector space of dimension \(12\). Call a nonzero section *smooth* when its zero divisor is geometrically smooth over \(\overline{\mathbf F}_2\). Call a linear subspace \(W\subseteq V\) *all-smooth* when every nonzero section in \(W\) is smooth. Then:

1. There are precisely \(1116\) smooth nonzero sections and \(44{,}070\) all-smooth vector-space pencils of dimension \(2\).
2. There are precisely \(8964\) all-smooth vector-space nets of dimension \(3\). Every such net has seven smooth genus-two curves, and no all-smooth subspace has dimension \(4\) or greater. Thus maximal *projective* dimension is \(2\).
3. Under \(\operatorname{Aut}_{\mathbf F_2}(S,\mathcal O_S(2,3))=\operatorname{PGL}_2(\mathbf F_2)\times\operatorname{PGL}_2(\mathbf F_2)\), all \(8964\) nets have trivial stabilizer; the systems comprise exactly \(249\) projective-automorphism orbits of size \(36\) each.
4. The unordered multisets of rational-point counts of the seven smooth curves in a net belong to precisely the following \(14\) types. These account for every net:

| Sorted rational-point counts of seven members | Nets | Automorphism orbits |
|:--|--:|--:|
| \((0,3,4,4,5,5,6)\) | 36 | 1 |
| \((0,4,4,4,5,5,5)\) | 288 | 8 |
| \((1,2,4,4,5,5,6)\) | 36 | 1 |
| \((1,3,3,5,5,5,5)\) | 216 | 6 |
| \((1,3,4,4,4,5,6)\) | 576 | 16 |
| \((1,4,4,4,4,5,5)\) | 1,152 | 32 |
| \((2,2,2,5,5,5,6)\) | 72 | 2 |
| \((2,2,3,4,5,5,6)\) | 216 | 6 |
| \((2,2,4,4,5,5,5)\) | 648 | 18 |
| \((2,3,3,4,4,5,6)\) | 432 | 12 |
| \((2,3,4,4,4,5,5)\) | 3,600 | 100 |
| \((3,3,3,3,5,5,5)\) | 180 | 5 |
| \((3,3,3,4,4,4,6)\) | 144 | 4 |
| \((3,3,4,4,4,4,5)\) | 1,368 | 38 |
| **Total** | **8964** | **249** |

These are counts of linear subspaces in a *fixed* coefficient space, not counts of abstract isomorphism classes of genus-two curves.

## Assumptions and scope
The coordinates of \(S\) are \(([X_0:X_1],[Y_0:Y_1])\). The standard basis of \(V\) is \(M_{ij}=X_0^{2-i}X_1^iY_0^{3-j}Y_1^j\), with \(0\leq i\leq2\) and \(0\leq j\leq3\). Encode a form \(F=\sum\epsilon_{ij}M_{ij}\) as the integer \(m(F)=\sum\epsilon_{ij}2^{4i+j}\) in \(1,\ldots,4095\). Addition of sections corresponds to bitwise exclusive-or of masks.

A concrete net is spanned by masks \(386,1566,2597\), with seven nonzero mask values \(386,1566,1948,2597,2983,3131,3513\). The geometry is *geometric* smoothness, not the weaker absence of rational singular points. Every smooth bidegree-\((2,3)\) divisor on the split quadric is geometrically connected: a decomposition into effective components of total bidegree \((2,3)\) would contain two components with positive intersection, hence a singular point. The adjunction formula gives \(g=(2-1)(3-1)=2\).

## Proof
**Exact geometric smoothness criterion.** For each nonzero mask, dehomogenize its bidegree-\((2,3)\) polynomial on the four affine charts \(X_0\ne0\), \(X_1\ne0\) and \(Y_0\ne0\), \(Y_1\ne0\). In any chart, let \(f\in\mathbf F_2[x,y]\) denote the dehomogenized equation. By the Jacobian criterion, this chart contains a geometric singularity precisely when the ideal \((f,\partial f/\partial x,\partial f/\partial y)\) is proper over the algebraic closure. The ideal is proper over the algebraic closure if and only if it is proper over \(\mathbf F_2\); by the weak Nullstellensatz this is equivalent to its reduced Gröbner basis not being \(\{1\}\). The four charts cover \(S\). The packaged exhaustive script checks the four ideals for each of the \(2^{12}-1=4095\) nonzero masks and finds exactly \(1116\) smooth masks. The seven masks of the displayed example are in that set.

**Subspace census.** Let \(T\) be the resulting set of smooth masks. Enumerate all pairs \(a<b\) from \(T\), put \(c=a\oplus b\), and retain the pencil if \(c\in T\), imposing \(a<b<c\) for uniqueness. This gives \(44{,}070\) pencils. For each pencil \(\{a,b,c\}\), enumerate \(d\in T\setminus\{a,b,c\}\) and retain \(d\) if \(a\oplus d,b\oplus d,c\oplus d\in T\). The four new masks together with \(a,b,c\) form an all-smooth net. The computation finds \(250{,}992\) pencil-extension pairs. Each three-dimensional \(\mathbf F_2\)-subspace contains exactly seven two-dimensional subspaces and, relative to each one, exactly four possible extension vectors in that three-space. Hence every net is counted exactly \(7\cdot4=28\) times, giving \(250{,}992/28=8964\). Canonical sorting and deduplication independently reproduce the same net count.

**Maximal dimension.** Fix any \(\mathbf F_2\)-point \(P\) of \(S\). The first-jet map from \(V\) into the three-dimensional space \(\mathcal O_S(2,3)|_P\oplus (T_P^*S\otimes\mathcal O_S(2,3)|_P)\) sends a section to its value and its two first-order derivatives at \(P\). Every vector subspace of dimension at least four has a nonzero element in this jet map's kernel, defining a divisor singular at \(P\). Thus every all-smooth subspace has dimension at most three. An exhaustive extension check independently confirms that none of the enumerated nets is contained in an all-smooth four-space.

**Automorphism orbits and arithmetic spectra.** The two rulings are distinguished by bidegrees \(2\) and \(3\), so the polarized surface's automorphism group is \(\operatorname{PGL}_2(\mathbf F_2)^2\), of order \(6\cdot6=36\). For each of its \(36\) elements, substitute the corresponding two binary linear transformations into the twelve monomials, reduce coefficients modulo two, and act on each net. Exhaustive orbit calculation gives \(249\) distinct orbits, all of cardinality \(36\). Finally, evaluate every section of every net at all \(3\cdot3=9\) rational points of \(S\), sort the seven resulting point counts, and accumulate the above \(14\)-type table. The counts sum to \(8964\), and the orbit column sums to \(249\).

## Verification
The standalone files `verify_geometry.py`, `verify_nets.cpp`, and `verify_all.sh` recreate the full census from the original coefficient space. The Python script requires SymPy and evaluates exactly \(4095\) four-chart Gröbner-basis tests, writing a sorted smooth-mask list. The C++17 program enumerates pencils, all nets and their exact extension incidences, proves the absence of four-spaces computationally, evaluates the rational-point strata, and recomputes the full polarized automorphism action. Execute `sh verify_all.sh` in the extracted file directory with `python`, `sympy`, and `g++` available. `smooth_masks.txt` and `verification_output.txt` are included as independently inspectable exact reference outputs. The compiled binary is produced by the script and is not a mathematical dependency. The checked reference output ends in `VERIFY_OK`.

## Relationship to prior work
Asgarli and Ghioca posed the existence of linear systems with smooth rational members over finite fields and gave examples for conics and quadric surfaces in *Smoothness in pencils of hypersurfaces over finite fields* (arXiv:2203.07169, first public March 14, 2022). Asgarli, Ghioca and Reichstein gave general existence and maximal-dimension results for hypersurfaces in projective space in *Linear families of smooth hypersurfaces over finitely generated fields* (arXiv:2207.00918, first public July 2, 2022). Their upper-bound argument is analogous to the first-jet observation here, which is not claimed as a new general principle. Their setting is degree-\(d\) hypersurfaces in \(\mathbf P^n\), not the entire polarized linear system \(|\mathcal O_S(2,3)|\) on \(\mathbf P^1\times\mathbf P^1\); neither inspected result provides the \(8964\) census, its \(249\) orbits, or the \(14\) genus-two arithmetic spectra. Asgarli and Ghioca's later work on *geometrically irreducible plane cubics* (arXiv:2407.18104) concerns a different embedded curve family and a weaker irreducibility condition.

## Limitations
The enumeration is exact only for the fixed polarized split quadric \((S,\mathcal O_S(2,3))\) over \(\mathbf F_2\). Neither arbitrary genus-two curves nor arbitrary quadratic twists nor larger fields are classified. The orbit equivalence is by polarized \(\mathbf F_2\)-automorphisms of \(S\), not by abstract curve isomorphism. The primary literature search cannot eliminate the possibility of an unindexed equivalent enumeration; independent outside validation has not been performed. The proof relies on the reproducible exhaustive symbolic computation for its numerical classification, while the general dimension bound and incidence-multiplicity argument are algebraic.

## References
1. S. Asgarli and D. Ghioca, *Smoothness in pencils of hypersurfaces over finite fields*, arXiv:2203.07169 (2022), https://arxiv.org/abs/2203.07169.
2. S. Asgarli, D. Ghioca and Z. Reichstein, *Linear families of smooth hypersurfaces over finitely generated fields*, arXiv:2207.00918 (2022), https://arxiv.org/abs/2207.00918.
3. S. Asgarli and D. Ghioca, *Linear system of geometrically irreducible plane cubics over finite fields*, arXiv:2407.18104 (2024), https://arxiv.org/abs/2407.18104.
