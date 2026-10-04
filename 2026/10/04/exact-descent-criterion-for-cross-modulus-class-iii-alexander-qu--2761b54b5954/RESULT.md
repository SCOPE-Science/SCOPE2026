# Exact descent criterion for cross-modulus class-(iii) Alexander quandles
## Finding
Consider degree-one cyclic Alexander modules
\[
M_i=\mathbb Z_{r_i}[t_i,t_i^{-1}]/(t_i-k_i)\cong\mathbb Z_{r_i},
\]
where \(r_i\ge1\), each integer \(k_i\) is fixed as part of the presentation, and \(\gcd(k_i,r_i)=1\). On the disjoint union \(X=\bigsqcup_i M_i\), interpret the class-(iii) non-identical-order formula of Arsiwalla and Kauffman literally on quotient classes, with no additional cross-fiber maps:
\[
(i,a)*(j,b)=(i,\,k_j a+(1-k_i)b\pmod{r_i}).
\]
Then this expression descends to a well-defined binary operation on the quotient classes if and only if
\[
r_i\mid(1-k_i)r_j\qquad\text{for every }i,j.
\]
Under these descent conditions, the operation is a quandle if and only if
\[
\gcd(k_j,r_i)=1\qquad\text{for every }i,j.
\]

Equivalently, if
\[
N=\operatorname{lcm}_i r_i,
\qquad
d_i=\operatorname{lcm}_j\frac{r_i}{\gcd(r_i,r_j)},
\]
then the complete criterion is
\[
k_i\equiv1\pmod{d_i}\quad\text{for every }i,
\qquad
\gcd(k_j,N)=1\quad\text{for every }j.
\]
This turns the source's statement that class-(iii) solutions for non-identical orders exist only in certain cases into an exact arithmetic classification for the degree-one cyclic family used in its concrete examples.

For the source's Example 7.3, \((r_1,r_2)=(2,4)\) and \((k_1,k_2)=(1,3)\). Here \((d_1,d_2)=(1,2)\) and \(N=4\), so both conditions hold. For Example 7.5, \((r_1,r_2)=(1,5)\) and \((k_1,k_2)=(1,k)\) with \(k\in\{2,3,4\}\). Here \((d_1,d_2)=(1,5)\), so the descent condition requires \(k\equiv1\pmod5\) and fails for all three displayed values.

This last conclusion is about the displayed quotient-module formula, not about the validity of the printed Cayley tables as abstract set-theoretic quandles. Because the first fiber has one element, those tables can be recovered by supplying the unique zero cross-fiber map, or by imposing an explicit representative convention. Such extra data are not present in the literal quotient-module expression.

## Assumptions and scope
The result treats precisely the degree-one cyclic factors \(\mathbb Z_{r_i}[t_i,t_i^{-1}]/(t_i-k_i)\) that occur in Examples 7.3 and 7.5 of the source. The integers \(k_i\) are fixed lifts in the module presentations. No assertion is made here about higher-degree factors in which \(t_i\) remains a non-scalar operator.

The phrase "literal quotient-module formula" means that the term \((1-k_i)b\) is required to depend only on the residue class \(b\in\mathbb Z_{r_j}\), without an independently specified homomorphism \(M_j\to M_i\). If such transition maps are added as extra structure, the correct general framework is broader; classical affine-mesh theory already uses explicit homomorphisms between heterogeneous abelian fibers.

## Proof
Fix indices \(i,j\). The only potentially ambiguous term in
\[
k_j a+(1-k_i)b\pmod{r_i}
\]
is the contribution of \(b\in\mathbb Z_{r_j}\). Replacing an integer representative \(b\) by \(b+r_j\) changes the value in \(\mathbb Z_{r_i}\) by
\[
(1-k_i)r_j.
\]
Therefore the expression depends only on the residue class of \(b\) if and only if
\[
r_i\mid(1-k_i)r_j.
\]
Requiring this for every ordered pair of fibers gives the stated descent criterion. The \(a\)-term is already well defined because \(a\) is reduced modulo the target modulus \(r_i\) and multiplication by the fixed integer \(k_j\) is an endomorphism of \(\mathbb Z_{r_i}\).

Assume now that the formula descends. Idempotence is immediate on every fiber:
\[
k_i a+(1-k_i)a=a.
\]
For a fixed right operand \((j,b)\), the right translation restricted to the target fiber \(M_i\) is the affine map
\[
a\longmapsto k_j a+(1-k_i)b.
\]
It is bijective if and only if multiplication by \(k_j\) is invertible on \(\mathbb Z_{r_i}\), equivalently \(\gcd(k_j,r_i)=1\). Thus right-invertibility for the whole disjoint union is equivalent to the cross-unit condition for every \(i,j\).

Right self-distributivity is formal once all cross terms are well defined. For \(a\in M_i\), \(b\in M_j\), and \(c\in M_\ell\), the left-hand side is
\[
k_\ell k_j a+(1-k_i)k_\ell b+(1-k_i)c.
\]
The right-hand side expands to
\[
k_j\bigl(k_\ell a+(1-k_i)c\bigr)
 +(1-k_i)\bigl(k_\ell b+(1-k_j)c\bigr),
\]
which simplifies to the same expression because the coefficient of \(c\) is \((1-k_i)(k_j+1-k_j)=1-k_i\). Hence no additional arithmetic condition is needed.

For the compact form of the descent criterion, write \(g_{ij}=\gcd(r_i,r_j)\). The divisibility
\[
r_i\mid(1-k_i)r_j
\]
is equivalent to
\[
\frac{r_i}{g_{ij}}\mid(1-k_i).
\]
Taking the least common multiple over \(j\) yields \(d_i\mid(1-k_i)\). Likewise, \(k_j\) is a unit modulo every \(r_i\) if and only if it is a unit modulo their least common multiple \(N\). This proves the equivalence and the theorem.

## Verification
The proof is symbolic and does not depend on finite search. The bundled verifier exhaustively checks all two-fiber systems with moduli between \(1\) and \(8\) and all source-admissible own-fiber unit parameters in the tested range. It verifies the equivalence between the pairwise and compact divisibility criteria, constructs explicit representative-dependence witnesses whenever descent fails, detects nonbijective right translations whenever the cross-unit condition fails, and checks all three quandle axioms whenever both criteria hold.

Its replay output is:

`VERIFY_OK systems=484 criterion_true=160 checked_quandles=160 descent_failure_witnesses=318 example7.3=PASS example7.5_k2_k3_k4=FAIL_DESCENT`

The verifier separately checks that the source's Example 7.3 satisfies both criteria and that the three parameter choices in Example 7.5 fail the descent criterion.

## Relationship to prior work
Arsiwalla and Kauffman define, for modules of non-identical cardinalities, the operation whose second component is reduced modulo the order of the left operand's module. Their Remark 5.3 says that class-(iii) solutions exist only in certain cases and Example 7.3 supplies one such case. Example 7.5 states that, for \(\mathbb Z_1\bigsqcup\mathbb Z_5\) with \(k=2,3,4\), the class-(iii) quandles are identical to class (ii). The arithmetic criterion above classifies exactly when their displayed class-(iii) quotient formula descends and separates the validity of an abstract Cayley table from the stronger claim that it is induced canonically by that quotient formula.

A public automated review of the recent preprint has already raised the generic issue that cross-fiber operations across different moduli need additional well-definedness justification. That observation is not claimed here as new. The contribution here is the exact necessary-and-sufficient divisibility and unit criterion for the source's scalar cyclic class-(iii) family, together with the resulting diagnosis of its two explicit non-identical-order examples.

The older structure theorem for medial quandles by Jedlička, Pilitowska, Stanovský and Zamojska-Dzienio represents heterogeneous affine quandles using affine meshes with explicit homomorphisms between component abelian groups. That framework explains conceptually why cross-fiber maps are natural data. The present criterion is a source-specific arithmetic specialization: multiplication by \(1-k_i\) induces the needed homomorphism \(\mathbb Z_{r_j}\to\mathbb Z_{r_i}\) exactly under the displayed divisibility condition.

## Limitations
The criterion is not a classification of all heterogeneous affine or medial quandles and does not supersede affine-mesh theory. It classifies only the literal scalar class-(iii) formula on degree-one cyclic factors, with fixed integer parameters and no extra transition maps.

It also does not claim that Example 7.5's Cayley tables fail the quandle axioms. The issue is canonical descent from quotient-module elements: a table produced after choosing extra cross-fiber data can still be a valid quandle even when the literal quotient expression is not representative independent.

The target is a very recent preprint and may be revised. A later version could add transition maps or state an equivalent arithmetic condition.

## References
1. Xerxes D. Arsiwalla and Louis H. Kauffman, *Multivariate Quandles as Groupoid Invariants*, arXiv:2609.30262v1, first posted 2026-09-24. Relevant material: Definition 4.9, Section 5.2, Remark 5.3, and Examples 7.3--7.5.
2. Přemysl Jedlička, Agata Pilitowska, David Stanovský and Anna Zamojska-Dzienio, *The structure of medial quandles*, Journal of Algebra 443 (2015), 300--334; arXiv:1409.8396.
3. Public structured review of *Multivariate Quandles as Groupoid Invariants*, PaperVerse, accessed 2026-10-01; the review independently flags a generic cross-fiber well-definedness issue.
