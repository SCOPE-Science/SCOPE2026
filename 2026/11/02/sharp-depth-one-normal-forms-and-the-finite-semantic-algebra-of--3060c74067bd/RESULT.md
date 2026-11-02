# Sharp depth-one normal forms and the finite semantic algebra of Belnapian S5 essence

## Finding

For every integer \(k\geq1\), consider the full four-valued S5 essence/accident language with \(k\) propositional letters, the connectives \(\neg,\sim,\wedge,\vee,\to\), and all twenty-four value-indexed essence and accident modalities of Petrukhin (2026). Formulas are identified when they have **the same complete four-valued value**, not merely the same designatedness, at every pointed model.

Set \(q=4^k\), \(c=2^k\), \(N=q2^{q-1}\), and \(N_{\mathrm{cl}}=c2^{c-1}\). The exact number of semantic formula classes is
\[
\boxed{\lvert\mathfrak F_k\rvert=2^{N_{\mathrm{cl}}}4^{N-N_{\mathrm{cl}}}=2^{2q2^{q-1}-c2^{c-1}}.}
\]
Every class has a representative with **modal nesting depth at most one**. A formula satisfiable at some point has a pointed model whose S5 equivalence cell contains at most \(q\) worlds; this world bound is sharp, even for a depth-one formula. In particular, \(\lvert\mathfrak F_1\rvert=2^{60}\) and \(\lvert\mathfrak F_2\rvert=2^{1048544}\).

More precisely, let \(Q=\{t,b,n,f\}^k\) be the set of complete atomic value vectors and let \(C=\{t,f\}^k\). The complete formula classes are in bijection with all functions
\[
 h:\{(a,S):\varnothing\ne S\subseteq Q,\ a\in S\}\longrightarrow\{t,b,n,f\}
\]
satisfying exactly one restriction: \(h(a,S)\in\{t,f\}\) whenever \(S\subseteq C\). This characterization specifies the mathematical object, not just its cardinality.

## Assumptions and scope

The four values are encoded as \(t=(1,0),\ b=(1,1),\ n=(0,0),\ f=(0,1)\), recording positive and negative information. De Morgan negation exchanges the coordinates; Boolean negation complements both coordinates. Conjunction takes the minimum of positive coordinates and maximum of negative coordinates; disjunction does the reverse. For implication, the positive coordinate is the classical implication of positive coordinates, while the negative coordinate is positive antecedent AND negative consequent. These are precisely the propositional tables used by Petrukhin.

An S5 equivalence class is a nonempty collection of worlds, each equipped with an arbitrary value vector in \(Q\). The parameter \(S\) is the **set of value vectors present**, irrespective of multiplicity, and \(a\) is the vector at the distinguished world. We work with the complete, twenty-four-modality language; the result does not automatically hold in any proper modal sublanguage. The use of all four value-indexed second-group modalities, notably \(\circ_b,\bullet_b,\widetilde\bullet_b\), matters in the expressiveness proof.

For any formula \(A\), write \(v(A,w)\in\{t,b,n,f\}\). The value-indexed modalities needed explicitly below are defined by Petrukhin's Definition 2.6. Writing \(\ast b=n\), their positive/negative coordinates obey:
\[
\begin{aligned}
 T\in v(\circ_i A,w)&\iff [v(A,w)=i\ \Rightarrow\ (\forall u)\,v(A,u)=i],\\
 F\in v(\circ_i A,w)&\iff [v(A,w)=i\ \land\ (\exists u)\,v(A,u)\ne\ast i],\\
 T\in v(\bullet_i A,w)&\iff [v(A,w)=i\ \land\ (\exists u)\,v(A,u)\ne i],\\
 F\in v(\bullet_i A,w)&\iff [v(A,w)=\ast i\ \Rightarrow\ (\forall u)\,v(A,u)=\ast i],\\
 T\in v(\widetilde\bullet_i A,w)&\iff [v(A,w)\ne i\ \land\ (\exists u)\,v(A,u)=i],\\
 F\in v(\widetilde\bullet_i A,w)&\iff [v(A,w)\ne\ast i\ \Rightarrow\ (\forall u)\,v(A,u)\ne\ast i].
\end{aligned}
\]
All quantified worlds above belong to the same S5 equivalence class. The other primitive modalities use the corresponding published clauses; they are needed for the upper bound but not the constructive completeness argument.

## Proof

**1. Upper bound by pointed support profiles.** Induct on formula structure. A propositional letter at a world depends only on its coordinate of \(a\). Truth-functional operations preserve this property. At a modal step, the induction hypothesis says that, as accessible worlds range through the cell, the set of values of the immediate subformula depends only on \(S\), and its value at the current world depends only on \((a,S)\). Each of the twenty-four modal definitions uses only these two pieces of information; therefore the result again depends only on \((a,S)\). Thus every formula induces a function on the claimed finite set of pointed profiles.

If every atomic vector in the cell belongs to \(C\), induction also shows that every formula is \(t\)- or \(f\)-valued there. The propositional connectives preserve the classical subalgebra, and substituting only \(t,f\) into each modal truth/falsity clause gives complementary Boolean coordinates. This proves the restriction \(h(a,S)\in\{t,f\}\) for \(S\subseteq C\). There are \(N=\sum_{\varnothing\ne S\subseteq Q}|S|=q2^{q-1}\) profiles, of which \(N_{\mathrm{cl}}=c2^{c-1}\) are all-classical. Hence the asserted expression is an upper bound.

**2. Crisp local value tests.** For a formula \(A\), the following four propositional terms take value \(t\) precisely when \(A\) has the indicated value, and take \(f\) otherwise:
\[
\begin{aligned}
 \delta_t(A)&=\neg(\neg A\vee\sim A),\\
 \delta_b(A)&=\neg(A\to A)\vee\sim(A\to A),\\
 \delta_n(A)&=(A\vee\neg A)\to(A\wedge\sim A),\\
 \delta_f(A)&=\neg A\wedge\sim A.
\end{aligned}
\]
Checking the four rows of the propositional truth tables proves these identities. For each \(a\in Q\), the conjunction \(L_a=\bigwedge_{j=1}^k\delta_{a_j}(p_j)\) is a crisp local test for atomic vector \(a\).

**3. Crisp tests for all supports, with only one modal layer.** Define
\[
 E_a=L_a\vee\widetilde\bullet_t L_a.
\]
Because \(L_a\) takes only \(t,f\), the published truth/falsity clauses give \(E_a=t\) at every world exactly when some world in the cell has atomic vector \(a\), and \(E_a=f\) otherwise. The proof has three exhaustive cases: \(L_a=t\) locally, \(L_a=f\) locally with a witness elsewhere, and no witness anywhere. For each nonempty \(S\subseteq Q\), put
\[
 D_S=\bigwedge_{a\in S}E_a\ \wedge\ \bigwedge_{a\notin S}\sim E_a,
 \qquad \chi_{a,S}=L_a\wedge D_S.
\]
Each \(\chi_{a,S}\) is a crisp \(t/f\) indicator of **exactly** the pointed profile \((a,S)\), and has modal depth one.

**4. A nonclassical value flag.** For any formula \(Z\) that takes only values \(b,f\) throughout a cell, define
\[
 G(Z)=(\circ_bZ\wedge Z)\vee\bullet_bZ\vee\widetilde\bullet_bZ.
\]
Direct substitution in Definition 2.6 gives \(G(Z)=b\) at every world if \(b\) appears anywhere as a value of \(Z\), and \(G(Z)=f\) everywhere otherwise. This uses all four possible configurations: an all-\(f\) cell, an all-\(b\) cell, and the two possible current-world values in a mixed cell. In an all-\(b\) cell, the first disjunct produces \(b\); in a mixed cell, \(\bullet_bZ\) does so at a \(b\)-world and \(\widetilde\bullet_bZ\) at an \(f\)-world.

Now let \(\beta_b(A)=\delta_b(A)\wedge A\) and \(\beta_n(A)=\delta_n(A)\wedge\sim A\). Each \(\beta_i\) equals \(b\) when \(A=i\) and \(f\) otherwise. Hence the formula
\[
 B_k=\bigvee_{j=1}^k\bigl(G(\beta_b(p_j))\vee G(\beta_n(p_j))\bigr)
\]
equals \(b\) at every world if some atomic vector anywhere in the cell is nonclassical, and equals \(f\) otherwise. The companion \(H_k=\delta_b(B_k)\wedge\sim B_k\) equals \(n\) if the cell contains a nonclassical atomic vector and equals \(f\) otherwise. Both have modal depth one.

**5. Surjectivity and exact counting.** Let \(h\) be any function satisfying the stated all-classical restriction. For each pointed profile \((a,S)\), choose the following expression: \(\chi_{a,S}\) when \(h(a,S)=t\); \(\chi_{a,S}\wedge B_k\) when the value is \(b\); \(\chi_{a,S}\wedge H_k\) when the value is \(n\); and the crisp constant \(F_0=\delta_t(p_1)\wedge\sim\delta_t(p_1)\) when the value is \(f\). Take the disjunction of all the non-\(f\) pieces, or \(F_0\) if there are none. At a given profile exactly one characteristic indicator is \(t\); all others are \(f\). For a nonclassical required output, the restriction ensures the cell has a nonclassical atomic vector, so the appropriate flag has exactly the required value. The disjunction therefore realizes \(h\) at every profile. This proves the upper bound is attained and the representatives have depth at most one.

**6. Sharp finite-world bound.** If a formula is realized at a world of profile \((a,S)\), retain one world of each vector in \(S\), retaining the distinguished world for its vector. Part 1 preserves the complete value of every formula, and at most \(q\) worlds remain. Conversely, the crisp depth-one formula \(\bigwedge_{a\in Q}E_a\) is \(t\) exactly in a cell containing every one of the \(q\) distinct atomic vectors; no smaller cell can satisfy it. This establishes sharpness.

## Verification

The standalone `checker.py` evaluates formulas as pairs of positive/negative information bits using the published truth/falsity clauses. Its deterministic tests cover: all sixteen input/output entries of the four crisp local tests; all 32 one-letter pointed profiles and their support indicators and flags; 12 independently prescribed complete four-valued functions over all 32 profiles, restricted to classical output on the four classical profiles; forty sampled two-letter pointed supports; and the first two exact exponent calculations. It prints `ALL_CHECKS_OK 1090 finite semantic checks`. This finite regression suite checks the constructive building blocks and examples. The induction and symbolic normal-form construction, not finite experimentation, prove the arbitrary-\(k\) theorem.

## Relationship to prior work

Petrukhin, *Essence and Accident Modalities Meet Belnapian Truth Values* (Studia Logica, first public online July 15, 2026; arXiv:2610.08323, October 6, 2026), supplies the four-valued S5 semantics and the value-indexed modalities in Definitions 2.5–2.8; Theorems 5–9 establish embeddings, completeness, and decidability. Those statements do not give the exact finite free semantic algebra, complete depth-one classification, or the sharp world threshold here. The distinction between truth and falsity coordinates is essential to the counting formula.

Earlier work of Odintsov, Skurt and Wansing, *On Definability of Connectives and Modal Logics over FDE* (2019), gives powerful expressibility results for other FDE modal systems and regular metalogical connectives. The present theorem concerns the exact finite-space term-function quotient of the particular full value-indexed S5 essence language, including a classical-preservation obstruction. Standard classical S5 pointed-type normal forms provide a relevant analogy but not this four-valued count.

## Limitations

The theorem concerns complete four-valued semantic equality, not quotienting solely by designated-truth equivalence or proof-theoretic interderivability. The modal signature includes **all twenty-four** published essence/accident operators; no minimum generating subfamily is claimed. For arbitrary S5 frames with multiple equivalence cells, apply the theorem pointwise to the cell containing the distinguished world. No result is asserted about arbitrary non-S5 or non-reflexive frames. The one-letter count should not be misread as the number of syntactic formulas of bounded length.

The novelty comparison used the accessible full arXiv text of the 2026 semantic paper and published descriptions/accessible material for earlier expressibility work. An older free-algebra or term-clone presentation under different terminology could imply the classification; independent historical-priority review has not been performed.

## References

1. Yaroslav Petrukhin, *Essence and Accident Modalities Meet Belnapian Truth Values*, Studia Logica (online July 15, 2026), DOI: https://doi.org/10.1007/s11225-026-10250-z; full arXiv text: https://arxiv.org/abs/2610.08323 (submitted October 6, 2026). Definitions 2.5–2.8 and Theorems 5–9.
2. Sergei P. Odintsov, Daniel Skurt, Heinrich Wansing, *On Definability of Connectives and Modal Logics over FDE*, Logic and Logical Philosophy 28 (2019), 631–659, DOI: https://doi.org/10.12775/LLP.2019.010.
3. Greg Restall, *Proofnets for S5: Sequents and Circuits for Modal Logic*, Logic Colloquium 2005 (published 2007), 151–172; classical S5 proof-theoretic background cited by Petrukhin.
