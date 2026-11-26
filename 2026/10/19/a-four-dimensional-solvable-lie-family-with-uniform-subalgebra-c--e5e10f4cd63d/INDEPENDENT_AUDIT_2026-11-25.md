# Independent mathematical audit

## correctness

PASS

Every internal subspace of the abelian V is a subalgebra (2q²+2q+4 choices). An external subspace is K(e+w)+W, with w mod W, and closes iff W is invariant under T=diag(1,1,λ); distinct eigenvalues force W=(W∩X)⊕(W∩Y). Summing the q^{3−dim W} cosets gives (q+1)(2q²+q+1) external subalgebras. A mixed pair fails iff the image of the internal subspace in V/W is noninvariant. For W=0 there are 2(q²−1) such internal subspaces; for W a line in X the quotient has q−1 mixed lines, each with q+1 preimages as a projected subspace (q lines and one plane). Larger W or W meeting Y gives a scalar quotient and no failures. Including both orders gives 2q²(q²−1)(3q+1). For two exterior subalgebras W_1,W_2 and cosets w_1,w_2, closure fails iff their coset difference in V/(W_1+W_2) is nonzero in both eigenspace projections. The difference map has fibres of size q^{3−dim(W_1∩W_2)}. Only two zero kernels, zero plus an X-line in either order, and two copies of the same X-line contribute, giving q²(q−1)²(q+1)(3q+1). Adding yields B(q); the displayed expansion and leading coefficient ratio give sd and the limit 1/4. Any K-linear isomorphism preserves the derived ideal V and intertwines the two actions up to a scalar; the uniquely repeated eigenvalue 1 forces scalar 1. All counting and projection arguments work in characteristic two as well. The frozen RREF verifier was inspected, not run; its recorded small-field results corroborate but do not establish the universal formula.

## originality

PASS

De Graaf's classification already distinguishes these isomorphism types, and the permutability degree itself is established terminology. The supported distinct content is the exact ordered-pair failure polynomial and subalgebra count for this normalized split family. The later affine-stabilization formula indeed covers exactly the same incidence structure: on the same vector space P_Y=(T−I)/(λ−1), and replacing T by P_Y does not change the subalgebra test for any vector subspace, hence also does not change sum-closure. The later entry explicitly describes the diagonal calculation as earlier; it is independent evidence of equivalent mathematical coverage, not evidence that the frozen calculation merely specialized an earlier affine count. The checked earlier primary results do not supply such a count.

## value

PASS

This computes a full ordered-pair incidence probability for a natural isomorphism family in the smallest dimension beyond the plane-count framework. It quantifies how often sum closure fails, shows a uniform 1/4 limiting degree for the family, and exhibits exactly what this invariant cannot distinguish about its q−2 isomorphism types. The informative part is the finite incidence calculation and mixed-versus-exterior failure split, not the familiar normal form or the scalar shift by itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
