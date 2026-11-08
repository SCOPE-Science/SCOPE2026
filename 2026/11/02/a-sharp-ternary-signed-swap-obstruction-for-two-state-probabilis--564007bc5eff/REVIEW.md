# Independent mathematical audit

## correctness

PASS

Two-state stochastic transition maps are affine contractions on [0,1]; any nontrivial unique maximum forces all suffix slopes nonzero and letter maps nonidentity. Swapping adjacent unequal letters changes final acceptance by the signed suffix-product times (1−s_a)(1−s_b)(h_b−h_a). All forced inequalities must embed in a strict fixed-point order, hence the graph must be acyclic. The six inequalities for 0120102 contradict one another for all slope signings. The source verify.py enumerates every 3-symbol-surjective word of length 3..7, every sign pattern and every order; an independent Kahn-topological-sort implementation confirms the exact table (6,36,150,540,1806) with 48 failures at n=7 and 8 canonical classes. Prefixed suffixes retain the inequalities; the cited published three-state construction supplies exact equality, not just a lower bound. The proof is necessary-only for two states; it does not prove the first genuinely ternary word of complexity 3 has length seven.

## originality

PASS

Best-of-knowledge comparison of mathematically equivalent statements and possible stronger coverage, including Resultary semantic search, relevant published repository search, and primary literature readings. Fixed-point inequalities for adjacent transpositions are exactly an order-embeddable directed graph for each slope signing. Gill treats only a binary two-map fixed-point order; the multi-letter simultaneous cycle condition and eight failure classes are not implied by his binary Theorem 4.1. Kjos-Hanssen gives A_P≤3 for all words, a stronger-looking complexity statement, but it provides no ternary exclusion of two-state machines; Gill supplies a binary classification only. The assessed result complements both and is not a corollary of either. Residual priority risks are recorded rather than treating negative searches as novelty proofs.

## value

PASS

This is a nontrivial structural necessary obstruction on a natural multi-letter generalization of probabilistic automatic complexity. It gives the first complete sharp small-length failure census for that obstruction and infinite positive-density families of exact maximal three-state complexity; this is neither a renamed binary classification nor a bare length-seven lookup.

The dated certificate retains the supplied scientific assessment, sources and limitations.
