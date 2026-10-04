# Idempotence and exact commutation of propositional hedged contractions
## Finding

Belardinelli and Zhang define contraction by a hedged public announcement directly on ordinary Kripke models. Their update leaves worlds and propositional valuations unchanged and only adds accessibility arrows.

For propositional contraction contents, this yields a complete algebra of repetition and order.

Let
\[
P=\llbracket\varphi\rrbracket_M\subseteq W
\]
be the truth set of a propositional formula \(\varphi\). For one agent at one source world, write its current successor set as \(S\subseteq W\). Then the contraction row map is
\[
c_P(S)=
\begin{cases}
S\cup(W\setminus P),&S\subseteq P,\\
S,&S\not\subseteq P.
\end{cases}
\]

The first result is idempotence:
\[
\boxed{c_P(c_P(S))=c_P(S).}
\]
Consequently, for every Kripke model \(M\) and every propositional \(\varphi\),
\[
\boxed{(M\div\varphi)\div\varphi=M\div\varphi.}
\]
Thus for every formula \(\chi\),
\[
\boxed{
[\div\varphi][\div\varphi]\chi
\leftrightarrow
[\div\varphi]\chi
}
\]
is valid.

There is also an exact commutation criterion. For two subsets \(P,Q\subseteq W\), the following are equivalent:

1. \(c_P\circ c_Q=c_Q\circ c_P\) on every successor set \(S\subseteq W\);
2. \(P=Q\) or \(P\cup Q=W\).

Therefore, for propositional formulas \(\varphi\) and \(\psi\), contraction by \(\varphi\) and contraction by \(\psi\) commute on every Kripke model exactly when
\[
\boxed{
\models_{\mathrm{CPL}}\varphi\leftrightarrow\psi
\quad\text{or}\quad
\models_{\mathrm{CPL}}\varphi\lor\psi.
}
\]
Equivalently, under exactly this condition, for every formula \(\chi\),
\[
\boxed{
[\div\varphi][\div\psi]\chi
\leftrightarrow
[\div\psi][\div\varphi]\chi
}
\]
is valid on all Kripke models.

If neither propositional condition holds, order dependence already occurs on a two-world model with an empty doxastic successor row.

## Assumptions and scope

The contraction operation is exactly Definition 4.1 of Belardinelli--Zhang. For a Kripke model
\[
M=(W,R,V),
\]
the updated successor set for agent \(a\) at world \(w\) is obtained by adding every world satisfying \(\neg\varphi\) precisely when \(a\) initially believes \(\varphi\) at \(w\).

The theorem restricts \(\varphi\) and \(\psi\) to propositional formulas. This restriction is essential because propositional truth is invariant under the update, while modal formulas can change truth value when accessibility arrows are added. The source paper explicitly exploits propositional invariance in its AGM-style results.

No seriality, transitivity, Euclideanness, reflexivity, or finiteness assumption is imposed on the accessibility relations or on \(W\).

The commutation criterion is universal: it characterizes when the two contractions commute for every Kripke model. Particular relations may accidentally commute even when the propositional criterion fails.

## Proof

Fix a propositional \(\varphi\) and put
\[
P=\llbracket\varphi\rrbracket_M.
\]
Because contraction does not change propositional valuations, \(P\) remains the truth set of \(\varphi\) after every contraction update.

For one accessibility row \(S=R_a(w)\),
\[
M,w\models B_a\varphi
\quad\Longleftrightarrow\quad
S\subseteq P.
\]
Definition 4.1 therefore becomes
\[
c_P(S)=
\begin{cases}
S\cup P^c,&S\subseteq P,\\
S,&S\not\subseteq P,
\end{cases}
\]
where
\[
P^c=W\setminus P.
\]

For idempotence, suppose first that \(S\not\subseteq P\). Then \(c_P(S)=S\), so another application changes nothing.

Suppose instead that \(S\subseteq P\). If \(P^c=\varnothing\), then \(c_P(S)=S\). If \(P^c\ne\varnothing\), then
\[
c_P(S)=S\cup P^c
\]
contains a point outside \(P\), so the updated row is not a subset of \(P\). The second application is therefore inactive. Thus
\[
c_P^2=c_P.
\]
Since the update acts row by row and leaves worlds and valuations fixed,
\[
(M\div\varphi)\div\varphi=M\div\varphi.
\]

Now fix two subsets \(P,Q\subseteq W\).

If \(P=Q\), commutation is immediate from idempotence.

Assume
\[
P\cup Q=W.
\]
Then
\[
P^c\subseteq Q,
\qquad
Q^c\subseteq P.
\]
Take any row \(S\subseteq W\).

If \(S\not\subseteq P\) and \(S\not\subseteq Q\), neither map changes \(S\).

If \(S\subseteq P\) but \(S\not\subseteq Q\), then applying \(c_Q\) first does nothing, while applying \(c_P\) adds \(P^c\). The witness already in \(S\setminus Q\) remains, so \(c_Q\) is still inactive afterward. Both orders therefore give
\[
S\cup P^c.
\]
The symmetric case is identical.

Finally suppose
\[
S\subseteq P\cap Q.
\]
Applying \(c_P\) adds \(P^c\subseteq Q\), so the resulting row remains a subset of \(Q\), after which \(c_Q\) adds \(Q^c\). Reversing the order gives the same set:
\[
S\cup P^c\cup Q^c.
\]
Thus the row maps commute whenever \(P=Q\) or \(P\cup Q=W\).

For necessity, suppose
\[
P\ne Q
\quad\text{and}\quad
P\cup Q\ne W.
\]
Take the empty row
\[
S=\varnothing.
\]
Then
\[
c_P(S)=P^c.
\]
Because \(P\cup Q\ne W\), there is a world outside both \(P\) and \(Q\), so \(P^c\not\subseteq Q\). Hence a subsequent \(Q\)-contraction is inactive and
\[
c_Q(c_P(\varnothing))=P^c.
\]
Similarly,
\[
c_P(c_Q(\varnothing))=Q^c.
\]
Since \(P\ne Q\), their complements differ. Hence the maps do not commute on all rows.

This proves the set-theoretic criterion.

To pass to formulas, if
\[
\models_{\mathrm{CPL}}\varphi\leftrightarrow\psi,
\]
then their truth sets agree in every model. If
\[
\models_{\mathrm{CPL}}\varphi\lor\psi,
\]
then their truth sets cover every model. Either condition therefore gives universal commutation.

Conversely, suppose neither propositional formula is valid. Since
\[
\not\models_{\mathrm{CPL}}\varphi\leftrightarrow\psi,
\]
there is a propositional valuation at which exactly one of \(\varphi,\psi\) is true. Since
\[
\not\models_{\mathrm{CPL}}\varphi\lor\psi,
\]
there is a propositional valuation at which both are false. Put these two valuations at two worlds of one Kripke model and give some agent an empty successor row. Then the two truth sets are unequal and do not cover the carrier, so the two update orders produce different successor sets.

For the dynamic-schema converse, choose a fresh atom \(r\) not occurring in \(\varphi\) or \(\psi\), and make \(r\) false at one world in the symmetric difference of the two final successor sets and true at all other worlds. The formula
\[
B_a r
\]
then distinguishes the two orders. Thus universal dynamic commutation fails.

## Verification

The bundled checker independently implements the row map
\[
c_P(S).
\]

For universe sizes through six, it exhaustively enumerates every triple
\[
(P,Q,S)
\]
and verifies:

\[
c_P(c_P(S))=c_P(S),
\]
and
\[
\bigl(\forall S\; c_P(c_Q(S))=c_Q(c_P(S))\bigr)
\quad\Longleftrightarrow\quad
P=Q\text{ or }P\cup Q=W.
\]

For every noncommuting pair in those sizes, it verifies that the empty row is a witness and that a one-atom belief test can distinguish the two final successor sets.

It also exhaustively checks, for all Boolean truth functions of at most two propositional atoms, that universal model commutation is equivalent to one of the two propositional conditions: equivalence is tautological or the disjunction is tautological.

The script prints `VERIFY_OK`.

The computation is corroborative. The theorem for arbitrary sets follows from the direct row-map proof.

## Relationship to prior work

Belardinelli and Zhang introduce hedged public announcement contraction and prove a complete reduction-axiom system for it. Their Definition 4.1 is exactly the update analyzed here. They also emphasize that propositional truth is unchanged by contraction, and Proposition 6.3 derives several AGM-style properties under propositional restrictions.

The paper does not state idempotence of propositional contraction, an exact commutation criterion for two contractions, or the two-world order-dependence boundary above. Full-text searches for idempotence and commutation terminology returned no such result. Its conclusion instead lists iterative properties of the broader generalized dynamic system among directions for future work.

The 2026 KR paper *Suspending Judgement: Belief Contraction in Dynamic Epistemic Logic* is a highly relevant independent approach to dynamic contraction. Accessible metadata confirms the topic, but the full text was not available in the comparison channel, so possible overlap under a different contraction semantics remains a literature risk.

The new result is specific to the Belardinelli--Zhang hedged public announcement operator. It is not inferred from generic AGM contraction postulates: the proof uses the operator's concrete rule of adding all counterexamples exactly when the current successor row lies inside the contracted truth set.

## Limitations

The idempotence and exact commutation theorem is restricted to propositional contraction contents. Modal contraction contents can change truth value when edges are added, and no corresponding classification is claimed.

The universal commutation criterion concerns arbitrary Kripke relations. On a fixed model, two contractions can commute accidentally even when their propositional truth sets are unequal and fail to cover the carrier.

No claim is made about commutation between contraction and expansion, revision, or arbitrary generalized event models.

The related 2026 KR contraction paper could contain an analogous theorem for its own semantics; its inaccessible full text is the main residual literature risk.

## References

[1] Gaia Belardinelli and Snow Zhang, “Belief Contraction in Dynamic Epistemic Logic,” *Electronic Proceedings in Theoretical Computer Science* 447 (2026), 137–157. arXiv:2606.31861. DOI:10.4204/EPTCS.447.8.

[2] Alexandru Baltag, Virginie Fiutek, and Sonja Smets, “Suspending Judgement: Belief Contraction in Dynamic Epistemic Logic,” *Proceedings of KR 2026*. DOI:10.24963/KR.2026/10.
