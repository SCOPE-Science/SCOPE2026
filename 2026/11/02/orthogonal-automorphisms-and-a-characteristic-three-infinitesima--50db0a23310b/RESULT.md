# The characteristic-three automorphism scheme of complete-bipartite evolution algebras

## Finding

Let \(k\) be a field of characteristic different from two and let \(r,s\ge2\) be integers invertible in \(k\). Let \(E=U\oplus V\) be the graph evolution algebra of \(K_{r,s}\), where \(U=k^r\), \(V=k^s\), and \(u_0\), \(v_0\) denote the vectors with all coordinates equal to one. The multiplication is
\[
 (u,v)(u',v')=((v\cdot v')u_0,(u\cdot u')v_0).
\]
Put \(U_0=u_0^\perp\), \(V_0=v_0^\perp\) for the coordinate dot products. The affine automorphism **group scheme** is
\[
 G=\mu_3\times O(U_0)\times O(V_0)
\]
if \(r\ne s\). If \(r=s\), it is \(G\rtimes (\mathbb Z/2\mathbb Z)_k\), with the constant group scheme acting by \((\alpha,P,Q)\mapsto(\alpha^{-1},Q,P)\) under the coordinate identification of the two parts. In particular, it is smooth exactly when \(\operatorname{char} k\ne3\). Its dimension is \(d=\binom{r-1}{2}+\binom{s-1}{2}\); its tangent dimension at the identity is \(d+1\) in characteristic three and \(d\) otherwise. In characteristic three the additional direction is the scalar derivation \(D|_U=\mathrm{id}\), \(D|_V=-\mathrm{id}\), not tangent to the reduced geometric group.

## Proof

Over any field extension of \(k\), the rank of multiplication by \((u,v)\) is the number of nonzero components among \(u,v\): the coordinate dot forms are nondegenerate and the images from the two summands are in distinct lines. Thus the locus of elements with multiplication rank at most one is \(U\cup V\). The only maximal linear subspaces in this union are the two summands, since a linear subspace containing one nonzero vector of each summand contains their sum. A field-valued automorphism therefore preserves the two sides or, only if \(r=s\), exchanges them. In the latter case the coordinate exchange \(\tau\) is an involutory automorphism.

To determine the scheme rather than just its field-valued points, consider the principal open where both diagonal blocks \(A,B\) of an automorphism matrix \(\left(\begin{smallmatrix}A&C\\D&B\end{smallmatrix}\right)\) are invertible. This open can be tested over any commutative \(k\)-algebra. Products between opposite sides give \(A^{\mathsf T}C=0\) and \(D^{\mathsf T}B=0\), hence \(C=D=0\) there. The submodule of products is spanned by the two direct summand vectors \(u_0,v_0\). Preservation of this submodule by the automorphism and its inverse gives \(Au_0=\alpha u_0\), \(Bv_0=\beta v_0\) with \(\alpha,\beta\) units. Product preservation within each side is equivalent to
\[
 A^{\mathsf T}A=\beta I_r,\qquad B^{\mathsf T}B=\alpha I_s.
\]
Taking the norms of \(u_0,v_0\) and using the units \(r,s\) gives \(\beta=\alpha^2\) and \(\alpha=\beta^2\), so \(\alpha^3=1\). Orthogonal decomposition into the all-ones line and its complement is valid over every coefficient algebra by the projections obtained by dividing by \(r,s\). Therefore the matrices are exactly \(A=\alpha(1\oplus P)\), \(B=\alpha^2(1\oplus Q)\), for the two isometries \(P,Q\). Conversely these matrices satisfy the displayed equations and preserve the two side products and the mixed products, giving the asserted isomorphism on the open.

In the balanced case its translate by \(\tau\) is disjoint from it, since simultaneous membership would require a block-diagonal matrix with invertible off-diagonal blocks. The one open (unbalanced case) or the union of the two opens (balanced case) covers the scheme: the field-valued argument applies to the residue field of every point. This proves the scheme identification, including over disconnected coefficient algebras. Conjugation by \(\tau\) interchanges the isometries and replaces \(\alpha\) by \(\alpha^2=\alpha^{-1}\).

Each orthogonal factor is smooth in characteristic different from two and has dimension \(\binom{r-1}{2}\) or \(\binom{s-1}{2}\), respectively. The finite factor \(\mu_3\) is étale if \(3\ne0\) and has coordinate algebra \(k[z,z^{-1}]/((z-1)^3)\) in characteristic three. In that characteristic the reduced geometric group omits the \(\mu_3\) direction, and setting \(\alpha=1+\epsilon\) over the dual numbers scales the second side by \(1+2\epsilon=1-\epsilon\). This is the stated derivation. In other characteristics \((1+\epsilon a)^3=1\) forces \(a=0\). The constant exchange factor is étale and does not change tangent dimension.

## Scope, related results, and verification

The result is about the automorphism functor and its infinitesimal structure for a singular algebra: \(\dim E^2=2<r+s\). The finite-field rational-point classification and orders, including cases where the characteristic divides a part size, are treated in [*Automorphisms of complete-bipartite evolution algebras over odd finite fields*](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-automorphisms-of-complete-bipartite-evolution-algebras-over-odd--79c475fcec77); those orders are not a claim here. A rational-point classification alone cannot see the extra dual-number direction. The graph-diagonal cube-root symmetry for bipartite algebras is already known (Rodiño Montoya, Viana Bedoya and Henao, [arXiv:2505.15604v1](https://arxiv.org/html/2505.15604v1), §2.3). Elduque and Labra's group-scheme exact sequence in [arXiv:1902.02191](https://arxiv.org/html/1902.02191) concerns perfect evolution algebras; here the mixed product equations identify the entire singular-algebra scheme and isolate the only nonreduced factor.

The companion `verify.py` checks multiplication and tangent equations in small prime-field examples; these diagnostics do not prove the assertion for arbitrary coefficient algebras. No assertion is made in characteristic two or when a part size is zero in \(k\).
