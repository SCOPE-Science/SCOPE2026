# Tangent rigidity of minimally filling genus-six curves on the binary split quadric

## Finding
Let \(k=\mathbf F_2\), \(S=\mathbf P^1_k\times\mathbf P^1_k\), and let \(U\) be the \(k\)-linear system of bidegree-\((4,3)\) sections vanishing at all nine points of \(S(k)\). A nonzero section \(F\in U\) is called *smooth* when its zero divisor \(C_F\) is smooth over an algebraic closure of \(k\). Then \(\dim_k U=11\), and precisely \(66\) of its \(2047\) nonzero sections are smooth.

For any two *distinct* smooth sections \(F,G\in U\), let \(t(F,G)\) count points \(P\in S(k)\) where the tangent lines \(T_PC_F\) and \(T_PC_G\) agree inside \(T_PS\). The **complete unordered-pair spectrum** is:

| \(t(F,G)\) | Number of unordered pairs |
| ---: | ---: |
| \(3\) | \(642\) |
| \(5\) | \(981\) |
| \(7\) | \(468\) |
| \(9\) | \(54\) |
| **Total** | **\(2145=\binom{66}{2}\)** |

In particular, **every two distinct smooth minimally filling curves share at least three tangent lines at their common rational points**. For every such pair, the divisor \(C_{F+G}\) is singular at all their shared-tangent points. Consequently there is **no two-dimensional \(k\)-linear subspace of \(U\) with all three nonzero members smooth**; the largest all-smooth vector-space dimension is \(1\). The smooth sections have exactly \(27\) distinct ordered nine-point rational-tangent patterns.

## Assumptions and scope
The surface is split, the field is exactly \(\mathbf F_2\), and the bidegree is ordered: \((4,3)\), not an arbitrary divisor class. The word filling means that the zero divisor includes every \(k\)-point of \(S\). All sections are counted as coefficient vectors, not as abstract curves, and pair counts are unordered pairs of distinct coefficient vectors. Because \(k^\times=\{1\}\), there is no nontrivial scalar identification. Smoothness means **geometric smoothness**, not only nonsingularity at rational points. A smooth \((4,3)\) curve has genus \((4-1)(3-1)=6\) by adjunction.

The tangent comparison is made at each of the nine common rational points on the fixed embedded surface; no claim is made about tangent coincidences at nonrational points or other bidegrees and fields.

## Proof
**1. Exhaustive description of the filling space.** Write the homogeneous coordinates \(([X_0:X_1],[Y_0:Y_1])\). Set \(D_X=X_0^2X_1+X_0X_1^2\) and \(D_Y=Y_0^2Y_1+Y_0Y_1^2\). Each vanishes at all three rational points of its factor. The bihomogeneous ideal of \(S(k)\) in bidegree \((4,3)\) is spanned by \(A D_X+B D_Y\), where \(A\) has bidegree \((1,3)\) and \(B\) has bidegree \((4,0)\). Their intersection consists of \(D_X D_Y\) multiplied by sections of bidegree \((1,0)\). Thus its dimension is \(8+5-2=11\). A coefficient basis takes all eight monomials of \(A\) and, modulo the overlap, the three even-index monomials of \(B\). This parametrizes all \(2^{11}=2048\) filling sections once, including zero.

**2. Exact geometric smoothness.** On the four standard affine charts of \(S\), dehomogenize a section to \(f(u,v)\). The section cuts out a geometric singular point on that chart if and only if the ideal \((f,\partial_u f,\partial_v f)\subset k[u,v]\) is proper; by the weak Nullstellensatz this is equivalent to its Gröbner basis *not* being \(\{1\}\). Exhaustively apply the exact Gröbner unit-ideal test to each of the \(2047\) nonzero coefficient vectors on all four charts. Both embedded programs implement the complete finite scan with distinct parametrizations and different monomial orders. They identify exactly \(66\) geometrically smooth sections, with projective-coordinate orbit sizes \(6,6,18,36\), agreeing with an independent orbit check.

**3. Exact tangent comparison.** Each smooth filling curve passes through every rational point. At a rational point \(P\), its local gradient \((\partial_u f(P),\partial_v f(P))\in\mathbf F_2^2\setminus\{0\}\) determines its tangent line. Over \(\mathbf F_2\), two nonzero gradient pairs define the same tangent line if and only if they are equal (the only invertible scalar is \(1\)). For each of the \(66\) sections, compute its ordered nine-point gradient pattern in the appropriate local coordinates. Comparing all \(\binom{66}{2}=2145\) unordered pairs yields the displayed exact spectrum and \(27\) distinct patterns. Both embedded independently parametrized verification programs reproduce the same histogram, including the absence of any pairs with fewer than three matching gradients.

**4. Pencil obstruction.** For two smooth filling sections \(F,G\) and any shared-tangent point \(P\), the equation \(F+G=0\) vanishes at \(P\) and its gradient is \(dF(P)+dG(P)=0\). Hence \(C_{F+G}\) is singular at \(P\) (or the sum is zero, excluded by distinctness). Every projective pencil over \(\mathbf F_2\) consists of three nonzero sections \(F,G,F+G\). The third section is singular at at least three rational points, ruling out an all-smooth pencil. Smooth sections exist by Step 2, so maximal all-smooth vector dimension is exactly one.

## Verification
Run `python verify.py` and `python verify_orbits.py` with a recent SymPy installation. They require no external data. The first enumerates the nine evaluation equations in the full 20-coordinate space and uses lexicographic Gröbner bases; the second builds an independent eleven-parameter basis from \(D_X,D_Y\), uses graded reverse lexicographic Gröbner bases, and computes the action of the \(36\)-element polarized automorphism group. Both independently obtain the \(66\) smooth coefficient vectors and the same \((3,5,7,9)\) pair histogram. Machine-readable saved output files can be regenerated byte-for-byte as normalized JSON after sorting keys.

As a secondary check, exactly \(364\) filling sections are nonsingular at all nine rational points and exactly \(512\) pencils have all three sections nonsingular there. Among these \(512\), exactly \(272\) contain zero geometrically smooth members and \(240\) contain one; none contains two or three. Thus the no-pencil phenomenon is genuinely stronger than the availability of locally nonsingular pencils.

## Relationship to prior work
Homma and Kim, *Filling curves for \(\mathbf P^1\times\mathbf P^1\)* (first public March 22, 2022), establish minimal bidegrees \((4,3)\) and \((3,4)\) over \(\mathbf F_2\) and exhibit a smooth example; their statements do not determine intersections of rational tangent patterns between different smooth sections. Asgarli and Ghioca, *Smoothness in pencils of hypersurfaces over finite fields* (first public March 14, 2022), study all-smooth pencils of projective hypersurfaces; that general framework does not entail the present degree-minimal, nine-base-point obstruction on a fixed split quadric. Ahammed, Campbell, and Moon (2025) extend smooth filling-curve existence questions on the split quadric, but their later work does not state this pair spectrum. The previously computed \(66\)-curve census is not the novelty claim; the full two-curve tangent spectrum, sharp three-point lower bound, and resulting fixed-filling-system obstruction are the claimed contribution.

## Limitations
The numbers depend on the fixed split surface, ordered bidegree, field and coefficient convention. The checker proves a finite exhaustive theorem, not a dimension-uniform assertion. Historical or unindexed presentations of the same cross-curve incidence data cannot be fully excluded, and existing individual-curve tables might allow the spectrum to be computed even if it is not explicitly stated. The supplied computational proof is deterministic and exactly reproducible, but its numerical enumeration should undergo independent external validation before publication.

## References
- M. Homma and S. J. Kim, *Filling curves for \(\mathbf P^1\times\mathbf P^1\)*, arXiv:2203.11595 (first public 2022-03-22), https://arxiv.org/abs/2203.11595.
- S. Asgarli and D. Ghioca, *Smoothness in pencils of hypersurfaces over finite fields*, arXiv:2203.07169 (first public 2022-03-14), https://arxiv.org/abs/2203.07169.
- M. Ahammed, M. Campbell, and H.-B. Moon, *Minimal algebraic space filling curves on the product of projective lines*, arXiv:2512.02796 (first public 2025-12-02; contextual comparison), https://arxiv.org/abs/2512.02796.
