# Exact frame correspondence for Box Excluded Middle
## Finding

Let \(\mathcal F=\langle W,\le,R\rangle\) be a birelational frame for intuitionistic modal logic, with \(\le\) an intuitionistic Kripke order and with the usual compatibility condition
\[
x\le y\ \wedge\ yRz\quad\Longrightarrow\quad xRz.
\]
Then the Box Excluded Middle scheme
\[
\Box\varphi\vee\neg\Box\varphi
\]
is valid on \(\mathcal F\), for every formula \(\varphi\) and every persistent valuation, if and only if the following first-order condition holds:
\[
x\le y\ \wedge\ xRz
\quad\Longrightarrow\quad
\exists u\,(yRu\ \wedge\ u\le z).
\tag{E}
\]

Condition \((E)\) is strictly weaker than the condition called \(\mathsf{BEM}\) by van der Giessen, Joosten, Mayaux, and Navarro Arroyo,
\[
x\le y\ \wedge\ xRz\quad\Longrightarrow\quad yRz.
\tag{BEM}
\]
Indeed, the two-point frame \(W=\{0,1\}\), ordered by \(0<1\), with
\[
R=\{(0,0),(0,1),(1,0)\},
\]
satisfies the basic birelational compatibility condition and \((E)\), hence validates Box Excluded Middle, but fails \(\mathsf{BEM}\) because \(0\le1\) and \(0R1\) while \(1R1\) is false. No one-point frame can separate \((E)\) from \(\mathsf{BEM}\), so two points are minimal.

## Assumptions and scope

The forcing clauses are the standard birelational clauses used in the cited source. In particular, truth is persistent upward along \(\le\),
\[
x\le y\ \wedge\ x\Vdash\varphi\quad\Longrightarrow\quad y\Vdash\varphi,
\]
and
\[
x\Vdash\Box\varphi
\quad\Longleftrightarrow\quad
\forall z\,(xRz\Rightarrow z\Vdash\varphi).
\]
Negation is intuitionistic, so
\[
x\Vdash\neg\psi
\quad\Longleftrightarrow\quad
\forall y\ge x,\ y\nVdash\psi.
\]

The result concerns validity on birelational frames. It does not assert a new completeness theorem for a different proof system, nor does it alter the mixed-model completeness theorem of the cited paper.

## Proof

Assume first that \((E)\) holds. Fix a formula \(\varphi\) and a world \(x\). If \(x\Vdash\Box\varphi\), then Box Excluded Middle holds at \(x\). Otherwise choose \(z\) with \(xRz\) and \(z\nVdash\varphi\). To prove \(x\Vdash\neg\Box\varphi\), take any \(y\ge x\). If \(y\Vdash\Box\varphi\), condition \((E)\) applied to \(x\le y\) and \(xRz\) gives a world \(u\) with \(yRu\) and \(u\le z\). From \(y\Vdash\Box\varphi\) we obtain \(u\Vdash\varphi\), and persistence along \(u\le z\) gives \(z\Vdash\varphi\), contradicting the choice of \(z\). Hence every \(y\ge x\) fails \(\Box\varphi\), so \(x\Vdash\neg\Box\varphi\). Thus \(\Box\varphi\vee\neg\Box\varphi\) is valid.

Conversely, suppose \((E)\) fails. Then there are \(x,y,z\) with \(x\le y\) and \(xRz\), but no \(u\) satisfies both \(yRu\) and \(u\le z\). Let the atomic valuation of \(p\) be the upward closure of the \(R\)-successors of \(y\):
\[
V(p)=\uparrow R(y)
=\{v:\exists u\,(yRu\wedge u\le v)\}.
\]
This valuation is persistent. Every \(R\)-successor of \(y\) belongs to \(V(p)\), so \(y\Vdash\Box p\). But \(z\notin V(p)\), while \(xRz\), hence \(x\nVdash\Box p\). Since \(x\le y\) and \(y\Vdash\Box p\), the intuitionistic clause for negation also gives \(x\nVdash\neg\Box p\). Therefore \(x\nVdash\Box p\vee\neg\Box p\). This proves necessity.

Finally, \(\mathsf{BEM}\) implies \((E)\) by taking \(u=z\). For the displayed two-point frame, the only nontrivial comparison is \(0\le1\). If \(0R0\), choose \(u=0\); if \(0R1\), again choose \(u=0\), using \(1R0\) and \(0\le1\). Hence \((E)\) holds. The same frame fails \(\mathsf{BEM}\) at \(0\le1\) and \(0R1\). On one point, \(x=y\) necessarily, so the antecedent and consequent of \(\mathsf{BEM}\) use the same \(R\)-fact and \(\mathsf{BEM}\) cannot fail.

## Verification

The proof above is symbolic and covers arbitrary frames and arbitrary formulas; finite enumeration is not used as an infinite proof. As a finite sanity check, `artifacts/verify_small.py` exhaustively enumerates every labeled partial order and every modal relation satisfying the basic birelational compatibility condition for \(|W|\le3\). It verifies that condition \((E)\) agrees exactly with validity of the atomic instance \(\Box p\vee\neg\Box p\) on all \(2\), \(34\), and \(2942\) admissible labeled frames of orders \(1\), \(2\), and \(3\), respectively. It also checks the two-point strict witness and reconstructs the published four-point counterexample.

The finite check is auxiliary only. The necessity proof uses the explicit persistent valuation \(V(p)=\uparrow R(y)\), and the sufficiency proof uses persistence of arbitrary formulas.

## Relationship to prior work

Van der Giessen, Joosten, Mayaux, and Navarro Arroyo introduce Box Excluded Middle and the frame condition \(\mathsf{BEM}\). Their Lemma 3.1.6 proves that \(\mathsf{BEM}\) is sufficient for Box Excluded Middle, and their Example 3.1.7 explicitly shows that the converse fails using a four-point frame. They do not give an exact frame condition for the scheme there.

Condition \((E)\) identifies the missing exact correspondence. It also explains their four-point example: its missing edge \(bRc\) is compensated by an edge \(bRd\) with \(d\le c\). The two-point frame above shows that strictness between exact validity and \(\mathsf{BEM}\) occurs at the smallest possible cardinality.

The underlying birelational semantics goes back to work such as Božić and Došen on normal intuitionistic modal logics. Searches of the recent source, exact-phrase web results, and related published finding records did not locate this exact correspondence or the two-point minimum witness.

## Limitations

The theorem is about the Box Excluded Middle scheme under the stated birelational semantics. It does not classify every alternative intuitionistic modal semantics or every possible mixed-model presentation. A general correspondence framework could subsume the calculation abstractly; no source stating this particular equivalence was located in the inspected literature.

The exhaustive checker covers only frames of at most three points and only the atomic instance. It supports the finite boundary claims but is not evidence for the general theorem, which is established by the symbolic proof.

## References

1. I. van der Giessen, J. J. Joosten, P. Mayaux, and V. Navarro Arroyo, “On the Contingency of Logic in Possible World Semantics,” *Logica Universalis* 19 (2025), 721–737, DOI 10.1007/s11787-025-00400-7; arXiv:2510.17302.
2. M. Božić and K. Došen, “Models for normal intuitionistic modal logics,” *Studia Logica* 43 (1984), 217–245, DOI 10.1007/BF02429840.
