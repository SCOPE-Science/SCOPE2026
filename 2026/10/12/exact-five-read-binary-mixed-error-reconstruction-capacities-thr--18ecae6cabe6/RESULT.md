# Exact five-read binary mixed-error reconstruction capacities through length eight

## Finding

For the single-deletion, at-most-one-substitution channel, the maximum cardinality of a binary five-distinct-read reconstruction code is

\[
(M_5(4),M_5(5),M_5(6),M_5(7),M_5(8))=(5,5,6,8,12).
\]

Every claimed value is an unrestricted maximum over all binary codebooks of its indicated length; no linearity or structural restriction is imposed.

## Assumptions and scope

Fix an integer \(4\le n\le8\), with alphabet \(\Sigma=\{0,1\}\). A transmission of \(x\in\Sigma^n\) suffers **exactly one deletion** and **at most one substitution** of a surviving bit. Thus the possible distinct received words form

\[
B(x)=\bigcup_{d=1}^n\left(\{x\text{ with its }d\text{th symbol deleted}\}\cup\bigcup_{j=1}^{n-1}\{\operatorname{flip}_j(x\text{ with its }d\text{th symbol deleted})\}\right).
\]

All occurrences of the same received string are counted **once**. Define \(M_5(n)\) as the maximum size of \(C\subseteq\Sigma^n\) for which

\[
\lvert B(x)\cap B(y)\rvert < 5\quad\text{for every distinct }x,y\in C.
\]

The five-read interpretation assumes five **distinct** observed outputs. At length \(n=4\), some balls have fewer than five elements, so this boundary case includes vacuous pairs. At every length \(n\ge5\), each ball has at least five outputs; the four non-vacuous small lengths are therefore \(5,6,7,8\).

## Proof

**Lower bounds.** The following codebooks are witnesses. For each row every distinct pair has at most four common received words; this is directly verified by both algorithms in the accompanying source files.

- Length \(4\): `0000`, `0001`, `0111`, `1100`, `1111`.
- Length \(5\): `00000`, `00111`, `10001`, `11100`, `11111`.
- Length \(6\): `000000`, `000111`, `011110`, `100001`, `111000`, `111111`.
- Length \(7\): `0000000`, `0000011`, `0001100`, `0011111`, `1100000`, `1110011`, `1111100`, `1111111`.
- Length \(8\): `00000000`, `00000111`, `00011111`, `00110010`, `01001100`, `01111110`, `10000001`, `11001111`, `11100000`, `11110011`, `11111000`, `11111111`.

**Upper bounds and complete search certificate.** For each fixed length \(n\), form the graph \(G_n\) with all \(2^n\) binary length-\(n\) words as vertices, and put an edge between distinct \(x,y\) exactly when \(\lvert B(x)\cap B(y)\rvert\le4\). By definition, admissible codebooks are exactly cliques in \(G_n\), so \(M_5(n)=\omega(G_n)\). Enumerating all received outputs by each deletion position and each of the zero or one surviving-bit substitutions gives the entire adjacency matrix, not a sample.

The standalone `verify.py` constructs these matrices in their entirety, confirms an independent substitute-before-delete construction of every ball, and uses a complete recursive clique search with an upper bound from greedy proper coloring. At a recursive search node with possible extensions \(P\), greedily partition \(P\) into independent color classes of \(G_n\). A clique in any processed prefix can contain at most one vertex of each color. The search takes candidate vertices in **reverse color order**. Before descending to a chosen vertex, it intersects the earlier processed prefix with that vertex's neighbors. If current clique size plus the corresponding prefix color count is no larger than the best clique already found, the branch is safely pruned. Every unpruned vertex choice is eventually traversed, so this computes the exact clique number, not a heuristic maximum.

An independent C++ implementation, `independent_check.cpp`, constructs error balls using integer bit operations and independently implements the same provably exhaustive coloring-bound search. Both programs return the exact clique sizes above, matching every explicit lower-bound witness. Hence the five displayed maxima are proved.

## Verification

Run `python3 verify.py` (Python standard library only); the final line must read `VERIFY_OK`. Optionally compile and run `g++ -O2 -std=c++17 independent_check.cpp -o independent_check && ./independent_check`. It too must report `VERIFY_OK`. The admissibility graph edge counts for lengths \(4\) through \(8\) are respectively \(38,115,552,2917,15194\); the Python search explores respectively \(6,6,7,100,1146\) recursive nodes, while the separately ordered C++ search explores \(5,5,7,78,140\) nodes. Node counts are implementation-specific diagnostics, **not** substitutes for the exhaustive-search proof and executable code.

## Relationship to prior work

Li, Sun and Ge (2026) developed a construction for five distinct reads with redundancy at most \(3\log_2 n+4\), but do not report the exact unrestricted cardinalities at lengths \(4\) through \(8\). Their 2025 predecessor establishes a construction for seven reads, not the present five-read optimum. Song, Cai and Quek (2025) bound mixed-channel ball intersections for longer words under hypotheses not yielding the present unrestricted short-length maxima. Thus the contribution is an exact small-block codebook-size profile for the same channel and fixed read budget, not a new asymptotic code family or an assertion that reconstruction itself was newly introduced.

## Limitations

The theorem concerns the binary alphabet, exactly one deletion, at most one substitution, exactly the read threshold five, and lengths \(4\) through \(8\). It does not determine values at \(n\ge9\), list all optimal codebooks, or establish rates for growing blocklengths. Exact verification relies on complete finite enumeration and sound clique-branch pruning; the numerical edge counts alone do not prove optimality. The inspected literature may omit an earlier unindexed computation of these small-block parameters.

## References

1. Yuling Li, Yubo Sun and Gennian Ge, *Correcting One Deletion and One Substitution with a Constant Number of Reads*, arXiv:2604.25294v1, 28 April 2026. https://arxiv.org/html/2604.25294v1
2. Yuling Li, Yubo Sun and Gennian Ge, *Binary Reconstruction Codes for Correcting One Deletion and One Substitution*, arXiv:2505.04232v1, 2025. https://arxiv.org/html/2505.04232v1
3. Song, Cai and Quek, *Sequence Reconstruction for the Single-Deletion Single-Substitution Channel*, arXiv:2501.03833v4, 2025. https://arxiv.org/html/2501.03833v4
