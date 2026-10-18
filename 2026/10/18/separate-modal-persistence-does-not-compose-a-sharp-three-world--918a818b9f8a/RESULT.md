# Separate modal persistence does not compose: a sharp three-world countermodel

## Finding

In the **extrinsic** bi-relational intuitionistic semantics, simultaneous persistence of every formula in the one-modality \(\Box\)-fragment and every formula in the one-modality \(\Diamond\)-fragment does **not** entail persistence of every mixed-modal formula **for a fixed model**. A counterexample uses three worlds and one propositional variable. No counterexample on fewer than three worlds exists, even if arbitrary additional propositional variables are allowed. Moreover, in any model satisfying both one-modality persistence assumptions, all formulas of modal nesting depth at most one are persistent; the counterexample separates them at depth two.

This answers negatively the fixed-model question stated as Problem 3.10 of Sato (2026), without contradicting its frame-level persistence equivalence.

## Assumptions and scope

A fusion model is \(M=(W,\leq,R,V)\), with a nonempty set \(W\), a reflexive transitive preorder \(\leq\), arbitrary binary relation \(R\), and propositional valuations \(V(q)\) that are upward closed under \(\leq\). Equality of worlds is not identified under the preorder. All connectives use the intuitionistic Kripke clauses. The **extrinsic** modal clauses are
\[
M,w\models\Box\varphi\iff\forall v\,(wRv\Rightarrow M,v\models\varphi),\qquad
M,w\models\Diamond\varphi\iff\exists v\,(wRv\land M,v\models\varphi).
\]
For \(\varphi\to\psi\), truth at \(w\) means that every \(v\geq w\) satisfying \(\varphi\) also satisfies \(\psi\). A formula is *persistent in a fixed model* if its truth set is upward closed. This property is weaker than persistence under all valuations on the underlying frame. The \(\Box\)-fragment allows the intuitionistic connectives and \(\Box\), but not \(\Diamond\); the \(\Diamond\)-fragment is analogous.

Our witness has \(W=\{a,b,c\}\) and the only strict preorder comparison \(a<b\). The modal successor sets and sole nonconstant atom are
\[
R[a]=\{a\},\qquad R[b]=\{a,c\},\qquad R[c]=\{a\},\qquad V(p)=P=\{b,c\}.
\]
Other propositional letters, if any, can be interpreted as constant false. The valuation is persistent since \(a\notin P\). There is no required reflexivity, seriality, symmetry, transitivity or confluence assumption on \(R\), though this witness happens to have a successor at every world.

## Proof

**1. The entire \(\Diamond\)-fragment is persistent.** For a truth set \(A\subseteq W\), write \(D(A)=\{w:R[w]\cap A\ne\varnothing\}\). Directly from the three successor rows,
\[
D(A)=
\begin{cases}
W,&a\in A,\\
\{b\},&a\notin A\text{ and }c\in A,\\
\varnothing,&a,c\notin A.
\end{cases}
\]
The set of all upsets of the preorder is
\[
\operatorname{Up}(W)=\{\varnothing,\{b\},\{a,b\},\{c\},\{b,c\},W\}.
\]
Each output of \(D\) is an upset, even when its input is arbitrary. Since the atomic valuations are upsets, and intuitionistic \(\land,\lor,\to,\bot\) preserve upsets, structural induction proves persistence of **every** \(\Diamond\)-only formula, with no depth restriction.

**2. The entire \(\Box\)-fragment is persistent.** For \(A\subseteq W\), set \(B(A)=\{w:R[w]\subseteq A\}\). The three-element family
\[
H=\{\varnothing,P,W\},\qquad P=\{b,c\},
\]
is closed under intersection, union and the intuitionistic Heyting implication of the upset algebra. For \(A,C\in H\), one has \(A\Rightarrow C=W\) if \(A\subseteq C\), and \(A\Rightarrow C=C\) otherwise. Directly from the successor rows,
\[
B(\varnothing)=\varnothing,\qquad B(P)=\varnothing,\qquad B(W)=W.
\]
All atomic truth sets, including false constants for extra letters, are in \(H\). Induction on formulas therefore proves that every \(\Box\)-only formula has truth set in \(H\), hence is persistent.

**3. Mixed persistence fails.** We calculate the truth sets of the subformulas:
\[
\llbracket\Diamond p\rrbracket=\{b\},\qquad
\llbracket p\to\Diamond p\rrbracket=\{a,b\},\qquad
\llbracket\Box(p\to\Diamond p)\rrbracket=\{a,c\}.
\]
The middle calculation uses the intuitionistic implication clause: at \(a\), every higher world where \(p\) holds is \(b\), which also satisfies \(\Diamond p\); at \(c\), \(p\) holds but \(\Diamond p\) fails. The final set is not upward closed because \(a\leq b\), \(a\) satisfies the displayed mixed formula, and \(b\) does not.

**4. Three worlds are necessary, even with arbitrarily many atoms.** A one-world model is automatically persistent. On two worlds, every preorder is, up to renaming, either discrete, a two-point chain \(a<b\), or the universal equivalence preorder. On a discrete preorder every truth set is an upset. Otherwise, assume all formulas of both one-modality fragments are persistent. In particular \(\Box\bot\) and \(\Diamond\top\) are persistent; their truth sets are complementary, and in a nondiscrete two-world preorder **the only subsets whose sets and complements are both upsets are \(\varnothing\) and \(W\)**. Thus either every modal successor row is empty or every modal successor row is nonempty.

For the universal equivalence preorder, every persistent atomic valuation is constant. Both modal operators preserve the two constant truth sets when successor-row emptiness is uniform, so every mixed formula is constant and persistent. For the chain, if all atomic valuations are constant the same argument applies. Otherwise some atomic letter has truth set \(\{b\}\). Persistence of the two one-modality formulas \(\Box q\) and \(\Diamond q\) implies that both \(B(\{b\})\) and \(D(\{b\})\) are upsets. The operators also map \(\varnothing\) and \(W\) to upsets, by uniform successor-row emptiness. These are **all** upsets of a two-element chain. As the intuitionistic connectives preserve upsets, induction proves persistence of all mixed formulas. Hence the three-world witness is cardinality-minimal.

**5. Modal depth two is necessary.** If both one-modality fragments are persistent, any subformula of depth one headed by \(\Box\) or \(\Diamond\) is itself in the appropriate fragment (its argument is propositional). These subformula truth sets are upsets; their combinations by intuitionistic connectives are upsets. The displayed separating formula has modal depth two.

## Verification

The standalone Python 3 checker `verify.py` directly computes the three-world upset lattice, the complete truth-set algebras generated by all formulas in each modality fragment (not just depth-bounded samples), and the truth set of the separating formula. It independently exhausts every labelled preorder, every modal relation and every two-letter persistent valuation on one or two worlds. The observed output is:

```
FINITE_MODEL_VERIFY_START
WITNESS_OK: all-unimodal-truth-sets-upward; box(p->dia(p))={a,c}
UNIMODAL_CLOSURES: (3, 6, 8)
TWO_POINT_EXHAUSTIVE_OK: configurations= 616 unimodally_persistent= 454
LOCAL_PERSISTENCE_COUNTEREXAMPLE_VERIFY_OK
```

Run `python3 verify.py` from the directory containing that file. The finite enumeration is a reproducibility check; the unbounded-formula assertions and the all-vocabularies two-world minimality follow from the algebraic and structural proofs above.

## Relationship to prior work

Sato (2026), Definition 3.2, formulates the extrinsic clauses, Proposition 3.7 characterizes persistence of each unimodal fragment **over all valuations** via confluence conditions, and Proposition 3.8 combines those conditions to obtain persistence in the full bimodal language **over all valuations**. Its Problem 3.10 explicitly asks whether the analogous implication holds for **one fixed model**. The present three-world construction answers that distinct question in the negative. It violates the \(\Box\)-p frame condition, so it is not covered by the positive frame-level result.

The published published-finding corpus study *Finite criterion for commuting box and diamond condensations* (2026) analyzes when two right-sided relation completions commute, not fixed-valuation persistence of syntax with both modalities. Its limitations expressly do not claim preservation of mixed-modal formulas. Its theorem neither produces nor rules out this counterexample.

Actual source/claim/alias searches found no pre-existing statement giving this particular fixed-model separation or the three-world lower bound. This supports, but does not establish, historical priority. The original thesis literature on fusion-model semantics has not been examined exhaustively.

## Limitations

The negative conclusion is about **extrinsic** modal semantics for one fixed model. It is not a counterexample to the intrinsic semantics, nor to the positive result for frames satisfying both confluence conditions. It does not classify all minimal witnesses up to isomorphism, nor does it establish a minimal number of relation edges or of propositional variables. The modal-depth and world-count lower bounds have precisely the assumptions stated above. Independent expert review and historical-priority certification have not been performed.

## References

[1] Yuta Sato, *Intuitionistic and Constructive Modal Logics for Classical Modal Logicians*, arXiv:2608.29708, first public version 30 August 2026, especially Definitions 3.1–3.4, Propositions 3.7–3.8, and Problem 3.10. https://arxiv.org/html/2608.29708

[2] *Finite criterion for commuting box and diamond condensations*, published-finding corpus research record, 4 October 2026, especially its Finding, Relationship to prior work, and Limitations. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-finite-criterion-for-commuting-box-and-diamond-condensations--c53088b3c02d
