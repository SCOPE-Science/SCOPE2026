# Scientific review

## Correctness — PASS

The polynomial resolvent proof explicitly treats each vertex position relative to the root-to-target path. Every cancellation uses characteristic two and the hypothesis that each nonleaf has even child count. The equality \(S_r+z^2S_{r-1}=1\) also holds at the root by setting \(S_{-1}=0\). These checks prove the complete adjacency-power kernel for every finite permitted tree. Its top coefficient is the nonzero outer product \(\ell\ell^{\mathsf T}\) and its next coefficient is zero, so the index and last-step fraction follow with exact quantifiers, including the one-vertex case. The attached standalone test is corroborative only.

## Originality — PASS (bounded)

The inspected full-text literature on infinite regular rooted-tree shifts and Cayley-tree automata does not establish this undirected finite-tree walk-parity kernel. ArXiv 1205.6785 develops tree-shift and surjectivity theory; arXiv 1211.7362 treats entropy and reversibility of Cayley-tree rules. General adjacency-powers counting walks does not by itself produce these characteristic-two cancellations. The equivalence of the kernel to a resolvent, a walk-parity formula and all matrix powers was checked in the comparison. Prior characteristic-two parity classifications on different graph families cannot specialize to these arbitrary shapes. Search coverage is not exhaustive; unindexed earlier tree-walk or binary spectral results might overlap, and a revised version rather than the 2012 original of one source was available for full-text reading.

## Mathematical value — PASS

The natural object is arbitrary *finite rooted even-branching trees*, not a cherry-picked finite range or a tabulated small instance. The finding gives one universal exact formula for every pair of vertices and every time, a sharp all-input extinction law, and a precise last-step half-population phenomenon. The surprising invariance under changes from two to four or more children is explained by the proof, enabling direct use as a walk-parity propagation identity.

## Boundaries

No assertion covers general trees, non-binary dynamics, or non-neighbour-XOR rules. The small verification calculations do not establish the infinite theorem independently. Human-independent checking of correctness and historical originality remains outstanding.

Self-review: passed. Independent audit: not yet performed.
