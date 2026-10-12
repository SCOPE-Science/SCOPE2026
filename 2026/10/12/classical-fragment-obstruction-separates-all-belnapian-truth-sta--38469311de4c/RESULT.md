# Classical-fragment obstruction separates all Belnapian truth-status modalities from inconsistency and indeterminacy

## Finding

Consider the four-valued S5 semantics for essence and accident introduced by Petrukhin [1]. Let \(\mathcal L_{b,n}\) contain propositional variables, the connectives \(\neg,\sim,\wedge,\vee,\to\), and **all eight** operators
\[
\circ_b,\ \circ_n,\ \bullet_b,\ \bullet_n,\ \widetilde{\circ}_b,\ \widetilde{\circ}_n,\ \widetilde{\bullet}_b,\ \widetilde{\bullet}_n.
\]
For every \(\star\in\{\circ,\bullet,\widetilde{\circ},\widetilde{\bullet}\}\) and \(J\in\{t,f,T,F\}\), the operator \(\star_J\) is **not definable** by a formula of \(\mathcal L_{b,n}\), even if definition means agreement only on the designated truth component rather than on both four-valued components. This holds over the full class of Petrukhin's S5 models and is already witnessed on a universal **two-world** frame.

In particular, all sixteen cases of Hypothesis 13 of [1] hold. The assertion is stronger than that hypothesis: definitions are disallowed even when the proposed defining formula may mix all four families of \(b\)- and \(n\)-indexed operators arbitrarily.

## Assumptions and scope

The truth values are \(t=\{T\}\), \(f=\{F\}\), \(b=\{T,F\}\), and \(n=\varnothing\). A formula is designated at a world when its value contains \(T\). The S5 accessibility is universal on a nonempty set of worlds \(W\). The propositional operations are exactly those in Definition 5 of the journal version of [1], while the indexed modal operations are those in its Definition 6. Thus, \(\neg\) denotes De Morgan negation, \(\sim\) denotes Boolean negation, and \(\to\) is the specified Belnapian implication, not an arbitrary material implication on four values.

For the labels \(J\in\{t,f\}\), the indexed modality tests equality of the operand to that value. For \(J\in\{T,F\}\), it tests membership of the indicated classical component. Conflation exchanges \(b\) and \(n\), and fixes \(t\) and \(f\). Only propositional variables and the indicated propositional connectives and eight modalities are allowed in a proposed definition: no primitive \(\Box\), \(\Diamond\), or independently named four-valued truth constants are assumed.

The claim is uniform for **every** candidate defining formula, including formulas of arbitrary finite modal depth and formulas mentioning extra propositional variables. It concerns semantic definability on the entire class of models, not the expressive power of models confined to nonclassical valuations.

## Proof

**Lemma (classical-fragment collapse).** Let \(M\) be an S5 model in which every propositional variable has value \(t\) or \(f\) at every world. Every \(\mathcal L_{b,n}\)-formula has value \(t\) or \(f\) at every world, and its value at a world \(w\) depends only on the valuations of its propositional variables **at \(w\)**, not on the valuations at other worlds.

*Proof.* Proceed by induction on formulas. The atomic case is immediate. The five connectives \(\neg,\sim,\wedge,\vee,\to\) preserve the two-element subalgebra \(\{t,f\}\), as is clear from the tables in Definition 5 of [1]; they are pointwise operations, so they also preserve locality. For the modal step suppose the subformula takes only \(t\) or \(f\) throughout \(W\). For each \(i\in\{b,n\}\), Definition 6 of [1], including its falsity clauses, gives
\[
\vartheta(\circ_i A,w)=\vartheta(\widetilde{\circ}_i A,w)=t,
\qquad
\vartheta(\bullet_i A,w)=\vartheta(\widetilde{\bullet}_i A,w)=f.
\]
Indeed neither \(i\) nor its conflation \(\ast i\) occurs at any world. For the two positive essence modalities the truth condition is vacuous and the falsity condition fails; for the two accident modalities the truth condition fails and the falsity condition holds. Each resulting formula is therefore an absolute classical constant on these models, independent even of the operand's local value. This establishes the induction step and the lemma. \(\square\)

**Separation for all sixteen operators.** Fix one \(\star\in\{\circ,\bullet,\widetilde{\circ},\widetilde{\bullet}\}\) and one \(J\in\{t,f,T,F\}\). Put \(e_J=t\) for \(J=t\) or \(J=T\), and \(e_J=f\) for \(J=f\) or \(J=F\). Let \(\overline e_J\) be the opposite value in \(\{t,f\}\). Choose
\[
c=\begin{cases}e_J,&\star\in\{\circ,\bullet\},\\
\overline e_J,&\star\in\{\widetilde{\circ},\widetilde{\bullet}\}.
\end{cases}
\]
On the universal frame \(W=\{r,s\}\), define two models \(M_0,M_1\) by setting \(p(r)=c\) in both models, \(p(s)=c\) in \(M_0\), and \(p(s)=\overline c\) in \(M_1\). Give every other variable the same classical value (say \(t\)) at every world in both models. Every atomic valuation at \(r\) is thus identical in \(M_0\) and \(M_1\). The lemma implies that every \(\mathcal L_{b,n}\)-formula has the same value at \(r\) in those models.

But the designated \(T\)-component of \(\star_Jp\) differs: by the truth clauses of Definition 6, its value at \(r\), in the order \((M_0,M_1)\), is
\[
\begin{array}{c|c}
\star& (\vartheta_{M_0}(\star_Jp,r),\vartheta_{M_1}(\star_Jp,r))\\\hline
\circ &(t,f)\\
\bullet &(f,t)\\
\widetilde{\circ}&(t,f)\\
\widetilde{\bullet}&(f,t).
\end{array}
\]
For \(J\in\{t,f\}\), the premise is an equality test; for \(J\in\{T,F\}\), it is the corresponding component-membership test. These agree on the two classical operand values, so the same four pairs apply in both cases. The falsity components also produce the displayed classical values, although the truth-component difference alone suffices.

Any proposed defining formula would agree at \(r\) in these two models, whereas its target operator does not. Thus no such definition exists. Since \(\star\) and \(J\) were arbitrary, all sixteen separations hold. \(\square\)

## Verification

Run `python3 verify.py` from the directory containing this result. This standalone standard-library checker implements all truth and falsity clauses of the four indexed operator families from Definition 6, both for exact status labels and for component labels. It checks that the five propositional operations preserve classical values, checks the constant behaviour of all eight \(b,n\)-indexed modalities for every assignment of classical values to two worlds, and checks all sixteen prescribed target separations. Its success marker is `VERIFY_OK`; its printed rows identify the local operand and both modal outputs.

The program enumerates only finite semantic instances. The **arbitrary-depth** nondefinability claim is established by the induction above, not by finite enumeration.

## Relationship to prior work

Petrukhin's *Essence and Accident Modalities Meet Belnapian Truth Values* [1] supplies the exact semantics and explicitly records the sixteen nondefinability assertions as **Hypothesis 13** in its July 2026 journal publication (Hypothesis 1 in the October 2026 arXiv layout). The paper's Propositions 8–12 give several relationships among indexed operators, and its embedding results involve a richer language containing necessity and possibility. They do not prove definability or nondefinability from just the \(b,n\) operators. The present proof resolves the stated hypothesis while strengthening the excluded defining language from each pair \(\{\star_b,\star_n\}\) to the combined eight-operator set.

Odintsov, Skurt, and Wansing [2] investigate definability and embeddings in other FDE-based modal systems, such as BK and modal bilattice logic; the published abstract does not state the particular separation proved here. The decisive direct comparison is with the formally stated, unresolved hypothesis in [1], rather than an absence of keyword matches. The general technique of using a subalgebra to separate expressive powers is classical; the mathematical content here is its uniform application to the specific eight Belnapian exceptional-status operators and all sixteen ordinary-status targets.

## Limitations

The result does not classify every definability relation among the full set of twenty-four modalities. It assumes the exact propositional signature and S5 truth clauses in [1]; adding \(\Box\), \(\Diamond\), or nonclassical constants to the purported defining language is outside its scope. Restriction to two-world classical-valued assignments is a countermodel technique, **not** a claim that every four-valued model collapses to two values. Possible independent or later discoveries of an equivalent proof are not excluded by the literature comparisons.

## References

[1] Y. Petrukhin, *Essence and Accident Modalities Meet Belnapian Truth Values*, **Studia Logica**, published online 15 July 2026, DOI: https://doi.org/10.1007/s11225-026-10250-z. Open-access version of record: https://link.springer.com/content/pdf/10.1007/s11225-026-10250-z.pdf. Preprint: https://arxiv.org/abs/2610.08323 (v1, 6 October 2026).

[2] S. P. Odintsov, D. Skurt, and H. Wansing, *On Definability of Connectives and Modal Logics over FDE*, **Logic and Logical Philosophy** 28 (2019), 631–659, DOI: https://doi.org/10.12775/LLP.2019.010.
