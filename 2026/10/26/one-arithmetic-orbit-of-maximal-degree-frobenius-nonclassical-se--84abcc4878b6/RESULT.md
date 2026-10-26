# One arithmetic orbit of maximal-degree Frobenius-nonclassical sextics over \(\mathbf F_4\)

## Finding
Every geometrically smooth Frobenius-nonclassical plane sextic over \(\mathbf F_4\) is projectively equivalent over \(\mathbf F_4\) to
\[
xyz(x^3+y^3+z^3)+(\alpha+1)x^6+\alpha y^6+z^6=0,
\qquad \alpha^2+\alpha+1=0.
\]
There are exactly \(960\) distinct such curves in fixed projective coordinates (counting equations modulo a nonzero scalar), constituting **one** \(\operatorname{PGL}_3(\mathbf F_4)\)-orbit. The stabilizer of each curve in this projective group has order \(63\). Each curve has no \(\mathbf F_4\)-rational point. Here Frobenius-nonclassical means that \(F\) divides \(\sum_i x_i^4\partial F/\partial x_i\), equivalently Frobenius sends every geometric curve point into its tangent line.

## Assumptions and scope
The base field is \(k=\mathbf F_4=\mathbf F_2[\alpha]/(\alpha^2+\alpha+1)\). Curves are *geometrically smooth* plane projective sextics in \(\mathbf P^2_k\). Coordinate equivalence uses \(\operatorname{PGL}_3(k)\), not isomorphism as abstract curves over extensions. The count \(960\) is of distinct degree-six homogeneous equations modulo scalar in fixed coordinates, rather than choices of a particular polynomial defining a curve.

## Proof
**Reduction to a 10-parameter normal form.** Proposition 4.8 of Asgarli--Duan--Lai (arXiv:2207.11981) establishes that each geometrically smooth Frobenius-nonclassical plane curve of degree \(q+2\) in characteristic two has, after unique scalar normalization, the partial derivatives
\[
(F_x,F_y,F_z)=(yz^q+y^qz,zx^q+z^qx,xy^q+x^qy).
\]
Taking \(q=4\), write \(H=xyz(x^3+y^3+z^3)\). Direct differentiation in characteristic two gives exactly this derivative triple for \(H\). A polynomial with all three derivatives zero over \(k\) is a polynomial in the squares of its variables, hence every normalized candidate is **uniquely**
\[
F=H+G(x^2,y^2,z^2),\qquad G\in k[U,V,W]_3.
\]
The ten ordered monomials of \(G\) are \(U^3,U^2V,U^2W,UV^2,UVW,UW^2,V^3,V^2W,VW^2,W^3\). Conversely each such \(F\) is Frobenius-nonclassical, since its fourth-power Frobenius tangency polynomial vanishes identically by cancellation of alternating pairs. There are exactly \(4^{10}=1,048,576\) normalized candidates, with no scalar duplication.

**Smoothness criterion, valid over the algebraic closure.** The simultaneous vanishing of the three derivatives is precisely \(\mathbf P^2(k)\), consisting of 21 geometric points. Indeed, where all coordinates are nonzero, the derivatives force \(x^3=y^3=z^3\), and the ratios are in \(k^*\); the cases with one or more zero coordinates similarly force the remaining nonzero coordinate ratio to be in \(k^*\). Therefore \(V(F)\) is geometrically smooth **if and only if** \(F(P)\ne0\) for all 21 projective \(k\)-points \(P\). In particular there is no unresolved search for singularities over untested extensions.

**Exhaustive finite arithmetic.** Represent \(k\) by the four two-bit numbers \(0,1,\alpha,\alpha+1\). Evaluate \(F\) at one normalized representative for each of the 21 points and test the above condition for every base-four coefficient vector of length ten. The self-contained exact checkers `verify_cpp.cpp` and `verify_python.py` use different implementations and both return exactly \(960\) admissible vectors. The C++ checker additionally ranges over all \(181,440\) invertible \(3\times3\) matrices over \(k\), acting on the 21 point evaluations by
\[
(T\cdot F)(P)=\det(T)^{-1}F(TP).
\]
This formula follows by the chain rule and the alternating covariance of the displayed gradient triple; it does not depend on the representative of \(T\) in \(\mathrm{GL}_3(k)\), because \(c^3=1\) for every \(c\in k^*\). The orbit of the displayed representative has exactly \(960\) elements; its stabilizer in \(\mathrm{GL}_3(k)\) has size \(189\). As the scalar subgroup has size three, its projective stabilizer has size \(63\). The Python checker independently constructs an orbit of size 960 using only four explicit invertible generators and verifies that every member belongs to the admissible list. Since the list itself has 960 members, this proves transitivity even without a generation theorem.

**Representative check without enumeration.** For the displayed curve the three coefficients \((\alpha+1,\alpha,1)\) are pairwise distinct and have sum zero. At a rational projective point with exactly one nonzero coordinate its value is one of these coefficients; with exactly two nonzero coordinates it is the sum of two distinct coefficients; and with all coordinates nonzero it equals \(xyz\). All values are nonzero. Thus it is geometrically smooth by the established singular-locus criterion.

## Verification
Compile `verify_cpp.cpp` using `g++ -O3 -std=c++17 verify_cpp.cpp -o verify_cpp` and execute `./verify_cpp`. Run `python verify_python.py` with Python 3 and NumPy. The first checker must report `smooth_forms=960`, `invertible_GL3=181440`, `orbit_size=960`, `stabilizer_GL3=189`; the second must report `admissible_coeff_vectors: 960`, `generator_orbit_size: 960`, `PGL3(F4)_order: 60480`, and `projective_stabilizer_order: 63`. Both programs fail on a disagreement with the required integer checks. `REFERENCE_OUTPUT.txt` records actual results from these package paths. The complete enumeration is over a finite explicitly defined coefficient set, so there is no asymptotic extrapolation.

## Relationship to prior work
Asgarli--Duan--Lai, *Frobenius nonclassical hypersurfaces* (arXiv:2207.11981, first posted 25 July 2022), prove the normal form and supply individual smooth examples for \(q=2,4,8\), including an \(\mathbf F_4\)-sextic. Their Proposition 4.8 and Example 4.11 are essential input; the normal form and existence of an example are **not** new. Their work does not state the exact 960 count or arithmetic single-orbit theorem. Cossidente--Siciliano, *The Automorphism Group of Plane Algebraic Curves with Singer Automorphisms* (Designs, Codes & Cryptography 39 (2006), 33--37, doi:10.1007/s10623-005-2153-6), give a projective classification **conditional on the presence of a Singer automorphism** and identify the geometric Singer-curve automorphism normalizer. This does not by itself establish that all smooth Frobenius-nonclassical sextics over \(\mathbf F_4\) satisfy that hypothesis or that they constitute one arithmetic projective class. An earlier census of all-smooth conic nets over \(\mathbf F_4\) also happens to give 960, but counts a different type of projective linear system and does not imply the present theorem.

## Limitations
The result is a fixed-field, fixed-degree classification, not a formula for every \(\mathbf F_{2^r}\). No independent external audit has occurred. Publication priority against older unindexed finite-geometric or automorphism-classification computations remains uncertain. The result neither determines automorphism groups over the algebraic closure nor claims that these curves are new as geometric isomorphism types.

## References
1. S. Asgarli, L. Duan, K.-W. Lai, *Frobenius nonclassical hypersurfaces*, arXiv:2207.11981, Proposition 4.8, Corollary 4.9, Example 4.11 (2022; later revision 2024), https://arxiv.org/pdf/2207.11981.
2. A. Cossidente, A. Siciliano, *The Automorphism Group of Plane Algebraic Curves with Singer Automorphisms*, Designs, Codes & Cryptography **39** (2006), 33--37, https://doi.org/10.1007/s10623-005-2153-6.
3. S. Asgarli, D. Ghioca, Z. Reichstein, *Linear families of smooth hypersurfaces over finitely generated fields*, arXiv:2207.00918 (2022), https://arxiv.org/abs/2207.00918 (distinct linear-system problem).
