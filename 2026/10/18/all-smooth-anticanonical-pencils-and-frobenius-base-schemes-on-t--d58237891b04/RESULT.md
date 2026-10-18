# All-smooth anticanonical pencils and Frobenius base schemes on the binary split quadric

## Finding

Let \(S=\mathbf P^1_{\mathbf F_2}\times\mathbf P^1_{\mathbf F_2}\), with anticanonical class \(-K_S=\mathcal O_S(2,2)\). An all-smooth rational anticanonical pencil means a two-dimensional \(\mathbf F_2\)-linear subspace of \(H^0(S,-K_S)\) for which every one of the three nonzero sections has geometrically smooth zero divisor. **Exactly 804 such pencils exist.** They form **13 orbits** under \(\operatorname{Aut}_{\mathbf F_2}(S)\cong(\operatorname{PGL}_2(\mathbf F_2)^2)\rtimes C_2\), of order 72.

Every one of the 804 pencils has geometrically reduced base scheme, consisting of eight distinct points over the algebraic closure. The complete Frobenius cycle distribution is:

| Frobenius degrees of the geometric base points | Pencils | Automorphism orbits | Rational base points |
|---|---:|---:|---:|
| \(1,7\) | 288 | 4 | 1 |
| \(1,1,6\) | 216 | 4 | 2 |
| \(1,2,5\) | 216 | 3 | 1 |
| \(8\) | 72 | 1 | 0 |
| \(2,3,3\) | 12 | 1 | 0 |
| **Total** | **804** | **13** | — |

In particular, exactly 72 all-smooth pencils have a single closed base point of degree eight; its eight geometric points form one Frobenius orbit. Another 12 pencils have two closed points of degree three and one of degree two. These cases both have no rational base points but different extension-field behavior. The numerical classification is of pencils of anticanonical **curves on a fixed split quadric**, not pencils of quadric hypersurfaces in projective space.

## Assumptions and scope

All geometry is over \(k=\mathbf F_2\), with geometric smoothness and reducedness taken after base extension to \(\overline k\). Fix homogeneous coordinates \(([U:V],[S:T])\) on the two factors. Index the nine standard monomials \(U^aV^{2-a}S^bT^{2-b}\), where \(a,b\in\{0,1,2\}\), by bit position \(3a+b\). A nonzero mask \(m\in\{1,\ldots,511\}\) denotes the sum of its selected monomials over \(\mathbf F_2\). A pencil is the unordered set of three nonzero masks \(\{m,n,m\oplus n\}\), where \(\oplus\) is bitwise addition in characteristic two.

Each geometrically smooth divisor has genus \((2-1)(2-1)=1\) by adjunction. Since \((2,2)\cdot(2,2)=8\), a pair of smooth anticanonical members without common components has a base scheme of length eight, counted with multiplicity.

## Proof

**1. Exhaustive smooth-member criterion.** For each of the 511 masks, use all four standard affine product charts, dehomogenizing \((U,V)\) and \((S,T)\) independently. On each chart form \(f(x,y)\) and its two partial derivatives. The curve is geometrically smooth exactly when the ideal \((f,\partial_x f,\partial_y f)\) contains 1 on every chart. Gröbner calculations in \(\mathbf F_2[x,y]\) identify exactly 144 smooth masks. This ideal criterion is valid over the algebraic closure because an ideal is proper precisely when it has a geometric common zero.

**2. Pencil and orbit census.** For each unordered pair of the 144 masks, test whether its bitwise sum is again smooth. Deduplicate each three-element subspace. The result is exactly 804 pencils. On the two ruling coordinates, the substitutions swapping the homogeneous coordinates and replacing the first by their sum generate each \(\operatorname{PGL}_2(\mathbf F_2)\). Together with interchange of the two rulings they generate the full 72-element automorphism group of the split quadric. Applying these five elementary transformations to the finite pencil set yields exactly 13 orbits: ten of size 72, two of size 36 and one of size 12.

For complete reproducibility, the following table gives a pair of generating masks for each orbit. The third mask is their exclusive-or; orbit size and base-cycle type are computed as described above and below:

| First mask | Second mask | Sum mask | Orbit size | Base degrees |
|---:|---:|---:|---:|---|
| 98 | 141 | 239 | 72 | \((1,7)\) |
| 98 | 142 | 236 | 72 | \((1,1,6)\) |
| 98 | 149 | 247 | 72 | \((1,2,5)\) |
| 98 | 159 | 253 | 72 | \((1,2,5)\) |
| 98 | 174 | 204 | 36 | \((1,1,6)\) |
| 98 | 283 | 377 | 72 | \((1,2,5)\) |
| 98 | 415 | 509 | 72 | \((8)\) |
| 98 | 431 | 461 | 12 | \((2,3,3)\) |
| 99 | 158 | 253 | 72 | \((1,1,6)\) |
| 99 | 188 | 223 | 72 | \((1,7)\) |
| 99 | 191 | 220 | 36 | \((1,1,6)\) |
| 99 | 284 | 383 | 72 | \((1,7)\) |
| 99 | 410 | 505 | 72 | \((1,7)\) |

**3. Geometric transversality and reducedness.** For every representative pair \(f,g\), test the intersection ideal \((f,g, f_xg_y-f_yg_x)\) in each of the four affine charts. All 52 Gröbner bases equal the unit ideal. Hence every intersection point is transverse and the base scheme geometrically reduced. The two divisors share no component: a common component would produce a positive-dimensional locus where their gradients are proportional, contradicting these tests. Bézout on \(S\) gives exactly eight distinct geometric base points. Since automorphisms preserve these properties, the conclusion holds for all 804 pencils.

**4. Arithmetic Frobenius cycles.** For each of the 13 representatives, enumerate common zeros in \(\mathbf P^1(\mathbf F_{2^r})^2\), for \(1\leq r\leq8\). The finite fields use irreducible binary polynomials with integer coefficient masks \(3,7,11,19,37,67,131,283\), respectively (the first represents \(t+1\)). All eight irreducibilities can be checked directly in \(\mathbf F_2[t]\). If \(N_r\) denotes the number of points over \(\mathbf F_{2^r}\), the number \(c_r\) of closed points of degree \(r\) is obtained recursively by \(c_r=(N_r-\sum_{d\mid r,\,d<r}d c_d)/r\). All representatives satisfy \(\sum_{r=1}^8 rc_r=8\). This is exhaustive because the base scheme is reduced of degree eight; no larger-degree geometric point remains. The recovered partitions and orbit sizes aggregate to the five rows above. For example, the representative \(m=98,n=415\) has \(N_1=\cdots=N_7=0\) and \(N_8=8\), and its affine elimination polynomial is the irreducible degree-eight polynomial \(x^8+x^7+x^6+x^4+x^3+x^2+1\). The representative \(m=98,n=431\) has \(N_1=0,N_2=2,N_3=6,N_6=8\), and consequently partition \(2,3,3\).

## Verification

The attached `verify_pencils.py` computes the geometric smoothness census, all pencils, and 13 group orbits, outputting `pencil_census.json`. `verify_transversality.py` independently checks the 52 chartwise Jacobian ideals and prints the representative elimination factorizations. `verify_base_spectra.cpp` directly counts geometric base points over every extension of degrees one through eight. Compile and compare with `expected_base_spectra.txt` using the exact commands in `VERIFICATION.md`. The table of thirteen representative masks is supplied as `representatives.txt`. The checks were replayed against these exact attached source files using Python 3 / SymPy 1.14 and a C++17 compiler; all stated expected counts and spectra were reproduced.

## Relationship to prior work

Asgarli and Ghioca, *Smoothness in pencils of hypersurfaces over finite fields* (arXiv:2203.07169, posted March 14, 2022), study the existence of all-smooth rational pencils of projective hypersurfaces; their main theorem and section 3 address projective-space hypersurfaces and explicitly constructed pencils of smooth **quadric surfaces**, not complete arithmetic classifications of pencils of genus-one anticanonical curves on one fixed split quadric. Their earlier paper *A Bertini type theorem for pencils over finite fields* (arXiv:2004.03479) concerns common transverse hyperplane sections of pencils of hypersurfaces, rather than base schemes of pencils in \(H^0(S,-K_S)\). Hamada and Hayano, *Classification of genus-1 holomorphic Lefschetz pencils* (arXiv:2008.02925), establish a complex-topological classification involving \(\mathbf P^1\times\mathbf P^1\) and eight complex base points, but not the characteristic-two finite-field Frobenius and orbit census here. The standard fact that a smooth \((2,2)\) curve on the split quadric is genus one is not new. The contribution is the exact 804-pencil classification, including 13 embedded symmetry orbits, universal transversality, and all five closed-point partitions.

## Limitations

The results apply only to the split surface over \(\mathbf F_2\), to its full anticanonical system, and to pencils with all three rational members smooth. No assertion is made about every geometric member of a pencil, about other finite fields, or about the nonsplit quadric. Projective-coordinate equivalence is taken under the entire rational automorphism group preserving the split quadric, not under abstract isomorphism of the genus-one members. Computational exhaustiveness relies on the explicit finite enumeration and independent algebraic reduction checks; these are finite computations, not an external formal proof certificate. An unindexed earlier complete census of the same finite problem may exist, so priority remains subject to independent literature review.

## References

- S. Asgarli and D. Ghioca, *Smoothness in pencils of hypersurfaces over finite fields*, arXiv:2203.07169, first posted 2022-03-14; Bull. Aust. Math. Soc. 107 (2023), 85–94.
- S. Asgarli and D. Ghioca, *A Bertini type theorem for pencils over finite fields*, arXiv:2004.03479, first posted 2020-04-07; Finite Fields Appl. 77 (2022), 101936.
- N. Hamada and K. Hayano, *Classification of genus-1 holomorphic Lefschetz pencils*, arXiv:2008.02925, first posted 2020-08-07.
