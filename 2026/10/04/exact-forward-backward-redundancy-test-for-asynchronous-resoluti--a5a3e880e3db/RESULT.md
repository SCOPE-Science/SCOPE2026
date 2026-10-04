# Exact forward-backward redundancy test for asynchronous resolutions
## Finding

Let \(A\) be a finite nonempty set of agents. In the asynchronous resolution semantics of Balbiani, van Ditmarsch, and Lerouvillois, write
\[
V_a(\vec G)=\operatorname{see}_a(\vec G)
\]
for the view of agent \(a\) after resolution history \(\vec G\).

Consider one occurrence of a nonempty resolution group \(B\) inside a history:
\[
\vec H=\vec P.B.\vec S.
\]
Let
\[
V_b=V_b(\vec P),\qquad
Q_a=V_a(\vec S),
\]
and define
\[
U_B=\bigcup_{b\in B}V_b,
\qquad
F_a=\bigcup_{q\in Q_a}V_q.
\]

Call the occurrence \(B\) **relation-redundant** when deleting it preserves every agent's final current epistemic accessibility relation for every underlying epistemic model.

Then \(B\) is relation-redundant if and only if
\[
\forall a\in A:\qquad
Q_a\cap B=\varnothing
\quad\text{or}\quad
U_B\subseteq F_a.
\]

More explicitly, the final view after deleting the occurrence is
\[
V_a(\vec P.\vec S)=F_a,
\]
whereas the final view with the occurrence retained is
\[
V_a(\vec P.B.\vec S)=
\begin{cases}
F_a,&Q_a\cap B=\varnothing,\\[2mm]
F_a\cup U_B,&Q_a\cap B\ne\varnothing.
\end{cases}
\]

Hence the displayed criterion is exact both for final views and, uniformly over all underlying epistemic models, for the induced current accessibility relations.

For an immediate resolution, \(\vec S=\varepsilon\), the criterion simplifies to:
\[
B\text{ is relation-redundant after }\vec P
\quad\Longleftrightarrow\quad
V_b(\vec P)=V_c(\vec P)
\text{ for all }b,c\in B.
\]
Thus an immediate repetition of the same resolution is always relation-redundant.

Finally, if \(n=|A|\), every history has a subhistory of length at most
\[
n(n-1)
\]
with the same final views and therefore the same final current accessibility relations in every underlying epistemic model.

## Assumptions and scope

The result uses the view update from the asynchronous semantics:
\[
\operatorname{see}_C(\varepsilon)=C,
\]
and, after appending a resolution \(B\),
\[
\operatorname{see}_C(\vec G.B)=
\begin{cases}
\operatorname{see}_{C\cup B}(\vec G),&C\cap B\ne\varnothing,\\
\operatorname{see}_C(\vec G),&C\cap B=\varnothing.
\end{cases}
\]
The source also proves
\[
\operatorname{see}_C(\vec G)
=
\bigcup_{c\in C}\operatorname{see}_c(\vec G)
\]
and identifies the current accessibility relation of agent \(a\) after history \(\vec G\) with the intersection of the base relations indexed by \(\operatorname{see}_a(\vec G)\).

The accepted claim concerns the **current relation state** induced by a history. It does not claim that deleting a relation-redundant event preserves the full history-sensitive asynchronous semantics. In fact, the source explicitly notes that two histories can have the same view for an agent while remaining distinguishable by that agent's history relation.

The bound \(n(n-1)\) is a general finite compression bound, not a claimed sharp maximum. Classical pairwise gossip admits sharper bounds for sequences in which every call immediately conveys new information.

## Proof

For any tuple of view sets
\[
\mathcal V=(V_a)_{a\in A},
\]
a resolution by \(B\) replaces the view of every participant by the union of the participants' current views and leaves every nonparticipant unchanged:
\[
(\mathsf U_B\mathcal V)_a=
\begin{cases}
\displaystyle\bigcup_{b\in B}V_b,&a\in B,\\[2mm]
V_a,&a\notin B.
\end{cases}
\]
Indeed, for \(a\in B\),
\[
\operatorname{see}_a(\vec G.B)
=
\operatorname{see}_{\{a\}\cup B}(\vec G)
=
\operatorname{see}_B(\vec G)
=
\bigcup_{b\in B}\operatorname{see}_b(\vec G).
\]

The update maps \(\mathsf U_B\) preserve arbitrary componentwise unions. Therefore a suffix \(\vec S\) acts linearly over set union. If
\[
Q_a=\operatorname{see}_a(\vec S)
\]
is computed from the initial singleton views, then for every input view tuple \(\mathcal V\),
\[
(\mathsf U_{\vec S}\mathcal V)_a
=
\bigcup_{q\in Q_a}V_q.
\]
This follows by induction on the length of \(\vec S\).

Apply this to the prefix view tuple
\[
\mathcal V=(V_a(\vec P))_{a\in A}.
\]
If the occurrence \(B\) is deleted, then the suffix produces
\[
V_a(\vec P.\vec S)
=
\bigcup_{q\in Q_a}V_q
=
F_a.
\]

If \(B\) is retained, then just before the suffix each row indexed by \(B\) has become
\[
U_B=\bigcup_{b\in B}V_b.
\]
Thus the suffix output at \(a\) is
\[
\bigcup_{q\in Q_a}
\begin{cases}
U_B,&q\in B,\\
V_q,&q\notin B.
\end{cases}
\]
If \(Q_a\cap B=\varnothing\), this is \(F_a\). Otherwise it is
\[
F_a\cup U_B.
\]
This proves the exact forward-backward formula and the view-equality criterion.

For accessibility relations, the source's semantics gives
\[
{\sim}^{\vec G}_a
=
\bigcap_{c\in V_a(\vec G)}{\sim}_c.
\]
Equal final views therefore imply equal final current relations in every model.

Conversely, suppose some final view changes. The view with \(B\) retained contains the view without \(B\), so choose an index
\[
c\in
V_a(\vec P.B.\vec S)\setminus V_a(\vec P.\vec S).
\]
Take
\[
W=\{0,1\}^{A}
\]
and let the base relation \({\sim}_d\) identify two worlds exactly when they agree in coordinate \(d\). For each \(C\subseteq A\),
\[
\bigcap_{d\in C}{\sim}_d
\]
is equality on the coordinates in \(C\). Distinct index sets therefore induce distinct intersection relations. Hence the two histories give different current accessibility relations for agent \(a\) in this model. The criterion is thus also necessary for model-independent relation redundancy.

For the immediate case \(\vec S=\varepsilon\),
\[
Q_a=\{a\}.
\]
Only participants matter, and the criterion becomes
\[
U_B\subseteq V_a
\qquad(a\in B).
\]
Since always \(V_a\subseteq U_B\), this is equivalent to
\[
V_a=U_B
\qquad(a\in B),
\]
which is equivalent to all participant views being equal. After one resolution by \(B\), all those views are equal to the same union, so repeating \(B\) immediately is relation-redundant.

For the compression bound, scan a history from left to right and delete every event that is immediately relation-redundant at the current view state. Such a deletion leaves the entire view tuple unchanged, so it cannot affect any later view update. Every retained event strictly enlarges at least one view. The integer potential
\[
\Phi=\sum_{a\in A}|V_a|
\]
starts at \(n\) and never exceeds \(n^2\). Therefore at most
\[
n^2-n=n(n-1)
\]
events are retained.

## Verification

The bundled checker independently implements the published view recursion and the forward-backward formula.

For every agent-set size \(1\le n\le4\), it exhaustively checks all choices of nonempty resolution group \(B\), all prefixes of length at most two, and all suffixes of length at most two. It verifies that the criterion
\[
Q_a\cap B=\varnothing
\quad\text{or}\quad
U_B\subseteq F_a
\]
holds exactly when deleting \(B\) leaves the final view tuple unchanged.

It also checks the immediate criterion directly, verifies that every immediate repetition is redundant, and constructs the coordinate-equality epistemic model used in the necessity proof to confirm that distinct view index sets induce distinct intersection relations.

The finite enumeration is a consistency check only. The theorem for arbitrary finite agent sets and arbitrary finite histories follows from the union-linear suffix argument.

## Relationship to prior work

Balbiani, van Ditmarsch, and Lerouvillois introduce the asynchronous resolution history semantics and prove the view facts used here. They explicitly note that equal views do not imply equality under the history-indistinguishability relation; in particular, repeating a resolution can leave an agent's view unchanged while still producing a distinguishable history. In their conclusion they ask whether one can determine when a resolution in a sequence is redundant because it is uninformative, giving immediate repetition as the motivating example.

The present result answers the **current-relation** version of that question for an arbitrary occurrence, not merely for a final event. The suffix is summarized by its contributor views \(Q_a\), yielding an exact forward-backward deletion test.

There is a substantial older literature on gossip protocols. In pairwise ordinary gossip, a call is commonly called redundant when neither participant learns a new secret, and sharp bounds are known for irredundant call sequences. Other work studies epistemically redundant calls and stuttering principles in pairwise gossip logics. Those results motivate the terminology but do not give the above arbitrary-group prefix/suffix criterion for the 2026 asynchronous resolution semantics.

## Limitations

Relation redundancy is weaker than full history-semantic redundancy. The source's relation \(\approx_a\) remembers aspects of event occurrence that the current view forgets, so formulas with nested distributed-knowledge structure may distinguish histories that induce identical current relations.

The compression bound \(n(n-1)\) is not asserted to be sharp. In the special pairwise gossip setting, sharper extremal bounds are known.

The theorem concerns deletion of one occurrence relative to the final current relation state. If one successively deletes several events, the redundancy test should be recomputed after each deletion because the relevant prefix and suffix contributor sets can change.

## References

[1] Philippe Balbiani, Hans van Ditmarsch, and Clara Lerouvillois, “Resolving Asynchronous Distributed Knowledge,” *Electronic Proceedings in Theoretical Computer Science* 447 (2026), 75–92. arXiv:2606.31855. DOI:10.4204/EPTCS.447.5.

[2] Andries E. Brouwer, Jan Draisma, and Bart J. Frenk, “Lossy Gossip and Composition of Metrics,” *Discrete & Computational Geometry* 53 (2015), 890–913. DOI:10.1007/s00454-015-9666-1.

[3] Hans van Ditmarsch, Ioannis Kokkinis, and Anders Stockmarr, “Reachability and Expectation in Gossiping,” in *Multi-Agent Systems and Agreement Technologies*, LNCS 10767 (2017), 93–109. DOI:10.1007/978-3-319-69131-2_6.
