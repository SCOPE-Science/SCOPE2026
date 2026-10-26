# Eight projective orbit types of smooth elliptic quartic intersections over \(\mathbf F_2\)

## Finding
Let \(W=H^0(\mathbf P^3_{\mathbf F_2},\mathcal O(2))\), a vector space of dimension ten. Exactly \(40,320\) of the \(174,251\) two-dimensional \(\mathbf F_2\)-subspaces of \(W\) have geometrically smooth scheme-theoretic intersections of their two generating quadrics. Each is a connected smooth complete-intersection curve of genus one and degree four. Under \(\operatorname{PGL}_4(\mathbf F_2)\), of order \(20,160\), these pencils form precisely eight orbits.

The canonical coefficient-mask representatives and orbit sizes are as follows. The ordering of the ten monomials is \(X_0^2,X_1^2,X_2^2,X_3^2,X_0X_1,X_0X_2,X_0X_3,X_1X_2,X_1X_3,X_2X_3\). Each representative is encoded by the masks of its three nonzero quadrics, in ascending order.

| Three coefficient masks | Orbit size | Rational points on intersection | Rational points on three quadrics | Projective stabilizer |
|---|---:|---:|---|---:|
| (20, 200, 220) | 10,080 | 3 | (7,9,5) | 2 |
| (20, 202, 222) | 5,040 | 5 | (7,9,9) | 4 |
| (20, 203, 223) | 5,040 | 1 | (7,5,5) | 4 |
| (20, 523, 543) | 2,520 | 4 | (7,7,9) | 8 |
| (20, 527, 539) | 5,040 | 2 | (7,7,5) | 4 |
| (20, 844, 856) | 2,520 | 4 | (7,7,9) | 8 |
| (192, 357, 421) | 5,040 | 2 | (9,5,5) | 4 |
| (192, 358, 422) | 5,040 | 4 | (9,5,9) | 4 |

In particular, there are \(5,040,10,080,10,080,10,080,5,040\) pencils with respectively \(1,2,3,4,5\) rational points on the intersection. Two inequivalent orbits of size \(2,520\) have both four rational intersection points and the same three-quadric point spectrum \((7,7,9)\).

## Assumptions and scope
The ground field is exactly \(\mathbf F_2\); smoothness and scheme-theoretic intersection are over the algebraic closure, not merely at rational points. Every pencil is an unmarked two-dimensional linear subspace (thus the three nonzero members are unordered). Equivalence is by projective linear change of the four ambient coordinates, not abstract isomorphism of genus-one curves. Every one of the \(174,251=(1023\cdot1022)/6\) pencils is included, including those with singular quadrics.

## Proof
Write any quadric as \(Q=\sum_i a_iX_i^2+\sum_{i<j}b_{ij}X_iX_j\). Its gradient is \(B_Q X\), where \(B_Q\) is the alternating matrix having off-diagonal entries \(b_{ij}\). By the Jacobian criterion, the complete intersection of independent quadrics \(Q_0,Q_1\) is smooth precisely when no geometric point satisfying both equations has linearly dependent gradients. This means that for some nonzero parameter \((s:t)\) the pencil member \(Q_{s,t}=sQ_0+tQ_1\) has a point in \(\mathbf P(\ker B_{s,t})\) also vanishing on the other independent member.

The degree-two Pfaffian \(\operatorname{Pf}(B_{s,t})=b_{01}(s,t)b_{23}(s,t)+b_{02}(s,t)b_{13}(s,t)+b_{03}(s,t)b_{12}(s,t)\) controls polar singularities: if it is not identically zero, all possible singular parameters are rational over \(\mathbf F_4\). At one of these parameters, the alternating polar has rank two or zero. In rank two, its kernel is a two-plane \(K\); the restricted quadratic \(Q_{s,t}|_K\) has no mixed polar terms and, over the perfect field \(\mathbf F_4\), is the square of a linear form. If this square is nonzero, there is a unique projective point of \(\mathbf P(K)\) on the member, and it is tested on the other quadric. If the square vanishes identically or the polar rank is zero, the singular locus has positive dimension and necessarily meets the other quadric over the algebraic closure. The resulting exact singular-point test is implemented in `count.c`; it checks all five parameters of \(\mathbf P^1(\mathbf F_4)\) and includes a separate check for identically-zero Pfaffians. None of its \(40,320\) accepted pencils has identically-zero Pfaffian. Thus no possible geometric singular parameter is omitted for any accepted pencil.

A first complete enumeration visits every canonical triple of nonzero binary quadric masks \(a<b<a\oplus b\). It yields exactly \(40,320\) smooth pairs, distributed by rational intersection points as stated. A second independent implementation in `direct16.c` tests all geometric Jacobian minors directly over \(\mathbf F_4\) and \(\mathbf F_{16}\), obtaining exactly the same set of \(40,320\) pencils. The latter finite-field check is not, by itself, proof of geometric smoothness over all extensions; the Pfaffian argument supplies that step. The agreement is equality of canonical pairs, not merely agreement of summary totals.

Finally, `orbits.c` constructs the coordinate permutations and elementary shear generators of \(\operatorname{GL}_4(\mathbf F_2)\), which generate the whole group, and performs a graph traversal of the orbit of every accepted canonical pencil. It produces eight disjoint orbits of the indicated sizes, totaling \(40,320\), including two distinct orbits with identical displayed rational point spectra. Smooth complete intersections of two quadrics in \(\mathbf P^3\) are connected, and their dualizing sheaf is \(\mathcal O_C(2+2-4)=\mathcal O_C\), so they are genus-one curves.

## Verification
Build `count.c`, `direct16.c`, and `orbits.c` with a C11 compiler. Run both enumeration programs with `--pairs`, extract the `PAIR` lines, and compare them byte-for-byte. Both print exactly \(40,320\) members; the first prints zero accepted cases with identically-zero Pfaffian, and the second reports \(40,656\) pencils surviving the direct \(\mathbf F_4\) test, of which \(336\) fail the \(\mathbf F_{16}\) test. Run `orbits.c` and check the complete eight-orbit table. The exact reference output is in `EXPECTED.txt`; `verify.sh` executes all steps.

## Relationship to prior work
Fevola–Mandelshtam–Sturmfels (2020) give a general geometric treatment of pencils of quadrics and, over an algebraically closed field of characteristic different from two, their Segre stratifications; their complex elliptic complete-intersection stratum does not determine the number or projective symmetry orbits over \(\mathbf F_2\). Bhargava–Cremona–Fisher (2020) discuss arithmetic genus-one models via binary quartics and local solubility over number fields; no equivalent finite-field binary quadric-pencil orbit census follows from their stated results. The present claim concerns the complete embedded characteristic-two census and the two orbit types sharing the same rational-point profiles. Existing literature and indexed research records were compared by implications as well as terminology.

## Limitations
This is a characteristic-two finite-field classification at \(\mathbf F_2\), not a formula for all finite fields or a classification under abstract isomorphism. Finite-field Jacobian enumeration is combined with a symbolic parameter-degree bound; enumeration without that bound would not establish geometric smoothness. The originality comparison cannot exclude all unindexed historical tables or computational catalogues; independent review has not been performed.

## References
1. C. Fevola, Y. Mandelshtam, and B. Sturmfels, *Pencils of Quadrics: Old and New* (2020), arXiv:2009.04334, first public version September 9, 2020.
2. M. Bhargava, J. Cremona, and T. Fisher, *The proportion of genus one curves over Q defined by a binary quartic that everywhere locally have a point* (2020), arXiv:2004.12085.
