# Single-exponential shuffle-square recognition from compressed runs

## Finding
Let \(w=\sigma_1^{L_1}\cdots\sigma_r^{L_r}\) be a nonempty word over any finite alphabet, represented by its \(r\) maximal constant runs, with each length \(L_i\geq1\) given in binary. One can decide whether \(w\) is a shuffle square (a partition of all its positions into two identical order-preserving subsequences) using **at most \(3^r\) instances of capacitated exact-degree matching**, each on at most \(r\) vertices and at most \(r\) edges and with binary-encoded capacities. Hence recognition, and reconstruction of a compressed witnessing split, take time
\[
3^r\,\operatorname{poly}(r,S),\qquad S=\sum_{i=1}^r\lceil\log_2(L_i+1)\rceil+\text{symbol-encoding size}.
\]
This is a deterministic fixed-parameter algorithm in the number of runs, even when the uncompressed length is exponentially larger than the input description. The reduction uses at most \(r\) genuinely free integer quantities, one per input run. No explicit expansion of the word is required.

## Assumptions and scope
The input alphabet is finite but need not have bounded cardinality. Adjacent \(\sigma_i\) are distinct because the runs are maximal. Equality tests on input symbols are included in \(S\). A shuffle square means that every position is assigned to track \(A\) or \(B\) and that the induced subsequences are **identical**, not merely anagrams, rotations or reversals. The empty word, if admitted, is trivially a shuffle square; the theorem treats nonempty words. Standard polynomial-time algorithms for capacitated integer \(b\)-matching (or exact-degree factors) are taken as an external algorithmic ingredient, using binary-encoded integral demands and capacities.

## Proof
**Run allocation.** Fix any allocation of the positions to the two tracks. Write \(x_i\) for the number of positions of run \(i\) sent to \(A\). The resulting track words are exactly
\[
A=\sigma_1^{x_1}\cdots\sigma_r^{x_r},\qquad B=\sigma_1^{L_1-x_1}\cdots\sigma_r^{L_r-x_r},
\]
where empty blocks are deleted. The order *within* a monochromatic input run cannot change either track word. Conversely, any integers \(0\le x_i\le L_i\) can be realized by assigning the first \(x_i\) positions of run \(i\) to \(A\) and the remainder to \(B\). Thus the existence of equal tracks is equivalent to the existence of such integer allocations with \(A=B\).

**Three-state patterns.** For every run choose exactly one of \(x_i=0\), \(x_i=L_i\), and \(1\le x_i\le L_i-1\). There are at most \(3^r\) choices. Discard the middle state if \(L_i=1\). Each choice specifies which run fragments appear in each track; after merging adjacent equal letters, it therefore determines the two sequences of *run symbols*, independently of the still-unknown middle-state counts. If those sequences differ, equal track words are impossible.

**Exact-degree graph.** Suppose the two run-symbol sequences coincide and have \(m\le r\) terms. Number their corresponding runs \(1,\ldots,m\). Create one vertex per term and one edge \(e_i\) for each middle-state input run \(i\). If the fragment from input run \(i\) belongs to output run \(p\) in \(A\), and to output run \(q\) in \(B\), join vertices \(p,q\) by \(e_i\); allow \(p=q\), when this is a loop contributing twice to its vertex degree. The edge multiplicity is the integer \(x_i\), with bounds \(1\le x_i\le L_i-1\). (Equivalently, shift the edge multiplicity by one to obtain lower bound zero.)

To see the vertex demands, for an output run \(j\), denote by \(I^A_j\), respectively \(I^B_j\), the set of input-run fragments that contribute to it on the indicated track. Equality of corresponding run lengths gives
\[
\sum_{i\in I^A_j}x_i=\sum_{i\in I^B_j}(L_i-x_i).
\]
Replace the fixed values \(x_i=0\) and \(x_i=L_i\) according to the chosen three-state pattern. Move all remaining variables to the left. A middle-state \(x_i\) occurs once on the left when its \(A\) fragment belongs to run \(j\), and once when its \(B\) fragment belongs to run \(j\). Hence the equation has precisely the form
\[
\sum_{i:e_i\ni j}x_i=d_j,
\]
where loops count twice, \(d_j\) is an explicitly computed integer, and an edge occurs with the indicated incidence. These are exactly the demands in a capacitated undirected integer \(b\)-matching instance. Any negative demand makes the pattern infeasible.

**Equivalence.** A feasible exact-degree matching supplies middle-state allocations \(x_i\) obeying every run-length equality; the two output sequences already have identical symbols, so \(A=B\), and the position assignment just described realizes the shuffle square. Conversely, a shuffle-square partition supplies allocations and exactly one three-state pattern; the same equations are satisfied, so that pattern's graph has a feasible exact-degree matching. No other constraints are hidden.

**Complexity.** Each pattern has at most \(r\) vertices and at most \(r\) edges; degrees, capacities and bounds have \(O(S)\) bits. Exact-degree capacitated integer \(b\)-matching in a general multigraph (including loops) can be decided and a feasible multiplicity vector recovered in polynomial time in this binary input size by standard \(b\)-matching/polyhedral algorithms; see the references. Applying this to at most \(3^r\) patterns proves the stated running-time bound. Returning each assigned count \(x_i\), rather than expanding the positions, gives a compressed witness of \(O(rS)\) bits.

## Verification
The included `verify.py` independently enumerates all binary words of lengths at most \(10\) and all ternary words of lengths at most \(7\), including the empty word as a boundary test: a total of \(5{,}327\) words. It compares a direct search through position subsets against a separate run-count search, the symbolic run-length equations, and the exact-degree incidence graph equations for each candidate allocation. It also validates a positive instance with \(117\)-bit run lengths without expansion. Executing `python3 verify.py` prints `RLE_SHUFFLE_REDUCTION_PASS` on success. These finite tests check the reduction's implementation; the infinite complexity bound is proved by the reduction and the cited classical matching algorithm, not by extrapolation from testing.

## Relationship to prior work
Grytczuk, Pawlik and Pleszczyński (2023) formulate shuffle-square variants and emphasize the binary recognition problem. Bulteau and Vialette established NP-completeness of binary shuffle-square recognition. Grytczuk, Pawlik and Ruciński (2025) give a general ordered nest-free-graph characterization and complete low-run classifications. Their characterization potentially yields a less compact parameterized feasibility procedure by introducing edge multiplicities between pairs of runs. The present claim is instead the explicit \(3^r\)-pattern **linear-size** exact-degree reduction, including a single-exponential factor and polynomial dependence on *binary-compressed* run lengths. It does not claim that fixed-parameter tractability by run count, in isolation, could not also be inferred from their graph model. The polynomial matching subroutine is classical and is not claimed new.

## Limitations
The displayed complexity is a parameterized upper bound, not a proven optimal dependence on \(r\), nor a polynomial-time algorithm in unrestricted \(r\). The polynomial matching routine is imported from published theory rather than implemented in `verify.py`; the verifier checks the problem-to-graph equivalence and small instances, not a production blossom implementation. The claim concerns perfect equality of two full scattered subsequences, not the maximum length of partial twins, multiway shuffles, or approximation. A more efficient or equivalent reduction may exist under alternative terminology; no absolute priority or independent certification is asserted.

## References
1. J. Grytczuk, B. Pawlik, M. Pleszczyński, *Variations on shuffle squares* (first public preprint August 26, 2023), arXiv:2308.13882, https://arxiv.org/abs/2308.13882 . The paper lists primary MSC2020 68R15.
2. J. Grytczuk, B. Pawlik, A. Ruciński, *Shuffle squares and nest-free graphs* (March 27, 2025), arXiv:2503.22043, https://arxiv.org/abs/2503.22043 .
3. L. Bulteau, S. Vialette, *Recognizing binary shuffle squares is NP-hard*, Theoretical Computer Science 806 (2020), 116–132.
4. A. N. Letchford, G. Reinelt, D. O. Theis, *Odd Minimum Cut Sets and b-Matchings Revisited*, SIAM J. Discrete Math. 22 (2008), 1480–1487, doi:10.1137/060664793. Polynomial separation for capacitated b-matching polyhedra.
5. H. N. Gabow, P. Sankowski, *Algorithms for Weighted Matching Generalizations I: Bipartite Graphs, b-matching, and Unweighted f-factors*, SIAM J. Comput. 50 (2021), 440–486, doi:10.1137/16M1106195.
