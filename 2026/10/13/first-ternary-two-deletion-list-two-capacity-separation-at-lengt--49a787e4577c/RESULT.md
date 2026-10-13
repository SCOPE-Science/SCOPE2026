# First ternary two-deletion list-two capacity separation at length six

## Finding
Let \(\Sigma=\{0,1,2\}\). For integers \(n\ge 2\) and \(L\ge1\), define \(M_3(n,2,L)\) as the largest cardinality of a code \(C\subseteq\Sigma^n\) such that, for every \(u\in\Sigma^{n-2}\), at most \(L\) distinct codewords of \(C\) contain \(u\) as an ordered subsequence. Then \(n=6\) is the **least** integer \(n\ge2\) for which
\[
M_3(n,2,2)>2M_3(n,2,1).
\]
Specifically, \(M_3(6,2,1)=11\), and a displayed 24-word code establishes \(M_3(6,2,2)\ge24>22\). At the shorter lengths, the exact pairs \((M_3(n,2,1),M_3(n,2,2))\), for \(n=2,3,4,5\), are \((1,2),(3,4),(3,6),(6,12)\).

## Assumptions and scope
A two-deletion shadow \(D_2(w)\) comprises all distinct length-\(n-2\) subsequences obtained by deleting exactly two positions of \(w\); repeated deletion choices yielding the same string count once. The list condition means \(|\{w\in C:u\in D_2(w)\}|\le L\) for each \(u\). Codes are not assumed linear. The theorem does **not** determine the exact value of \(M_3(6,2,2)\); it proves a sufficient lower bound of 24.

## Proof
For each \(n\), index all \(3^n\) words and all \(3^{n-2}\) possible deletion outputs in lexicographic order. Write \(A_{u,w}=1\) precisely when \(u\in D_2(w)\). A list-\(L\) code is the support of a zero-one vector \(x\) satisfying \(Ax\le L\mathbf1\).

The files `code_2_1.txt` and `code_2_2.txt` are implicit in `verify.py`; files `code_n_L.txt` for \(3\le n\le6\) contain explicit distinct words attaining every smaller asserted capacity and the length-six values 11 and 24. The verifier independently regenerates deletion shadows and checks all incidence inequalities.

For \(2\le n\le5\), `dual_certificates.json` gives, for each \(L=1,2\), nonnegative rational multipliers \(y_u\) and \(z_w\) for the constraints \(Ax\le L\mathbf1\) and \(x_w\le1\). For every word, the verifier establishes exactly in rational arithmetic
\[
\sum_{u\in D_2(w)}y_u+z_w\ge1.
\]
It follows that every feasible integer \(x\) satisfies \(\sum_wx_w\le L\sum_uy_u+\sum_wz_w\). The eight upper bounds, in increasing \(n\), are \((1,2)\), \((3,9/2)\), \((3,6)\), and \((33/5,63/5)\). Taking integer parts and using the explicit witnesses proves the exact shorter-length capacities.

For \(n=6,L=1\), construct a simple graph on all 729 ternary words, joining two words when their two-deletion shadows are disjoint. A unique-decoding code is exactly a clique in this graph. The provided `clique.cpp` uses a complete branch-and-bound enumeration: at each node its candidate graph is greedily partitioned into independent color classes, whose count upper-bounds any clique extension. It branches on the last remaining candidate or discards it; both alternatives are covered. The color bound prunes only branches incapable of improving the incumbent 11 supplied by `code_6_1.txt`. Running this exact-integer checker visits 1,680,903 recursion nodes and terminates with `best=11`, showing no clique of cardinality 12 exists. The independent 11-word witness proves \(M_3(6,2,1)=11\).

Finally `code_6_2.txt` contains 24 distinct words and the direct shadow test finds no output compatible with more than two; thus \(M_3(6,2,2)\ge24\). Since \(24>2\cdot11\) whereas all shorter capacities satisfy \(M_3(n,2,2)\le2M_3(n,2,1)\), length six is the first strict separation.

## Verification
From the directory containing all attached files, execute `python3 verify.py` with Python 3 and a C++17 compiler `g++`. The program generates all incidence matrices independently of `dual_certificates.json`, checks every rational certificate and every witness, compiles and executes `clique.cpp` with a full graph passed by standard input, and reports `VERIFY_OK`. An actual execution returned all eight exact dual bounds, `CLIQUE best=11 nodes=1680903`, and `VERIFY_OK`. The clique algorithm uses finite exhaustive branching with safe coloring bounds; no numerical optimization solver is required for the final proof.

## Relationship to prior work
Lin (arXiv:2609.26650v1, September 22, 2026) motivates two-deletion list decoding but gives asymptotic binary lower bounds, not this finite ternary threshold. Le and Nguyen (arXiv:1502.02727v3, Section I and Appendix B, Tables III–V) tabulate sizes of particular generalized Helberg residue codes, explicitly *not* maxima over all ternary codes; their length-six value four must not be confused with the global unique-decoding maximum eleven here. Liu, Tjuawinata, and Xing (arXiv:2306.02868) give asymptotic-construction results for nonbinary two-deletion codes. The present exact incidence classification and first separation are not consequences of the cited results.

## Limitations
The result is restricted to alphabet size three, two deletions, and list sizes one and two. It gives a lower bound, not an exact value, for the list-two length-six capacity. Publicly indexed finite-code tables may be incomplete; a previously unindexed identical computation cannot be excluded. The nearest 2026 preprint was available at abstract level during comparison, so a hidden appendix or full-text finite computation is a residual originality risk. Independent examination of the computation and broader literature has not been carried out.

## References
- A. D. Lin, *Lower Bounds for all List-Decodable Deletion Codes*, arXiv:2609.26650v1 (first posted 2026-09-22), https://arxiv.org/abs/2609.26650.
- T. A. Le and H. D. Nguyen, *New Multiple Insertion-Deletion Correcting Codes for Non-Binary Alphabets*, arXiv:1502.02727v3 (2015), https://users.rowan.edu/~nguyen/papers/1502.02727v3.pdf.
- S. Liu, I. Tjuawinata, and C. Xing, *Explicit Construction of q-Ary 2-Deletion Correcting Codes With Low Redundancy*, arXiv:2306.02868 (2023), https://arxiv.org/abs/2306.02868.
