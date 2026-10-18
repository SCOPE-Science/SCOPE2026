# Sharp syntactic arity collapse for positive instantial logic on finite-width orders

## Finding

**Theorem (uniform syntactic elimination and sharpness on each ordered carrier).** Let \(P=(W,\leq)\) be any nonempty partial order of **finite width** \(w\geq1\); the set of worlds \(W\) may be infinite. In the negation- and implication-free positive instantial neighbourhood language with both independent witness \(\Box\) and co-witness \(\Diamond\) modalities, every formula is uniformly equivalent, over all persistent two-sided neighbourhood models based on \(P\), to a formula whose modal instance lists have length at most \(w\). The equivalence holds at every world for every persistent valuation and preserves modal nesting depth.

The translation is constructive, depends only on the integer \(w\), and does not refer to the neighbourhood families or the chosen valuation. Moreover, **this bound is sharp on every fixed such carrier**: for each \(P\), including infinite carriers of finite width, there are two persistent models on the same \(P\) indistinguishable by all formulas of instance arity less than \(w\), at arbitrary nesting depth, but distinguished by one depth-one co-witness formula of instance arity \(w\).

Here are exact elimination identities. For \(n>w\), let \(\Pi_w(n)\) be the finite set of partitions \(\pi\) of \(\{1,\ldots,n\}\) into between one and \(w\) nonempty blocks. For a block \(C\), set
\[
\mu_C=\bigwedge_{i\in C}\alpha_i,\qquad
\nu_C=\bigvee_{i\in C}\alpha_i.
\]
Write \(\pi=\{C_1,\ldots,C_r\}\), in any fixed canonical block order. Then, at every world of every model as above,
\[
\boxed{
\Box(\alpha_1,\ldots,\alpha_n;\psi)
\ \equiv\
\bigvee_{\pi\in\Pi_w(n)}
\Box(\mu_{C_1},\ldots,\mu_{C_r};\psi)
}
\]
and
\[
\boxed{
\Diamond(\alpha_1,\ldots,\alpha_n;\psi)
\ \equiv\
\bigwedge_{\pi\in\Pi_w(n)}
\Diamond(\nu_{C_1},\ldots,\nu_{C_r};\psi).
}
\]
The two dual partition operators (joins for the witness disjunction, meets for the co-witness conjunction) are essential. The displayed equivalence sign is semantic metanotation, not a new connective of the object language.

## Assumptions and scope

For a partial order \(P\), an upset \(A\subseteq W\) satisfies \(a\in A\land a\leq b\Rightarrow b\in A\). A persistent two-sided frame assigns to each world \(s\) two families \(N^\Box(s),N^\Diamond(s)\subseteq\operatorname{Up}(P)\) satisfying \(s\leq t\Rightarrow N^\Box(s)\subseteq N^\Box(t)\) and \(N^\Diamond(t)\subseteq N^\Diamond(s)\). Propositional valuations are arbitrary upsets. No requirement of nonempty neighbourhoods, supplementation, seriality, or closure under intersections is made.

For arbitrary **upset** arguments \(A_1,\ldots,A_n,B\), define the witness operation at \(s\) by
\[
f_n(A_1,\ldots,A_n;B)(s)=1
\iff \exists U\in N^\Box(s)\,[U\subseteq B\ \land\ \forall i\ (U\cap A_i\ne\varnothing)].
\]
The independent co-witness operation is
\[
g_n(A_1,\ldots,A_n;B)(s)=1
\iff\forall U\in N^\Diamond(s)\,[U\cap B\ne\varnothing\ \lor\ \exists i\ (U\subseteq A_i)].
\]
For zero instances, the existential disjunction in \(g_0\) is false. These are the **untyped** persistent semantics of Das, Khanra, and Sardar. The width is the largest cardinality of an antichain; a finite width is attained by some finite antichain. Truth sets of all formulas are upsets under persistence.

The result is not a general claim about arbitrary infinite-width frames, full classical INL with negation, typed labelled canonical models, other algebraic languages, or formula-size complexity. Only the maximal **number of modal instance arguments** is bounded. The separate scope argument is not counted.

## Proof

**Lemma 1 (finite-sample antichain compression).** Given finitely many points \(x_1,\ldots,x_n\) of a width-\(w\) poset, choose all maximal elements among these points. There are at most \(w\), and every sampled point lies below one chosen maximal point. Likewise the minimal points among the sample number at most \(w\), and every sampled point lies above one of them. No finiteness hypothesis on the whole poset is needed.

**Lemma 2 (witness partition identity).** Fix a world \(s\) and a neighbourhood \(U\in N^\Box(s)\). Suppose \(U\subseteq B\) and \(U\cap A_i\ne\varnothing\) for all \(i=1,\ldots,n\). For every \(i\), choose \(x_i\in U\cap A_i\). By Lemma 1, there are at most \(w\) distinct maximal sampled points \(y_1,\ldots,y_r\), and we can assign each index \(i\) to one \(y_j\) above \(x_i\). This assignment gives a partition \(\pi\). Each \(y_j\in U\), since it is one of the chosen points, and \(y_j\in A_i\) for every index in its assigned block, since each \(A_i\) is upward closed. Therefore \(U\) witnesses \(\Box(\bigwedge_{i\in C_1}A_i,\ldots,\bigwedge_{i\in C_r}A_i;B)\). Conversely, any neighbourhood witnessing the grouped version intersects every original \(A_i\), because each block meet is a subset of its factors. Taking disjunction over all partitions proves the first displayed identity for \(n>w\). It also holds trivially for \(n\leq w\) if no rewriting is performed.

**Lemma 3 (co-witness partition identity).** A diamond formula fails at \(s\) if and only if there is \(U\in N^\Diamond(s)\) with \(U\cap B=\varnothing\) and \(U\not\subseteq A_i\) for every \(i\). From such a counter-neighbourhood, pick \(x_i\in U\setminus A_i\). Choose the at-most-\(w\) **minimal** sampled elements \(z_1,\ldots,z_r\), assigning each \(i\) to one \(z_j\leq x_i\). Since \(A_i\) is an upset, \(x_i\notin A_i\) and \(z_j\leq x_i\) imply \(z_j\notin A_i\). Consequently \(z_j\notin\bigcup_{i\in C_j}A_i\), while \(z_j\in U\), for every block. The same \(U\) refutes the diamond with the block-join instance list, so at least one conjunct on the right-hand side fails. Conversely, if a block-join formula fails, its refuting neighbourhood is outside every block union and hence outside every original \(A_i\). It also misses \(B\). Thus the original diamond fails. This proves the second identity.

**Uniform recursive elimination.** Translate subformulas first, then apply the appropriate identity to every translated modal application whose number of instances exceeds \(w\). Replacements use only finite lattice joins or meets and modal instances of length at most \(w\). Lemmas 2–3 remain valid for the translated subformula truth sets because they are upsets; semantic equivalence survives every context by structural induction. Each replacement introduces no additional modal nesting, so modal depth does not increase. This algorithm is uniform in the width, independent of the frame's neighbourhood functions, and works on infinite carriers.

**Sharpness on each fixed \(P\).** Choose an antichain \(E=\{e_1,\ldots,e_w\}\subseteq W\) of maximum size and put \(S=\uparrow E\). Construct two persistent models with the same valuations and empty box neighbourhood families at every world. At every world let the first diamond family be
\[
\mathcal D^- =\{T\in\operatorname{Up}(P): T\subsetneq S\}
\]
and let the second be \(\mathcal D^+=\mathcal D^-\cup\{S\}\). Both are valid constant (hence downward-persistent) diamond assignments.

Fix any \(k<w\) and arbitrary upset instance sets \(A_1,\ldots,A_k\) and scope \(B\). Since \(\mathcal D^-\subseteq\mathcal D^+\), it suffices to show that any new failure caused by the neighbourhood \(S\) in the plus model was already caused by some \(T\in\mathcal D^-\). If \(S\cap B=\varnothing\) and \(S\not\subseteq A_i\) for all \(i\), choose \(x_i\in S\setminus A_i\) and let \(T=\uparrow\{x_1,\ldots,x_k\}\), with \(T=\varnothing\) when \(k=0\). Then \(T\subseteq S\), \(T\cap B=\varnothing\), and \(T\not\subseteq A_i\) for every \(i\). The set \(T\) is a **proper** upset: if \(e_j\in T\), then some \(x_i\leq e_j\), while \(e_\ell\leq x_i\) for some \(e_\ell\in E\); the antichain property forces \(e_j=e_\ell=x_i\). Thus \(T\) contains at most \(k<w\) of the \(w\) points of \(E\), whereas \(S\) contains them all. It follows that every co-witness operation of arity less than \(w\) agrees in both frames, for **all** upset arguments. All box operations also agree (both are constantly false). By structural induction, every formula with instance arity below \(w\), at arbitrary nesting depth, has identical truth sets in the two models under every shared persistent valuation.

Define the persistent valuation
\[
V(p_j)=S\setminus\{e_j\}\quad(1\leq j\leq w),\qquad V(\bot)=\varnothing.
\]
Because each \(e_j\) is minimal inside \(S\), all these sets are upsets of \(P\). Every proper upset \(T\subsetneq S\) omits at least one \(e_j\) and hence lies in \(V(p_j)\). Therefore
\[
\Delta_w=\Diamond(p_1,\ldots,p_w;\bot)
\]
is true at every world in the minus model. But the added neighbourhood \(S\) does not meet the empty scope and is not a subset of any \(V(p_j)\); it refutes \(\Delta_w\) in the plus model at every world. Hence no formula using fewer than \(w\) instance arguments can be equivalent to \(\Delta_w\) on all persistent models on this **fixed poset**. Sharpness and both claims follow.

## Verification

The self-contained standard-library script `check_pinl_width.py` directly evaluates the set-valued witness and co-witness clauses, the partition translations, and the two sharpness frames. The tested posets include a chain, a fork, a diamond, a disjoint union of chains, four-point antichains, and a six-point crown. For small instances it exhaustively enumerates argument upsets; for larger instances it uses fixed-seed sampling. All of its claims are explicitly finite.

A successful run produced `PINL_WIDTH_VERIFY_OK comparisons=1204834 lower_checks=76857`, including 1,204,834 local identity comparisons and 76,857 lower-arity frame comparisons. It also checked an arity-\(w\) separating valuation on each sample. The infinite-carrier and all-formula conclusions derive from the proved finite-sample and structural-induction arguments, **not** from experimental extrapolation.

## Relationship to prior work

Das, Khanra, and Sardar, *Positive Instantial Neighbourhood logic* (arXiv:2606.08083, first posted 6 June 2026; revised 16 July 2026), introduce precisely this negation-free two-sided persistent semantics and its algebraic operations, and develop typed canonical completeness and an admissible-open representation. Their full accessible manuscript, including Sections 3, 7 and 9, does not state the displayed **partition identities**, a constructive elimination of high-arity formulas, or a sharp bound on **each fixed finite-width order** (including infinite orders).

The published finite Boolean-BAIO cutoff for ordinary instantial neighbourhood frames reconstructs neighbourhood memberships from arguments up to the *number of worlds* and gives a discrete lower-bound example. It does not imply a frame-independent translation into low-arity **positive** terms or establish the two-sided co-witness sharpness for every ordered carrier.

Finite-poset observational-signature analysis also shows that low arities can distinguish semantic neighbourhood signatures, with a uniform width threshold. Determination of high-arity operations by low-arity signatures, however, does not itself yield a **single positive formula** defining each high-arity operation from low-arity operators. The present partition identities give precisely that uniform syntactic reduction, without relying on maximal points of the whole carrier; they therefore work even when the carrier is infinite with no maximal points. Furthermore the previously known discrete sharpness example does not establish **fixed-order sharpness** on an arbitrary poset. Both strengthenings are proved here, including the independent diamond side.

De Groot's arity-indexed Hennessy–Milner/van Benthem results for classical INL concern bisimulation and first-order expressive characterization on Boolean neighbourhood structures, rather than the ordered two-sided positive syntax. Only its accessible abstract was inspected; possible unindexed analogous algebraic identities remain a literature risk.

## Limitations

Finite width is an explicit hypothesis; this result makes no assertion about infinite-width orders. The normal-form translation can duplicate subformulas and no polynomial output-size bound is claimed. The bound refers to the number of **instance** formulas, not the total ordinary connective arity or modal nesting depth. The two sides require the exact witness/co-witness conventions defined above. The lower-bound pair allows empty neighbourhoods and otherwise unrestricted families; stronger frame restrictions may admit smaller cutoffs. No model-theoretic assertion about arbitrary typed canonical structures is made. An independent audit has not been performed, and unindexed or inaccessible equivalence results cannot be excluded.

## References

[1] Litan Kumar Das, Anupam Khanra, Sujit Kumar Sardar, *Positive Instantial Neighbourhood logic: Typed Completeness and Admissible-Open Representation*, arXiv:2606.08083 (version 1 dated 6 June 2026; version 2 dated 16 July 2026). https://arxiv.org/html/2606.08083v2.

[2] *Sharp finite instance-arity cutoff for instantial neighbourhood frames*, published published-finding corpus research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-sharp-finite-instance-arity-cutoff-for-instantial-neighbourhood--d0e614d1df15.

[3] Jim de Groot, *Thomason Duality for Instantial Neighbourhood Frames*, Journal of Symbolic Logic (online 2026), DOI:10.1017/jsl.2026.10202.

[4] Jim de Groot, *Hennessy–Milner and Van Benthem for Instantial Neighbourhood Logic*, Studia Logica 110 (2022), 717–743, DOI:10.1007/s11225-021-09975-w (abstract inspected; full text unavailable).

[5] Johan van Benthem, Nick Bezhanishvili, Sebastian Enqvist, Junhua Yu, *Instantial Neighbourhood Logic*, Review of Symbolic Logic 10 (2017), 116–144, DOI:10.1017/S1755020316000447.
