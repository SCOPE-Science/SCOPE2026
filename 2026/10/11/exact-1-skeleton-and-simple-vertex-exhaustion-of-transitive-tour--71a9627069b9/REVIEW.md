# Independent mathematical audit

## correctness

PASS

For n≥3, each r_{ij} (i<j) is exposed uniquely by h_i=1,h_j=−1 and other h_t=0, and P_n has affine dimension n−1 (the r_{1j} affine span has x_1=1, whereas r_{23} has x_1=0). For a pair of positive roots an exposed edge is equivalent to a functional attaining its strict maximum only at that pair. Explicit integer witnesses give shared-tail/head edges and j<k disjoint-interval edges; strictly increasing h with two unit increments of 1 and all others 2 witnesses consecutive unit-root chains at maximum −1. Non-chain overlaps contradict r_{ij}+r_{kℓ}=r_{iℓ}+r_{kj}; a chain at equal maximum T forces T<0 by the long root, and any nonunit member splits into two positive roots with scores ≤T, forcing T≤2T<T, contradiction. The positive-witness edges persist in conv(P_n∪{0}); every unit-chain witness necessarily has negative score and disappears there, giving exactly n−2 additional edges upon removing 0. Counting shared head/tail, disjoint intervals and unit chains yields 2*C(n,3)+C(n,4)+n−2; the stated local-degree formula follows directly. With ℓ=j−i, a=i−1, b=n−j, simple degree n−1 occurs for ℓ=2 with a,b≤1 (1,2,1,0 for n=3,4,5,≥6) and for ℓ=1 only twice when n=3; ℓ≥3 is never simple. A root r_{iℓ} gives every forbidden pair a two-step graph path, proving diameter 1 for n=3 and 2 for n≥4. Independent SciPy HiGHS feasibility checks compared all 756 root pairs over n=3,...,8 and separately checked edge counts and simple vertices without executing the repository verifier. Finite checks do not replace the all-n argument.

## originality

PASS

Best-of-knowledge PASS for the explicit all-n edge classification, n−2 negative-support new edges, all local degrees and sharp simple-vertex cutoff. Exact predecessor domains were compared: Cho 1999 treats the full signed root polytope and the positive-plus-origin facets; Setiabrata 2021 gives all faces of the positive-plus-origin polytope; Numata et al. 2022 gives general quiver facet criteria and a full-face theorem only under a rank-function hypothesis absent for transitive tournaments. General facet recursion can in principle derive specific edges, so the claimed novelty is the direct closed form and nonorigin structural calculation, not a new root-polytope definition or an assertion that no prior methods apply.

## value

PASS

The positive type-A root polytope is a natural all-dimensional member of the directed-edge-polytope family. An exact combinatorial adjacency test, every local graph degree, the all-n edge polynomial, the precise n−2-edge change caused by deleting the origin, and the sharp disappearance of simple vertices from n=6 are structurally motivated invariants with plausible use in combinatorial polytope comparison and computations. They are neither a one-off small instance nor merely a restatement of a known table; their value does not rely on higher-face classifications or a downstream theorem. Limitations: no higher-dimensional f-vector, Ehrhart theory or exceptional broader quiver theorem is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
