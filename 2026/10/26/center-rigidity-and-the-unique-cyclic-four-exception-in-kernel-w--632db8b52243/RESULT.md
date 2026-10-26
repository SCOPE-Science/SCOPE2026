# Center rigidity and the unique cyclic-four exception in kernel–wreath skew-brace towers

## Finding
Let \(R\) be a finite group, let \(T\) be a nontrivial finite abelian group and let \(\chi:R\twoheadrightarrow T\) be a surjective homomorphism. Put \(t=|T|\), let \(T\) act regularly by left translation on the \(t\) factors of \(R^T\), and define
\[
W=R^T\rtimes T,\qquad
\varepsilon((r_x)_{x\in T},u)=\Bigl(\prod_{x\in T}\chi(r_x)\Bigr)u,\qquad
G=\ker\varepsilon.
\]
Write \(\Delta(c)=((c)_{x\in T},1_T)\). Then the center is **exactly**
\[
\boxed{Z(G)=\Delta(Z(R))}
\]
unconditionally except when \(R\cong T\cong C_2\) and \(\chi\) is an isomorphism. In this sole exceptional case \(G\cong C_4\), so \(Z(G)=G\), strictly larger than \(\Delta(Z(R))\cong C_2\).

Consequently, in any iterated kernel–wreath construction with multiplicative groups \(R_0,R_1,\ldots\), the diagonal embeddings identify \(Z(R_m)\) with \(Z(R_0)\) for every \(m\geq0\), unless \(R_0\cong C_2\). Starting with \(C_2\) produces \(R_1\cong C_4\), after which all centers are diagonal copies of \(C_4\). In particular, the simple skew-brace towers originating from the \(A_5\) construction with multiplicative seed \(A_4\times C_5\) have multiplicative center \(C_5\) at every level, although their orders grow as \(60^{p^m}\) for \(p\in\{3,5\}\).

## Assumptions and scope
All groups are finite. The quotient group \(T\) is nontrivial and abelian; \(\chi\) is onto. For \(u\in T\), the action on the base group is \((u\cdot r)_x=r_{u^{-1}x}\). Multiplication in \(W\) is
\[
(r,u)(s,v)=((r_xs_{u^{-1}x})_{x\in T},uv).
\]
Since \(T\) is abelian, \(\varepsilon\) is a homomorphism. Its kernel has order \(|R|^t\). This kernel is precisely the multiplicative group of the kernel–wreath skew brace defined by Damele. The theorem describes multiplicative-group centers, not the centers of the additive groups.

## Proof
Put \(B=G\cap R^T=\{(r_x)_{x\in T}:\prod_x\chi(r_x)=1_T\}\). Two elementary properties are essential.

First, the projection \(B\to R\) onto **each** coordinate is onto: given \(a\in R\), put \(a\) in the chosen coordinate and a compensating element \(b\) with \(\chi(b)=\chi(a)^{-1}\) in a distinct coordinate. Such a coordinate exists because \(t\geq2\).

Second, the projection \(\rho:G\to T\), \((r,u)\mapsto u\), is onto: for prescribed \(u\), choose \(a\in R\) with \(\chi(a)=u^{-1}\), put it in one coordinate, and use top component \(u\).

For \(c\in Z(R)\), the diagonal \(\Delta(c)\) belongs to \(G\), because \(\chi(c)^t=1_T\) by Lagrange's theorem. It commutes with all base entries because \(c\) is central in \(R\), and with all coordinate translations because it is constant. Thus \(\Delta(Z(R))\leq Z(G)\).

Let \(g=(r,u)\in Z(G)\). We first exclude \(u\neq1_T\) unless \(R=T=C_2\). If \(\ker\chi\neq1\), choose \(k\neq1\) in that kernel. The base element supported at a single coordinate \(x\) with value \(k\) belongs to \(B\); conjugation by \(g\) transports its nontrivial support to \(ux\), which differs from \(x\) for \(u\neq1_T\) under the regular action. This contradicts centrality.

If \(\ker\chi=1\), then \(R\cong T\) is abelian. When \(t>2\) and \(u\neq1_T\), choose distinct coordinates \(x,y\) with \(y\neq ux\), and a nonidentity \(a\in R\). The element of \(B\) taking the values \(a\) at \(x\), \(a^{-1}\) at \(y\), and the identity elsewhere is not invariant under translation by \(u\): the translated element is nontrivial at \(ux\), where the original is trivial. As all base entries commute in this case, conjugation by \(g\) acts on \(B\) by that translation alone. Again centrality fails. The only remaining case with \(u\neq1_T\) is \(R\cong T\cong C_2\), treated below.

Suppose \(u=1_T\). Since \(g\) commutes with \(B\) and the coordinate projections of \(B\) are onto, each entry \(r_x\) lies in \(Z(R)\). As \(\rho:G\twoheadrightarrow T\), centrality of \(g\) against lifts of all \(u\in T\) forces its tuple to be translation-invariant: the base entries are central, so conjugation by a lift acts on the tuple by coordinate permutation. Transitivity of the regular action forces \(r_x=c\) independent of \(x\). Hence \(g=\Delta(c)\), where \(c\in Z(R)\).

Finally suppose \(R=T=C_2=\langle a\rangle\) with \(\chi\) the identity. Then \(|G|=|R|^{|T|}=4\). The element \(h=((a,1),a)\in G\) satisfies \(h^2=((a,a),1)\neq1\), so \(h\) has order four and \(G=\langle h\rangle\cong C_4\). Its center is all of \(G\).

For iteration, the displayed classification applies independently at each step, and the diagonal center agrees with the center under the canonical diagonal subbrace embedding. If \(R_0\not\cong C_2\), none of its successive groups can be \(C_2\), since \(|R_{m+1}|=|R_m|^{|T_m|}\) with \(|T_m|\geq2\). If \(R_0=C_2\), its only nontrivial quotient is \(C_2\); the first step is \(C_4\), and no subsequent step is exceptional. The \(A_5\) examples follow from Damele's seed \(R_0\cong A_4\times C_5\), with \(Z(R_0)\cong C_5\), and the available quotients \(C_3,C_5\).

## Verification
The standalone program `verify.py` enumerates the exact elements of nine finite kernels (including nonabelian bases \(S_3\), \(D_8\), \(A_4\) and noncyclic top group \(C_2\times C_2\)), multiplies all pairs, and identifies their centers by exhaustive commutation tests. It directly confirms the unique cyclic-four exception and the predicted diagonal centers. Run `python verify.py`; success prints `VERIFY_OK`. This is finite corroboration only: the quantified theorem follows from the preceding proof.

## Relationship to prior work
Damele, *Kernel–wreath constructions and infinite families of finite simple skew braces* (arXiv:2609.20401v1, 2026), introduces the kernel \(G\), proves that its top projection is surjective, constructs the diagonal seed embedding and obtains infinite simple-brace towers; see Theorem 3.1, Lemma 3.2 and Theorem 3.7. Those definitions and tower-existence results are prior work. The present theorem determines the **center of that index-\(t\) kernel**, including the exceptional enlargement and exact behavior under iteration.

Classical group theory identifies the center of an ordinary regular wreath product with the constant tuples in the base center; for an explicit discussion see the standard-wreath exercise attributed to Robinson. However, knowing \(Z(W)\) does **not** determine \(Z(G)\) for an index-\(t\) subgroup: the exceptional case here has \(Z(G)\cong C_4\) but \(Z(W)\cong C_2\). Skuratovskii and Williams (arXiv:1901.00061v15, Section 3) study centers and commutators of permutational wreath products, rather than this kernel. A published 2026 note on kernel–wreath abelianization establishes an abelianization formula, a different invariant that does not by itself imply the center formula.

## Limitations
This theorem assumes a finite base group, a *surjective* homomorphism onto a *nontrivial abelian* top group, and the specific balanced kernel of \(\varepsilon\). It makes no claim for arbitrary index subgroups, nonregular top actions, or nonabelian quotient targets. The argument is a short direct group calculation, not a new classification of all skew braces. The precise-center statement was not found in the inspected primary texts, but implicit coverage by earlier wreath-subgroup results remains a residual originality risk; no independent review has been performed.

## References
1. Marco Damele, *Kernel–wreath constructions and infinite families of finite simple skew braces*, arXiv:2609.20401v1, first posted 17 September 2026, https://arxiv.org/pdf/2609.20401.
2. Ruslan Skuratovskii and Aled Williams, *Irreducible Bases and Subgroups of a Wreath Product in Applying to Diffeomorphism Groups Acting on the Möbius Band*, arXiv:1901.00061v15, https://arxiv.org/html/1901.00061v15.
3. Derek J. S. Robinson, *A Course in the Theory of Groups*, 2nd ed., Exercise 1.6.14 (ordinary regular-wreath center; cited via a public exercise discussion).
4. *Kernel-wreath abelianization order and the exterior-square correction* (2026), public research record at https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-kernel-wreath-abelianization-exterior-square--07de60556165 (abstract inspected; full record not retrieved).
