# A sharp two-world boundary for unary modal positivity

## Finding

Let \(F=(W,R)\) be a Kripke frame with exactly two worlds \(W=\{0,1\}\). A **unary modal term operation** is the map \(f_\varphi:\mathcal P(W)\to\mathcal P(W)\) induced by a formula \(\varphi(p)\) in the basic classical modal language with Boolean connectives and \(\Box,\Diamond\). It is **positive** when it is represented by a formula using only \(p,\bot,\top,\wedge,\vee,\Box,\Diamond\); it is **monotone** when \(A\subseteq B\) entails \(f_\varphi(A)\subseteq f_\varphi(B)\). Write \(P_R\) for the set of positive unary term operations and \(M_R\) for the set of monotone unary term operations (represented by unrestricted unary modal formulas).

**Classification.** Every monotone unary modal term operation on \(F\) is positive, \(M_R=P_R\), exactly when
\[
\neg\bigl(0R1\ \wedge\ 1R0\ \wedge\ (0R0\ \vee\ 1R1)\bigr).
\]
Thus exactly three of the sixteen labeled two-world frames fail unary positivity, in two isomorphism classes: the full two-world cluster and the two-way edge with precisely one reflexive loop. Every one-world frame has \(M_R=P_R\), so two worlds is the least cardinality of a failing frame.

More precisely, label a relation by \(m=\sum_{i,j\in\{0,1\}}2^{2i+j}\mathbf 1[iRj]\) and write its two rows as subset bit masks \(r_0,r_1\in\{0,1,2,3\}\). Let \(T_R\) denote all unary modal term operations. For the ten isomorphism types, the **complete** finite-algebra census is:

| Representative \(m\) | Rows \((r_0,r_1)\) | \(|P_R|\) | \(|T_R|\) | \(|M_R|\) | \(|M_R\setminus P_R|\) |
| ---: | :---: | ---: | ---: | ---: | ---: |
| 0 | (0, 0) | 3 | 4 | 3 | 0 |
| 1 | (1, 0) | 9 | 16 | 9 | 0 |
| 2 | (2, 0) | 18 | 64 | 18 | 0 |
| 3 | (3, 0) | 18 | 64 | 18 | 0 |
| 5 | (1, 1) | 6 | 16 | 6 | 0 |
| 6 | (2, 1) | 6 | 16 | 6 | 0 |
| 7 | (3, 1) | 10 | 64 | 18 | 8 |
| 9 | (1, 2) | 3 | 4 | 3 | 0 |
| 11 | (3, 2) | 6 | 16 | 6 | 0 |
| 15 | (3, 3) | 5 | 16 | 6 | 1 |

Here rows use the bit convention \(0\mapsto\varnothing\), \(1\mapsto\{0\}\), \(2\mapsto\{1\}\), \(3\mapsto W\). The three failing labeled relation masks are \(7,14,15\).

## Assumptions and scope

The language has **one propositional variable and no fixed additional parameter variables**. Formula equivalence, monotonicity, and positive representability are all evaluated uniformly over valuations on the **fixed frame** \(F\) (not over all frames of a modal logic, nor over all vocabulary sizes). A formula using negation or implication may still represent a positive term operation; the predicate is semantic, not a restriction on its original syntax. Both modal operators use ordinary Kripke semantics; no seriality, transitivity, or reflexivity is assumed of \(R\).

## Proof

**1. Finite normal form for all modal terms.** Encode any subset \(A\subseteq W\) by its two-bit mask \(a\in\{0,1,2,3\}\). Encode a unary operation by the four-tuple
\[
\widehat f=(f(\varnothing), f(\{0\}),f(\{1\}),f(W))\in\{0,1,2,3\}^{4}.
\]
There are exactly \(4^4=256\) possible such tuples. For row masks \(r_i\) define the modal set transforms
\[
D_R(a)=\{i:r_i\cap a\ne\varnothing\},\qquad
B_R(a)=\{i:r_i\subseteq a\},
\]
with sets identified with their masks. For operations \(f,g\), the interpretations of the connectives are pointwise intersection and union, and pointwise complement \(W\setminus f(a)\); modal application is composition \(D_R\circ f\) or \(B_R\circ f\).

Starting from the constant operations \(\varnothing,W\) and identity \(a\mapsto a\), close under these operations. Omitting complement gives exactly \(P_R\); including complement gives exactly \(T_R\). The forward inclusion follows by structural induction on formulas. Conversely, every closure step is witnessed by applying its connective to already represented formulas, so the least fixed point contains no spurious operations. Since there are only 256 possible tuples, the closure **terminates exactly**, irrespective of formula depth. This is a complete decision procedure rather than a bounded formula-length experiment.

**2. Monotone filter and exhaustive partition.** For each \(f\in T_R\), monotonicity reduces to the four inclusion tests
\[
f(\varnothing)\subseteq f(\{0\}),\quad f(\varnothing)\subseteq f(\{1\}),\quad
f(\{0\})\subseteq f(W),\quad f(\{1\})\subseteq f(W).
\]
For every \(m\in\{0,\ldots,15\}\), both least fixed points and this exact filter are computed by the accompanying two independent verification programs. Their exhaustive 16-frame results identify exactly the failures \(m\in\{7,14,15\}\). Exchanging the names of the two worlds partitions the 16 labeled relations into the ten isomorphism classes displayed above and preserves all counts. Therefore the displayed Boolean criterion is necessary and sufficient for all two-world relations.

**3. Explicit strictness in both failing types.** For both representatives \(m=7\), having rows \((3,1)\), and \(m=15\), having rows \((3,3)\), consider
\[
\chi(p)=\Diamond p\wedge(\Box p\vee\neg p).
\]
On either frame its operation maps \(\varnothing\mapsto\varnothing\), \(\{0\}\mapsto\{1\}\), \(\{1\}\mapsto\{0\}\), and \(W\mapsto W\). This is monotone on the four-element subset lattice.

To see directly that this operation is **not** positive, let model \(A\) interpret \(p\) as \(\{1\}\) and model \(B\) interpret \(p\) as \(\{0\}\), both on the same frame. The relation
\[
Z=\{(0,0),(0,1),(1,0)\}\subseteq W_A\times W_B
\]
preserves truth of the atom \(p\) in the forward direction and has the forth-and-back clauses for \(R\) at all three related pairs, for both \(m=7\) and \(m=15\). Therefore induction over the positive syntax shows \(A,x\models\psi\) and \(xZy\) imply \(B,y\models\psi\) for every positive formula \(\psi\). But \(A,0\models\chi\), \(0Z0\), and \(B,0\not\models\chi\). Consequently no positive formula agrees with \(\chi\) on either frame. The other bad labeled case \(m=14\) is isomorphic to \(m=7\).

**4. Minimality.** When \(|W|=1\), each of the two possible accessibility relations has three positive unary term operations, and the monotone subset of the four unrestricted unary term operations also has three. The same finite-algebra argument establishes equality on both one-world frames.

## Verification

Run `python3 check_unary.py` and `python3 check_unary_independent.py`. The first program constructs tuple-valued term operations by a worklist closure, verifies monotonicity, all sixteen row patterns, the stated simulations and the failure formula, and checks one-world minimality. The second independently represents the same functions by eight-bit truth tables, recomputes both full fixed points using a different saturation algorithm, and checks the entire sixteen-frame table. Both programs were executed successfully on the packaged source before the scientific assessment.

The exhaustive check covers **all formula interpretations** because closure under the grammar reaches an actual fixed point inside the complete 256-function universe. It does not establish an analogous result for more than two worlds or more than one free variable.

## Relationship to prior work

Dvorkin's *Monotonicity versus positivity in modal logics* (2026), Proposition 4.8, already proves failure of unary positivity on the **complete two-point cluster** and gives a simple monotone nonpositive formula there; that special case is not claimed as new. Dvorkin's *On Interpretations of Normal Modal Logics* (2026), Example 2.4, repeats this cluster obstruction and identifies its operation as completely additive, while chiefly classifying additive terms for selected modal logics. Proposition 4.16 proves positivity for the reflexive two-world frame of type \(D_1\), another covered case. The result here is the **complete sixteen-relation boundary and ten-type exact operation census**, including the previously unclassified bidirectional **one-loop nontransitive** frame. Dvorkin's general preservation framework motivates the positive-simulation argument but does not supply the displayed complete two-world table. Searches for equivalent two-world classifications, modal unary clones, and finite positive term spectra identified no directly dominating published classification; this is not a proof of historical uniqueness.

## Limitations

Only a single propositional variable without parameters is considered. The full two-point cluster failure and the \(D_1\) positivity case are known from the cited primary paper. The new result is an exact finite classification with a machine-replayable complete closure certificate; it does not generalize positivity to higher-world frames. No claim is made that no unindexed equivalent classification exists. The computer programs provide reproducibility but not independent mathematical peer review.

## References

1. Lev Dvorkin, *Monotonicity versus positivity in modal logics*, arXiv:2602.02837 (first submitted 2 February 2026), especially Section 4.3, Propositions 4.8 and 4.16, and the finite-frame preservation discussion in Proposition 4.12. https://arxiv.org/abs/2602.02837
2. Lev Dvorkin, *On Interpretations of Normal Modal Logics*, Electronic Proceedings in Theoretical Computer Science **447** (2026), 321–340, arXiv:2606.31871, especially Example 2.4. https://arxiv.org/abs/2606.31871
3. Patrick Blackburn, Maarten de Rijke, Yde Venema, *Modal Logic*, Cambridge University Press (2001), for standard Kripke-frame semantics.
