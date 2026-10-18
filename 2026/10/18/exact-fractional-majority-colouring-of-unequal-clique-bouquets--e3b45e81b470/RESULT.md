# Exact fractional majority colouring of unequal clique bouquets

## Finding
For any integer \(t\ge1\) and any positive integers \(s_1,\ldots,s_t\), let \(G=K_1\vee\bigsqcup_{i=1}^{t}K_{s_i}\), with central vertex \(h\) and peripheral cliques \(C_i\) of size \(s_i\). Let \(D\) be obtained from \(G\) by replacing each edge with its two oppositely directed arcs. Then the fractional majority colouring number is
\[
\chi^*_{\mathrm{maj}}(D)=\max_{1\le i\le t}\frac{s_i+1}{\lfloor s_i/2\rfloor+1}.
\]
In particular, it equals \(2\) if at least one \(s_i\) is odd, while when all \(s_i\) are even it equals \(2-2/(s_{\max}+2)\), where \(s_{\max}=\max_i s_i\). The order, number, and relative sizes of other peripheral cliques do not affect this value.

## Assumptions and scope
All graphs and digraphs are finite and loopless. The number of peripheral cliques is \(t\ge1\); each peripheral clique is nonempty, \(s_i\ge1\), and all vertices are labelled when speaking of explicit set distributions. There are no edges between distinct peripheral cliques. Both directed arcs of each undirected edge belong to \(D\).

A vertex set \(S\subseteq V(D)\) is *majority-stable* when \(2|N_D^+(v)\cap S|\le d_D^+(v)\) for every \(v\in S\). A *fractional majority colouring* is a finite family of nonnegative weights \(w_S\), one per majority-stable set, satisfying \(\sum_{S\ni v}w_S\ge1\) for each vertex \(v\). Its weight is \(\sum_S w_S\), and \(\chi^*_{\mathrm{maj}}(D)\) is the minimum weight. The empty set may be assigned weight zero.

## Proof
Put \(a_i=\lfloor s_i/2\rfloor\), \(b_i=a_i+1\), and \(L=\max_i(s_i+1)/b_i\). Every peripheral vertex in \(C_i\) has outdegree \(s_i\), whereas the hub has outdegree \(\sum_i s_i\).

**Local capacity lemma.** Every majority-stable set \(S\) satisfies
\[
|S\cap(\{h\}\cup C_i)|\le b_i\qquad(1\le i\le t).
\]
To prove this, write \(k_i=|S\cap C_i|\). If \(h\notin S\), then each selected peripheral vertex in \(C_i\) has exactly \(k_i-1\) selected out-neighbours, so \(k_i\le a_i+1=b_i\); the case \(k_i=0\) is immediate. If \(h\in S\) and \(k_i>0\), then every selected peripheral vertex has exactly \(k_i\) selected out-neighbours, forcing \(k_i\le a_i\), and therefore \(1+k_i\le b_i\); again \(k_i=0\) is immediate.

**Lower bound.** Let \((w_S)\) be any feasible fractional majority colouring, of total weight \(W\). Sum the vertex covering inequalities over the \(s_i+1\) vertices of \(\{h\}\cup C_i\). By the local capacity lemma,
\[
 s_i+1\le\sum_Sw_S|S\cap(\{h\}\cup C_i)|\le b_iW.
\]
Thus \(W\ge(s_i+1)/b_i\) for every \(i\), and therefore \(W\ge L\).

**Matching upper bound.** Define two probability distributions on vertex sets. Under \(\mathcal H\), include the hub and choose independently, for each \(i\), a uniformly random \(a_i\)-element subset of \(C_i\). Under \(\mathcal B\), omit the hub and choose independently, for each \(i\), a uniformly random \(b_i\)-element subset of \(C_i\). Each sampled \(\mathcal H\)-set is majority-stable: its selected peripheral vertices have exactly \(a_i\le s_i/2\) selected out-neighbours, and its hub has \(\sum_i a_i\le\lfloor\sum_i s_i/2\rfloor\) selected out-neighbours. Each sampled \(\mathcal B\)-set is majority-stable: every selected peripheral vertex has exactly \(b_i-1=a_i\) selected out-neighbours, while the hub is absent.

Place total weight \(1\) on the distribution \(\mathcal H\), and total weight \(L-1\) on \(\mathcal B\). These are nonnegative because \(L\ge1\). The hub receives covering weight \(1\). A peripheral vertex in \(C_i\) receives covering weight
\[
 \frac{a_i}{s_i}+(L-1)\frac{b_i}{s_i}=\frac{Lb_i-1}{s_i}\ge1,
\]
since \(Lb_i\ge s_i+1\). The total weight is \(1+(L-1)=L\), proving the opposite inequality and hence the displayed identity.

**Parity statement.** If \(s_i=2a+1\) is odd then \((s_i+1)/(a_i+1)=2\). If \(s_i=2a\) is even, then the ratio is \((2a+1)/(a+1)=2-2/(s_i+2)\), which is strictly below \(2\) and increases with even \(s_i\). This proves the two cases without excluding \(s_i=1\) or \(t=1\).

## Verification
The independent direct implementation in `verify.py` constructs the actual symmetric directed adjacency relation and enumerates all subsets, testing the definition \(2|N_D^+(v)\cap S|\le d_D^+(v)\) for every selected vertex. It then solves the fractional covering linear program after compressing by the natural clique-permutation symmetries. It tested all \(230\) ordered profiles with between one and four cliques, sizes from \(1\) through \(4\), and at most \(11\) vertices, examining a total of \(189012\) candidate subsets. All computed optima match the displayed rational formula to tolerance \(10^{-8}\). Recorded outputs include \((2,4)\mapsto5/3\), \((2,3)\mapsto2\), and \((2,2,2)\mapsto3/2\). The theorem for unbounded profiles is proved above; these finite checks are not used as an infinite proof. Reproduce with `python verify.py` using Python 3, NumPy, and SciPy's HiGHS linear-programming solver.

## Relationship to prior work
Ben-Ameur and Maddaloni's October 8, 2026 preprint (arXiv:2610.11997) develops general bounds and algorithmic complexity for fractional majority colourings, including a universal \(523/140\) upper bound. The present theorem is an exact value and constructive optimal fractional colouring for the bidirected join of one vertex with arbitrarily many unequal complete graphs, not a consequence of that universal bound alone. Anastos, Lamaison, Steiner, and Szabó's earlier majority-colouring work (arXiv:1911.01954, published 2021) established fractional majority bounds and the associated relaxation. The relaxation and its linear-programming interpretation are prior art; the precise clique-bouquet classification is the result addressed here. Ordinary fractional proper colouring, vertex-majority colouring, and strong-majority edge colouring have different feasible sets and are not identified with this invariant. An uncatalogued general block-sum theorem might imply the present result, so definitive bibliographic priority is not established.

## Limitations
The result requires the symmetric bidirection, one common hub, and complete peripheral cliques with no edges joining distinct peripheral cliques. It does not classify optimal fractional colourings uniquely, establish an exact formula for arbitrary block graphs or non-symmetric orientations, or prove bibliographic uniqueness. The linear-programming checks are finite, use floating-point tolerances, and do not substitute for the proof. Independent external validation has not been performed.

## References
- W. Ben-Ameur and A. Maddaloni, *Fractional majority coloring of digraphs: bounds and inapproximability*, arXiv:2610.11997 (first posted October 8, 2026), https://arxiv.org/abs/2610.11997.
- M. Anastos, A. Lamaison, R. Steiner, and T. Szabó, *Majority Colorings of Sparse Digraphs*, arXiv:1911.01954 (first posted November 5, 2019), https://arxiv.org/abs/1911.01954; *Electronic Journal of Combinatorics* 28(2), P2.31 (2021), https://doi.org/10.37236/10067.
