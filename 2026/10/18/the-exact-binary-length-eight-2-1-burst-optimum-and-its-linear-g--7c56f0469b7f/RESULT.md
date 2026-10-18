# The exact binary length-eight \((2,1)\)-burst optimum and its linear gap

## Finding
For the binary exact \((2,1)\)-burst channel, which replaces two adjacent bits by one arbitrary bit, define \(A_{2,1}(8)\) as the greatest size of a length-eight code with disjoint received-word sets. Then
\[
A_{2,1}(8)=14.
\]
Moreover, the largest **binary linear** correcting code under the same channel has exactly \(8\) words. Thus the unrestricted optimum is nonlinear and exceeds the linear optimum by \(6\) words. All received balls have exactly \(8\) distinct seven-bit outputs, so the ordinary sphere-packing estimate gives \(A_{2,1}(8)\le16\), which is strictly unattainable.

## Assumptions and scope
A transmitted word is \(x\in\{0,1\}^{8}\). At a chosen position \(i\in\{1,\ldots,7\}\), remove the symbols in positions \(i,i+1\) and insert \(b\in\{0,1\}\) **at that position**. Denote the set of all distinct length-seven outputs by \(B(x)\). A correcting code is a subset \(C\subseteq\{0,1\}^{8}\) with \(B(x)\cap B(y)=\varnothing\) whenever \(x,y\in C\) are distinct. The channel performs exactly this one burst; it does not allow an arbitrary deletion and an insertion at unrelated positions. The statement concerns only length \(8\) and the binary alphabet.

Write an integer between \(0\) and \(255\) as an eight-bit binary word, with leading zeroes retained. An explicit optimal code is
\[
C=\{12,21,34,51,72,87,126,129,178,187,207,212,237,240\}.
\]
An eight-word linear correcting code is the binary span of the three eight-bit vectors represented by \(21,79,164\).

## Proof
**Ball construction.** For each of the \(256\) possible source words, enumerate the seven starting positions and two replacement bits. There are exactly \(8\) distinct outputs for each source word, as established by the full enumerator in `proof_checker.cpp` and independently by string slicing in `verify_independent.py`. This implies the ordinary packing bound \(\lfloor 2^7/8\rfloor=16\). The integer list above contains \(14\) distinct source words. Direct output-set intersection checks, performed in both supplied programs, establish that their balls are pairwise disjoint. Consequently \(A_{2,1}(8)\ge14\).

**Finite upper-bound certificate.** Form a graph \(G\) on the \(256\) source words; distinct vertices are adjacent precisely when their output balls are disjoint. A correcting code is exactly a clique of \(G\). The stand-alone C++17 program `proof_checker.cpp` reconstructs all balls, then all graph edges, with integer bit operations. It exhaustively rules out a clique of size \(15\) or more by the following exact branch-and-bound method. At any recursive state, \(P\) contains all possible extension vertices compatible with the selected prefix. Greedily partition the induced graph on \(P\) into classes of mutually nonadjacent vertices, and order the vertices by their nondecreasing class number. Any clique in the first \(j\) classes has at most \(j\) vertices. Traverse the ordered vertices backward: if the prefix size plus the current class number is less than \(15\), no remaining branch can reach \(15\); otherwise branch on including that vertex, replace \(P\) by its neighbors inside \(P\), and then remove the vertex from the remaining sibling branches. Every possible clique either belongs to such an inclusion branch or survives in a later exclusion branch. Hence the pruning cannot discard any clique of size at least \(15\).

The implementation checks all \(256\) generated ball sizes and graph symmetry, then completes the recursion with no size-\(15\) clique, visiting \(430977\) recursive states. Its exact finite proof together with the exhibited \(14\)-word code gives \(A_{2,1}(8)=14\). A separate string-based enumerator builds the \(128\)-row by \(256\)-column received-word incidence matrix and an integer set-packing model; an independent mixed-integer optimization returns the same optimum, but the branch-and-bound program rather than the optimizer report is the stand-alone upper-bound certificate.

**Linear optimum.** The three displayed binary vectors are independent and their eight binary sums have pairwise disjoint received sets, which both programs check. Conversely, every binary linear code has power-of-two cardinality, and the unrestricted bound \(14\) excludes any linear code of cardinality \(16\) or higher. Thus the linear maximum is exactly \(8\).

## Verification
From the package directory, run `g++ -std=c++17 -O2 proof_checker.cpp -o proof_checker` and then `./proof_checker`. This checks source/output enumeration, all ball cardinalities, witness feasibility, the linear span and the exhaustive upper-bound search. Its success line is `VERIFIED maximum size 14, maximum linear size 8, packing bound 16, search nodes 430977`.

As a separate cross-check, run `python3 verify_independent.py` with NumPy and SciPy installed. It uses string slicing, a distinct incidence-matrix construction and a mixed-integer optimizer; its success line is `INDEPENDENT_CHECK_OK 14 8 14`. The C++17 proof checker needs only the standard library; the Python test is supplementary. Neither program uses precomputed channel tables.

## Relationship to prior work
Lu and Zhang define general exact \((t,s)\)-burst errors, prove constancy of their received-ball size and derive a sphere-packing inequality. Their general result gives the present upper bound \(16\) but not the attained value \(14\). Schoeny, Wachter-Zeh, Gabrys and Yaakobi give specific \((2,1)\)-burst-correcting constructions and general redundancy bounds without identifying this short-block optimum. The analogous published exact binary \((3,1)\)-burst profile at length \(8\) concerns deleting **three**, not two, neighboring symbols. A published at-most-one two-substring-edit benchmark permits more operations than the fixed \((2,1)\)-burst channel; its length-eight optimum does not determine the restricted optimum \(14\). A finite binary deletion-plus-arbitrary-substitution benchmark likewise concerns a different, broader channel. Statement-level searches did not locate a published theorem that determines both the present nonlinear and linear optima.

## Limitations
The upper-bound result is a finite exhaustive certificate for exactly \(256\) length-eight inputs, not a theorem for arbitrary length. Reproducibility depends on compiling/running the complete C++ program; the independent mixed-integer check is not itself the mathematical certificate. The literature comparison supports originality relative to inspected primary sources and published results but cannot exclude unindexed tables or differently named equivalent computations. No independent external audit is claimed.

## References
1. Z. Lu and Y. Zhang, *t-Deletion-s-Insertion-Burst Correcting Codes*, arXiv:2201.10259v1, first posted 25 January 2022; https://arxiv.org/abs/2201.10259 .
2. C. Schoeny, A. Wachter-Zeh, R. Gabrys and E. Yaakobi, *Codes Correcting a Burst of Deletions or Insertions*, arXiv:1602.06820v1, first posted 22 February 2016; https://arxiv.org/abs/1602.06820 .
3. *Exact binary \((3,1)\)-burst code sizes through length \(8\)*, public result: https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-binary-3-1-burst-code-sizes-through-length-8--531630cac2ea .
4. *Exact initial profile for binary \(2\)-substring-edit codes*, public result: https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-initial-profile-for-binary-2-substring-edit-codes--cadcb4698a54 .
5. *Exact binary one-deletion one-substitution codes at lengths seven and eight*, public result: https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-binary-one-deletion-one-substitution-codes-at-lengths-seve--49b7ae777343 .
