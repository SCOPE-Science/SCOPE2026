# Independent mathematical audit

## correctness

PASS

For an outside vertex in part i, its distance multiset is {|W|-a_i copies of 1, a_i copies of 2}; two outside vertices in distinct parts are adjacent and collide exactly when their active occupancies are equal. Fixing k active parts, k distinct nonnegative occupancies have sum at least 0+...+(k-1), with equality feasible for sorted active sizes m_j exactly when m_j>=j. For fixed k, replacing any active part by a larger one preserves feasibility and weakly decreases |W|, so the optimum uses the k largest parts, giving precisely the set K and displayed minimum. This establishes the universal formula; the verifier exhausts all multipartite isomorphism types through order eleven as a stress test. One nonessential post-proof explanatory sentence in RESULT.md says the r=2 value one comes from 'one active part with occupancy 0'; that wording is imprecise for general K_{a,b}, but the preceding criterion/formula and the conclusion lodim=1 are correct (for K_{1,1}, k=1 gives one; otherwise the feasible k=2 profile 0,1 gives one). It is not used in the proof.

## originality

PASS

The 2025 full primary paper introduces local outer multiset dimension and proves the bipartite value one plus several other small-diameter families; whole-document inspection found no multipartite theorem. The published complete-multipartite Resultary theorem concerns the stronger global outer multiset dimension, where every pair outside W must be distinguished, and therefore does not imply this local-adjacency formula. The 2026 survey abstract advertises outer-multiset diameter-two bounds and other multiset results but not an arbitrary complete-multipartite local-outer formula. No covering exact theorem was found.

## value

PASS

Complete multipartite graphs are a standard dense diameter-two/join family, and the local-outer parameter was introduced specifically to make such multiset identification finite. The theorem gives a complete arbitrary-part-size optimization law and cleanly separates it from the much stronger global outer invariant. This is a natural exact family result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
