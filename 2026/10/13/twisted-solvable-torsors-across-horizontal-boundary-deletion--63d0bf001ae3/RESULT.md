# Twisted solvable torsors across horizontal boundary deletion
## Finding
Let \(X\) be a connected locally Noetherian scheme over \(\operatorname{Spec}\mathbf Z\), let \(D\) be a horizontal effective Cartier divisor, and put \(U=X\setminus\operatorname{Supp}(D)\). Assume Yamaguchi's condition \((\dagger)\): \(X\) is regular along \(D\); every prime component of \(D\) contains a normal-crossings point of residue characteristic \(2\); and, after every connected finite étale cover \(X'\to X\), every prime component of \(D\times_X X'\) has geometrically integral generic fiber.

For every finite locally constant sheaf \(\mathcal A\) of solvable groups on \(X_{\mathrm{et}}\), restriction induces a bijection of pointed sets
\[
H^1_{\mathrm{et}}(X,\mathcal A)\;\xrightarrow{\sim}\;H^1_{\mathrm{et}}(U,\mathcal A|_U).
\]
Here nonabelian \(H^1\) means isomorphism classes of torsors. If \(\mathcal A\) is abelian, the bijection is an isomorphism of groups.

## Assumptions and scope
Choose a geometric base point of \(U\), and write \(G=\pi_1^{\mathrm{et}}(U)\), \(H=\pi_1^{\mathrm{et}}(X)\), and \(K=\ker(G\to H)\). Yamaguchi's Theorem 2.5 proves that \(G\to H\) is surjective and that \(K\) is topologically perfect under the hypotheses above.

By the finite-lisse/fundamental-group equivalence, the stalk \(A\) of \(\mathcal A\) is a finite solvable group equipped with a continuous \(H\)-action. After pullback to \(U\), the \(G\)-action factors through \(H\), so \(K\) acts trivially on \(A\). No solvability assumption is imposed on the monodromy image in \(\operatorname{Aut}(A)\).

## Proof
A class in \(H^1_{\mathrm{et}}(U,\mathcal A|_U)\) is represented by a continuous nonabelian cocycle \(z:G\to A\). For \(k_1,k_2\in K\), triviality of the \(K\)-action gives
\[
z(k_1k_2)=z(k_1)z(k_2),
\]
so \(z|_K:K\to A\) is a continuous homomorphism. Its image is a finite quotient of the topologically perfect group \(K\), hence is perfect. It is also a subgroup of the solvable group \(A\), hence solvable. A perfect solvable finite group is trivial, so \(z(k)=1\) for every \(k\in K\).

Therefore \(z\) is constant on cosets of \(K\) and factors uniquely through a cocycle \(\bar z:H\to A\). Conversely every cocycle on \(H\) inflates to one on \(G\). The usual coboundary relation is defined by an element of \(A\) and is preserved in both directions because the action of \(G\) factors through \(H\). Thus inflation/restriction gives the claimed bijection on nonabelian \(H^1\). In the abelian case these pointed sets are groups and the same argument gives a group isomorphism.

## Verification
The critical geometric input is Yamaguchi's Theorem 2.5, where the kernel of \(\pi_1^{\mathrm{et}}(U)\to\pi_1^{\mathrm{et}}(X)\) is proved topologically perfect under exactly the stated condition \((\dagger)\). The identification of finite locally constant sheaves with finite fundamental-group sets/modules is the Stacks Project, Tag 0DV4; the torsor interpretation of first cohomology is recorded in Tags 03AG and 03AJ.

The only group-theoretic step is that a finite continuous image of a topologically perfect profinite group is perfect, while a perfect solvable group is trivial. This proves the statement without an enumeration or asymptotic argument.

## Relationship to prior work
Yamaguchi proves equality of maximal prosolvable quotients and a residual factorization criterion for linear representations, but the paper does not state a twisted torsor or \(H^1\) invariance theorem. The result here is not merely the constant-coefficient reformulation of the maximal-prosolvable quotient statement: a solvable coefficient group can have nonsolvable automorphism group. For example, for \(A=(\mathbf Z/2\mathbf Z)^4\), \(\operatorname{Aut}(A)=\operatorname{GL}_4(\mathbf F_2)\) is nonsolvable, while the argument above still applies to every monodromy action that comes from \(X\).

The Stacks Project supplies the standard equivalence between finite locally constant objects, fundamental-group actions, and torsors; it does not contain this boundary-deletion consequence.

## Limitations
The result concerns finite locally constant coefficient sheaves on \(X\) whose fiber group is solvable. It does not cover nonsolvable fibers, arbitrary coefficient sheaves defined only on \(U\), or higher étale cohomology. The proof is a formal but nontrivial consequence of the newly available topological-perfectness theorem, so the principal originality risk is that the same consequence may have been left implicit in unindexed discussions of perfect kernels.

## References
N. Yamaguchi, “Extension of solvable coverings across horizontal divisors over the integers”, arXiv:2610.02948v1, first public 2026-10-02, especially Theorem 2.5 and Corollary 2.6.

The Stacks Project, Tag 0DV4, “Locally constant sheaves and the fundamental group”.

The Stacks Project, Tags 03AG and 03AJ, “First cohomology and torsors”.
