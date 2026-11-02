# Complete cyclic Lyndon-factor counts for binary order-five de Bruijn sequences

## Finding

Let \(\mathcal B_5\) be the \(2{,}048\) binary de Bruijn cycles of order five, counted up to rotation. Every \(W\in\mathcal B_5\) is a circular word of length \(32\) containing each binary five-letter block exactly once. For each of its \(32\) cuts \(j\), let \(w_j\) be the non-wrapping length-\(32\) linear traversal starting there. Let \(L(w_j)\) be the number of factors in the unique Chen–Fox–Lyndon factorization of \(w_j\), with binary order \(0<1\).

The complete rooted distribution is:

| \(L(w_j)\) | Number of cycle-cut pairs |
|---:|---:|
| 1 | 2,048 |
| 2 | 8,304 |
| 3 | 11,896 |
| 4 | 12,698 |
| 5 | 10,946 |
| 6 | 7,944 |
| 7 | 4,903 |
| 8 | 3,083 |
| 9 | 1,820 |
| 10 | 995 |
| 11 | 480 |
| 12 | 247 |
| 13 | 120 |
| 14 | 39 |
| 15 | 11 |
| 16 | 2 |
| **Total** | **65,536** |

For a cycle \(W\), put \(H(W)=\max_{0\le j<32}L(w_j)\). The *complete* distribution of \(H\) over the \(2{,}048\) cycles is:

| \(H(W)\) | Number of cycles |
|---:|---:|
| 7 | 2 |
| 8 | 94 |
| 9 | 484 |
| 10 | 640 |
| 11 | 421 |
| 12 | 237 |
| 13 | 118 |
| 14 | 39 |
| 15 | 11 |
| 16 | 2 |
| **Total** | **2,048** |

In particular every cycle has **exactly one** cut with \(L=1\); the largest attainable number of factors is \(16\) and exactly two cycle-cut pairs attain it. The two corresponding canonical cycles, each beginning at its unique occurrence of five zeroes, are

\[
\mathtt{00000111110110101001100100010111},
\qquad
\mathtt{00000111110110101001100101110001}.
\]

In both cases the maximizing cut begins at zero-based offset \(5\). All integer tables refer to **factor count**, not the number of distinct Lyndon substrings or the FKM concatenation count.

## Assumptions and scope

A nonempty word \(u\) over the ordered binary alphabet is Lyndon if it is strictly lexicographically smaller than each of its nonidentity cyclic rotations. The Chen–Fox–Lyndon theorem yields a unique expression \(w=u_1\cdots u_t\) with Lyndon factors \(u_1\ge\cdots\ge u_t\). Set \(L(w)=t\). A cyclic de Bruijn sequence is counted modulo rotation, **not** modulo reversal or bit complementation. Every one of its \(32\) distinct cuts is counted separately, with no sentinel inserted. The theorem is exclusively for binary order five.

## Proof

**1. An exhaustive and injective encoding.** Write each five-bit state as \(v=16a+s\), where \(a\in\{0,1\}\) and \(0\le s<16\). For each of the \(2^{16}\) Boolean tables \(g=(g_0,\ldots,g_{15})\), define
\[
F_g(16a+s)=2s+(a\oplus g_s).
\]
Here \(\oplus\) means exclusive OR. The two predecessors with common four-bit suffix \(s\) map to the two distinct five-bit states \(2s\) and \(2s+1\), so each \(F_g\) is a permutation of the \(32\) states. Its orbit of \(0\) visits all \(32\) states if and only if it is one permutation cycle. In that case, the high bits of the successive visited states form a binary de Bruijn cycle: the successive states are exactly its five-bit cyclic factors.

Conversely, for any order-five de Bruijn cycle, the next-symbol rule induces a permutation of five-bit windows. Since all thirty-two windows occur, the two different windows sharing a four-bit suffix must have different successor bits, or their successor five-bit windows would coincide. Thus their successor bits are complementary, yielding exactly one Boolean table \(g\). Since the window \(\mathtt{00000}\) occurs once, anchoring at it gives exactly one canonical word per cycle. Hence the above test of all \(65{,}536\) tables neither omits nor duplicates any cycle.

**2. An independent exhaustive construction.** Consider the binary order-four de Bruijn directed multigraph: vertices are four-bit words and edges are five-bit words; an edge goes from its first four bits to its last four. Every order-five cycle is an Euler tour using each of the \(32\) labeled edges once. Anchor at the unique all-zero five-bit edge. Exhaustive two-branch depth-first traversal, rejecting previously used edges and requiring closure at the origin, returns exactly the same \(2{,}048\) canonical cycles as the Boolean-table enumeration. This checks both the cycle count and the encoded words without assuming the first algorithm's output is complete.

**3. Exhaustive factor verification.** For each canonical cycle and each of its \(32\) rotations, `checker.py` computes the Chen–Fox–Lyndon factorization in two ways: Duval's standard linear algorithm, and a separate definition-level search for the longest Lyndon prefix of the remaining suffix, testing each candidate against **all** proper cyclic rotations. The latter additionally checks that the obtained Lyndon factors form a non-increasing sequence, which independently certifies them as the unique Chen–Fox–Lyndon factorization. The implementations agree on all \(65{,}536\) traversals. Exact integer counters then give both tables and the two extreme witnesses. All input tables, cuts and candidate Lyndon prefixes are fully exhausted, not randomly sampled.

**4. The unique one-factor root.** Every de Bruijn cycle is primitive: if it had proper period, its cyclic length-five factors could not all be distinct. A primitive necklace has exactly one lexicographically least rotation, which is a Lyndon word. A rooted traversal has \(L=1\) exactly when it is Lyndon. Therefore each cycle contributes exactly one such root, independently explaining the first entry \(2{,}048\).

Together the exhaustive bijection, two separate cycle constructions, two factorization checks and exact counters prove the finite classification.

## Verification

Run `python3 checker.py` in a standard Python environment (version \(3.9\) or later; no third-party packages). It independently computes all cycle sets and all root factorizations, checks the displayed distributions and two maximizing cuts, and prints `VERIFY_OK` on success. The run that produced this package printed `VERIFY_OK`, \(2{,}048\) cycles and \(65{,}536\) roots, with the two distributions displayed above. The checker is an exact exhaustive proof-by-computation for a fixed finite space; it does not extrapolate to higher orders.

## Relationship to prior work

The Fredricksen–Maiorana construction connects de Bruijn cycles to a particular concatenation of Lyndon words. Kociumaka, Radoszewski and Rytter analyze Lyndon ranking and decoding of the lexicographically least de Bruijn sequence, including the FKM construction. Daykin analyzes algorithms for the *general* unique maximal Lyndon factorization. Bonomo and collaborators study Lyndon factorization together with conjugates, BWT and suffix sorting. The present theorem instead enumerates the **Chen–Fox–Lyndon factor count of every linear rotation of every order-five de Bruijn cycle**. A prescribed list of Lyndon words used to construct one special cycle does not give this rooted full-population factor-count distribution, and the cited general-purpose algorithms do not supply the numerical classification.

## Limitations

The result is finite and specific to order five, standard binary alphabet ordering and the unique non-increasing Chen–Fox–Lyndon factorization. It does not classify higher orders, other alphabet sizes, factor lengths or distinct Lyndon substrings. Priority against unindexed tables is not established conclusively. Independent validation has not been performed.

## References

1. T. Kociumaka, J. Radoszewski and W. Rytter, *Efficient Ranking of Lyndon Words and Decoding Lexicographically Minimal de Bruijn Sequence*, arXiv:1510.02637, first submitted 9 October 2015, https://arxiv.org/abs/1510.02637. Primary historical source.
2. H. Fredricksen and J. Maiorana, *Necklaces of beads in k colors and k-ary de Bruijn sequences*, Discrete Mathematics 23 (1978), 207–210, https://doi.org/10.1016/0012-365X(78)90002-X.
3. D. E. Daykin, *Algorithms for the Lyndon unique maximal factorization*, Journal of Combinatorial Mathematics and Combinatorial Computing 77 (2011), 65–74, https://combinatorialpress.com/jcmcc-articles/volume-077/algorithms-for-the-lyndon-unique-maximal-factorization/.
4. S. Bonomo, S. Mantaci, A. Restivo, G. Rosone and M. Sciortino, *Suffixes, Conjugates and Lyndon Words*, Developments in Language Theory (2013), 131–142, https://doi.org/10.1007/978-3-642-38771-5_13.
