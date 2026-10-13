# Signed-trace compression for weak-negation neighborhood modalities

## Finding
Let \(\Gamma\) be a finite set of formulas and \(\psi\) a formula in the weak-negation bimodal language with \(\neg,\wedge,\vee,\to,\Box,\Diamond\). Let \(F=\operatorname{Sub}(\Gamma\cup\{\psi\})\), and let \(Q=\{\alpha:\#\alpha\in F,\ \#\in\{\Box,\Diamond\}\}\) be its set of distinct **modal operands**, with \(k=|Q|\). Under the unrestricted, four-independent-neighborhood membership semantics described below, every pointed model has a pointed finite model preserving **both** signed truth sets of every formula in \(F\) at all retained worlds and using at most
\[
B(k)=\begin{cases}1,&k=0,\\2k-1,&k\ge1.\end{cases}
\]
The bound is worst-case sharp for the associated task of simultaneously separating all distinct positive and all distinct negative operand sets while retaining a prescribed point (not claimed sharp as a minimum model-size bound). Consequently, deciding **finite-premise local semantic consequence** \(\Gamma\models\psi\) and, in particular, validity, is **coNP-complete** for these unrestricted semantics.

## Assumptions and scope
A signed model has a nonempty set \(W\), independent atomic sets \(P_p^+,P_p^-\subseteq W\), and four unrestricted neighborhood assignments \(N_{\#}^{\sigma}:W\to\mathcal P(\mathcal P(W))\), one for each \(\#\in\{\Box,\Diamond\}\) and \(\sigma\in\{+,-\}\). Every formula \(\theta\) has two sets \([\theta]^+,[\theta]^-\subseteq W\). Atomic components equal \(P_p^\sigma\); positive components obey
\[
[\neg\alpha]^+=[\alpha]^-,\quad
[\alpha\wedge\beta]^+=[\alpha]^+\cap[\beta]^+,\quad
[\alpha\vee\beta]^+=[\alpha]^+\cup[\beta]^+,\quad
[\alpha\to\beta]^+=(W\setminus[\alpha]^+)\cup[\beta]^+.
\]
For each modality and each sign, the membership clause is
\[
[\#\alpha]^\sigma=\{w\in W:[\alpha]^\sigma\in N_{\#}^{\sigma}(w)\}.
\]
For every nonmodal compound formula the negative set is unconstrained by these clauses; different formulas may be assigned independently, consistently with syntactic identity. This formulation is the unrestricted membership semantics in Vaz and Skurt's Definitions 2.3 and Section 3, with both rejection-neighborhood clauses present. **No** interaction, monotonicity, closure, seriality, normality, exclusion or exhaustion property is imposed. In particular, neither the more restrictive CLuN/CLaN model conditions nor stronger axiom-specific frame classes are asserted to inherit the bound.

A pointed countermodel to \(\Gamma\models\psi\) is \((M,w_0)\) with \(w_0\in\bigcap_{\gamma\in\Gamma}[\gamma]^+\) but \(w_0\notin[\psi]^+\). Only the positive sign determines designated satisfaction; preserving the negative sign as well is essential for formulas involving \(\neg\) or negated modalities. \(F\) is finite and subformula-closed, and \(Q\) counts *distinct syntactic operands* (no duplication of identical subformulas).

## Proof
**1. Separating-trace lemma.** Fix a finite family \(\mathcal A=\{A_1,\ldots,A_t\}\) of distinct subsets of an arbitrary \(W\) and a distinguished point \(w_0\). Starting from \(U=\{w_0\}\), if two distinct sets in \(\mathcal A\) have the same trace on \(U\), choose a point of their symmetric difference outside \(U\) and add it. This increases the number of trace-equivalence classes by at least one and cannot merge any existing classes. Thus at most \(t-1\) points are added to the initial singleton (zero additions when \(t\le1\)). Previous separations remain separated under later enlargement.

**2. Joint signed separation.** Apply the lemma first to the collection of distinct positive operand sets \(\{[\alpha]^+: \alpha\in Q\}\), and then to the distinct negative operand sets \(\{[\alpha]^-:\alpha\in Q\}\), using the already-selected \(U\) as the starting set in the second pass. If \(k>0\), each collection has at most \(k\) members; the total number of added points is at most \(2(k-1)\). Hence \(|U|\le2k-1\). If \(k=0\), use \(U=\{w_0\}\). For each sign independently, distinct full operand sets now have distinct traces on \(U\).

**3. Reconstruction on \(U\).** Set \(W'=U\). Restrict atomic positive and negative sets to \(U\). For each compound nonmodal \(\theta\in F\), prescribe \([\theta]^{\prime,-}=[\theta]^-\cap U\); the semantics permits this choice. For every \(w\in U\), sign \(\sigma\), modality \(\#\), and \(\alpha\in Q\), prescribe
\[
[\alpha]^\sigma\cap U\in N_{\#}^{\prime,\sigma}(w)
\quad\Longleftrightarrow\quad
[\alpha]^\sigma\in N_{\#}^{\sigma}(w).
\]
This is consistent because equality of two traces forces equality of the respective original operand sets within that sign. Define each neighborhood's membership on all other subsets of \(U\) arbitrarily, for example as false. A structural induction over \(F\) now proves
\[
[\theta]^{\prime,\sigma}=[\theta]^\sigma\cap U
\qquad(\theta\in F,\ \sigma\in\{+,-\}).
\]
Atomic cases hold by restriction. The positive \(\neg\) case uses the preserved negative child set; positive Boolean cases use set operations and complement relative to \(U\); negative nonmodal cases are the prescribed free sets. Both signs of modal cases follow from the membership prescription after applying the induction hypothesis to their operands. Arbitrary choices for the other formulas outside \(F\) extend this finite partial valuation to the whole syntax by induction, so \(M'\) is a genuine signed model, not merely a truth table. Since \(w_0\in U\), the original pointed signed truth profile for \(F\) is preserved.

**4. Sharpness for simultaneous signed traces.** Fix \(k\ge2\). Choose distinct points \(w_0,a_1,\ldots,a_{k-1},b_1,\ldots,b_{k-1}\), and signed sets for distinct atoms \(p_0,\ldots,p_{k-1}\) with \([p_0]^+=[p_0]^-=\varnothing\), \([p_i]^+=\{a_i\}\), and \([p_i]^-=\{b_i\}\) for \(1\le i<k\). An \(U\) containing \(w_0\) can preserve distinct traces of *all* \(k\) positive atom sets and *all* \(k\) negative atom sets only if every \(a_i\) and every \(b_i\) belongs to \(U\). Thus \(|U|\ge2k-1\). These atoms can be made operands of \(k\) modal subformulas. The statement is a sharpness result for the explicit trace-separation requirement; arbitrary alternative models or weaker preservation conditions might use fewer worlds.

**5. Polynomial countermodel certificate.** For input \(\Gamma,\psi\), compute the finite subformula set \(F\) and \(k\). Guess \(1\le n\le B(k)\), a root index, and for each \(\theta\in F\) two \(n\)-bit columns \(c_\theta^+,c_\theta^-\). Check every positive truth-table clause for \(\neg,\wedge,\vee,\to\). For any two modal occurrences \(\#\alpha,\#\beta\in F\) with the same modality, and each sign \(\sigma\), check
\[
c_\alpha^\sigma=c_\beta^\sigma\ \Longrightarrow\ c_{\#\alpha}^\sigma=c_{\#\beta}^\sigma.
\]
Finally require every premise's positive bit at the root to be true and the conclusion's bit false. Every genuine countermodel compresses to a passing certificate by steps 1–3. Conversely, from any passing certificate take the guessed worlds, put each atom's signed sets equal to its columns and freely assign the negative sets of nonmodal compounds. For each fixed \(\#\), sign and world, put a subset in \(N_{\#}^\sigma(w)\) exactly when it occurs as a guessed operand-sign column whose modal parent-sign column contains that world. The displayed checks make this well-defined. Give all unlisted subsets negative membership. Induction realizes all guessed columns, and hence the pointed countermodel. The certificate and checks have polynomial size and runtime because \(n\le\max(1,2|F|-1)\).

**6. Lower bound.** Reduce classical propositional tautology in \(\wedge,\vee,\lnot\) to unrestricted validity. Introduce a fresh atom \(f\) and translate classical \(\lnot H\) as \(T(H)\to f\), commuting with \(\wedge,\vee\), while preserving atoms. Set \(T_f(G)=T(G)\vee f\). If \(f\) is verified, this is verified; otherwise its positive value equals the classical truth value of \(G\), by induction, regardless of all independent rejection components. Thus \(T_f(G)\) is valid exactly when \(G\) is a classical tautology. Classical tautology is coNP-complete, so validity is coNP-hard; validity is a special case of finite-premise local consequence. Together with step 5, both problems are coNP-complete.

## Verification
The self-contained standard-library scripts `verify_polarity.py` and `verify_certificates.py` reproduce checks. Execute from one directory with `python3 verify_polarity.py` and `python3 verify_certificates.py`. Observed output was `VERIFY_OK cases=2700 with_modal=2028 max_worlds=5 max_subformulas=23` and `VERIFY_OK certificates=1500 boolean_translation_instances=9600`. The first test randomly assigns four independent neighborhood functions over finite worlds, compresses by both trace families, reconstructs and compares *all* signed subformula columns. The second verifies the column-consistency certificate on 1,500 random finite models and checks the tautology translation on 9,600 classical truth assignments. Finite randomized checks are **not** substitutes for any universal proof step above.

## Relationship to prior work
Vaz and Skurt (2026, arXiv:2606.30297v1) introduce the two-independent-modalities CLoNE semantics and the extension with negative neighborhood functions, proving soundness, completeness and correspondence. The theorem here concerns finite compression, an explicit signed-table certificate and the resulting unrestricted finite-premise local-consequence complexity; these are not among their stated theorems. Drobyshevich and Skurt (2021) develop FDE-based bi-neighborhood modal semantics in which the modal neighborhoods test *proof pairs*, with stronger constraints on propositional rejection, rather than the present individual signed-set membership semantics. Dalmonte and Mazzullo (2023) establish coNP bounds for several **classically negated** combinations of non-normal modal logics; their classical result means that the bare complexity class is **not** intrinsically new. The substantive distinction is a simultaneous positive/negative trace bound and explicit coNP decision certificate for the newer weak-negation, four-independent-neighborhood clauses. A general previously-known extensional-neighborhood argument might possibly imply part of this result; see limitations.

## Limitations
There is no proof of sharpness of the minimal countermodel size itself. The finite model theorem makes no assertion for extensions with additional closure, interaction, normality or frame restrictions, for CLuN/CLaN, for global consequence, or for infinite premise sets given non-finitely. The membership model specified above is essential: FDE neighborhood operators acting on **ordered pairs** of signed sets are different semantics. The result does **not** say ordinary positive satisfiability is NP-complete: unrestricted weak-negation semantics may make positive satisfiability trivial. The literature search and full-text comparisons reduce but do not remove the possibility of a disguised general-filtration or extensionality theorem. Independent audit has not been performed.

## References
1. M. Vaz Silva and D. Skurt, *Modal Extensions of CLoN with Bi-neighborhood Semantics* (2026), arXiv:2606.30297v1, first public 2026-06-29, Sections 2–3. https://arxiv.org/abs/2606.30297
2. S. Drobyshevich and D. Skurt, *Neighbourhood Semantics for FDE-Based Modal Logics*, Studia Logica 109 (2021), 1273–1309, DOI:10.1007/s11225-021-09948-z.
3. T. Dalmonte and A. Mazzullo, *CoNP Complexity for Combinations of Non-normal Modal Logics*, TABLEAUX 2023, 302–321, DOI:10.1007/978-3-031-43513-3_17.
4. T. Dalmonte, N. Olivetti and S. Negri, *Non-normal modal logics: bi-neighbourhood semantics and its labelled calculi*, Advances in Modal Logic 12 (2018), 159–178, for the classical bi-neighbourhood background. https://ticamore.logic.at/publications/DalOliNeg-AIML-2018.pdf
