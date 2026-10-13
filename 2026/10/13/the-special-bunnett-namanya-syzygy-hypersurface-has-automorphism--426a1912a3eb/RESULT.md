# The special Bunnett–Namanya syzygy hypersurface has automorphism group \(\operatorname{GL}_2\)
## Finding
Work over \(\mathbf C\). Consider the smooth bidegree-\((2,1)\) hypersurface
\[
X_0=V\!\left(y_0x_0^2+y_1x_1^2+y_2x_2^2+y_3x_0x_1\right)\subset \mathbf P^2\times\mathbf P^3.
\]
Then
\[
\operatorname{Aut}(X_0)\cong \operatorname{GL}_2(\mathbf C).
\]
In particular, \(\operatorname{Aut}(X_0)\) is connected of dimension \(4\), and
\[
h^0(X_0,T_{X_0})=4.
\]
The diagonal two-dimensional torus displayed by Bunnett--Namanya is therefore a maximal torus, not the whole positive-dimensional automorphism group.

## Assumptions and scope
The ground field is \(\mathbf C\). The hypersurface is exactly the special smooth member displayed in Section 5.4.2 of Bunnett--Namanya. Put
\[
W_0=\langle x_0^2,x_1^2,x_2^2,x_0x_1\rangle\subset H^0(\mathbf P^2,\mathcal O_{\mathbf P^2}(2)).
\]
Its four generators have no common zero, so the associated syzygy construction is a smooth projective bundle. The claim is the full abstract/algebraic automorphism group over \(\mathbf C\), using the source's extension argument that identifies automorphisms of these \(X_W\) with the projective stabilizer of \(W\).

## Proof
Bunnett--Namanya show in their syzygy-bundle discussion that the Picard group is \(\mathbf Z\oplus\mathbf Z\), that its two distinguished classes cannot be exchanged, and that the corresponding complete linear systems extend every automorphism to the ambient product. For linearly independent coefficients this gives
\[
\operatorname{Aut}(X_W)\simeq \operatorname{Stab}_{\operatorname{PGL}_3}(W).
\]
They also note that passing to the annihilator in the dual quadratic representation preserves the stabilizer.

For the displayed member, under the coefficient pairing the annihilator is the pencil
\[
U=W_0^\perp=\langle z_0z_2,z_1z_2\rangle.
\]
Its base ideal is
\[
(z_0z_2,z_1z_2)=(z_2)\cap(z_0,z_1),
\]
so its base scheme is the reduced union
\[
H\cup\{p\},\qquad H=V(z_2),\quad p=[0:0:1].
\]
Any projective transformation preserving \(U\) preserves its base scheme. Since its two irreducible components have different dimensions, it must preserve \(H\) and \(p\) separately.

Conversely, a projective transformation preserving both \(H\) and \(p\) is represented, in the chosen coordinates, by a block-diagonal matrix
\[
\begin{pmatrix}
A&0\\
0&c
\end{pmatrix},
\qquad A\in\operatorname{GL}_2(\mathbf C),\quad c\in\mathbf C^\times.
\]
Such a matrix plainly preserves \(z_2\langle z_0,z_1\rangle=U\). Hence
\[
\operatorname{Stab}_{\operatorname{PGL}_3}(U)
=\bigl(\operatorname{GL}_2\times\mathbf G_m\bigr)/\mathbf G_m^{\mathrm{diag}}.
\]
The map represented by
\[
(A,c)\longmapsto c^{-1}A
\]
induces an isomorphism of algebraic groups
\[
\bigl(\operatorname{GL}_2\times\mathbf G_m\bigr)/\mathbf G_m^{\mathrm{diag}}\cong\operatorname{GL}_2.
\]
Combining this with the source's automorphism--stabilizer identification proves the claim.

Finally, over characteristic zero the tangent space at the identity of the automorphism group is \(H^0(X_0,T_{X_0})\). Since \(\dim\operatorname{GL}_2=4\), the displayed group is smooth of dimension \(4\) and therefore
\[
h^0(X_0,T_{X_0})=4.
\]

## Verification
The primary full text was inspected at Section 5.4.2. It defines the syzygy hypersurfaces, states the automorphism--stabilizer identification, and then introduces exactly the displayed \(X_0\), proving it smooth and exhibiting only a diagonal torus action.

The included script `verify_bunnett_special_stabilizer.py` independently checks the infinitesimal stabilizer of
\[
U=\langle z_0z_2,z_1z_2\rangle.
\]
It obtains block-diagonal Lie algebra \(\mathfrak{gl}_2\oplus\mathfrak{gl}_1\), dimension \(5\) inside \(\mathfrak{gl}_3\), hence dimension \(4\) after quotienting by scalar matrices. Its recorded output ends in `VERIFY_OK`. This finite symbolic calculation checks the tangent computation; the global group identification follows from the base-scheme argument above.

## Relationship to prior work
Bunnett--Namanya prove the key reduction
\[
\operatorname{Aut}(X_W)\simeq\operatorname{Stab}_{\operatorname{PGL}_3}(W)
\]
and, for the special member \(X_0\), state that the diagonal torus acts faithfully, thereby showing that the automorphism group is positive-dimensional. They do not compute the full stabilizer of this special member. Their same section treats the general member via a four-point conic pencil, which is a different stabilizer stratum.

The present calculation determines the complete group for their explicit special example. Targeted searches using the exact equation, the annihilator pencil, syzygy-bundle terminology, projective-stabilizer language, and \(\operatorname{GL}_2\) aliases did not locate a checked source stating or implying this exact result.

## Limitations
The statement concerns this single special member in characteristic zero. It is not a classification of all degenerate/special four-dimensional subspaces \(W\subset H^0(\mathbf P^2,\mathcal O(2))\), nor does it describe every automorphism-group jump in the family. The proof relies on the source's ambient-extension identification for the smooth syzygy hypersurfaces and then computes the stabilizer of this particular annihilator pencil. No claim is made in positive characteristic.

## References
Dominic Bunnett and Caroline Namanya, *Finite automorphism groups of hypersurfaces via Bott vanishing*, arXiv:2609.38572v1, Section 5.4.2, first public 2026-09-29. https://arxiv.org/abs/2609.38572v1
