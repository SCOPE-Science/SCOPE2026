# Matrix amplification collapses \(\sqrt{\Delta}\)-fineness to fineness
## Finding
Let \(R\) be a nonzero unital \(\sqrt{\Delta}\)-fine ring, where \(\Delta(R)=\{a\in R: a+U(R)\subseteq U(R)\}\) and \(\sqrt{\Delta(R)}=\{a\in R: a^m\in\Delta(R)\text{ for some }m\ge1\}\). Then, for every integer \(n\ge2\), the full matrix ring \(M_n(R)\) is an ordinary fine ring: every nonzero matrix is a sum of a unit and a nilpotent matrix. Consequently, if a \(\sqrt{\Delta}\)-fine ring that is not fine exists, then fineness is not Morita-invariant: \(M_2(R)\) is fine while its standard full corner \(E_{11}M_2(R)E_{11}\cong R\) is not. Equivalently, a positive answer to full-corner descent for fine rings would force every \(\sqrt{\Delta}\)-fine ring to be fine.

This isolates the possible obstruction in the recent \(\sqrt{\Delta}\)-fine problem at matrix size one. All full matrix amplifications of size at least two already lie in the classical fine class.

## Assumptions and scope
All rings are associative, unital, and nonzero. For a ring \(S\), write
\[
\Delta(S)=\{a\in S: a+U(S)\subseteq U(S)\},
\qquad
\sqrt{\Delta(S)}=\{a\in S: a^m\in\Delta(S)\text{ for some }m\ge1\}.
\]
A ring is \(\sqrt{\Delta}\)-fine when every nonzero element is a sum of a unit and an element of \(\sqrt{\Delta(S)}\). A ring is fine when every nonzero element is a sum of a unit and a nilpotent.

The theorem applies to every integer \(n\ge2\). It does not prove that the original ring \(R\) is fine; that is precisely the remaining size-one question.

## Proof
Danchev, Hasanzadeh, Moussavi, and Javan prove two premises for a \(\sqrt{\Delta}\)-fine ring \(R\): first, \(R\) is simple; second, \(M_n(R)\) is \(\sqrt{\Delta}\)-fine for every \(n\ge1\).

Because \(R\) is a nonzero unital simple ring, its Jacobson radical is zero. Indeed, \(J(R)\) is a two-sided ideal, so simplicity gives \(J(R)=0\) or \(J(R)=R\), while \(1\notin J(R)\).

Leroy and Matczuk prove that for every unital ring \(S\) and every \(n\ge2\),
\[
\Delta(M_n(S))=J(M_n(S))=M_n(J(S)).
\]
Applying this with \(S=R\) gives \(\Delta(M_n(R))=0\). Therefore
\[
\sqrt{\Delta(M_n(R))}
=\{X\in M_n(R):X^m=0\text{ for some }m\ge1\},
\]
which is exactly the set of nilpotent matrices.

Now fix \(n\ge2\) and a nonzero \(X\in M_n(R)\). Since \(M_n(R)\) is \(\sqrt{\Delta}\)-fine, there are a unit \(U\in U(M_n(R))\) and \(A\in\sqrt{\Delta(M_n(R))}\) with \(X=U+A\). The preceding paragraph makes \(A\) nilpotent, so \(M_n(R)\) is fine.

For the Morita consequence, take \(n=2\) and \(e=E_{11}\). The idempotent \(e\) is full because
\[
E_{11}+E_{22}=E_{11}+E_{21}eE_{12}\in M_2(R)eM_2(R),
\]
so \(M_2(R)eM_2(R)=M_2(R)\). Its corner satisfies \(eM_2(R)e\cong R\). Hence any \(\sqrt{\Delta}\)-fine but non-fine \(R\) would be a non-fine full corner of the fine ring \(M_2(R)\), disproving full-corner descent and therefore Morita invariance of fineness. The contrapositive gives the final implication in the finding.

## Verification
The proof is symbolic and uses no finite enumeration. The critical imported identities were checked against the cited primary sources: the 2026 preprint states simplicity and closure under \(M_n(-)\), while Leroy--Matczuk state \(\Delta(M_n(S))=J(M_n(S))=M_n(J(S))\) for \(n\ge2\). The corner calculation is explicit.

Boundary checks are essential. The Leroy--Matczuk identity is used only for \(n\ge2\), so no conclusion about \(\Delta(R)\) itself is inferred. Likewise, the theorem does not assume semilocality, stable range one, or that \(\Delta(R)=J(R)\).

## Relationship to prior work
The 2026 preprint introduces \(\sqrt{\Delta}\)-fine rings, proves they are simple, proves matrix closure, and ends with the open question whether every \(\sqrt{\Delta}\)-fine ring is fine. Its indexed abstract does not state that every amplification \(M_n(R)\) with \(n\ge2\) is already classically fine, nor the Morita consequence.

Leroy--Matczuk supply the independent matrix identity for \(\Delta\), but do not study \(\sqrt{\Delta}\)-fine rings. Călugăreanu--Lam prove that matrix rings over fine rings are fine and explicitly ask whether fineness descends to full corners, equivalently whether it is Morita-invariant. Zhou's later Morita-context results give criteria when the corner rings are already assumed fine and do not settle general descent. Combining these statements yields the structural reduction proved here.

## Limitations
The result leaves the existence of a \(\sqrt{\Delta}\)-fine non-fine ring unresolved. It is a reduction, not a construction of a Morita counterexample. The full text of the 2026 preprint was not accessible through the available open full-text route during comparison; its arXiv metadata, indexed abstract, exact-title searches, and theorem-level statements needed for the proof were available. Thus there remains a residual originality risk that the same corollary appears inside that preprint without being indexed, although targeted searches for the matrix-fineness and Morita formulations did not surface it.

## References
1. P. Danchev, O. Hasanzadeh, A. Moussavi, A. Javan, “\(\sqrt{\Delta}\)-Fine Rings,” arXiv:2608.30734v1, first submitted 2026-08-31.
2. A. Leroy, J. Matczuk, “Remarks on the Jacobson radical,” Contemporary Mathematics 727 (2019), 269--276, DOI: 10.1090/conm/727/14640.
3. G. Călugăreanu, T. Y. Lam, “Fine rings: A new class of simple rings,” Journal of Algebra and Its Applications 15 (2016), 1650173, DOI: 10.1142/S0219498816501735.
4. Y. Zhou, “The fineness properties of Morita contexts,” Journal of Algebra and Its Applications 21 (2022), 2250205, DOI: 10.1142/S021949882250205X.
