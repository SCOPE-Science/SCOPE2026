# Joint nondefinability of sixteen Belnapian essence and accident modalities

## Finding

In Petrukhin's four-valued S5 semantics [1, Definition 2.6], **none** of the sixteen indexed operators
\[
\star_J,\qquad \star\in\{\circ,\bullet,\widetilde\circ,\widetilde\bullet\},\quad J\in\{t,f,T,F\},
\]
is definable using the propositional connectives together with **all eight operators jointly** from
\[
\star_b,\star_n,\qquad \star\in\{\circ,\bullet,\widetilde\circ,\widetilde\bullet\}.
\]
This strengthens the individual-pair nondefinability conjectured in [1, Hypothesis 1]. The impossibility holds already for equality of the *designated truth component*, and all sixteen failures have explicit one-world/two-world pointed separating models with classical atomic valuations.

More structurally, on arbitrary nonempty S5 models in which every atom is everywhere classical (valued \(t\) or \(f\)), each formula in the eight-operator \(b/n\) reduct has a classical truth value at every world and is equivalent there to a **pure propositional** formula. Each positive or negative essence operator indexed by \(b\) or \(n\) becomes classical truth; each such accident operator becomes classical falsehood.

## Assumptions and scope

Take the exact four-valued semantics of [1, Definitions 2.4–2.6]. The values are \(t=\{T\}\), \(f=\{F\}\), \(b=\{T,F\}\), and \(n=\varnothing\). An S5 model has a nonempty world set \(W\), with every world accessible from every other world. The propositional connectives are De Morgan negation \(\neg\), Boolean negation \(\sim\), conjunction, disjunction, and the specified implication \(\to\). Optional propositional truth-value abbreviations count only as their defining propositional formulas. There is **no primitive** \(\Box\), \(\Diamond\), quantification over worlds, or named-world operator in the reduct under consideration.

For \(\star\in\{\circ,\bullet,\widetilde\circ,\widetilde\bullet\}\), let \(\star_j\) denote exactly the corresponding connective from [1], not an alternative non-contingency connective from a different FDE semantics. A definition of \(\star_J\) would be one uniform formula \(\delta(p)\) of the reduct, possibly with additional variables, whose value (or even just whose positive-truth component) agrees with \(\star_Jp\) at every pointed model for all valuations. We prove failure even when the extra variables may be freely valued: fix equal values at the distinguished points of the two witness models. This is ordinary explicit definability, not nonexistence of arbitrary model translations.

## Proof

**1. Classical-valuation collapse.** Say a valuation is *crisp* when \(v(q,w)\in\{t,f\}\) for every propositional variable \(q\) and world \(w\). Prove simultaneously by structural induction for every formula \(A\) of the joint eight-operator reduct:

(i) \(v(A,w)\in\{t,f\}\) for every \(w\); and (ii) there exists a classical propositional formula \(c(A)\) in the same atomic variables such that \(v(A,w)=c(A)(v(-,w))\), interpreting classical true and false as \(t\) and \(f\). For atomic formulas the assertion is immediate. By the truth tables of [1, Definition 2.5], all five propositional connectives preserve \(\{t,f\}\) and agree on it with their ordinary classical interpretations.

For the modal induction step, all values of the immediate subformula lie in \(\{t,f\}\) at every world. Since neither \(b\) nor \(n\) occurs, and conflation exchanges precisely those two values (\(\ast b=n\), \(\ast n=b\)), [1, Definition 2.6, second group, eight clauses] gives, for both \(j=b,n\),
\[
 v(\circ_jA,w)=v(\widetilde\circ_jA,w)=t,
 \qquad v(\bullet_jA,w)=v(\widetilde\bullet_jA,w)=f.
\]
For example, \(\circ_j\)'s positive clause is vacuous, and its negative clause requires \(v(A,w)=j\), which is impossible. For \(\widetilde\circ_j\), the antecedent and conclusion of its universal positive clause are always true, while its negative clause would require a world of value \(\ast j\), which cannot exist. For \(\bullet_j\), positive truth requires \(v(A,w)=j\), impossible, and its negative implication has false antecedent. For \(\widetilde\bullet_j\), positive truth requires a world of value \(j\), impossible, while its negative implication has true antecedent and a universally true conclusion. Thus \(c(\circ_j A)=c(\widetilde\circ_j A)=\top\) and \(c(\bullet_j A)=c(\widetilde\bullet_j A)=\bot\), with the constants understood as propositional abbreviations (e.g. \(\top:=q\to q\), \(\bot:=\neg(q\to q)\) for an atom \(q\)). The induction is complete for arbitrary formula nesting and arbitrary nonempty world sets. Consequently, on crisp models the evaluation of every reduct formula at a distinguished world depends *only* on atomic values at that world.

**2. Sixteen separating pairs.** Fix a target index \(J\in\{t,f,T,F\}\), and set
\[
 q_J=\begin{cases}t,&J\in\{t,T\},\\ f,&J\in\{f,F\};\end{cases}
 \qquad \bar q_J=\begin{cases}f,&q_J=t,\\t,&q_J=f.\end{cases}
\]
Take model \(M_1\) with only world \(w\), and model \(M_2\) with two worlds \(w,u\), both using universal S5 accessibility. In both models assign identical crisp atomic truth values at \(w\). In the positive (un-tilded) cases put \(v(p,w)=q_J\) and \(v(p,u)=\bar q_J\); in the negative (tilded) cases put \(v(p,w)=\bar q_J\) and \(v(p,u)=q_J\). Other atoms, if any, have the same values at \(w\) in the two models (assign arbitrary crisp values elsewhere). The one-world model uses only the indicated value at \(w\).

Checking the positive and negative truth/falsity clauses of [1, Definition 2.6], with the crucial fact that \(t,f\) are each fixed under conflation, yields the following **full-valued** outcomes, where columns denote evaluation at the common point \(w\):

| Target operator | \(M_1,w\) | \(M_2,w\) |
| --- | --- | --- |
| \(\circ_J p\) | \(t\) | \(f\) |
| \(\bullet_J p\) | \(f\) | \(t\) |
| \(\widetilde\circ_J p\) | \(t\) | \(f\) |
| \(\widetilde\bullet_J p\) | \(f\) | \(t\) |

For \(J=t,f\) the displayed truth and falsity conditions use exact values; for \(J=T,F\) they use presence of the selected truth/falsity component. On \(\{t,f\}\), each selected status simply designates one of the two classical values, so both checks coincide for the specific witnesses. The table holds for **each** of the four indices \(J\), hence for all sixteen targets.

Every reduct formula, irrespective of its modal nesting or combination of all eight \(b/n\)-indexed operators, has the **same value** at \(w\) in these two pointed models by Step 1. Each target instead changes value and designatedness. Hence no reduct formula can define any target. Since the joint reduct contains each individual pair \(\{\star_b,\star_n\}\), the original narrower conjecture follows as well. \(\square\)

## Verification

Execute `python3 verify.py` from the directory containing this document and the supplied script. The checker directly implements [1, Definition 2.6] using two-bit FDE values, exhaustively checks the eight source-operator collapse clauses on all classical input assignments of lengths one through five, evaluates the sixteen target witnesses, and tests 12,000 sampled nested formulas mixing all eight source operators. The reproducible output includes `VERIFY_OK`, `eight_modal_collapse_checks 2064`, `two_world_target_separations 16`, and `sampled_reduct_term_comparisons 12000`.

These finite tests are corroboration only. The all-formulas/all-models conclusion depends on the structural induction and explicit two-world semantic comparison given above, **not** on enumerating a finite search space.

## Relationship to prior work

Petrukhin [1] supplies the exact semantics and explicitly states the sixteen separate nondefinability questions as **Hypothesis 1**, after Proposition 3. This theorem establishes those conjectured nondefinabilities and, more strongly, nondefinability even when all eight \(b/n\)-status essence/accident modalities are simultaneously available. In contrast, [1] proves embeddings into a richer language possessing standard necessity/possibility; those embeddings cannot imply definability in the restricted eight-operator language, because they introduce modal resources excluded here.

Odintsov, Skurt and Wansing [2] analyze definitional and translation expressiveness of FDE-based modal logics with different operators (including necessity and bilattice connectives). Their general setting motivates looking for invariants but neither states nor proves this result for Petrukhin's status-indexed essence/accident operators. Earlier four-valued non-contingency work [3] concerns a distinct modality and frame semantics.

## Limitations

The result concerns **uniform formula definability** over *all* S5 models in the precisely specified reduct; it does not deny definitions using the richer \(\Box/\Diamond\) language, characterize every sublanguage of the twenty-four operators, or prove independence under nonstandard translations of whole models. The truth-status obstruction uses a classical-valuation subclass; the full four-valued semantics is nevertheless essential to defining the \(b/n\) operators whose collapse is exploited. No independent mathematical validation has been carried out.

## References

[1] Y. Petrukhin, *Essence and Accident Modalities Meet Belnapian Truth Values*, *Studia Logica*, published online 15 July 2026, DOI: 10.1007/s11225-026-10250-z. Public complete manuscript arXiv:2610.08323v1 (6 October 2026), Definition 2.6, Proposition 3, Hypothesis 1. https://arxiv.org/html/2610.08323v1

[2] S. P. Odintsov, D. Skurt, H. Wansing, *On Definability of Connectives and Modal Logics over FDE*, *Logic and Logical Philosophy* 28 (2019), 631–659. DOI: 10.12775/LLP.2019.010. https://doi.org/10.12775/LLP.2019.010

[3] A. Kozhemiachenko and A. Vashentseva, *Non-contingency in a Paraconsistent Setting*, 2024. https://arxiv.org/abs/2312.14815
