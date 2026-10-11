# A mod-11 split in the branched-cover homology of the Himeno--Teragaito links
## Finding
For every integer \(m\ge1\), let
\[
Y_m=(K_m\cup A)(2m+15,0),
\]
where \(K_m\cup A\) is the two-component link used by Himeno and Teragaito. Their Montesinos-trick construction identifies
\[
Y_m\cong\Sigma_2(D(1-m)),
\]
where \(D(1-m)\) is quasi-alternating. Put
\[
d=\gcd(m+2,11).
\]
Then
\[
H_1(Y_m;\mathbb Z)\cong
\mathbb Z/d\mathbb Z\oplus
\mathbb Z/((m+2)^2/d)\mathbb Z.
\]
Equivalently,
\[
H_1(Y_m;\mathbb Z)\cong
\begin{cases}
\mathbb Z/(m+2)^2\mathbb Z,&m\not\equiv9\pmod{11},\\
\mathbb Z/11\mathbb Z\oplus\mathbb Z/((m+2)^2/11)\mathbb Z,&m\equiv9\pmod{11}.
\end{cases}
\]
Thus the source family's double branched covers have cyclic first homology for ten residue classes modulo \(11\), but a genuinely noncyclic first homology group on the class \(m\equiv9\pmod{11}\). In particular, every \(D(1-m)\) in that residue class is not a two-bridge link.

## Assumptions and scope
The parameter is an arbitrary integer \(m\ge1\). Integral surgery coefficients are measured in the usual meridian--preferred-longitude coordinates. Reversing an orientation can change the signs of the two off-diagonal entries in the surgery matrix, but it does not change its Smith normal form.

The conclusion concerns only the first integral homology group of the double branched cover and the resulting two-bridge obstruction. It does not classify the manifolds \(Y_m\), nor does cyclic first homology in the other residue classes imply that \(Y_m\) is a lens space.

## Proof
Himeno and Teragaito state that the linking number of \(K_m\) with \(A\), under suitable orientations, is \(m+2\), and they consider surgery coefficients \(2m+15\) on \(K_m\) and \(0\) on \(A\). Therefore the first homology of the filled manifold is presented by the integral linking matrix
\[
L_m=
\begin{pmatrix}
2m+15&m+2\\
m+2&0
\end{pmatrix}.
\]
Indeed, the meridians of the two link components generate the first homology of the exterior, and the two filling slopes impose the two rows of this matrix.

The matrix has full rank because
\[
\det L_m=-(m+2)^2\ne0.
\]
For a full-rank \(2\times2\) integer matrix, the first Smith invariant is the greatest common divisor of its entries. Hence
\[
d_1=\gcd(2m+15,m+2)=\gcd(11,m+2)=d,
\]
where the middle equality follows from
\[
(2m+15)-2(m+2)=11.
\]
The product of the two Smith invariants is the absolute determinant, so
\[
d_2=\frac{(m+2)^2}{d}.
\]
Because \(d\) is either \(1\) or \(11\), and \(11\mid(m+2)\) whenever \(d=11\), one has \(d\mid d_2\). Thus the Smith normal form is \(\operatorname{diag}(d,d_2)\), which proves the displayed homology decomposition.

Now \(d=11\) exactly when \(m+2\equiv0\pmod{11}\), that is, exactly when \(m\equiv9\pmod{11}\). In that case both invariant factors are divisible by \(11\), so the group is noncyclic. In every other residue class \(d=1\), so the first summand is trivial and the group is cyclic of order \((m+2)^2\).

Finally, the double branched cover of a two-bridge link is a lens space (with the usual degenerate conventions in the trivial cases), and a lens space has cyclic first homology. Since Himeno and Teragaito identify \(Y_m\) with the double branched cover of \(D(1-m)\), the noncyclic cases \(m\equiv9\pmod{11}\) cannot be two-bridge links.

## Verification
The primary preprint was inspected at Lemma 3.1 and Claim 3.2. It records the surgery \((K_m\cup A)(2m+15,0)\), the linking number \(m+2\), the handle-slide identity producing the coefficient \(11\), the link \(D(1-m)\), its determinant \((m+2)^2\), its quasi-alternating property, and the identification of the surgery manifold with its double branched cover.

The homology computation was reconstructed independently from the surgery relations. The determinant of the presentation matrix is \(-(m+2)^2\), agreeing with the source's branch-link determinant. The Smith invariants multiply to \((m+2)^2\), and the first invariant is exactly \(\gcd(m+2,11)\). For example, the groups at \(m=1,2,9,20\) are respectively \(\mathbb Z/9\mathbb Z\), \(\mathbb Z/16\mathbb Z\), \(\mathbb Z/11\mathbb Z\oplus\mathbb Z/11\mathbb Z\), and \(\mathbb Z/11\mathbb Z\oplus\mathbb Z/44\mathbb Z\).

No finite enumeration is used to prove the all-parameter statement.

## Relationship to prior work
Himeno and Teragaito introduce the family \(D(1-m)\) as the branch set in their proof that a related surgery is an L-space. They compute only the determinant \((m+2)^2\) of the branch link, not the Smith normal form or the cyclic/noncyclic classification of the cover's first homology. Their handle-slide calculation is nevertheless what exposes the fixed integer \(11\) responsible for the congruence split.

The full first-homology group is strictly finer than its order: the determinant alone cannot distinguish \(\mathbb Z/q^2\mathbb Z\) from noncyclic groups of the same order. Here that distinction becomes periodic and exact, and it gives an infinite obstruction to the branch links being two-bridge.

Targeted searches for the exact branch-link notation, the surgery coefficients, Smith normal form, cyclicity, the congruence \(m\equiv9\pmod{11}\), and two-bridge consequences did not locate an equivalent statement. The closest indexed result using the same Himeno--Teragaito family concerns crossing number and bounded hyperbolic volume, not branched-cover homology.

## Limitations
The argument computes only \(H_1\); it does not determine the homeomorphism type, linking pairing, Heegaard Floer correction terms, or fundamental group of \(Y_m\). Noncyclic first homology obstructs a lens-space cover, but cyclic first homology does not prove that the cover is a lens space or that the branch link is two-bridge.

The Smith-normal-form calculation is short and uses standard surgery algebra. Its mathematical value is the exact all-parameter group structure and the resulting infinite congruence obstruction for the newly introduced quasi-alternating branch links. An unindexed note could contain the same refinement.

## References
1. K. Himeno and M. Teragaito, *Asymmetric L-space knots with arbitrary braid index*, arXiv:2609.28917v1, first posted 2026-09-24; especially Lemma 3.1 and Claim 3.2.
2. W. B. R. Lickorish, *An Introduction to Knot Theory*, Graduate Texts in Mathematics 175, Springer, 1997; the discussion of double branched covers of two-bridge links.
