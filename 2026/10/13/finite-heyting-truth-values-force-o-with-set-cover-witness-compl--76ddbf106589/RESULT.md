# Finite Heyting truth values force Łoś, with Set-Cover witness complexity
## Finding
Let \(H=\mathcal O(X)\) be finite and let \(\mathcal M\) be an \(H\)-valued first-order structure satisfying the function-symbol Assumption used in Aratake's main theorem. Then the finite-witness condition of that theorem is automatic. Consequently every maximal filter on \(H\) is \(\mathcal M\)-generic and, for every maximal filter \(\mathfrak m\), Aratake's Łoś equivalence holds for all formulas covered by the theorem.

There is also an exact finite optimization statement. For a formula \(\varphi(v,\mathbf a)\), write
\[
u_b=\left\lVert\varphi^G(b,\mathbf a)\right\rVert,\qquad
E=\bigvee_{b\in\mathcal M}u_b,
\]
and let \(j(x)=\neg\neg x\). Put \(B=\mathrm{Reg}(H)=\{x:jx=x\}\), the Boolean algebra of regular elements, and let
\[
T=jE,\qquad
S_b=\{p\in\mathrm{At}(B):p\le ju_b\}.
\]
If \(r_*(\varphi,\mathbf a)\) denotes the least cardinality of a finite set \(F\subseteq\mathcal M\) such that
\[
\bigvee_{b\in F}u_b\le E\le j\!\left(\bigvee_{b\in F}u_b\right),
\]
then
\[
\boxed{\;
r_*(\varphi,\mathbf a)
=\tau\!\left(\mathrm{At}(B)\cap\downarrow T,\{S_b:b\in\mathcal M\}\right),
\;}
\]
where \(\tau\) is the minimum set-cover number. Therefore
\[
\boxed{\;r_*(\varphi,\mathbf a)\le |\mathrm{At}(B)|.\;}
\]
The bound is sharp for every \(k\ge1\). Moreover, the associated decision problem is NP-complete already when \(H\) is a finite powerset Boolean algebra, equality is crisp, there are no function symbols, and the language has only one unary predicate.

## Assumptions and scope
The result is a finite-truth-value corollary and refinement of Aratake's Theorem 3.14, not a new version of Łoś's theorem for arbitrary frames. The structure must satisfy the same function-symbol Assumption as that theorem. No finiteness of the domain of \(\mathcal M\) is required; only the truth-value frame \(H\) is finite.

The minimum \(r_*\) is defined using finite subsets, so \(r_*=0\) when \(E=0\). The NP-completeness statement concerns the explicitly represented restricted Boolean case described below. It does not claim that every natural encoding of arbitrary Heyting-valued structures has the same complexity.

The Boolean special case of automatic fullness is already implicit in Pierobon and Viale's Boolean-valued fullness theorem: over a finite Boolean algebra, any family of truth values has a finite subfamily with the same supremum. The contribution claimed here is the finite Heyting conclusion through Aratake's theorem, the sharper regular-skeleton atom bound, the exact set-cover characterization, and the resulting optimization complexity.

## Proof
Aratake's Proposition 2.13 gives
\[
E=\left\lVert\exists v\,\varphi^G(v,\mathbf a)\right\rVert
 =\bigvee_{b\in\mathcal M}u_b.
\]
Hence the left inequality in the finite-witness condition is automatic for every finite \(F\subseteq\mathcal M\). Only the right inequality needs attention.

The double-negation map \(j=\neg\neg\) is a nucleus. Its fixed points form the Boolean algebra \(B=\mathrm{Reg}(H)\), whose join is
\[
x\vee_B y=j(x\vee_H y).
\]
Because \(H\) is finite, the set \(\{ju_b:b\in\mathcal M\}\) has only finitely many distinct values. Moreover,
\[
jE
=j\!\left(\bigvee_bu_b\right)
=\bigvee_B\{ju_b:b\in\mathcal M\}.
\]
The first inequality follows from \(u_b\le ju_b\). For the reverse inequality, every \(ju_b\le jE\), so the Boolean join of all \(ju_b\)'s is at most \(jE\).

A finite Boolean algebra is atomic. Thus each atom \(p\le T=jE\) lies below at least one \(ju_b\). Choose one such \(b_p\) for each atom below \(T\). Then
\[
T\le \bigvee_B\{ju_{b_p}:p\le T\}
 =j\!\left(\bigvee_{p\le T}u_{b_p}\right).
\]
Since \(E\le jE=T\), this gives Aratake's right inequality with at most \(|\mathrm{At}(B)|\) witnesses. Therefore condition (i) of Theorem 3.14 holds for every formula. The equivalence proved in that theorem yields genericity of every maximal filter and the stated Łoś equivalence.

For the exact minimum, a finite set \(F\) satisfies the right inequality exactly when
\[
T\le j\!\left(\bigvee_{b\in F}u_b\right)
 =\bigvee_B\{ju_b:b\in F\}.
\]
In a finite Boolean algebra this is equivalent to saying that every atom below \(T\) lies below at least one \(ju_b\) with \(b\in F\). That is precisely the set-cover condition
\[
\mathrm{At}(B)\cap\downarrow T\subseteq\bigcup_{b\in F}S_b.
\]
Taking minimum cardinalities proves the displayed identity for \(r_*\).

Sharpness is already witnessed by Boolean-valued unary structures. Let \(H=\mathcal P(\{1,\dots,k\})\), let the domain be \(\{1,\dots,k\}\), use crisp equality and global extents, and interpret a unary predicate by
\[
R(i)=\{i\}.
\]
For \(\varphi(v)=R(v)\), the existential value is the top element, while each witness covers exactly one Boolean atom. Hence exactly \(k\) witnesses are necessary.

Finally take an arbitrary Set Cover instance with universe \(U\) and sets \(C_1,\dots,C_m\) whose union is \(U\). Let \(H=\mathcal P(U)\), domain \(\{1,\dots,m\}\), and define \(R(i)=C_i\). Then a set of elements \(F\) is an Aratake witness set for \(\exists v\,R(v)\) exactly when \(\{C_i:i\in F\}\) covers \(U\). The restricted decision problem is therefore Set Cover verbatim. Membership in NP is immediate from bit-vector union, so the decision problem is NP-complete.

## Verification
The accompanying `verify.py` independently replays the finite algebraic layer on all \(242\) labeled posets with at most four points. For each poset it forms the Heyting algebra of upsets, computes double negation, its regular Boolean algebra, and all atoms. It exhausts every family of possible witness truth values and compares two independently computed optima: the minimum cardinality satisfying the double-negated Aratake inequality, and the minimum atom-cover cardinality. The equality and the regular-atom upper bound hold in all \(172740\) witness-family checks.

The checker also verifies the sharp powerset examples for \(k=1,\dots,12\). Its terminal line is:

`VERIFY_OK 172740 witness-family checks over 242 labeled posets through four points; sharpness k<=12`

This computation is a finite replay of the algebraic identities, not a substitute for the proof for arbitrary finite \(H\).

## Relationship to prior work
Aratake proves a characterization of the Heyting-valued structures for which Łoś's theorem holds at every maximal filter. The key condition is the existence, for every formula, of finitely many witnesses satisfying the two inequalities used above. In the proof from Łoś back to the witness condition, Aratake passes to the Boolean algebra of regular elements and uses compactness of its Stone spectrum to extract a finite subcover. The paper does not state the finite-frame corollary, an atom bound, a minimum set-cover formula, or the complexity consequence; direct full-text searches found no occurrence of “finite Heyting” or “atom” in this role.

Pierobon and Viale prove the corresponding Boolean-valued fullness theorem: fullness is equivalent to existential truth values being finite suprema of witness values. Their formulation already makes automatic fullness over a finite Boolean algebra immediate. Their paper does not cover the non-Boolean finite Heyting conclusion or the regular-skeleton set-cover optimization; direct inspection of the fullness section found no “atom” or “witness” terminology for this refinement.

Bell and the standard Boolean-valued literature treat stronger maximum principles obtained from mixing, often producing a single mixed witness. That is a different hypothesis and mechanism. Here no mixing or completeness of the valued set is assumed beyond Aratake's stated function-symbol Assumption; finiteness of the truth-value frame alone forces the weaker finite-witness condition needed for all-maximal-filter Łoś.

Targeted published-finding corpus searches and exact web searches were run under Heyting-valued/finite truth-value/Łoś/maximal-filter, regular-element/atom-cover, maximum-principle, and set-cover formulations. No equivalent finite-Heyting statement or optimization theorem was located. Because the deduction from Aratake's theorem is short, an unindexed or unpublished observation remains a realistic priority risk.

## Limitations
This is a sharp finite specialization of a published general theorem, so its conceptual depth lies in exposing what finiteness forces and in the optimization interpretation rather than in a new forcing construction. The source theorem's function-symbol Assumption remains essential to the claimed Łoś conclusion. The literature search cannot prove bibliographic uniqueness, and no independent audit has been performed.

## References
1. Hisashi Aratake, “Sheaves of Structures, Heyting-Valued Structures, and a Generalization of Łoś's Theorem,” arXiv:2012.04317v1 (2020); *Mathematical Logic Quarterly* 67 (2021), 445–468, DOI 10.1002/malq.202000088. See Proposition 2.13 and Theorem 3.14.
2. Moreno Pierobon and Matteo Viale, “Boolean valued models, presheaves, and étalé spaces,” arXiv:2006.14852 (2020). See Definition 4.12 and Theorem 4.13.
3. John L. Bell, *Set Theory: Boolean-Valued Models and Independence Proofs*, 3rd ed., Oxford University Press, 2005, for the classical Boolean-valued maximum principle and mixing method.
