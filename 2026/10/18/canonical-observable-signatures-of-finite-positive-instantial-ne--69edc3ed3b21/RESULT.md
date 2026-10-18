# Canonical observable signatures of finite positive instantial neighbourhood frames

## Finding

Let \((W,\leq)\) be a nonempty finite poset. Its upsets form \(\operatorname{Up}(W)\), and \(M=\operatorname{Max}(W)\) is the set of its maximal points. The positive instantial box and diamond operations on upsets are
\[
\begin{aligned}
F_{\mathcal B}(A_1,\ldots,A_r;B)
&\iff \exists U\in\mathcal B\ (U\subseteq B\ \land\ U\cap A_i\ne\varnothing\ \text{for every }i),\\
G_{\mathcal D}(A_1,\ldots,A_r;B)
&\iff \forall U\in\mathcal D\ (\exists i\ U\subseteq A_i\ \lor\ U\cap B\ne\varnothing),
\end{aligned}
\]
where \(\mathcal B,\mathcal D\subseteq\operatorname{Up}(W)\), \(r\geq0\), and all arguments are upsets. For \(r=0\), the existential disjunction in the diamond clause is false.

Define two finite **observable signatures**:
\[
\begin{aligned}
\sigma_\Box(\mathcal B)
&=\{U\in\mathcal B:\nexists V\in\mathcal B\ (V\subsetneq U\ \land\ V\cap M=U\cap M)\},\\
\sigma_\Diamond(\mathcal D)
&=\{U\in\mathcal D:\nexists V\in\mathcal D\ (U\subsetneq V\ \land\ U\cap M=V\cap M)\}.
\end{aligned}
\]

**Canonical-signature theorem.** Two box-neighbourhood families induce identical \(F\)-operations on all upset arguments and at all arities if and only if their \(\sigma_\Box\) signatures agree. Two diamond-neighbourhood families induce identical \(G\)-operations if and only if their \(\sigma_\Diamond\) signatures agree. In both cases **arities at most the width** \(w=\operatorname{width}(W)\) suffice to determine the signature, hence all arities. This width bound is sharp as a uniform bound over finite posets.

Consequently, two persistent two-sided neighbourhood frames on the **same fixed poset** induce identical truth sets for every positive instantial formula under every common upward-closed valuation if and only if their two observable signatures agree at every world. The pointwise signatures are semantic invariants; pruning them independently across worlds need not preserve the frame's persistence axioms.

**Nonfaithfulness and exact chain quotient.** Each of the box- and diamond-family-to-operator maps is injective for every family on \(W\) if and only if \(W\) is an antichain. On any non-antichain poset there are distinct **persistent** box assignments, and also distinct persistent diamond assignments, that no formula, at any nesting depth or arity, distinguishes when the other modality is held fixed. Unlike the box, a diamond formula of instance arity zero detects the presence of the empty neighbourhood even on a one-point frame. On an \(n\)-point chain, among frames whose box and diamond assignments are each **constant over worlds**, the number of equivalence classes under truth of all positive instantial formulas and all persistent valuations is exactly
\[
\boxed{4(n+1)^2}.
\]

## Assumptions and scope

Use precisely the ordinary **untyped**, persistent, two-sided neighbourhood semantics of Das–Khanra–Sardar, with both modal instance lists of finite length (including length zero). Worlds are a finite nonempty partially ordered set, valuations assign arbitrary upsets to variables, and every neighbourhood itself is an upset. A frame has \(\mathcal B_x\subseteq\mathcal B_y\) and \(\mathcal D_y\subseteq\mathcal D_x\) whenever \(x\leq y\). No supplementation, seriality, or closure property is assumed for a local neighbourhood family.

The comparison uses the **same labelled poset**, the same valuation, and the same worlds, not general modal equivalence up to bisimulation or a claim about different posets. A local operation has a Boolean truth value at its chosen world for each tuple of upset arguments. All power-set and cardinality assertions below are finite.

## Proof

**1. Upset intersections see maximal points.** If \(U,A\) are upsets of finite \(W\), then
\[
U\cap A\ne\varnothing\ \Longleftrightarrow\ (U\cap M)\cap A\ne\varnothing.
\]
Indeed, any \(x\in U\cap A\) lies below some maximal \(m\in W\), and upward closure puts \(m\) in both sets. For the converse take the displayed common maximal point.

**2. Box signature is sufficient.** If \(V\subsetneq U\) belong to \(\mathcal B\) and have identical maximal trace \(V\cap M=U\cap M\), then any witness \(U\) for \(F\) can be replaced by \(V\): the support condition survives because \(V\subseteq U\), while each intersection survives by step 1. Repeated deletion (a finite process) leaves exactly the inclusion-minimal members within each maximal-trace class, namely \(\sigma_\Box(\mathcal B)\), without changing \(F\) at any arity.

**3. Box signature is necessary.** Suppose two signatures differ and choose an inclusion-minimal \(U\) in their symmetric difference. Without loss, \(U\in\sigma_\Box(\mathcal B_1)\setminus\sigma_\Box(\mathcal B_2)\). Let \(T=U\cap M\), use support \(B=U\), and supply one instance argument \(\{m\}\) for each \(m\in T\) (zero arguments if \(U=\varnothing\)). Singleton maxima are upsets. The first family satisfies the resulting box test via \(U\). If the second does too, it has some \(V\subseteq U\) with \(T\subseteq V\). Necessarily \(V\cap M=T\). Replacing \(V\) by an inclusion-minimal member in its trace class produces \(V_0\in\sigma_\Box(\mathcal B_2)\) with \(V_0\subseteq U\). It cannot equal \(U\). Nor can it belong to \(\sigma_\Box(\mathcal B_1)\), since this would contradict minimality of \(U\) inside its trace class. Therefore \(V_0\) belongs to the symmetric difference and is strictly smaller than \(U\), a contradiction. The test has at most \(|M|\leq w\) instances.

**4. Diamond signature is sufficient.** If \(U\subsetneq V\) belong to the diamond family with the **same maximal trace**, then whenever \(U\) makes the co-witness condition false, so does \(V\): if \(U\not\subseteq A_i\) then also \(V\not\subseteq A_i\), and by step 1 the requirement \(U\cap B=\varnothing\) is equivalent to \(V\cap B=\varnothing\) because their maximal traces agree. A larger same-trace neighbourhood therefore dominates the smaller one as an obstruction to the universally quantified diamond clause. Repeated finite deletion leaves precisely \(\sigma_\Diamond(\mathcal D)\), including the empty neighbourhood if present, and changes no diamond operation.

**5. Diamond signature is necessary.** For any upset \(U\), let \(T=U\cap M\). Use the scope upset \(B=M\setminus T\), and one instance upset \(A_s=W\setminus\downarrow s\) for each minimal element \(s\in\operatorname{Min}(U)\) (no instances when \(U=\varnothing\)). For any upset \(V\), the diamond test is **false** precisely when some neighbourhood \(V\in\mathcal D\) obeys
\[
V\cap(M\setminus T)=\varnothing
\quad\text{and}\quad
V\not\subseteq W\setminus\downarrow s\quad\text{for each }s\in\operatorname{Min}(U).
\]
Since \(V\) is upset, \(V\not\subseteq W\setminus\downarrow s\) if and only if \(s\in V\). Thus the second condition is exactly \(U=\uparrow\operatorname{Min}(U)\subseteq V\); this also holds for empty \(U\). The first condition asserts \(V\cap M\subseteq T\). Together with \(U\subseteq V\), which gives \(T\subseteq V\cap M\), the conditions are exactly
\[
U\subseteq V\quad\text{and}\quad V\cap M=U\cap M.
\]
Therefore this truth test detects whether the family contains **a superset of \(U\) with the same maximal trace**. This finite within-trace upper-closure relation uniquely determines its inclusion-maximal generators, namely \(\sigma_\Diamond(\mathcal D)\). Explicitly, if two signatures differ, choose an inclusion-maximal \(U\) in their symmetric difference and apply the displayed test: the first family witnesses failure via \(U\); a witness in the other would extend to a strictly larger, same-trace maximal representative in the symmetric difference, contradicting maximality. The test has \(|\operatorname{Min}(U)|\leq w\) instance arguments. When \(U=\varnothing\), it is a zero-instance test with scope \(M\), distinguishing a family containing the empty neighbourhood from one lacking it.

**6. From operations to formulas.** If the two local signatures agree for every world, steps 2–5 show equality of all box/diamond operations on all tuples of upsets. Structural induction on formulas, using persistence of truth sets, proves equality of formula truth sets for every valuation. Conversely, give independent propositional variables arbitrary prescribed upset truth sets and apply a depth-one box or diamond formula; equality of every formula under every valuation forces equality of the associated operations. Therefore steps 3 and 5 recover the signatures. This argument does not require a canonical frame obtained by pointwise pruning to remain persistent.

**7. Width is sharp.** On a discrete \(w\)-point poset, fix the diamond families to be empty and, at every world, let the two box families be respectively all proper subsets of \(W\) and all subsets. Both assignments are persistent. For fewer than \(w\) instance arguments, any witness using \(W\) can be replaced by the set of at most one chosen witness point from each instance set (the empty set when there are no instances); this is a proper subset and still satisfies the support condition. At instance arity \(w\), support \(W\) and the \(w\) singleton instance arguments separate the assignments. Thus no smaller bound works uniformly for width \(w\). This discrete lower-bound construction is also present in the earlier finite BAIO cutoff literature; the ordered-poset width upper bound and canonical PINL signatures are the additional content here.

**8. Faithfulness and the chain count.** When \(W\) is an antichain, every upset is its own maximal trace, so both signatures equal the entire original family. Conversely, if there is a nonmaximal \(x\), put \(U=\uparrow x\) and \(V=U\cap M\). Then \(\varnothing\ne V\subsetneq U\), both are upsets, and \(V\cap M=U\cap M\). Distinct **constant** box families \(\{V\}\) and \(\{V,U\}\) have identical box signatures, while distinct constant diamond families \(\{U\}\) and \(\{V,U\}\) have identical diamond signatures. Holding the other component fixed gives inequivalent raw persistent frames with the same complete formula semantics. On one world, \(\Diamond(;\top)\) distinguishes an empty diamond family from one containing \(\varnothing\), as follows directly from the universal clause.

On an \(n\)-world chain, the \(n\) nonempty upsets are linearly ordered by inclusion and share one maximal trace. The box signature is determined by whether the empty upset occurs (two choices) and by the smallest nonempty neighbourhood, if any (\(n+1\) choices including none), giving \(2(n+1)\) box signatures. The diamond signature is determined independently by whether the empty upset occurs (two choices) and by the **largest** nonempty neighbourhood, if any (\(n+1\) choices including none), giving another \(2(n+1)\) signatures. Independent constant assignments realize each possible pair persistently, and step 6 distinguishes different pairs. Hence there are exactly \(4(n+1)^2\) semantic classes of constant two-sided neighbourhood assignments.

## Verification

A standalone Python 3 standard-library checker independently evaluates both modal clauses on finite upset lattices for every local neighbourhood family on eleven finite posets: singleton, two-point antichain and chain, three-point antichain, chain, fork and inverted fork, four-, five-, and six-point chains, and two disjoint two-point chains. It compares the complete truth tables for all upset arguments through the poset width with the stated canonical signatures, in both directions. The checker covers 1,100 local families on each modality, including all 256 on the three-point antichain and all 512 on the disjoint union of two two-point chains. It additionally checks the explicit two-world box counterexample and one-world detection of an empty diamond neighbourhood at instance arity zero, and two-world diamond nonfaithfulness through arity four. Run `python3 verify.py`. Its final line reports successful checks. The mathematical argument is universal for all finite posets and does not infer such a statement from finite enumeration.

## Relationship to prior work

Das, Khanra and Sardar (2026) define the untyped positive instantial modalities on persistent two-sided neighbourhood models and give algebraic semantics; they identify a full duality programme as future work. Their modal clauses (Section 3), algebraic operations (Section 7), and discussion (Section 9) do not provide the above exact fibrewise observational quotient, box maximal-trace signature, two-point nonfaithfulness, or finite-chain census. The canonical/typed distinction in their paper is separate from the present *same-poset, untyped, all-valuations* equality.

De Groot (2026) establishes Thomason duality for classical instantial frames based on the **full powerset** Boolean algebra, where arbitrary singleton argument sets recover every neighbourhood. A published finite-instance cutoff result explicitly sharpens that reconstruction on \(n\) worlds. That Boolean reconstruction does not transfer to intuitionistic upsets, since a singleton \(\{x\}\) is not an upset when \(x\) is nonmaximal. Our classification quantifies precisely the resulting information loss and gives a width rather than cardinality bound for the observable quotient. Standard antichain representations of monotone neighbourhood families under different one-place semantics provide related background, but do not imply the two-sided instantial signature formulas on ordered carriers.

## Limitations

This theorem addresses finite carriers with unrestricted families of upward-closed neighbourhoods under the precise two-sided PINL clauses. The canonical signatures are pointwise observational data, not in general a persistent retraction or a functorial dual equivalence. The formula-equivalence criterion compares frames on the **same** carrier and order. The exact \(4(n+1)^2\) count refers to **constant** assignments on a chain, not the total number of equivalence classes of all variable persistent assignments. The result does not establish a general infinite-frame duality, adequacy of the typed canonical semantics, or a complexity classification. Finite checker results do not prove the general theorem. Equivalent characterizations in inaccessible or unindexed literature remain possible.

## References

[1] Litan Kumar Das, Anupam Khanra, and Sujit Kumar Sardar, *Positive Instantial Neighbourhood logic*, arXiv:2606.08083, first submitted June 6, 2026, Sections 3, 7 and 9. https://arxiv.org/abs/2606.08083.

[2] Jim de Groot, *Thomason Duality for Instantial Neighbourhood Frames*, Journal of Symbolic Logic, published online April 10, 2026. DOI:10.1017/jsl.2026.10202.

[3] *Sharp finite instance-arity cutoff for instantial neighbourhood frames*, published published-finding corpus record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-sharp-finite-instance-arity-cutoff-for-instantial-neighbourhood--d0e614d1df15. The compared result concerns full Boolean-set BAIO reconstruction.

[4] Jim de Groot, *Hennessy-Milner and Van Benthem for Instantial Neighbourhood Logic*, Studia Logica 110 (2022), 717–743, DOI:10.1007/s11225-021-09975-w. Abstract and publication metadata inspected; full text not available in the consulted open channel.

[5] Sabine Frittella, Alessandra Palmigiano, and Luigi Santocanale, *Dual Characterizations for Finite Lattices via Correspondence Theory for Monotone Modal Logic*, Journal of Logic and Computation 27 (2017), DOI:10.1093/logcom/exw011. Related minimal-neighbourhood antichain formalism under different semantics; the exact page range is not asserted here.
