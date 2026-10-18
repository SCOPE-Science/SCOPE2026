# Scientific review: complete type-A root toric Fano singular strata

## Correctness — PASS

The proof determines every face cone by its disjoint top/bottom index sets. The complete bipartite incidence-rank calculation proves that nonsimplicial cones occur precisely when both sets have at least two elements; the tree-basis argument proves all other cones unimodular. Minimal singular cones are consequently the \(2\)-by-\(2\) squares. Their star fan is the product of one-dimensional complete fans, because remaining indices choose top, bottom, or unused independently, with opposite quotient rays. A saturated four-index basis gives the conifold semigroup relation exactly. The polar cube proves the restricted anticanonical polarization, and its normalized volume gives the degree. Terminality and Cartier Fano status follow from the root lattice-point classification and integral polar. The symbolic checker tested every face for \(4\leq n\leq7\), but the infinite result is based on the lattice proof.

## Originality — PASS, with literature risk

Ardila--Beck--Hoşten--Pfeifle--Seashore [1, Proposition 8] supply the classical product-of-simplices facets and lattice-point structure; these facts are established prior art. Higashitani [2] studies this directed-graph toric Fano construction and supplies the global smoothness criterion. Kara--Portakal--Tsuchiya [3] prove graph-theoretic codimension-three \(\mathbb Q\)-factoriality obstructions, identifying the relevance of four-cycles. Their published results, in the inspected material, do not explicitly give the complete irreducible singular-component description \((\mathbb P^1)^{n-4}\), uniform transverse conifold equations, or the restricted anticanonical degree formula \(n!/4\). Rietsch--Williams [4] treat the wider root-polytope toric framework. The six square facets for the four-index case are known and are not claimed novel. An equivalent reinterpretation of the classical facet geometry remains possible; this review is not an independence or priority certification.

## Mathematical value — PASS

The result is an all-dimensional, complete geometric classification of the reduced singular locus of a canonical Gorenstein toric Fano family. It determines exact irreducible components, each component's isomorphism type, the generic transverse local equation, and an intrinsic anticanonical degree. That is stronger than a yes/no smoothness or codimension-three criterion and can inform singular-stratum intersection theory. No claim about the nonreduced Jacobian singular subscheme or all nongeneric intersection germs is made.

## Verification and boundaries

The dependency-free `check.py` prints `VERIFY_OK` after exact finite combinatorial tests for \(n=4,5,6,7\). These tests check the proof's structural inputs and do not themselves prove the family theorem. The lattice calculations in RESULT.md provide the all-size argument. The principal residual risk is equivalent coverage in unidentified toric or root-polytope literature, especially formulations deriving orbit closures from products of simplices.

Self-review: passed. Independent audit: not yet performed.

## References

[1] F. Ardila, M. Beck, S. Hoşten, J. Pfeifle, K. Seashore, *Root polytopes and growth series of root lattices*, arXiv:0809.5123, Section 3, Proposition 8, https://arxiv.org/abs/0809.5123.

[2] A. Higashitani, *Smooth Fano polytopes arising from finite directed graphs*, arXiv:1103.2202, https://arxiv.org/abs/1103.2202.

[3] S. Kara, I. Portakal, A. Tsuchiya, *Rigid Gorenstein toric Fano varieties arising from directed graphs*, arXiv:2103.06404, https://arxiv.org/abs/2103.06404.

[4] K. Rietsch, L. Williams, *Root, flow, and order polytopes, with connections to toric geometry*, arXiv:2406.15803, https://arxiv.org/abs/2406.15803.
