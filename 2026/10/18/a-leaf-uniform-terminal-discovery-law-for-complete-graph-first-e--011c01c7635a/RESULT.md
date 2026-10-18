# A leaf-uniform terminal discovery law for complete-graph first-entrance trees

## Finding
For any finite labeled rooted tree \(T\) on \(n\ge2\) vertices with root \(r\), sample the successive vertices of a complete-graph walk independently and uniformly, starting at \(r\). Record, for each vertex discovered after the root, the vertex from which it was first entered. Conditional on the resulting first-entrance tree being exactly \(T\), the *last newly discovered vertex* is uniformly distributed over the leaves of \(T\).

Writing \(k=n-1\), let \(\mathcal L(T)\) be the ancestor-compatible permutations \(\tau=(\tau_1,\ldots,\tau_k)\) of the nonroot vertices, and let \(p(x)\) be the parent of \(x\). Define
\[
 w_T(\tau)=\prod_{i=1}^{k-1}\left(k-i+1\right)^{\mathbf1\{p(\tau_{i+1})=\tau_i\}}.
\]
For the set \(\Lambda(T)\) of leaves, the refined order-mass identity is
\[
 \sum_{\substack{\tau\in\mathcal L(T)\\\tau_k=v}}w_T(\tau)
 =\begin{cases}k!/|\Lambda(T)|,&v\in\Lambda(T),\\0,&v\notin\Lambda(T).\end{cases}
\]
In particular, conditional on the tree, the marginal of the last discovery is independent of leaf depth and of the number of internal vertices on its root path.

## Assumptions and scope
All trees are finite, connected, labeled and rooted. A leaf is a vertex with no children; since \(n\ge2\), the root is not a leaf. The walk uses transition probabilities \(1/n\) to each vertex, including the present vertex. The same conditional-order law holds for the ordinary complete-graph walk without holding steps, which merely discards waits. All conditioned tree events have positive probability.

## Proof
**1. The conditional-order mass.** Zheng [1, Theorem 6.2 and Corollary 4.9] proves for a complete-graph first-entrance tree that
\[
 \Pr(\tau\mid T)=w_T(\tau)/k!,\qquad \tau\in\mathcal L(T).
\]
We refine this by constructing a permutation map that realizes these weights and identifies the last element.

**2. The expansion map.** Given an arbitrary permutation \(\sigma\) of the \(k\) nonroot vertices, scan its entries from left to right. Upon encountering \(x\), emit all as-yet-unemitted nonroot ancestors of \(x\) in their root-to-leaf order, then emit \(x\) if it has not already been emitted. Denote the resulting tree-compatible permutation by \(E_T(\sigma)\).

**3. Exact fiber sizes.** Fix an ancestor-compatible order \(\tau\). Its preimages can be constructed backwards. Begin with a one-symbol list \((\tau_k)\). For \(i=k-1,k-2,\ldots,1\), insert \(\tau_i\) into the list already containing \(\tau_{i+1},\ldots,\tau_k\). If \(p(\tau_{i+1})=\tau_i\), every one of the \(k-i+1\) insertion positions is permitted. Otherwise only the first position is permitted. To justify this rule, compare the first new output of the expansion map after all earlier entries in \(\tau\) have been emitted: an element can be emitted before its appearance in the input precisely by a descendant that triggers its ancestor chain. The next required output after \(\tau_i\) is \(\tau_{i+1}\). For a nonparent pair, placing \(\tau_i\) after the first input symbol forces the wrong next output; for a parent pair, scanning that symbol emits \(\tau_i\) before \(\tau_{i+1}\) irrespective of the insertion position. Induction over these suffixes shows these choices are both necessary and sufficient; distinct insertion sequences yield distinct input permutations. Consequently
\[
 |E_T^{-1}(\tau)|=w_T(\tau).
\]
This also gives a direct bijective proof of the total order-mass identity by summing fibers over all \(k!\) input permutations.

**4. Terminal-leaf symmetry.** Every leaf \(v\) can only be emitted when the scan encounters \(v\) itself, because \(v\) has no proper descendants. Every nonleaf \(x\) is emitted no later than the first encounter of any one of its descendant leaves. Hence the last output of \(E_T(\sigma)\) is precisely the leaf whose position is latest among leaves in the input permutation \(\sigma\). All \(k!\) inputs are equally weighted, so by exchangeability each leaf is last in exactly \(k!/|\Lambda(T)|\) permutations. Counting the fibers from Step 3 gives the refined identity, and the conditional-order formula in Step 1 gives the stated probability law.

## Verification
The proof is finite and combinatorial, valid for every \(n\ge2\). The accompanying standalone `verify.py` exhaustively generates labeled trees for small sizes, forms the weighted linear-extension masses, and independently checks permutation expansion and terminal-leaf symmetry. Finite checks are supplementary evidence, not a substitute for the fiber proof.

## Relationship to prior work
Zheng [1] establishes the conditional joint order distribution and the unrefined normalization \(\sum_\tau w_T(\tau)=k!\), and explicitly identifies later discovery-position marginals as an outstanding issue. The terminal-position refinement here gives a closed form for one such marginal and a direct permutation-fiber interpretation. Fredes and Marckert [2] provide prior combinatorial treatments of Aldous–Broder-type first-entrance trees. The unconditional uniformity of the final coupon-collected label is elementary; the conditional uniformity restricted to *the leaves of a prescribed realized tree* is the new assertion.

## Limitations
The result applies to complete-graph walks with uniform transitions. It does not assert uniformity at intermediate discovery positions, for general underlying transition matrices, or among leaves conditional on additional information about discovery times. The complete conditional-order formula itself is prior work, not a novel claim here. As for any literature-based originality assessment, an equivalent unindexed or differently phrased theorem may exist.

## References
[1] H. Zheng, *The Order Mass Identity of Rooted Forests, with a Direct Proof of the Extended Aldous–Broder Theorem*, arXiv:2610.13063 (first public version 2026-10-09), Theorem 6.2, Corollary 4.9 and discussion of later-position marginals. https://arxiv.org/abs/2610.13063

[2] L. Fredes and J.-F. Marckert, *A combinatorial proof of Aldous–Broder theorem for general Markov chains*, arXiv:2102.08639 (2021). https://arxiv.org/abs/2102.08639
