# The two components of \(\mathcal M(-1,2,2)\) meet in dimension \(10\)
## Finding
Let
\[
\mathcal M=\mathcal M(-1,2,2)
\]
be the Gieseker moduli space of stable rank-\(2\) torsion-free sheaves on \(\mathbf P^3\). Let
\[
\overline{\mathcal R}\subset\mathcal M
\]
be the \(11\)-dimensional closure of the stable reflexive locus and let
\[
T=\operatorname T(-1,2,4,1)\subset\mathcal M
\]
be the \(15\)-dimensional elementary-transformation component.

Then
\[
\dim(\overline{\mathcal R}\cap T)=10.
\]
Therefore the intersection is a divisor in \(\overline{\mathcal R}\) and has codimension \(5\) in \(T\).

The initiating paper explicitly asks for the dimension of this intersection after Proposition 4.5. The argument below answers that dimension question. It does not prove that the intersection is irreducible.

## Assumptions and scope
All schemes are over \(\mathbf C\). We use the stable-pair correspondence of Almeida--Jardim--Oliveira for
\[
v_2=(-1,2,2).
\]
Fix
\[
0<\delta<\frac12.
\]
Write
\[
\mathcal P=\mathcal S^\delta(v_2(1))
\]
for the associated stable-pair space and
\[
\Gamma:\mathcal P\longrightarrow \operatorname{Hilb}^{2,-1},
\qquad
\Psi:\mathcal P\longrightarrow\mathcal M
\]
for the Hilbert-scheme and forgetful morphisms.

The Hilbert scheme
\[
\operatorname{Hilb}^{2,-1}=\operatorname{Hilb}^{2t+2}(\mathbf P^3)
\]
has two smooth irreducible components:
\[
C',\qquad \dim C'=11,
\]
whose general point is a conic together with a point, and
\[
S,\qquad \dim S=8,
\]
whose general point is a pair of skew lines.

Put
\[
D=C'\cap S.
\]

## Proof
The description of \(\operatorname{Hilb}^{2t+2}(\mathbf P^3)\) by Soulimani--Gulbrandsen says that \(D\) consists precisely of the following degenerations: an incident pair of lines with the spatial embedded point at their intersection, or a planar double line with a spatial embedded point.

The locus of distinct incident line pairs with their spatial embedded point has dimension \(7\). Indeed, choose the intersection point
\[
p\in\mathbf P^3,
\]
which contributes \(3\) parameters. Lines through \(p\) form \(\mathbf P^2\), so an unordered pair of distinct such lines contributes \(4\) parameters. For the resulting singular conic, the spatial embedded-point structure is the distinguished spatial member of the one-dimensional family of embedded-point structures. Hence this locus has dimension
\[
3+4=7.
\]

The planar-double-line part has dimension at most \(6\): choose a line in \(\mathbf P^3\) (\(4\) parameters), a plane containing it (\(1\) parameter), and the support point of the embedded structure on the line (\(1\) parameter). Consequently
\[
\dim D=7.
\]
A general point of the \(7\)-dimensional incident-line locus is nonplanar because the embedded point is spatial.

Almeida--Jardim--Oliveira decompose the stable-pair space as
\[
\mathcal P=\mathcal P_1\cup\mathcal P_2,
\]
where
\[
\mathcal P_1=\Gamma^{-1}(C'),
\qquad
\dim\mathcal P_1=15,
\]
and
\[
\mathcal P_2=\overline{\Gamma^{-1}(S\setminus D)},
\qquad
\dim\mathcal P_2=11.
\]
Moreover
\[
\Psi(\mathcal P_1)=T,
\qquad
\Psi(\mathcal P_2)=\overline{\mathcal R}.
\]

Because \(\Gamma\) is proper, the image \(\Gamma(\mathcal P_2)\) is closed. It contains the dense open set \(S\setminus D\), so
\[
\Gamma(\mathcal P_2)=S.
\]
Therefore
\[
Z:=\mathcal P_1\cap\mathcal P_2
=
(\Gamma|_{\mathcal P_2})^{-1}(D).
\]
The set \(Z\) is a proper closed subset of the irreducible \(11\)-fold \(\mathcal P_2\), hence
\[
\dim Z\le10.
\]
On the other hand, \(\Gamma|_{\mathcal P_2}:\mathcal P_2\to S\) is dominant between irreducible varieties of dimensions \(11\) and \(8\). Every nonempty fibre has dimension at least
\[
11-8=3.
\]
Since \(D\) has a \(7\)-dimensional component, a component of its inverse image dominating that component has dimension at least
\[
7+3=10.
\]
Thus
\[
\dim Z=10.
\]

It remains to compare \(Z\) with the intersection in the sheaf moduli space. The fibre of \(\Psi\) over a sheaf \(E\) is
\[
\Psi^{-1}([E])=\mathbf P H^0(E(1)),
\]
hence is irreducible. If
\[
[E]\in \Psi(\mathcal P_1)\cap\Psi(\mathcal P_2),
\]
then this irreducible projective-space fibre meets both closed sets \(\mathcal P_1\) and \(\mathcal P_2\), and it is covered by their intersections with the fibre because
\[
\mathcal P=\mathcal P_1\cup\mathcal P_2.
\]
Irreducibility of the fibre forces those two closed subsets to meet. Hence
\[
\Psi(Z)=
\Psi(\mathcal P_1)\cap\Psi(\mathcal P_2)
=
T\cap\overline{\mathcal R}.
\]

Finally, a general point of the \(7\)-dimensional incident-line part of \(D\) is nonplanar. Proposition 3.9 of the initiating paper gives
\[
h^0(E(1))=1
\]
exactly for a nonplanar associated scheme. Thus \(\Psi\) is generically one-to-one on a \(10\)-dimensional component of \(Z\) dominating that incident-line locus. Consequently
\[
\dim\Psi(Z)=10.
\]
This proves
\[
\dim(\overline{\mathcal R}\cap T)=10.
\]

## Verification
The accompanying `verify.py` checks the numerical dimension chain used by the proof:
\[
\dim D=3+4=7,
\qquad
\dim\mathcal P_2-\dim S=3,
\qquad
7+3=10,
\]
and the resulting codimensions
\[
11-10=1,
\qquad
15-10=5.
\]
It also checks that the planar-double-line stratum has parameter count at most \(6\), so it cannot raise the dimension of \(D\).

These finite checks do not replace the geometric inputs: the classification of the two Hilbert-scheme components and their intersection, the proper stable-pair morphism, the two stable-pair components, the projective-space fibres of \(\Psi\), or Proposition 3.9. Those are cited below and are used explicitly in the proof.

The saved replay output ends in `VERIFY_OK`.

## Relationship to prior work
Almeida--Jardim--Oliveira prove that \(\mathcal M(-1,2,2)\) has exactly the two components \(\overline{\mathcal R}\) and \(T\), with dimensions \(11\) and \(15\), and identify them as the images of the two components of the stable-pair space. After Proposition 4.5 they state explicitly that it would be interesting to determine whether
\[
\overline{\mathcal R}\cap T
\]
is irreducible and to compute its dimension. They do not give that dimension.

Soulimani--Gulbrandsen give the required detailed geometry of
\[
\operatorname{Hilb}^{2t+2}(\mathbf P^3).
\]
Their description identifies its component intersection as incident lines or planar double lines carrying the spatial embedded point. Their work does not address the rank-\(2\) sheaf-moduli intersection above.

Targeted searches for the exact moduli space, the two component names, the dimension \(10\), the stable-pair intersection, and equivalent formulations did not locate an earlier statement of this answer.

## Limitations
The result computes only the dimension. It does not settle the other part of the question in the initiating paper, namely whether
\[
\overline{\mathcal R}\cap T
\]
is irreducible.

The argument is set-theoretic at the final component-intersection level. It does not determine the scheme structure, multiplicity, generic singularity type, or local intersection multiplicity of the two components.

The dimension proof depends on the published geometric description of the Hilbert-scheme intersection and on the stable-pair correspondence. An older source using different notation for the same sheaf-moduli boundary remains a residual originality risk, although no such statement was located.

## References
1. C. Almeida, M. Jardim, L. Oliveira, *The moduli space of torsion-free sheaves with quasi-maximal third Chern class*, arXiv:2609.32668v1, 2026; especially Theorem 4.1, Proposition 4.4, Proposition 4.5, and Proposition 3.9.
2. S. Alaoui Soulimani, M. G. Gulbrandsen, *Bridgeland stability conditions and skew lines on \(\mathbf P^3\)*, Communications in Algebra 52 (2024), 3081--3114.
3. D. Chen, I. Coskun, S. Nollet, *Hilbert scheme of a pair of codimension two linear subspaces*, Communications in Algebra 39 (2011), 3021--3043.
4. M. Jardim, D. Mu, *Modular Serre correspondence via stable pairs*, arXiv:2501.08480, 2025.
