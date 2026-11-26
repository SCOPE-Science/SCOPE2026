# A single integral cup product realizes two-torsion for Petersen two-point configurations

## Finding

Let \(P=KG(5,2)\) be the Petersen graph. Number its vertices by the lexicographically ordered two-subsets of \(\{0,1,2,3,4\}\); number the edges lexicographically by their endpoint pairs, starting at zero, and orient each edge from the smaller endpoint to the larger. The edges numbered \(0,1,2,3,4,5,6,7,9\) form a spanning tree. Collapse this tree, map each oriented chord once around its own coordinate circle in \((S^1)^6\), and add the images of the two particles in the torus. Write \(\alpha_i\) for the pullback of the degree-one generator on chord coordinate \(i\).

On the ordinary unordered collision-free configuration space \(X=\operatorname{UConf}_2(|P|)\), the **single product**
\[
\kappa=(\alpha_8+\alpha_{10})\smile(\alpha_{14}-\alpha_{10})\in H^2(X;\mathbb Z)
\]
has exact order two. In the individual chord products this is
\[
\kappa=-\alpha_8\smile\alpha_{10}+\alpha_8\smile\alpha_{14}+\alpha_{10}\smile\alpha_{14}.
\]
It therefore generates the unique torsion subgroup of \(H^2(X;\mathbb Z)\), using the known group \(H_1(X;\mathbb Z)\cong\mathbb Z^6\oplus\mathbb Z/2\). The assertion here is not that torsion exists or that it is a *sum* of degree-one products, but that this particular pair of total-motion classes has torsion product.

## Assumptions and scope

The points are unordered, may lie in edge interiors, and must be distinct everywhere. The result is about ordinary integral singular cohomology. The formula depends on the declared graph orientation and chord coordinates. No minimality of its support or analogous claim for arbitrary nonplanar graphs is asserted.

## Proof

The standard cubical discretization \(UD_2(P)\) includes into \(X\) by a homotopy equivalence: every path between distinct essential vertices has at least one edge, and every essential cycle has length at least five, satisfying the two-particle subdivision conditions [1, Thm. 3.1]. Its 1-cells are \((i,v)\) with \(v\) not an endpoint of \(e_i\); its 2-cells are \((i,j)\) with \(i<j\) and disjoint endpoint pairs. Orient the former by the edge and the latter by the product in the displayed order. For \(e_i=[a,b]\), \(e_j=[d,f]\), their boundary is
\[
 \partial(i,j)=(j,b)-(j,a)-(i,f)+(i,d).
\]
There are 45 vertices, 120 edges and 75 squares. In each dimension enumerate cells lexicographically, starting at zero.

The torus map in the Finding is cellular for the circle product structure with one vertex per circle. On a square from two chord edges the ordered factors map to the corresponding coordinate circles; if either edge is a tree edge, the map factors through a circle or is constant. Consequently \(\alpha_p\smile\alpha_q\) for \(p<q\) is represented by the indicator of square \((p,q)\) (zero if the square is absent). The squares of the \(\alpha_i\) vanish by pullback from the torus. Thus the cellular cochain \(c\) for \(\kappa\) has its only nonzero entries \(c_{62}=-1\), \(c_{65}=c_{69}=1\); these are the squares \((8,10),(8,14),(10,14)\).

Write \(D=\partial_2^{\mathsf T}\). An integral 1-cochain \(u\) with \(Du=2c\) is specified below. Entries not listed are zero.

| Coefficient of \(u\) | 1-cell indices |
|---|---|
| \(-2\) | 5 |
| \(-1\) | 1, 2, 4, 6, 9, 25, 33, 34, 37, 58, 61 |
| \(1\) | 16, 24, 30, 32, 36, 38, 50, 51, 52, 53, 54, 60, 62, 76, 77 |
| \(2\) | 68, 69, 84 |

For nonvanishing, over \(\mathbb F_2\) let \(z\) be the sum of the squares with indices
```
0, 1, 3, 4, 6, 7, 10, 11, 16, 17, 19, 22, 23, 25, 27, 29,
31, 32, 36, 37, 38, 39, 41, 44, 45, 47, 49, 51, 55, 57,
58, 62, 63, 65, 67, 69
```
Applying the displayed square boundary to these cells gives zero modulo two. All three nonzero entries of \(c\) are in \(z\), so \(\langle c\bmod 2,z\rangle=1\). Therefore \(c\bmod 2\) is not a coboundary and neither is \(c\). Together with the integral identity \(Du=2c\), this proves exact order two. The torsion subgroup of \(H^2\) is \(\mathbb Z/2\) by the integral universal coefficient theorem and the known \(H_1\) [2].

## Verification

Run `python3 verify.py` (standard library only). It reconstructs the cells and checks the signed integer identity \(Du=2c\), the binary cycle condition, and the odd pairing. The checker forms \(c\) directly from the two linear forms on chord coordinates in the Finding, without relying on the positions of wedge-basis products.

## Relationship to prior work

The known Petersen homology [2] supplies the abstract torsion subgroup, and pentagon-product tori describe integral \(H_2\) [3]. Integral top-degree cohomology generation by degree-one classes also follows from the symmetric square: the discretization is a subcomplex of a two-dimensional cell model of \(\operatorname{Sym}^2(|P|)\), so restriction in degree two is surjective. The symmetric square of a bouquet of circles is homotopy equivalent, by the circle-multiplication map, to the 2-skeleton of the torus [4, Lemmas 2–3], whose degree two is generated by products. Neither abstract homology, the torus pairings on integral cycles, nor this surjectivity identifies a single product that represents the nonzero torsion element. A related indexed calculation for \(K_6\) [5] uses a different graph and chord system.

## References

1. D. Farley and L. Sabalka, *Discrete Morse theory and graph braid groups*, [arXiv:math/0410539](https://arxiv.org/abs/math/0410539).
2. *Two-particle Petersen configuration homology as an \(S_5\)-module*, indexed note [2bac82e0590d](https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-two-particle-petersen-configuration-homology-as-an-s-5-module--2bac82e0590d).
3. *Six pentagon tori determine the integral \(S_5\)-lattice of Petersen two-point configurations*, indexed note [9b713b5d8d10](https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-six-pentagon-tori-determine-the-integral-s-5-lattice-of-petersen--9b713b5d8d10).
4. S. Kallel and P. Salvatore, *Symmetric products of two dimensional complexes*, [arXiv:math/0510176](https://arxiv.org/abs/math/0510176).
5. *Integral degree-one generation and a torsion cup product for two unordered particles on \(K_6\)*, indexed note [aab3bbadc9eb](https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-integral-degree-one-generation-and-a-torsion-cup-product-for-two--aab3bbadc9eb).
