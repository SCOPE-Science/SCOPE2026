# Block weaving does not imply atomwise weaving for local fusion-frame systems

## Finding
Bhandari's Theorem 3.1 in *A note on weaving fusion frames* asserts an equivalence between weaving of two fusion frames and ordinary weaving of the two flattened families of weighted local frame vectors. The forward implication is false.

A counterexample exists with a single fusion block. Let \(\mathcal H=\mathbb R^2\), let \(I=\{{1}\}\), take
\[
V_1=W_1=\mathcal H,\qquad v_1=w_1=1,
\]
and choose local orthonormal bases
\[
(f_{{11}},f_{{12}})=(e_1,e_2),\qquad (g_{{11}},g_{{12}})=(e_2,e_1).
\]
The fusion-frame pair is weaving, but the flattened ordinary frames \((e_1,e_2)\) and \((e_2,e_1)\) are not woven. Consequently fusion weaving is strictly weaker than atomwise weaving of arbitrary chosen local frames.

The converse direction survives: atomwise weaving of the flattened local systems implies weaving of the fusion frames. The exact correct local characterization is blockwise weaving, in which an outer choice of a fusion block selects all local atoms from that block together. This blockwise formulation is already present in Neyshaburi--Arefijamaal, Lemma 2.2.

## Assumptions and scope
For a countable outer index set \(I\), suppose \(\{{(V_i,v_i)}\}}_{{i\in I}}\) and \(\{{(W_i,w_i)}\}}_{{i\in I}}\) are weighted closed-subspace systems in a Hilbert space, and for each \(i\) let \(\{{f_{{ij}}}\}}_{{j\in J_i}}\) and \(\{{g_{{ij}}}\}}_{{j\in J_i}}\) be local frames for \(V_i\) and \(W_i\). Assume the local lower bounds are uniformly positive and local upper bounds uniformly finite, as in the source theorem.

Fusion weaving quantifies over subsets \(\sigma\subseteq I\): choosing \(i\in\sigma\) selects the whole fusion block \((V_i,v_i)\), while choosing \(i\notin\sigma\) selects the whole block \((W_i,w_i)\). Ordinary weaving of the flattened local frames instead quantifies over arbitrary subsets of the atomic index set
\[
K=\{{(i,j):i\in I,\ j\in J_i}\}.
\]
Those are different quantifiers unless additional hypotheses force atom-level choices to behave like block-level choices.

## Proof
For the counterexample, the only outer subsets are \(\varnothing\) and \(\{{1}\}\). Either choice produces the one-element fusion family \(\{{(\mathbb R^2,1)}\}\), for which
\[
\|P_{{\mathbb R^2}}x\|^2=\|x\|^2.
\]
Hence both fusion weavings have exact lower and upper bounds \(1\).

Each local family is an orthonormal basis, so every local frame bound in the hypotheses equals \(1\). The flattened ordinary frames are
\[
F=(e_1,e_2),\qquad G=(e_2,e_1).
\]
Ordinary weaving allows an arbitrary atomic subset of \(\{{1,2}\}\). Select the first coordinate from \(F\) and the second coordinate from \(G\). The resulting weaving is
\[
(e_1,e_1).
\]
For \(x=e_2\), its frame energy is \(0\), so it is not a frame for \(\mathbb R^2\). Thus fusion weaving does not imply atomwise weaving of the flattened local frames.

For the surviving converse, suppose the two flattened systems are woven with universal ordinary-frame bounds \(L>0\) and \(U<\infty\). Let the local frame bounds satisfy
\[
a\le A_i,C_i\quad\text{{and}}\quad B_i,D_i\le b
\]
for all \(i\), with \(a>0\) and \(b<\infty\). For an outer subset \(\sigma\subseteq I\), use the atomic subset
\[
\tau_\sigma=\{{(i,j)\in K:i\in\sigma\}}.
\]
The corresponding ordinary weaving is a frame, and its energy \(Q_\sigma(x)\) satisfies
\[
L\|x\|^2\le Q_\sigma(x)\le U\|x\|^2.
\]
If
\[
E_\sigma(x)=\sum_{{i\in\sigma}}v_i^2\|P_{{V_i}}x\|^2+\sum_{{i\notin\sigma}}w_i^2\|P_{{W_i}}x\|^2,
\]
then the local frame inequalities give
\[
aE_\sigma(x)\le Q_\sigma(x)\le bE_\sigma(x).
\]
Therefore
\[
\frac{{L}}{{b}}\|x\|^2\le E_\sigma(x)\le\frac{{U}}{{a}}\|x\|^2
\]
uniformly in \(\sigma\). Hence atomwise weaving of the flattened local systems implies fusion weaving.

## Verification
The counterexample is exact and requires no numerical approximation. All hypotheses of the source theorem are met: there is a common local index set \(J_1=\{{1,2}\}\), positive unit weights, closed subspaces equal to the ambient Hilbert space, and local frame bounds all equal to \(1\). The failed atomic weaving is exhibited explicitly and annihilates \(e_2\).

The quantifier mismatch was checked against the full statement and proof of Bhandari's Theorem 3.1. In the published proof of the forward direction, the displayed estimates are made only for \(\sigma\subseteq I\), so all local atoms belonging to a chosen outer block move together. Ordinary weaving, however, requires the estimate for every atomic subset of the common flattened index set.

The reverse implication was reconstructed independently from the definitions and uniform local bounds, as shown above.

## Relationship to prior work
Bemrose--Casazza--Gröchenig--Lammers--Lynch define ordinary weaving by requiring a frame for every subset of the common vector index set. Bhandari's Theorem 3.1 states that weaving of fusion frames is equivalent to ordinary weaving of the two flattened local systems, but its forward proof only treats block-constant atomic choices.

Earlier, Neyshaburi--Arefijamaal, Lemma 2.2, gave the appropriate local-frame characterization of weaving fusion frames: for every partition of the outer fusion index set, one takes the union of the entire corresponding local-frame blocks. That result is a blockwise statement and does not imply atomwise weaving of two globally flattened local frames.

Thus the new point is not a new blockwise characterization. It is the explicit failure of the stronger atomwise equivalence asserted in the 2024/2025 source, together with the exact one-way correction: atomwise local weaving implies fusion weaving, but not conversely.

## Limitations
The counterexample concerns Theorem 3.1 as stated and does not invalidate results that use only blockwise local-frame selection. It also does not classify additional hypotheses under which fusion weaving might force atomwise weaving. No claim is made that the earlier blockwise equivalence is new. If condition (2) was intended to use a nonstandard block-constant meaning of “weaving frames,” then the displayed proof matches that blockwise interpretation, but this is not the ordinary atomwise weaving definition cited in the same literature.

## References
1. A. Bhandari, *A note on weaving fusion frames*, arXiv:2409.01288; New York J. Math. 31 (2025), 54--65. First public version: 2024-09-02.
2. F. Arabyani Neyshaburi and A. A. Arefijamaal, *Weaving Hilbert space fusion frames*, arXiv:1802.03352, 2018.
3. T. Bemrose, P. G. Casazza, K. Gröchenig, M. C. Lammers, and R. G. Lynch, *Weaving frames*, Operators and Matrices 10 (2016), 1093--1116, doi:10.7153/oam-10-61.
