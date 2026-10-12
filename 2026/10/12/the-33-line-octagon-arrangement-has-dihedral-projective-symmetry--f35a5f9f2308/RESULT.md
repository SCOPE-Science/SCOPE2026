# The \(33\)-line octagon arrangement has dihedral projective symmetry of order \(16\)
## Finding
Let \(r^2=2\). For the \(33\)-line arrangement \(\mathcal O_{33}\subset\mathbb P^2_{\mathbb C}\) written explicitly in Pokora--Roulleau, the full projective automorphism group is
\[
\operatorname{Aut}_{\mathbb P^2}(\mathcal O_{33})\cong C_8\rtimes C_2,
\]
where the nontrivial element of \(C_2\) acts on \(C_8\) by inversion. Hence the group is dihedral of order \(16\). One may take
\[
R=\begin{pmatrix}1&1&0\\-1&1&0\\0&0&\sqrt2\end{pmatrix},
\qquad
S=\begin{pmatrix}1&-1&0\\-1&-1&0\\0&0&\sqrt2\end{pmatrix}.
\]
In \(\operatorname{PGL}_3(\mathbb C)\), these satisfy \(R^8=S^2=1\) and \(SRS=R^{-1}\).

## Assumptions and scope
The arrangement is exactly the \(\mathcal O_{33}\) of Theorem B of arXiv:2403.20024v1, over \(\mathbb C\), with the displayed choice \(r^2=2\). The statement concerns projective automorphisms of the reduced union of its \(33\) lines. It does not classify abstract automorphisms of the full intersection lattice independently of projective realizability, nor does it address the related \(49\)- or \(61\)-line arrangements.

## Proof
Exact intersection of the \(33\) displayed line normals gives the published multiplicity profile
\[
n_2=108,\qquad n_3=40,\qquad n_5=16,\qquad n_8=5.
\]
The five multiplicity-eight points are precisely
\[
[0:0:1],\quad [1:1+\sqrt2:0],\quad [1:1-\sqrt2:0],\quad
[1:-1+\sqrt2:0],\quad [1:-1-\sqrt2:0].
\]
Among them, the latter four are collinear on \(z=0\), while \([0:0:1]\) is off that line. Thus every projective automorphism preserves \(z=0\) and fixes \([0:0:1]\). After projective scaling its matrix therefore has block form
\[
\begin{pmatrix}A&0\\0&\kappa\end{pmatrix},
\qquad A\in\operatorname{GL}_2(\mathbb C),\quad \kappa\ne0.
\]

On \(z=0\), write the four slopes as
\[
1+\sqrt2,\quad 1-\sqrt2,\quad -1+\sqrt2,\quad -1-\sqrt2.
\]
Their cross-ratio is \(-1\), so they form a harmonic quadruple. Its stabilizer in \(\operatorname{PGL}_2(\mathbb C)\) has order \(8\). Hence there are at most eight possibilities for the projective class of \(A\).

For each of those eight possibilities, the image of the first displayed line of \(\mathcal O_{33}\) restricts \(\kappa\) to a finite list. Exact substitution against all \(33\) line normals leaves exactly two values of \(\kappa\) for each \(A\). Therefore
\[
|\operatorname{Aut}_{\mathbb P^2}(\mathcal O_{33})|\le16.
\]
Conversely, the exact line-normal calculation verifies \(16\) distinct projective transformations preserving all \(33\) lines. The displayed matrices \(R\) and \(S\) belong to this set, have projective orders \(8\) and \(2\), and satisfy \(SRS=R^{-1}\). They therefore generate a dihedral subgroup of order \(16\), which meets the upper bound and is the full automorphism group.

## Verification
The standalone script `verify.py` uses only Python's standard library and exact arithmetic in \(\mathbb Q(\sqrt2)\). It reconstructs all intersection points and verifies the multiplicity counts; identifies the five multiplicity-eight points; enumerates all \(24\) permutations of the four points at infinity and solves exactly for the \(\operatorname{PGL}_2\) maps, obtaining exactly \(8\); checks every possible lift against every one of the \(33\) line normals, obtaining exactly \(16\); and verifies the order profile
\[
1^1,\quad 2^9,\quad 4^2,\quad 8^4,
\]
which is the profile of the dihedral group of order \(16\). A clean replay prints `VERIFY_OK`.

## Relationship to prior work
Pokora--Roulleau construct \(\mathcal O_{33}\) from a regular octagon by a point-line operator, list all \(33\) equations, prove rigidity, and prove freeness with exponents \((15,17)\). Their paper does not state the projective automorphism group. A related paper of Kühne--Roulleau studies the realization-space matroid \(M_n\) attached to a regular \(n\)-gon together with its symmetry lines and records \(\operatorname{Aut}(M_n)\cong\mathbb Z/n\mathbb Z\rtimes(\mathbb Z/n\mathbb Z)^*\). That is a different \(2n\)-line matroid and does not determine the projective stabilizer of the \(33\)-line arrangement here.

## Limitations
The result is specific to the displayed \(\mathcal O_{33}\). It does not claim that all combinatorial automorphisms of its intersection lattice are projectively realizable, and it does not give automorphism groups for the analogous \(\mathcal O_{49}\) or \(\mathcal O_{61}\). A residual originality risk is that the same stabilizer may have been computed under different arrangement nomenclature or in non-indexed computational notes.

## References
1. P. Pokora and X. Roulleau, *Construction of free arrangements using point-line operators*, arXiv:2403.20024v1, first public 2024-03-29.
2. L. Kühne and X. Roulleau, *Regular polygons, line operators, and elliptic modular surfaces as realization spaces of matroids*, arXiv:2312.03470v1.
