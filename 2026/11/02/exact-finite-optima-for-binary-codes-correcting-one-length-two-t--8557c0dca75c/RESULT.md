# Exact finite optima for binary codes correcting one length-two tandem duplication

## Finding
Let \(n\) be an integer with \(3\le n\le15\). Write \(M(n)\) for the largest number of distinct binary words of length \(n\) that can be transmitted without ambiguity after **exactly one** tandem duplication of a block of length two. Thus each word \(x=uvw\) with \(|v|=2\) can produce \(uvvw\), and the sets of all resulting length-\(n+2\) words must be pairwise disjoint for distinct members of a code.

The exact optima are:

| \(n\) | \(M(n)\) | Largest code correcting any number of length-two duplications |
|---:|---:|---:|
| 3 | 8 | 8 |
| 4 | 16 | 16 |
| 5 | 28 | 28 |
| 6 | 48 | 48 |
| 7 | 84 | 80 |
| 8 | 148 | 132 |
| 9 | 260 | 216 |
| 10 | 460 | 352 |
| 11 | 816 | 572 |
| 12 | 1440 | 928 |
| 13 | 2552 | 1504 |
| 14 | 4568 | 2436 |
| 15 | 8224 | 3944 |

The third column is the known unique-root-class benchmark, recomputed by counting the decomposition classes below, not an asserted new optimum for unbounded errors. Already at \(n=7\), one-error correction admits strictly more codewords than correcting arbitrarily many length-two duplications.

## Assumptions and scope
The alphabet is \(\{0,1\}\); block length is fixed at two; source words have exactly \(n\) symbols; a channel output is produced by copying one consecutive block of exactly two symbols and placing it immediately after its original. A code is valid precisely when no two distinct codewords share an output. The results are finite, for all integers \(3\le n\le15\), with no assertion for larger \(n\), different alphabets, or different duplication lengths. When the channel allows *at most* one duplication, the same maximum applies, since unchanged outputs have length \(n\) and duplicated outputs have length \(n+2\).

## Proof
**1. An invertible derivative.** For a binary word \(x=x_0\cdots x_{n-1}\), retain its first two bits and take the length-\(n-2\) derivative \(z_i=x_{i+2}\oplus x_i\). The original word is recovered uniquely from these first two bits and the derivative by the recurrence \(x_{i+2}=x_i\oplus z_i\). A length-two tandem duplication leaves the first two bits unchanged and inserts exactly two zero symbols consecutively in the derivative. Conversely, insertion of two consecutive zeros in a derivative arises from such a tandem duplication. This is the fixed-duplication derivative correspondence of Jain--Farnoud--Schwartz--Bruck [1].

**2. Natural disjoint classes.** Write the derivative uniquely as
\[
z=0^{r_1}1\,0^{r_2}1\cdots1\,0^{r_m},\qquad r_j=\rho_j+2s_j,
\]
where \(m\ge1\), \(\rho_j\in\{0,1\}\), and \(s_j\) are nonnegative integers. Any tandem duplication increases just one \(s_j\) by one; the initial two bits, the number \(m-1\) of ones, and the ordered parity vector \((\rho_1,\ldots,\rho_m)\) are unchanged. Hence different such classes cannot share a channel output. Let \(L=n-2\), \(r=\sum_j\rho_j\), and
\[
t=\frac{L-(m-1)-r}{2}.
\]
For each admissible choice with integer \(t\ge0\), the class consists exactly of the integer compositions \((s_1,\ldots,s_m)\) of \(t\). There are four choices of the initial pair of bits and \(\binom mr\) choices of the parity vector.

**3. Confusability inside one class.** For distinct compositions \(s\) and \(s'\), their sets of possible one-step duplicated outputs intersect exactly when \(s+e_i=s'+e_j\) for some coordinate vectors \(e_i,e_j\). Since both compositions have the same sum, this is equivalent to \(\|s-s'\|_1=2\). Define \(G(m,t)\) to have all nonnegative integer \(m\)-tuples summing to \(t\) as vertices, adjacent if their \(\ell_1\) distance is two, and write \(\alpha(m,t)\) for its independence number. Then the exact maximum satisfies the identity
\[
M(n)=4\sum_{m=1}^{L+1}\ \sum_{\substack{0\le r\le m\\L-m+1-r\text{ is a nonnegative even integer}}}\binom mr\,\alpha\!\left(m,\frac{L-m+1-r}{2}\right).
\]
This equality proves both an upper bound (the sum of classwise independence bounds) and the attainability of that sum (choose a maximum independent set independently in each class and invert the derivative).

**4. Exact finite independence computation.** For the stated range of \(n\), the formula uses precisely the 56 composition graph types listed in `alpha.csv`, the largest with 126 vertices. The supplied standalone `verify.cpp` independently regenerates every vertex and compatibility edge and performs an **exhaustive maximum-clique search on the complement** of each \(G(m,t)\). Its greedy coloring partitions the remaining compatibility candidates into independent color classes and provides the rigorous upper bound of one selected vertex per color; a branch is pruned only if this bound cannot improve the largest already exhibited clique. Every unpruned candidate branch is explored. At completion the computed value is therefore an upper bound, while the stored clique is a matching lower-bound witness. The code checks the \(\ell_1\) distances of its witnesses and, after inverting all derivative classes, independently constructs **every codeword and every one-step descendant**, checking pairwise output disjointness.

Summing the verified independence numbers with the integer coefficients in the displayed identity yields the table. There is no probabilistic estimate, timeout-based inference, or unproved extrapolation: the finite exhaustive computation is part of the proof for this bounded domain.

## Verification
Compile and run `verify.cpp` with a C++17 compiler supporting the standard library and GCC's set-bit iteration extension:

```sh
g++ -std=c++17 -O3 verify.cpp -o verify
./verify
```

It must print lines `n,optimal,distinct_descendants` for all 13 orders and terminate with `VERIFY_OK`. The program derives the table, rather than relying solely on checking declared values. The independent `crosscheck.py` reconstructs the **original duplication channel directly**, without using the derivative classes, and solves the complete finite conflict graph for each \(3\le n\le9\), terminating with `CROSSCHECK_OK`. Run it using `python3 crosscheck.py`. The 56 exact graph values are archived separately in `alpha.csv` for inspection and reuse.

## Relationship to prior work
Jain, Farnoud, Schwartz and Bruck [1], first public on June 1, 2016, introduced the derivative mapping and a general reduction to constant-weight \(\ell_1\) codes; they proved the optimal sizes of the **unbounded-duplication** codes, but explicitly left optimal finite-error composition-code constructions open after their Theorem 20. The contribution here is the complete exact classwise computation and resulting single-error optimum sequence for \(3\le n\le15\), **not** the derivative mapping or the reduction itself. Lenz, Wachter-Zeh and Yaakobi [2] give bounds and constructions for tandem and palindromic duplication codes, without this finite exact optimum table. Kovačević and Tan [3] establish asymptotic optimality of fixed-length-duplication constructions and do not imply these finite exact cardinalities. Chee and coauthors [4] consider arbitrary short-length duplications over a ternary alphabet rather than the present single-length binary channel.

The earlier discrete-simplex code paper of Kovačević and Vukobratović [5] studies the **same nonnegative-composition metric**, but characterizes *perfect* codes (sphere-tilings), not finite maximum-distance-two independent-set packings; its theorems do not supply the present independence numbers. Brouwer, Cioabă, Haemers and Vermette [6] and Ahadi, Mollahajiaghaei and Dehghan [7] study **simplicial rook graphs**, whose adjacency means that two compositions differ in precisely two coordinates, including transfers of multiple units. Here adjacency requires *a single-unit transfer* (\(\ell_1\)-distance exactly two). For example, the rook graph on the four compositions of three into two parts is complete (independence number one), while our unit-transfer graph is a four-vertex path (independence number two). Thus the known rook-graph independence formulas and asymptotic bounds are not exact formulas for the graph needed here.

A closely related research record establishes the **edge count** of a fixed-length-duplication confusability graph, not its independence number. Edge counts do not determine independence numbers in general, and that result does not imply the table. Other nearby records involve palindromic duplication, burst edits, or inverse branching and likewise do not establish the current maxima.

## Limitations
The certified range ends at \(n=15\), and the search does not enumerate all optimal codebooks. The lower bounds depend on the correctness of the supplied exhaustive clique-search algorithm and its fully specified finite instances; the independent direct-channel cross-check covers only lengths through nine. Independently replicated computations and historical-priority review are not claimed. Unindexed earlier tables or stronger results may exist. No asymptotic formula, general block-length theorem, or decoding-complexity bound is established.

## References
[1] S. Jain, F. Farnoud, M. Schwartz and J. Bruck, *Duplication-Correcting Codes for Data Storage in the DNA of Living Organisms*, arXiv:1606.00397 (first public 2016-06-01), https://arxiv.org/abs/1606.00397.

[2] A. Lenz, A. Wachter-Zeh and E. Yaakobi, *Duplication-Correcting Codes*, arXiv:1712.09345 (2017), https://arxiv.org/abs/1712.09345.

[3] M. Kovačević and V. Y. F. Tan, *Asymptotically Optimal Codes Correcting Fixed-Length Duplication Errors in DNA Storage Systems*, arXiv:1808.10328 (2018), https://arxiv.org/abs/1808.10328.

[4] Y. M. Chee, J. Chrisnata, H. M. Kiah and T. T. Nguyen, *Deciding the Confusability of Words under Tandem Repeats*, arXiv:1707.03956 (2017), https://arxiv.org/abs/1707.03956.

[5] M. Kovačević and D. Vukobratović, *Perfect Codes in the Discrete Simplex*, arXiv:1307.3142 (first public 2013-07-11), https://arxiv.org/abs/1307.3142.

[6] A. E. Brouwer, S. M. Cioabă, W. H. Haemers and J. R. Vermette, *Notes on simplicial rook graphs*, published online 2015-09-09, https://doi.org/10.1007/s10801-015-0633-y.

[7] A. Ahadi, M. Mollahajiaghaei and A. Dehghan, *On the maximum number of non attacking rooks on a high-dimensional simplicial chessboard*, arXiv:2102.00535 (2021), https://arxiv.org/abs/2102.00535.
