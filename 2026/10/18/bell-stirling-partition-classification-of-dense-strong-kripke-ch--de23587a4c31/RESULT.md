# Bell–Stirling partition classification of dense strong Kripke chains

## Finding

Fix an integer \(n\geq1\) and the linearly ordered frame carrier
\[
C_n=\{0<1<\cdots<n-1\}.
\]
A binary relation \(R\subseteq C_n\times C_n\) is **strong** if \(iRj\Rightarrow i\leq j\), **prefix-closed** if \(i\leq k\) and \(kRj\) imply \(iRj\), and **dense** if \(R\subseteq R\circ R\), meaning every edge \(iRj\) factors through an intermediate \(k\) with \(iRk\) and \(kRj\). Such frames form a natural finite-chain subclass of strong dense intuitionistic modal frames used in the Kripke semantics of propositional lax logic.

**Classification.** Each strong prefix-closed relation is determined by integers \(d_j\in\{-1,0,\ldots,j\}\), with
\[
iRj\quad\Longleftrightarrow\quad i\leq d_j.
\]
It is dense precisely when
\[
\forall j\in C_n:\qquad d_j=-1\quad\text{or}\quad d_{d_j}=d_j.
\]
Dense relations are therefore in canonical bijection with the set partitions of \(\{\ast,0,\ldots,n-1\}\): \(d_j=-1\) marks membership of the distinguished block containing \(\ast\), while a non-distinguished block has its least member \(r\) as the common value \(d_j=r\) for all its members.

**Exact counts.** Let \(s(R)=|\{j:jRj\}|\), the number of reflexive worlds. Writing \(\left\{\begin{smallmatrix}a\\b\end{smallmatrix}\right\}\) for a Stirling number of the second kind and \(B_a\) for the \(a\)-th Bell number, for every \(0\leq k\leq n\),
\[
\#\{R:s(R)=k\}=\left\{\begin{matrix}n+1\\k+1\end{matrix}\right\},
\qquad
\#\{R\}=B_{n+1}.
\]
Exactly \(B_n\) of these relations are serial, with serial rank profile
\[
\#\{R:\text{serial},\ s(R)=k\}=\left\{\begin{matrix}n\\k\end{matrix}\right\}.
\]
The nonserial count is \(B_{n+1}-B_n\). Because every finite chain is order-rigid, these are also the corresponding counts up to order-preserving frame isomorphism.

**Modal-semantic quotient and exact fibres.** The relation acts on the Heyting algebra \(\operatorname{Up}(C_n)\) of upward-closed subsets by
\[
\Box_R U=\{i\in C_n:\forall j\ (iRj\Rightarrow j\in U)\}.
\]
For dense strong prefix-closed \(R\), put \(S=\{j:jRj\}\). Then, for every upward-closed \(U\),
\[
\boxed{\Box_R U=\{i:S\cap\{i,i+1,\ldots,n-1\}\subseteq U\}.}
\]
Consequently two such relations induce the same modal operation on all upward-closed sets **if and only if** they have the same reflexive-world set \(S\). Every \(S\subseteq C_n\) is realized. Thus the \(B_{n+1}\) relations induce exactly \(2^n\) distinct nucleus operators; in fact these are all nuclei on \(\operatorname{Up}(C_n)\). The exact number of relations inducing the nucleus associated with a fixed \(S\) is
\[
\boxed{\prod_{j\notin S}\left(1+|S\cap\{0,\ldots,j-1\}|\right).}
\]
An empty product is one.

## Assumptions and scope

The underlying carrier is the *fixed* finite chain \(C_n\), with its indicated order, and the relation is allowed to be empty. A frame is required to satisfy **all three** of strongness, prefix closure and density in the precise sense stated above. No reflexivity or seriality is assumed unless it is explicitly counted as a subfamily. Composition \(R\circ R\) is interpreted existentially and without reversing the edge direction.

An upward-closed valuation sends propositional variables to upward-closed subsets of \(C_n\). We count raw labelled relations, the corresponding order-isomorphism classes, the number of reflexive worlds, and the modal operations as *different* quantities; equality of the last does not mean equality of the raw accessibility relations. The article by van der Giessen places strong dense frames in the context of propositional lax logic but does not supply the classification established here.

## Proof

### 1. Incoming-column normal form

For fixed \(j\), strongness confines its predecessor set to \(\{0,\ldots,j\}\). Prefix closure forces this predecessor set to be an initial segment. It is uniquely either empty, denoted by \(d_j=-1\), or \(\{0,\ldots,d_j\}\) for a unique \(d_j\in\{0,\ldots,j\}\). Conversely every such column-choice vector satisfies strongness and prefix closure. In particular these two conditions imply transitivity: if \(iRk\) and \(kRj\), then \(i\leq k\) by strongness, and prefixing the edge \(kRj\) by \(i\leq k\) yields \(iRj\).

### 2. Necessary and sufficient density test

Fix \(j\) with \(d_j\geq0\), put \(r=d_j\), and observe that \(rRj\). If \(R\subseteq R\circ R\), then this edge admits \(rRk\) and \(kRj\). Strongness gives \(r\leq k\), whereas \(kRj\) and the definition of \(d_j=r\) give \(k\leq r\). Thus \(k=r\), so \(rRr\), equivalently \(d_r=r\). This proves necessity.

Conversely, assume every nonempty column has \(d_{d_j}=d_j\). Given \(iRj\), let \(r=d_j\), so \(i\leq r\), \(rRr\) and \(rRj\). Prefix closure applied to \(i\leq r\) and \(rRr\) gives \(iRr\). Hence \(iRrRj\), proving density. This also shows that each edge factors through a reflexive world between its endpoints.

### 3. Partition bijection, ranks and seriality

Call \(r\) a *root* when \(d_r=r\). The density criterion states that every nonempty column is labelled by one of these roots, and this root is no greater than the column index. Construct a partition by grouping all indices with the same nonnegative label into a block and grouping all indices with label \(-1\) with the extra point \(\ast\). In a non-starred block with root \(r\), every member is at least \(r\), and \(r\) itself is in the block; therefore \(r\) is exactly its minimum.

For the inverse, start with any partition of \(\{\ast,0,\ldots,n-1\}\). Set \(d_j=-1\) for members of the block containing \(\ast\); on every other block set \(d_j\) equal to the minimum of that block. These choices obey \(d_j\leq j\) and the density test, and the two constructions invert one another. The roots are exactly the minima of the non-starred blocks. Thus partitions with precisely \(k+1\) blocks correspond to frames with precisely \(k\) reflexive worlds, giving the Stirling and Bell formulas.

If the top world \(n-1\) has any successor, strongness makes it \(n-1\) itself. Therefore seriality implies \((n-1)R(n-1)\). Conversely, if the top world is reflexive, prefix closure makes every world access the top world, so the relation is serial. The top world is a root exactly when its partition block is its singleton; removing that singleton gives a partition of \(\{\ast,0,\ldots,n-2\}\) into \(k\) blocks when there are \(k\) roots originally. This proves the serial Stirling and Bell counts, including \(n=1\).

### 4. Modal collapse and fibre cardinality

For a dense relation let \(S=\{r:d_r=r\}\). Fix \(i\) and an upward-closed \(U\). For every \(r\in S\) with \(r\geq i\), prefix closure of the loop \(rRr\) gives \(iRr\). Thus \(i\in\Box_RU\) forces every such \(r\) to lie in \(U\).

For the reverse implication, assume all roots \(r\geq i\) lie in \(U\), and let \(iRj\). Write \(r=d_j\). The density criterion says \(r\in S\), while \(i\leq r\leq j\). By hypothesis \(r\in U\), so upward closure of \(U\) gives \(j\in U\). Hence \(i\in\Box_RU\) and the displayed modal formula is proved.

Every subset \(S\) is realized by setting \(d_r=r\) on \(S\) and \(d_j=-1\) elsewhere. Distinct subsets induce distinct modal maps: if \(i\in S\setminus T\), choose \(U=\{i+1,\ldots,n-1\}\). The displayed formula shows \(i\notin\Box_SU\) while \(i\in\Box_TU\). The symmetric case follows by interchanging \(S,T\). Thus exactly \(2^n\) modal maps occur.

These operations are nuclei: they preserve the greatest upset and binary intersections, are extensive because \(R\subseteq\leq\), and are idempotent because \(R\circ R=R\) (transitivity and density together). Conversely on any finite chain, every extensive monotone idempotent self-map is determined by its set of fixed elements, which can be any subset containing the top element. Every monotone map on a chain preserves binary meets; hence there are exactly \(2^n\) nuclei on the \((n+1)\)-element chain \(\operatorname{Up}(C_n)\). All are realized above.

For fixed \(S\), the columns indexed by \(r\in S\) have the forced value \(d_r=r\). At each index \(j\notin S\), any one of the \(|S\cap\{0,\ldots,j-1\}|\) earlier roots or the empty value \(-1\) can be chosen independently. The product formula follows; summing it over all \(S\) recovers \(B_{n+1}\) from the partition classification.

## Verification

The standalone standard-library Python program `verify_dense_chains.py` enumerates every incoming-column vector from the unrestricted strong prefix-closed family, through \(n=7\). For each vector it constructs the full binary relation and checks strongness, prefix closure, the *literal* existential relational-density condition, and the idempotent-label criterion independently. For the dense relations it separately checks seriality, the number of reflexive worlds, every possible upward-closed event's modal truth set, the exact fibre product, and all Stirling rank counts.

The verified totals for \(n=1,2,3,4,5,6,7\) are respectively
\[
2,\ 5,\ 15,\ 52,\ 203,\ 877,\ 4140;
\]
the serial totals are
\[
1,\ 2,\ 5,\ 15,\ 52,\ 203,\ 877;
\]
and the modal-operator counts are
\[
2,\ 4,\ 8,\ 16,\ 32,\ 64,\ 128.
\]
The verifier terminates with `VERIFY_OK` on success. These exhaustive finite computations are corroboration, not the proof for unbounded \(n\): the arguments above establish the general classification.

## Relationship to prior work

Goldblatt introduced geometric-modal semantics and strong dense frames for propositional lax logic; van der Giessen's treatment explicitly recounts the strongness and prefix-closure conditions, their transitivity consequence, and Goldblatt's finite strong dense completeness semantics. Neither source's identified discussion supplies the partition coding, Stirling rank-refinement, or exact semantic fibres. Goldblatt's full original article was not accessible for a definitive entire-text comparison, so possible older coverage under geometric or nuclear terminology is a residual risk, not ruled out merely by its absence from search results.

The published result *Factorial census of AP-compatible doxastic and epistemic chain frames* already observes the very same column-cutoff parametrization for the **ambient strong prefix-closed** finite-chain relations and derives \((n+1)!\), with \(n!\) serial relations. This preliminary parametrization is not claimed as new. The present theorem restricts to the additional density condition, obtains the exact partition-bijection and rank profile, and identifies which raw frames have identical modal operations. Those density and fibre conclusions do not follow as stated from the ambient factorial result.

The published result *Bell-number census for the S4-like finite-chain flat frames* concerns a different Heyting–Lewis frame class: its rows are upward-closed, it imposes reflexivity on a composed relation and transitivity, and it counts \(B_{n+1}-B_n\) relations. This number happens also to be the present family's **nonserial** count, but a numerical coincidence is not a proof of equivalence. Its theorem does not state the density-cutoff test, partition-rank distribution, or modal-fibre classification in this article's strong-frame semantics. A possible unexamined reduction between the families remains an originality risk.

## Limitations

The bijection and product fibres rely on the total order; branching partial orders have non-principal predecessor downsets and require separate investigation. The theorem counts raw relations rather than distinct modal logics or general finite Goldblatt frames. It asserts no optimal modal decision procedure and no extension of the partition coding to arbitrary frames. Bell and Stirling numbers, the concept of nuclei, and the ambient factorial cutoff normal form are pre-existing mathematics; their names and earlier uses are not claimed as new. The precise novelty claim is this density-conditioned structure, its rank-refined census, and its exact relationship to the corresponding modal operators.

A relevant 1981 original paper could not be inspected in full. Additional literature unindexed under different terminology may contain an equivalent chain specialization. Independent audit has not been performed.

## References

[1] Iris van der Giessen, “Admissible rules for six intuitionistic modal logics,” *Annals of Pure and Applied Logic* 174 (2023), article 103233, first publicly available 21 December 2022. DOI: 10.1016/j.apal.2022.103233. Lawful open-access full text: https://pure-oai.bham.ac.uk/ws/portalfiles/portal/186893449/1_s2.0_S0168007222001488_main.pdf (especially Section 1, page 5).

[2] Robert I. Goldblatt, “Grothendieck Topology as Geometric Modality,” *Mathematical Logic Quarterly* 27 (1981), 495–529. DOI: 10.1002/malq.19810273104 (publisher landing page inspected; full text not available for the present comparison).

[3] “Factorial census of AP-compatible doxastic and epistemic chain frames,” public mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-factorial-census-of-ap-compatible-doxastic-and-epistemic-chain-f--0af5835bf78b (full published `RESULT.md` inspected).

[4] “Bell-number census for the S4-like finite-chain flat frames,” public mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-bell-number-census-for-the-s4-like-finite-chain-flat-frames--6ab97388fd68 (full published `RESULT.md` inspected).
