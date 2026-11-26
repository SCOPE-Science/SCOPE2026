# Independent mathematical audit

## correctness

PASS

Use the simple forbidden union, counting each common edge once. Selecting j disjoint forbidden edges leaves (2n−2j−1)!! possible extensions, while an overlapping selection has zero extensions. Inclusion–exclusion therefore applies the signed odd-double-factorial functional to the product of the matching-generating polynomials of the union components. For a cycle of length l≥4 the trace of T^l with T=[[1,z],[1,0]] counts the weighted cyclic binary edge selections with no adjacent 1s. Cayley–Hamilton or the two-eigenvalue identity yields tr(T^{2m})²−tr(T^{4m})=2 det(T^{2m})=2z^{2m}; multiplication by the residual polynomial and shifting the functional produces exactly 2d(ρ), including sign and empty residual. The complement of the residual forbidden union has minimum degree ≥2r−3≥r for r≥3, so Dirac yields a Hamilton cycle and hence a perfect matching. For r=2 the complement has a perfect matching in both types; r=0 and r=1 give 1 and 0 respectively. For ρ=(1) the witnesses are non-neighbours of A. After one complete round there are the three classes {A}, N(A), and its remaining non-neighbours. A witness has zero adjacency into {A}; common-neighbour equality and regularity determine both other counts. Thus the second-round colours coincide. The natural full automorphism action follows from Godsil–Meagher Lemma 10.1 and preserves the cycle type, so the witnesses are in distinct full rooted orbits. Independent bounded counts give 33 versus 31 for n=4 and 328 versus 328 for n=5; they are consistency checks only.

## originality

PASS

The association scheme, the full natural automorphism group, and the transfer and refinement tools are prior. The inspected comparisons did not cover the single-shift identity with its unique exceptional residual and explicit odd-size rooted refinement obstruction. A same-day distinct record exhibits a genuine counting-logic overlap but on different objects and without a marked vertex.

## value

PASS

The formula isolates an exact local change in a natural graph under a natural equal-cycle split, identifying when the second-round rooted count loses a real orbit distinction. It gives an explicit all-odd-size finite-round lower bound in a graph family with known but nontrivial symmetry; neither the finite counts alone nor the old automorphism theorem gives that lower bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
