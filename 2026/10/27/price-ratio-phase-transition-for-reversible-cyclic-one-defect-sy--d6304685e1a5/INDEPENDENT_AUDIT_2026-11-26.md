# Independent mathematical audit

## correctness

PASS

The endpoint of a trajectory from q is q+A−C+kH_q modulo n. For d=gcd(n,k)>1 the starting residue differences modulo d are preserved. For d=1 and a reset, the H_q exhaust the residues modulo n, forcing some trajectory to meet at least n−1 effective b's. Each of its at least n−2 gaps goes from k to 0; ineffective b's do not move that trajectory and positive-price rotations cannot improve on either simple directed arc. Independently the image rank drops by at most one per b. The sum of the two lower bounds is attained: after the j-th b the deleted states are 0,−k,…,−(j−1)k, and translation by −k then b extends the list since k is still present. Equality forces exactly n−1 b's, all effective on the selected trajectory, no outer rotations, and one cheapest arc per gap. The arcs are distinct literal words at a tie, and n=2 has zero gaps and just b. This holds for all positive real prices, not just tested integers. The frozen verifier was inspected, not executed. An independent reverse multi-source shortest-path and path-count computation (python3 reproductions/frozen_math_checks.py, automata) agreed for 162 priced cases and 9 unreachable cases with n≤9; it does not prove the universal claim.

## originality

PASS

Pass the exact bidirectional positive-price optimum and the classification of all literal minimizers together. The gcd obstruction and the forward-only word are not the novelty; the cited and closest mirrored statements inspected do not imply the optimization over words with two independently priced directions. This is a bounded best-of-knowledge judgment.

## value

PASS

This is a natural inverse-generator extension of the cycle-plus-one-merge family. The optimum is not just a unit-cost threshold: it determines when the cheaper letter need not give the cheaper arc, and identifies precisely when and how the set of optimum words grows exponentially. The same exact lower bound rules out cheaper interleavings or extra merges across all parameters and prices in the family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
