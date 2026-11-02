# A nonsplit toric stable limit of the characteristic-three Auer–Top quartic pencil

## Finding
Over \(K=\mathbb F_3((t))\), consider the genus-three plane quartic
\[
 C_t:\quad x^4+y^4+z^4=(1+t^2)(x^2y^2+y^2z^2+z^2x^2).
\]
The following explicit model has nonsplit, totally toric stable reduction:
\[
\mathscr C:\quad Q=tw,\qquad w^2=R
\]
in the relative weighted projective space \(\mathbb P(1,1,1,2)_{\mathbb F_3[[t]]}\), where \(Q=x^2+y^2+z^2\), \(R=x^2y^2+y^2z^2+z^2x^2\), and \(w\) has weight two.

The geometric special fiber consists of two smooth rational conics meeting at four transverse \(\mathbb F_3\)-rational nodes. Arithmetic Frobenius swaps the two components and fixes all four nodes. The connected generalized Jacobian is therefore
\[
 \operatorname{Pic}^0(\mathscr C_0/\mathbb F_3)\simeq
 \left(R^1_{\mathbb F_9/\mathbb F_3}\mathbb G_m\right)^3,
 \qquad \#\operatorname{Pic}^0(\mathscr C_0)(\mathbb F_3)=64.
\]
At every node the model has completed étale-local equation \(uv=t^2\) after passage to \(\mathbb F_9\). Consequently its minimal regular semistable model has dual graph \(K_{2,4}\), and the **geometric** Néron component group of the generic-fiber Jacobian is
\[
 \Phi(\overline{\mathbb F}_3)\simeq
 (\mathbb Z/2\mathbb Z)^2\oplus\mathbb Z/8\mathbb Z.
\]
Its order is \(32\). The stable special fiber itself has precisely four \(\mathbb F_3\)-points, all singular.

## Assumptions and scope
The residue characteristic is exactly three; \(K=\mathbb F_3((t))\) and its valuation ring is \(A=\mathbb F_3[[t]]\). The family is the Auer–Top symmetric quartic with parameter \(\lambda=t^2\). The quartic is smooth of genus three over \(K\), because \(\lambda\ne0,1\) and \(\lambda+3\ne0\) in \(K\). Every statement about geometric components or geometric component groups means after extension of the residue field to its algebraic closure. The Néron component-group structure is *not* asserted for the subgroup of \(\mathbb F_3\)-rational components.

## Proof
**1. The model and its generic fiber.** Set \(S=x^2-y^2\) and \(B=x^2+y^2\). In characteristic three the polynomial identities are
\[
 x^4+y^4+z^4-(1+\lambda)R=Q^2-\lambda R,
 \qquad R+S^2=BQ.
\]
On \(t\ne0\) the equation \(Q=tw\) eliminates \(w\) and gives \(Q^2-t^2R=0\), exactly the smooth plane quartic above. Neither fiber meets the singular vertex of the weighted projective ambient space. The complete intersection is proper; its reduced, pure one-dimensional special fiber and local complete-intersection property imply flatness over the DVR.

**2. Two conjugate components and four nodes.** At \(t=0\) one has \(Q=0\) and \(R=-S^2\). Over \(\mathbb F_9=\mathbb F_3(i)\), with \(i^2=-1\), the special fiber is the union
\[
 D_+: Q=0,\ w=iS,\qquad D_-:Q=0,\ w=-iS.
\]
Both are the smooth plane conic \(Q=0\), hence geometrically rational. Their intersections satisfy \(Q=S=w=0\). Since \(S=0\) forces \(x=\pm y\) and then \(z=\pm x\), projective scaling yields exactly
\[
 [x:y:z:w]=[1:\epsilon:\delta:0],\qquad
 \epsilon,\delta\in\{1,-1\}.
\]
At these four points \(S\) is a local parameter on \(Q=0\): on \(x=1\), \(\partial S/\partial y=-2y\) and \(\partial Q/\partial z=2z\) are units. The two branches have distinct tangents. Thus the fiber is nodal and each rational component meets the other in four nodes, making it stable. The arithmetic genus is \(0+0+4-2+1=3\). As \(i^3=-i\), Frobenius exchanges \(D_+\) and \(D_-\), while it fixes their four rational intersections. An \(\mathbb F_3\)-point must belong to both geometric components and hence is one of the four nodes.

**3. The exact thickness.** On \(x=1\), using \(Q=tw\), the other defining equation becomes
\[
 w^2+(1-y^2)^2=t(1+y^2)w.
\]
Write \(U=1-y^2\), \(B_1=1+y^2\), and \(W=w-tB_1/2\). Then
\[
 W^2+U^2=t^2B_1^2/4.
\]
At any of the four nodes, \(U\) is an étale local coordinate and \(B_1\) is a unit. Over \(\mathbb F_9\), put
\[
 u=2(W+iU)/B_1,\qquad v=2(W-iU)/B_1.
\]
Their Jacobian in \((W,U)\) is invertible, and \(uv=t^2\) exactly. Therefore there are four ordinary \(A_1\) singularities in the *total surface*, one over each stable node. Resolving each inserts one exceptional rational curve between the two original components, giving the simple graph \(K_{2,4}\).

**4. The arithmetic torus and geometric Néron component group.** The geometric dual graph of the stable fiber has two vertices and four parallel edges, so its first homology is free of rank three. All four edges are rational and Frobenius interchanges their endpoints. Orient all edges from \(D_+\) to \(D_-\); Frobenius reverses every orientation and hence acts as \(-1\) on \(H_1\). Since the normalizations have genus zero, the identity component of the generalized Jacobian is the unique rank-three torus with this Galois character lattice, namely the third power of the quadratic norm-one torus. Each norm-one factor has \(3+1=4\) rational points, giving \(4^3=64\).

For the geometric component group of the Jacobian's Néron model, use the degree-class/graph-Jacobian theorem for a regular semistable curve. The minimal regular model's dual graph \(K_{2,4}\) has reduced Laplacian
\[
 L=\begin{pmatrix}
4&-1&-1&-1&-1\\
-1&2&0&0&0\\
-1&0&2&0&0\\
-1&0&0&2&0\\
-1&0&0&0&2
\end{pmatrix}.
\]
Its Smith form is \(\operatorname{diag}(1,1,2,2,8)\), yielding the asserted finite abelian group and order \(32\).

## Verification
Run `python verify.py` with SymPy as declared in `requirements.txt`. The verifier checks the defining identities modulo three, exhaustively enumerates the four projective rational intersections, verifies the local completed-square equation and invertibility of its coordinate changes, and computes the exact integer Smith form. The geometric flatness, stable-curve criterion, and Néron comparison are mathematical arguments stated above; finite enumeration is not used as a substitute for them.

## Relationship to prior work
Auer and Top provide the smooth symmetric genus-three pencil and its elliptic isogeny decomposition. The broad geometric **stable-reduction type** lies within the general Ciani-quartic classification of Bouw–Coppola–Kılıçer–Kunzweiler–Lorenzo García–Somoza; no novelty is claimed for that reduction-type category alone. Busonero–Melo–Stoppino and Chiodo give general graph-theoretic formulas for Néron component groups, so the abstract graph-to-group step is also not new. The narrowly claimed additional calculation is the simultaneous **explicit arithmetic descent of the special-fiber torus**, four equal node thicknesses, and the resulting geometric Néron component group for this specific characteristic-three valuation of the Auer–Top family. This combined parameter-specific determination was not located in the inspected sources or mathematical-record searches. That negative search result is not a guarantee of historical priority.

## Limitations
This concerns one fixed characteristic-three degeneration, not the reduction types of the entire Ciani moduli stratum. The stable geometric graph and the graph-to-component-group formalism are known in greater generality. Only the geometric component group is determined, not its \(\mathbb F_3\)-rational subgroup or Frobenius action. The generic Jacobian's full Néron model, conductor, and higher ramification invariants are not computed. Historical overlap, especially in specialized older accounts of symmetric quartics and arithmetic stable reduction, remains possible; independent scientific auditing has not been performed.

## References
- Roland Auer and Jaap Top, *Some genus 3 curves with many points*, arXiv:math/0201320v1 (first public version 2002-01-16), §1.2, https://arxiv.org/pdf/math/0201320.
- Irene Bouw, Nirvana Coppola, Pınar Kılıçer, Sabrina Kunzweiler, Elisa Lorenzo García and Anna Somoza, *Reduction types of genus-3 curves in a special stratum of their moduli space*, arXiv:2003.07633 (first public version 2020-03-17), https://arxiv.org/pdf/2003.07633.
- Simone Busonero, Margarida Melo and Lidia Stoppino, *Combinatorial aspects of nodal curves*, arXiv:math/0602553, §3.2, https://arxiv.org/pdf/math/0602553.
- Alessandro Chiodo, *Néron models of \(\operatorname{Pic}^0\) via \(\operatorname{Pic}^0\)*, especially §4 on thickness-decorated graphs, https://webusers.imj-prg.fr/~alessandro.chiodo/papers/neron.
