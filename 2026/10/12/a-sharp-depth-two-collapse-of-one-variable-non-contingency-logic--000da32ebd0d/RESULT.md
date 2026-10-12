# A sharp depth-two collapse of one-variable non-contingency logic on irreflexive cliques

## Finding
Fix an integer \(n\geq 1\) and the irreflexive complete Kripke frame \(K_n^\circ=(W,R)\), where \(|W|=n\) and \(wRv\) exactly when \(w\ne v\). Consider the language with one propositional variable \(p\), arbitrary Boolean connectives, and the non-contingency operator \(\Delta\). Two formulas are equivalent when they have the same truth value at **every pointed valuation on this fixed frame**. Their exact equivalence-class counts, indexed by the largest nesting depth of \(\Delta\), are

| Frame size | Depth zero | Depth one | Every depth at least two |
| --- | ---: | ---: | ---: |
| \(n=1\) or \(n=2\) | 4 | 4 | 4 |
| \(n=3\) | 4 | 16 | 16 |
| \(n\geq4\) | 4 | 16 | 64 |

Thus every single-variable formula has a depth-at-most-two equivalent on \(K_n^\circ\) for every \(n\geq4\), with **the same translation also valid simultaneously for all such frame sizes**. Depth two is optimal: exactly sixteen equivalence classes have representatives of depth at most one, whereas sixty-four have depth-at-most-two representatives.

The six depth-two equivalence types arise from the truth of \(p\) at the pointed world and three states of the multiset of truth values at its other worlds: an extreme count, a distinguished single exceptional neighbor, or a genuinely mixed interior count. In particular \(\Box p\), interpreted over the same irreflexive accessibility, is not definable by this language on any \(K_n^\circ\) with \(n\geq2\).

## Assumptions and scope
Let a valuation be \(V\subseteq W\); write \(\mathfrak M=(K_n^\circ,V)\). For each formula \(\varphi\),
\[
\mathfrak M,w\models \Delta\varphi\quad\Longleftrightarrow\quad
\left(\forall v\ne w\;\mathfrak M,v\models\varphi\right)
\;\lor\;
\left(\forall v\ne w\;\mathfrak M,v\not\models\varphi\right).
\]
Both universal statements are true for an empty successor set; hence \(\Delta\varphi\) is true there. Boolean constants can be formed from \(p\) and its negation if not explicitly included. The modal depth of \(\Delta\varphi\) is one more than the depth of \(\varphi\). Equivalence is considered first for each fixed \(n\); the uniformity statement concerns the family of all \(n\geq4\), and **not** arbitrary graph frames, multiple propositional variables, or reflexive complete graphs.

For a pointed valuation \((V,w)\), put
\[
a=\mathbf 1_{w\in V}\in\{0,1\},\qquad b=|V\setminus\{w\}|\in\{0,\ldots,n-1\}.
\]
When \(n\geq4\), define the following six nonempty classes of pointed valuations:
\[
\begin{array}{ll}
E_0:\ a=0,\ b\in\{0,n-1\},& E_1:\ a=1,\ b\in\{0,n-1\};\\
S_0:\ a=0,\ b=1,&S_1:\ a=1,\ b=n-2;\\
M_0:\ a=0,\ 2\leq b\leq n-2,&M_1:\ a=1,\ 1\leq b\leq n-3.
\end{array}
\]
For \(n=3\), delete the empty \(M\)-classes; for \(n\leq2\), only the truth of \(p\) at \(w\) remains distinguishable.

## Proof
**1. Explicit separation.** Write
\[
\alpha=\neg\Delta(p\wedge\Delta p),\qquad
\beta=\neg\Delta(\neg p\wedge\Delta p).
\]
On \(K_n^\circ\) for \(n\geq4\), \(\Delta p\) is true precisely when \(b\in\{0,n-1\}\). An inspection of the exceptional neighbor shows that \(\alpha\) is true precisely on \(S_0\): if \(a=0,b=1\), the unique neighbor satisfying \(p\) has all other neighbors falsifying \(p\), so it satisfies \(p\wedge\Delta p\), while the remaining neighbors do not. Outside this case \(p\wedge\Delta p\) has constant truth on all successors. By exchanging \(p\) and \(\neg p\), \(\beta\) is true precisely on \(S_1\). The four formulas \(p,\Delta p,\alpha,\beta\), all of modal depth at most two, therefore distinguish the six listed classes. Each class has a depth-at-most-two characteristic formula formed from these four formulas using Boolean connectives. Consequently **every union of classes** is definable at depth at most two, giving at least \(2^6=64\) distinct equivalence classes.

**2. Closure under arbitrary nesting.** Fix a formula \(\varphi\) whose truth is constant on the six classes. The successor classes visible from each pointed valuation are as follows:

| Class of pointed valuation | Successor classes present |
| --- | --- |
| \(E_0\) or \(E_1\) | A single class (which can vary with the extreme valuation) |
| \(S_0\) | Both \(E_1\) and \(S_0\) |
| \(S_1\) | Both \(S_1\) and \(E_0\) |
| \(M_0\) or \(M_1\) | Both \(M_0\) and \(M_1\) |

These statements follow by pointing at a different world, replacing \(a\) by the neighbor's truth value and updating \(b\) accordingly. Both classes listed in each two-class row occur, by the defining inequalities on \(b\). It follows immediately that \(\Delta\varphi\) is true on every \(E\)-class; on \(S_0\) iff \(\varphi(E_1)=\varphi(S_0)\); on \(S_1\) iff \(\varphi(S_1)=\varphi(E_0)\); and on both \(M\)-classes iff \(\varphi(M_0)=\varphi(M_1)\). In particular \(\Delta\varphi\) is itself constant on each of the six classes. Induction on formula complexity, using Boolean closure, proves that **no formula of any depth** can separate two pointed valuations belonging to the same class. Hence the exact total is at most sixty-four, attaining the lower bound in Step 1. Because the successor-class table is independent of \(n\geq4\), the same depth-two representatives work uniformly across those frame sizes.

**3. Boundary sizes and sharpness.** For \(n=3\), \(E_0,E_1,S_0,S_1\) remain and \(M_0,M_1\) are empty. The same closure argument, with the final table row deleted, gives at most sixteen classes, and the pair \(p,\Delta p\) separates all four classes, giving exactly sixteen even at depth one. For \(n=1,2\), every world has at most one successor, so \(\Delta\varphi\) is always true; a formula reduces to a Boolean formula in \(p\), giving exactly four classes. For \(n\geq3\), the two truth values of \(p\) together with the two truth values of \(\Delta p\) give precisely four distinguishable depth-one types and all sixteen Boolean unions. At modal depth zero there are only four Boolean functions of \(p\). Therefore the displayed depth counts are exact and depth two is genuinely needed once \(n\geq4\).

**4. A boundary on expressivity.** At any fixed \(n\geq2\), take two pointed valuations with the same \(a\) but with \(b=0\) and \(b=n-1\), respectively. The closure partition puts them in the same \(E_a\)-class, yet \(\Box p\) is false at the first and true at the second. Thus no formula of the one-variable Boolean-\(\Delta\) language defines \(\Box p\) on this frame. This is a corollary of the classification, not a claim about arbitrary frames.

## Verification
The included standalone, deterministic Python program `check_normal_form.py` computes truth values on every valuation and every distinguished world of \(K_n^\circ\) for \(1\leq n\leq9\). It forms all Boolean unions of current modal-depth types, applies the actual neighborhood semantics of \(\Delta\), and refines the depth partition; it independently checks the predicted six-class signatures, verifies modal closure of **all** \(2^k\) type unions, and tests the failure of definability of \(\Box p\) at each permitted finite size. The recorded output `CHECK_OUTPUT.txt` ends in `VERIFY_OK`. To reproduce, run `python3 check_normal_form.py` with Python 3.8 or later. This finite check corroborates but **does not replace** the arbitrary-size inductive proof above.

## Relationship to prior work
Wang and Zenger (2026) introduce a uniform proof-theoretic treatment of non-contingency logic over classes specified by generalized path conditions. Fan (2018) studies non-contingency through neighborhood semantics, associated bisimulations, frame definability, and axiomatization. Ding and Yang (2026) give general bundled-modality expressivity and Hennessy–Milner results that include the non-contingency operator. Those general semantics and invariance perspectives motivate, but do not by themselves state, the present **explicit finite six-type quotient, the exact sixty-four-formula count, or its sharp modal-depth bound on the irreflexive complete frames**. The result should be read as a specialized quantitative refinement, not a challenge to the more general prior bisimulation or proof-theory results.

## Limitations
The conclusion concerns one variable, complete **irreflexive** finite frames and Boolean non-contingency formulas; it is not asserted for multiple variables, arbitrary frames, or all modal bundles. A full-text copy of the recent Wang–Zenger preprint could not be examined; its public title, date, authors and abstract were checked, and its potential overlap remains a literature risk despite its different stated emphasis. Literature indexing under terms such as “knowing whether,” “contingency,” or “Boolean modal clone” could conceal an equivalent exact finite normal form. No independent review has been performed. Finite checker runs alone cannot establish claims for all \(n\).

## References
1. Yunsong Wang and Lukas Zenger, *Proof Theory for Non-Contingency Logic*, arXiv:2609.38975, first public September 30, 2026. https://arxiv.org/abs/2609.38975
2. Jie Fan, *Neighborhood Contingency Logic: A New Perspective*, Studies in Logic 11(4) (2018), 37–55; arXiv:1802.02291. https://arxiv.org/abs/1802.02291
3. Yifeng Ding and Yuanzhe Yang, *A General Theory of Propositional Modal Bundled Modalities*, arXiv:2603.26268; EPTCS 447 (2026), doi:10.4204/EPTCS.447.17. https://arxiv.org/abs/2603.26268
