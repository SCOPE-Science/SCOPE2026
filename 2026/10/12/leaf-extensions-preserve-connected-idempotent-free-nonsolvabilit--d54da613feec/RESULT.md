# Leaf extensions preserve connected idempotent-free nonsolvability in evolution algebras
## Finding
Let \(E\) be a finite-dimensional evolution algebra over a field \(k\), with natural basis \(e_1,\ldots,e_d\). Suppose that:

- \(E\) is non-degenerate;
- the associated graph of this natural basis is connected;
- zero is the only idempotent of \(E\); and
- \(E\) is not solvable.

For any integer \(r\ge0\), form \(L_r(E)\) by adjoining natural-basis vectors \(f_1,\ldots,f_r\), preserving the multiplication on \(E\), and declaring
\[
f_j^2=e_1\quad(1\le j\le r),
\]
with every other product involving an \(f_j\) equal to zero. Then \(L_r(E)\) is again non-degenerate, graph-connected, idempotent-free, and nonsolvable. Consequently, by the standard connected-graph criterion for non-degenerate evolution algebras, \(L_r(E)\) is indecomposable as a direct sum of nonzero ideals.

Apply the lemma to the Hu--Wen exceptional algebra \(E_2\). For every field \(k\) with \(\operatorname{char}k\ne2\) and every \(n\ge3\), this gives an explicit \(n\)-dimensional example \(A_n\) with natural basis \(e_1,\ldots,e_n\), mixed basis products zero, and
\[
e_1^2=-e_1-e_3,\qquad e_2^2=-2e_1+2e_2,\qquad e_3^2=e_1+e_3,\qquad e_i^2=e_1\quad(4\le i\le n).
\]
Thus the higher-dimensional failure of the solvability-versus-idempotent implication persists without zero direct summands and under the simultaneous structural requirements of non-degeneracy and indecomposability.

## Assumptions and scope
An evolution algebra has a natural basis whose distinct basis elements multiply to zero. Its derived series is \(E^{(1)}=E\) and \(E^{(m+1)}=E^{(m)}E^{(m)}\). Here non-degenerate means \(\operatorname{Ann}(E)=0\), and indecomposable means not expressible as a direct sum of two nonzero ideals.

The leaf-extension lemma itself has no characteristic restriction. The characteristic condition \(\operatorname{char}k\ne2\) enters only through the Hu--Wen seed used in the all-dimensional corollary.

## Proof
Write an element of \(L_r(E)\) uniquely as
\[
x+y,\qquad x\in E,\qquad y=\sum_{j=1}^r b_jf_j.
\]
Because no basis square in the construction has an \(f_j\)-component, the \(f_j\)-coordinate of \((x+y)^2\) is zero. Hence, if \((x+y)^2=x+y\), then every \(b_j=0\). The idempotent equation then reduces to \(x^2=x\) inside \(E\), forcing \(x=0\). Thus leaf extension preserves idempotent-freeness.

Every original natural-basis square remains nonzero because \(E\) is non-degenerate, and every new square is the nonzero vector \(e_1\). If an element annihilates \(L_r(E)\), multiplication by each natural-basis vector shows that every coefficient is zero. Therefore \(L_r(E)\) is non-degenerate.

The associated graph is obtained from the connected graph of \(E\) by attaching each new vertex \(f_j\) to vertex \(e_1\). It is therefore connected. The decomposition theorem of Cabrera Casado, Siles Molina, and Velasco says that a non-degenerate evolution algebra is irreducible exactly when its associated graph is connected, so \(L_r(E)\) is indecomposable.

The original algebra \(E\) is a subalgebra of \(L_r(E)\). Inductively,
\[
E^{(m)}\subseteq L_r(E)^{(m)}\qquad(m\ge1).
\]
If \(L_r(E)\) were solvable, then some term on the right would vanish, forcing the corresponding derived term of \(E\) to vanish. This contradicts nonsolvability of \(E\). Thus leaf extension preserves nonsolvability.

For the explicit corollary, set
\[
u=e_1+e_3,\qquad v=e_2+e_3,\qquad S=\operatorname{span}\{u,v\}.
\]
The Hu--Wen multiplication gives
\[
u^2=0,\qquad uv=u,\qquad v^2=-u+2v,
\]
so \(S^2=S\). For \(A_3=E_2\), one has \(A_3^{(m)}=S\) for \(m\ge2\). For \(n\ge4\), the additional square \(e_4^2=e_1\) gives
\[
A_n^{(2)}=\operatorname{span}\{e_1,e_2,e_3\},
\]
whose square is \(S\); hence \(A_n^{(m)}=S\) for every \(m\ge3\).

## Verification
The leaf-extension proof is symbolic and uniform in \(r\). The accompanying `verify.py` is a finite regression check for the explicit Hu--Wen corollary. It checks the multiplication identities, graph connectivity, nonzero basis squares, derived-space ranks, and exhaustive idempotent counts in selected small prime fields and dimensions. Its expected terminal line is `CHECK_OK`.

## Relationship to prior work
Hu and Wen construct the three-dimensional idempotent-free nonsolvable algebra \(E_2\) over every field of characteristic different from \(2\). To obtain higher-dimensional complex counterexamples, they explicitly use direct sums \(E_2\oplus Z_{n-3}\) with zero algebras; those examples are degenerate and decomposable for \(n>3\).

A concurrent 2026 paper by Barei gives a different three-dimensional complex counterexample and remarks that it can be extended to any dimension. Inspection of the complete five-page paper found no statement about non-degeneracy, connectedness, irreducibility, indecomposability, or annihilators, and no general leaf-extension lemma. Thus its all-dimensional remark covers the existence of larger counterexamples, but it does not imply the structural preservation result proved here.

Cabrera Casado, Siles Molina, and Velasco supply the general implication from non-degeneracy plus graph connectedness to irreducibility. Their decomposition theorem does not supply the idempotent-preserving leaf extension or the all-dimensional counterexamples above.

## Limitations
The result does not classify all indecomposable idempotent-free nonsolvable evolution algebras. The Hu--Wen corollary excludes characteristic \(2\), although the abstract leaf-extension lemma itself does not. Barei's statement that his example can be extended to any dimension leaves a residual originality risk that an unstated intended extension may share some features of the present construction; the inspected paper does not state the structural properties or the general preservation lemma claimed here.

## References
1. Xing-Yu Hu and Ran Wen, *Idempotent-free non-solvable evolution algebras over \(\mathbb{C}\)*, arXiv:2609.25023v1, 2026.
2. Andres Barei, *On Solvable Evolution Algebras and a Conjecture by García-Martínez and Pérez-Rodríguez*, 2026.
3. Yolanda Cabrera Casado, Mercedes Siles Molina, and M. Victoria Velasco, *Evolution algebras of arbitrary dimension and their decompositions*, arXiv:1601.01832v2, 2016; Linear Algebra and its Applications 495 (2016), 122--162.
