# A ternary atlas of elliptic biquadratics, branch pairs and QRT periods

## Finding
Let \(S=\mathbf P^1_{\mathbf F_3}\times\mathbf P^1_{\mathbf F_3}\). Every geometrically smooth zero divisor \(C_F\) of a nonzero section \(F\in H^0(S,\mathcal O(2,2))\), considered up to \(\mathbf F_3^\times\)-scaling of its equation, is an elliptic curve with two degree-two ruling maps. Write \(N=\#C_F(\mathbf F_3)\), let \(r_1,r_2\) be the numbers of rational geometric ramification points of those maps, and let \(m\) be the exact order on \(C_F\) of the composite of their deck involutions (in either order). The unordered branch pair is denoted \(\{r_1,r_2\}\).

There are exactly **5,184** smooth equations, forming exactly **14** orbits under the order-\(1,152\) group \(\operatorname{Aut}_{\mathbf F_3}(S)=\operatorname{PGL}_2(\mathbf F_3)^2\rtimes C_2\). Their full joint distribution is:

| \(N\) | \(\{r_1,r_2\}\) | \(m\) | Equations | Ambient orbits |
| ---: | :---: | ---: | ---: | ---: |
| 2 | \(\{0,2\}\) | 2 | 288 | 1 |
| 3 | \(\{1,1\}\) | 3 | 576 | 1 |
| 4 | \(\{0,0\}\) | 2 | 288 | 2 |
| 4 | \(\{0,2\}\) | 4 | 576 | 1 |
| 4 | \(\{0,4\}\) | 2 | 144 | 1 |
| 4 | \(\{2,2\}\) | 2 | 144 | 1 |
| 5 | \(\{1,1\}\) | 5 | 1,152 | 2 |
| 6 | \(\{0,0\}\) | 3 | 288 | 1 |
| 6 | \(\{0,2\}\) | 2 | 288 | 1 |
| 6 | \(\{0,2\}\) | 6 | 576 | 1 |
| 6 | \(\{2,2\}\) | 3 | 288 | 1 |
| 7 | \(\{1,1\}\) | 7 | 576 | 1 |
| **Total** | | | **5,184** | **14** |

In particular the maximal possible QRT order is exactly **seven**, and it occurs for precisely **576** equations in **one ambient projective orbit**. A representative is
\[
U^2ST+2U^2T^2+UVS^2+UVT^2+V^2S^2=0.
\]
Its seven rational points form one seven-cycle under the composite deck map. These assertions concern a single smooth bidegree-\((2,2)\) curve and its two ruling involutions, not an arbitrary birational map preserving a pencil of such curves.

## Assumptions and scope
All fields, coefficients, points, equivalences and counts here are over \(\mathbf F_3\), except when checking geometric smoothness over the algebraic closure. A projective equation is a nonzero nine-component coefficient vector modulo its two nonzero scalars, not an arbitrary ordered polynomial presentation. Each equation defines one effective divisor on the **split** quadric; the 14 equivalence classes are under ambient automorphisms, not abstract unmarked elliptic-curve isomorphism.

Use the monomial order
\[
F=\sum_{i,j=0}^2 c_{ij}U^{2-i}V^iS^{2-j}T^j,
\]
with coefficient index \(3i+j\). Normalize the first nonzero coefficient to one. The two degree-two maps are restrictions of the two projections. A rational geometric ramification point means \(P\in C_F(\mathbf F_3)\) at which the corresponding morphism has ramification index two. For a double cover in characteristic three, this is equivalent to a repeated root in its homogeneous quadratic fibre. The composite deck map is an automorphism of the entire smooth curve, not merely a permutation defined on its rational points.

## Proof
**1. Smoothness reduces to squarefreeness of a binary quartic.** Write
\[
F=A(U,V)S^2+B(U,V)ST+C(U,V)T^2
\]
for binary quadratics \(A,B,C\). The first projection has branch form
\[
\Delta_1(U,V)=B(U,V)^2-4A(U,V)C(U,V),
\]
and the second projection has the analogous form \(\Delta_2(S,T)\). Since the characteristic is odd, a finite quadratic map is locally given after completing the square by \(w^2=\Delta_1\). If a fibre polynomial vanishes identically, all three coefficients vanish at its base point and \(\Delta_1\) has a multiple zero there. Otherwise a multiple zero of \(\Delta_1\) is exactly a singularity of this double-cover model, while a simple zero yields a smooth ramification point. Thus \(C_F\) is geometrically smooth if and only if \(\Delta_1\) is squarefree as a *homogeneous* quartic, equivalently for \(\Delta_2\). The procedure includes the point at infinity and tests the derivative/gcd over \(\mathbf F_3\), a valid squarefreeness test over its algebraic closure. A geometrically smooth divisor of class \((2,2)\) is connected, hence integral, since distinct positive effective component classes would meet; its genus is \((2-1)(2-1)=1\).

**2. Exact exhaustive orbit census.** There are \((3^9-1)/2=9,841\) normalized nonzero equations. The two factors admit the three substitutions \((U,V)\mapsto(V,U)\), \((U,V)\mapsto(U+V,V)\), \((U,V)\mapsto(2U,V)\); apply these also to \((S,T)\), together with factor interchange. The seven operations generate the full order-\(1,152\) ambient group. Breadth-first orbit propagation partitions all 9,841 coefficient vectors into 41 disjoint orbits. Squarefreeness testing on one representative per orbit identifies 14 smooth orbits whose sizes sum to 5,184. Complete representative masks and sizes for both smooth and singular cases are in `data/orbits.json`. The separate symbolic verifier generates all 24 elements of each \(\operatorname{PGL}_2(\mathbf F_3)\) factor independently and confirms that the 41 orbits exhaust precisely those 9,841 forms. It also tests each of the 41 representatives for absence of geometric singular points by requiring the Jacobian ideal to be the unit ideal on **all four** affine charts. These tests agree with the branch-quartic criterion on every orbit.

**3. Arithmetic and dynamics on each smooth orbit.** Direct evaluation at the 16 rational points of \(S\) gives \(N\). The roots of \(\Delta_i\) among the four points of \(\mathbf P^1(\mathbf F_3)\) give the two rational ramification counts. Each deck involution takes a rational point to the other point in its degree-two fibre, fixing a ramified point. Composing the two resulting permutations gives the displayed \(m\), checked independently using fibrewise gradients rather than discriminants. The data give all 12 joint strata in the table. Since the ambient group preserves \(N\), the unordered branch pair and the order of the composite, orbit weights prove the whole distribution.

**4. The computed order is the order of the geometric automorphism.** A smooth genus-one curve over \(\mathbf F_3\) has a rational point in every tabulated case; choose it as origin and write \(E=C_F\). Each degree-two line bundle \(L_i\) gives a deck involution \(x\mapsto a_i-x\), where \(a_i\in E(\mathbf F_3)\) represents \(L_i\in\operatorname{Pic}^2(E)\). The two line bundles are distinct: otherwise the product map would have image a \((1,1)\) graph, not a smooth \((2,2)\) curve. Hence the composite is translation by the **nonzero** rational point \(a_2-a_1\), up to sign. Its order is its order as a permutation of rational points. Hasse's inequality \(N\le 3+1+2\sqrt3<8\) gives the general bound \(m\le7\). The computation identifies exactly one smooth orbit with \(N=7\), representative coefficient mask 1020, orbit size 576; on it the nonzero translation has exact order seven. This proves sharpness and uniqueness under ambient equivalence.

## Verification
Run `python verify/census.py` using Python 3 standard library from the extracted package, and compare its generated structure to `data/orbits.json`. It enumerates and partitions all 9,841 equations, tests binary-quartic squarefreeness, evaluates rational points and branch divisors and determines the deck-product orders. Then run `python verify/symbolic_crosscheck.py` with SymPy. This second program does not import the first. It constructs all 24 projective matrices per factor explicitly, checks each of the 41 full orbits, computes Gröbner bases of every representative's four affine Jacobian ideals (164 exact ideals), and recomputes the rational branch and order data by a distinct method. Both programs returned success on the packaged files. The JSON and programs are complete, finite reproducibility certificates; no random samples or timeouts are treated as mathematical proofs.

## Relationship to prior work
Li and Takenawa (2022) study QRT maps on complex biquadratic elliptic curves, explain their decomposition into the two ruling involutions and the elliptic translation description, and give the binary-quartic discriminant smoothness criterion. Those *general principles* are prior work, not claimed new here. Alonso, Suris and Wei (2023) likewise present the QRT construction on \(\mathbf P^1\times\mathbf P^1\) in their broader three-dimensional study. Bastien and Rogalski (2020) analyze periods for a special real biquadratic family. These works do not state the complete all-equation \(\mathbf F_3\) ambient orbit classification or its joint rational-branch/QRT-order atlas in the inspected material. The contribution here is the finite-field **complete joint classification** and its single extremal order-seven orbit, not the elliptic group-law description or the Hasse bound alone.

## Limitations
This is restricted to \(\mathbf F_3\) and the split quadric, with equivalence under the ambient automorphism group. It does not classify abstract elliptic curves without their two line bundles, other finite fields, singular biquadratics, or the dynamics of arbitrary QRT pencils. Although the cited primary sources and targeted literature/record searches did not reveal this exact table, a pre-existing unpublished, unindexed or implicit finite-field classification remains a priority risk.

## References
1. X. Li and T. Takenawa, *Solving the Quispel–Roberts–Thompson maps using Kajiwara–Noumi–Yamada's representation of elliptic curves*, first publicly posted 2022-03-23, arXiv:2203.12319, especially §§1–3. https://arxiv.org/abs/2203.12319
2. J. Alonso, Y. B. Suris and K. Wei, *A Three-Dimensional Generalization of QRT Maps*, Journal of Nonlinear Science 33 (2023), article 117, especially §2. https://doi.org/10.1007/s00332-023-09976-0
3. G. Bastien and M. Rogalski, *The Periodic Orbits of a Dynamical System Associated with a Family of QRT-Maps*, Qualitative Theory of Dynamical Systems 19 (2020), article 57. https://doi.org/10.1007/s12346-020-00393-2
4. T. Fisher, *The invariants of a genus one curve*, Proceedings of the London Mathematical Society 97 (2008), 753–782, general background on genus-one model invariants. https://doi.org/10.1112/plms/pdn021
