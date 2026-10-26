# A sharp two-state theorem for bilateral truthmaking over chains

## Finding

**Theorem (uniform sharp two-state property).** Fix an integer \(k\ge1\) and a finite set of formulas in the alphabet \(p_1,\ldots,p_k\) with connectives \(\neg,\wedge,\vee\). In the bilateral, non-inclusive exact-truthmaker interpretation with unrestricted positive and negative atomic valuations on all nonempty chains (finite or infinite), a finite conjunction of truthmaking and non-truthmaking requirements on these formulas at one common state is satisfiable if and only if it is satisfiable at the top of the chain \(0<1\). This includes all choices of sign in each requirement.

As a consequence, truthmaker/falsemaker semantic equivalence and signed truthmaker entailment over all such chains are decidable by evaluation of exactly \(3^{2k}=9^k\) canonical signed atomic profiles on the two-state chain; using syntax-tree evaluation, time is \(O(9^k L)\), with \(L\) the total length of the formulas tested. The two-state bound is optimal for bilateral equivalence. A structural companion result characterizes chains among join-semilattices by the universal inclusion \(\lVert p\wedge q\rVert^+\subseteq\lVert p\vee q\rVert^+\) under unrestricted valuations; its first counterframe has three states.

## Assumptions and scope

A frame is a nonempty totally ordered set \((S,\le)\). Binary fusion is \(a\sqcup b=\max\{a,b\}\); no greatest or least element is required, and the chain may be infinite. For each propositional letter \(p_i\), the positive and negative atomic valuation sets \(V^+(p_i),V^-(p_i)\subseteq S\) are arbitrary and independent, possibly empty, overlapping or nonconvex. The language contains only propositional letters and \(\neg,\wedge,\vee\): there are no constants, quantifiers, extra modalities, classical negation, or global truth conditions.

For a formula \(\varphi\), write \(T_\varphi=\lVert\varphi\rVert^+\) and \(F_\varphi=\lVert\varphi\rVert^-\). For sets \(A,B\subseteq S\), define \(A\odot B=\{\max(a,b):a\in A,\ b\in B\}\). The complete semantics is:

\[
\begin{aligned}
&T_{p_i}=V^+(p_i),\qquad F_{p_i}=V^-(p_i),\\
&T_{\neg\varphi}=F_\varphi,\quad F_{\neg\varphi}=T_\varphi,\\
&T_{\varphi\wedge\psi}=T_\varphi\odot T_\psi,\quad F_{\varphi\wedge\psi}=F_\varphi\cup F_\psi,\\
&T_{\varphi\vee\psi}=T_\varphi\cup T_\psi,\quad F_{\varphi\vee\psi}=F_\varphi\odot F_\psi.
\end{aligned}
\]

A signed condition at a state asks either for membership or for nonmembership in \(T_\varphi\) or \(F_\varphi\). A positive (respectively negative) consequence \(\varphi\models_+\psi\) (respectively \(\models_-\)) is inclusion \(T_\varphi\subseteq T_\psi\) (respectively \(F_\varphi\subseteq F_\psi\)) in every such model. Bilateral equivalence requires both equalities.

## Proof

**Lemma 1 (four-bit local calculus).** Fix a state \(s\). For any \(A\subseteq S\), put \(e_A(s)=\mathbf1_{s\in A}\) and \(h_A(s)=\mathbf1_{A\cap(-\infty,s]\ne\emptyset}\). Then

\[
\begin{aligned}
 e_{A\cup B}(s)&=e_A(s)\lor e_B(s),&
 h_{A\cup B}(s)&=h_A(s)\lor h_B(s),\\
 e_{A\odot B}(s)&=(e_A(s)\land h_B(s))\lor(h_A(s)\land e_B(s)),&
 h_{A\odot B}(s)&=h_A(s)\land h_B(s).
\end{aligned}
\]

Indeed, on a chain \(\max(a,b)\le s\) exactly when \(a,b\le s\); furthermore \(\max(a,b)=s\) exactly when one factor equals \(s\) and the other is at most \(s\). These equivalences prove both fusion equations even for infinite or empty sets (existential witnesses involve only two elements). The union equations are immediate.

For every \(\varphi\), simultaneously maintain
\[
 (e^+_\varphi,e^-_\varphi,h^+_\varphi,h^-_\varphi)(s)
 = (e_{T_\varphi},e_{F_\varphi},h_{T_\varphi},h_{F_\varphi})(s).
\]
The semantic clauses together with Lemma 1 give a deterministic Boolean recurrence for this four-bit vector: atoms supply two \((e,h)\) pairs, negation swaps signs, conjunction uses fusion on the positive pair and union on the negative pair, and disjunction uses union on the positive pair and fusion on the negative pair. By induction on formula complexity, all four bits for all formulas depend only on the \(2k\) signed atomic pairs at \(s\).

**Lemma 2 (universal profile realization).** For every signed atomic set, \(e\le h\), so its only possible \((e,h)\) values are \((0,0),(0,1),(1,1)\). Given any arbitrary assignment of these three values to each of the \(2k\) independently signed atoms, take \(S'=\{0<1\}\) and at the distinguished top \(1\) interpret that signed atom by \(\emptyset,\{0\},\{1\}\), respectively. All atomic profiles are then realized exactly. By Lemma 1 and structural induction, *every* formula has the same four-bit truthmaking profile at the chosen original state and at \(1\) in this canonical model. Conversely, any two-state top-point model is already a model on a chain. Thus any finite Boolean combination of signed truthmaking and non-truthmaking requirements at one point can be transferred in both directions. There are \(3^{2k}=9^k\) canonical atomic profiles, and each is processed by one traversal of the relevant formula trees; this proves the theorem and the stated computational upper bound.

**Sharpness.** Let \(\alpha=p\wedge(p\vee q)\), \(\beta=p\). On a singleton, fusion equals set intersection and union behaves Booleanly, so the positive set of \(\alpha\) is \(V^+(p)\cap(V^+(p)\cup V^+(q))=V^+(p)\); the negative set is \(V^-(p)\cup(V^-(p)\cap V^-(q))=V^-(p)\). Thus \(\alpha\) and \(\beta\) agree bilaterally on all one-state frames. On \(0<1\), put \(V^+(p)=\{0\}\), \(V^+(q)=\{1\}\), and both negative valuations empty. Then \(1\in T_\alpha\) but \(1\notin T_\beta\). No one-state bound can decide equivalence.

**Sharp chain boundary.** On a chain, \(A\odot B\subseteq A\cup B\) because \(\max(a,b)\) equals one factor. Conversely, in a join-semilattice containing incomparable elements \(a,b\), let \(c=a\sqcup b\notin\{a,b\}\), set \(V^+(p)=\{a\}\), \(V^+(q)=\{b\}\), and choose negative valuations arbitrarily. Then \(c\in T_{p\wedge q}\setminus T_{p\vee q}\). Any finite nonchain join-semilattice must have at least three points, attained by the fork \(a,b<c\), proving the optimal boundary.

## Verification

Run `python3 truthmaker_chain_checker.py` (no nonstandard dependencies). The checker evaluates exact recursive sets and independently computed local profiles on every valuation for chains of 1, 2 and 3 states with two atoms, and for a 4-state chain with one atom; it checks 835824 formula/profile cases. It independently tests the two fusion identities for all subset pairs on every chain of sizes 1 through 6 (30948 state-level gate cases), the universal singleton absorption identity, the explicit two-state sharpness witness, and the three-state fork boundary. Expected line: `TRUTHMAKER_TWO_POINT_CHECK_OK 835824 30948 SHARP_2 NONCHAIN_3`.

These finite checks do not prove the arbitrary-formula, arbitrary-atom or infinite-chain quantifiers; Lemmas 1 and 2 provide those proofs. The Python source is included in this package.

## Relationship to prior work

The exact bilateral semantic clauses follow the non-inclusive option spelled out in Knudstorp (2023, Definition 2.4), also discussed by Aloni et al. (2026, Section 2). General effective translations and finite-model/decidability results for truthmaker logics are established in Knudstorp (2023), and are not new here. Aloni et al. (2026) develop translations of richer state-based logics into modal languages over semilattices; they are the recent motivation for examining the special behavior of totally ordered fusion.

The contribution isolated here is a **formula-independent**, sharp two-state bound for all signed exact truthmaking observations on chains, with explicit three-valued atomic profiles, a uniform decision procedure, and a minimal nonchain boundary. This statement does not claim a new general decidability theorem for arbitrary semilattices or the richer bilateral state-based language. Comparison against wider generic finite-model arguments must preserve the chain-specific two-state bound and unrestricted non-inclusive valuations, not merely match the conclusion 'decidable'.

## Limitations

The theorem is only about the propositional \(\neg,\wedge,\vee\) language, non-inclusive exact semantics, unrestricted bilateral valuations and totally ordered fusion. It need not extend to arbitrary join-semilattices, classical modal connectives, global model modalities, alternative inclusive/replete/convex clauses, or other valuation restrictions without new arguments. The algorithm is exponential in the number of distinct propositional letters; no matching computational complexity lower bound is asserted. Historical priority is qualified: an earlier specialized chain treatment or a sufficiently strong generic theorem not located in the checked literature could subsume the result. Finite checker data cannot eliminate this possibility. Independent validation has not been performed.

## References

1. M. Aloni, A. Baltag, J. van Benthem, N. Bezhanishvili and S. B. Knudstorp, *Teams, Truthmakers, Translations* (2026), arXiv:2610.15680v1, publicly submitted 2026-10-11. https://arxiv.org/abs/2610.15680
2. S. B. Knudstorp, *Logics of Truthmaker Semantics: Comparison, Compactness and Decidability*, Synthese 202 (2023), article 206, doi:10.1007/s11229-023-04401-1. Author-available PDF: https://knudstorp.github.io/pdfs/Logics%20of%20Truthmaker%20Semantics.%20Comparison%2C%20Compactness%20and%20Decidability.pdf
3. J. Korbmacher, *Proof Systems for Exact Entailment*, Review of Symbolic Logic (2022), doi:10.1017/S175502032200020X. https://doi.org/10.1017/S175502032200020X
4. K. Fine and M. Jago, *Logic for Exact Entailment*, Review of Symbolic Logic 12 (2019), 536–556, doi:10.1017/S1755020318000151. https://doi.org/10.1017/S1755020318000151
