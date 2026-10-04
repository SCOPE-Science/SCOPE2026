# Ternary length-five extremizers cannot use shorter codewords
## Finding
For ternary variable-length non-overlapping codes \(S\subseteq\bigcup_{i=2}^{5}\{0,1,2\}^{i}\), the maximum cardinality is \(17\), while the maximum among codes containing at least one word of length \(<5\) is exactly \(16\). Consequently every \(17\)-word code has all codewords of length \(5\), and the minimum average length at \((q,n,\widetilde C)=(3,5,17)\) is exactly \(5\).

The bound with a shorter word is sharp. One example of size \(16\) contains the word `0001`; an explicit size-\(17\) extremizer with every word of length \(5\) is also supplied by the verifier.

## Assumptions and scope
A variable-length code is taken in the standard sense used by Wang and Wang: no nonempty proper prefix of any codeword may be a suffix of any codeword (including itself), and no distinct shorter codeword may occur as a contiguous subword of a longer one. The alphabet is exactly \(\{0,1,2\}\), and permitted word lengths are \(2,3,4,5\).

For two distinct admissible words \(x,y\), call them compatible when neither is a subword of the other and, for every overlap length \(k\leq\min(|x|,|y|)\), the length-\(k\) prefix of either word differs from the length-\(k\) suffix of the other. A variable-length non-overlapping code is therefore exactly a clique in this finite compatibility graph.

## Proof
There are exactly \(216\) individually self-non-overlapping ternary words of lengths \(2\) through \(5\): respectively \(6,18,48,144\). Construct the compatibility graph on these \(216\) vertices using the two defining conditions above.

An exact branch-and-bound maximum-clique search gives clique number \(17\). The search uses a greedy proper coloring of every remaining induced subgraph as a rigorous upper bound: vertices assigned the same color are pairwise nonadjacent, so a clique can take at most one vertex from each color. The verifier explores every branch not eliminated by this bound and returns an explicit \(17\)-vertex clique, proving both the upper and lower bounds.

To test whether a shorter word can occur in an extremizer, force each of the \(72\) vertices of lengths \(2,3,4\) in turn. For a forced vertex \(v\), every other codeword must lie in its neighborhood, so the largest code containing \(v\) is \(1+\omega(G[N(v)])\). Re-running the same exact clique search for all \(72\) neighborhoods gives maximum \(16\). An explicit \(16\)-word witness containing `0001` shows this upper bound is sharp.

Thus every size-\(17\) code consists only of length-\(5\) words. Its average word length is therefore \(5\). Since a size-\(17\) witness exists, the minimum average length for \((q,n,\widetilde C)=(3,5,17)\) is exactly \(5\).

## Verification
`artifacts/verify_ternary_variable_n5.py` uses only the Python standard library. It regenerates all candidates, checks the graph definition directly, solves the full maximum-clique problem, solves every forced-short-word subproblem, and rechecks the returned witnesses pairwise. The captured output in `artifacts/verification.txt` ends with `VERIFY_OK` and reports

- candidate counts \(6,18,48,144\) by lengths \(2,3,4,5\);
- total candidate count \(216\);
- unrestricted maximum \(17\); and
- maximum with at least one word shorter than \(5\) equal to \(16\).

The exhaustive search is finite; it does not extrapolate from sampling.

## Relationship to prior work
Stanovnik, Moškon, and Mraz computed exact fixed-length optima for small parameters; their work gives the fixed-length ternary length-five frontier but does not impose or analyze the presence of a shorter word in a variable-length code. Wang and Wang proved that a variable-length code of maximum word length \(n\) cannot exceed the fixed-length maximum \(C(n,q)\), and studied the minimum possible average length. Their general lower bound gives only \(\lceil\log_3 17\rceil=3\) for the present cardinality, whereas the finite classification above gives the exact value \(5\).

The closest published-database records located during comparison likewise concern either the fixed-length value at length five or a general stationary occupancy inequality. The latter implies a stronger generic lower bound than \(3\) here but still does not force average length \(5\). The present claim is the exact small-parameter variable-length boundary: allowing even one word shorter than five drops the maximum from \(17\) to \(16\).

## Limitations
The result is confined to the ternary alphabet and maximum word length \(5\). It does not classify all size-\(17\) fixed-length codes up to equivalence, and it does not assert an analogous one-unit drop for other alphabet sizes or lengths. The upper bounds are computer-assisted finite proofs; their validity depends on the graph model matching the stated definition and on the exact branch-and-bound implementation, both of which are exposed in the standalone verifier.

## References
1. L. Stanovnik, M. Moškon, M. Mraz, “In search of maximum non-overlapping codes,” arXiv:2307.12593 (first public version 2023-07-24); later *Designs, Codes and Cryptography* 92 (2024), 1299–1326, DOI 10.1007/s10623-023-01344-z.
2. G. Wang, Q. Wang, “On the maximum size of variable-length non-overlapping codes,” arXiv:2402.18896 (first public version 2024-02-29); later *Designs, Codes and Cryptography* (2024).
3. C. Qin, G. Luo, “A generalized construction of variable-length non-overlapping codes,” *Designs, Codes and Cryptography* 93 (2025), 2229–2243, DOI 10.1007/s10623-025-01585-0.
