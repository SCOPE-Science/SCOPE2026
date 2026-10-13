# Affine rigidity of binary eight-word maximum-distance symbol-pair codes

## Finding

Every eight-word binary code meeting the cyclic symbol-pair Singleton bound at minimum distance \(n-1\) is affine; no nonlinear exception exists. Its block length is necessarily \(3\le n\le7\). The exact numbers of labeled eight-word codes are

| Length \(n\) | Codes containing \(0\) | All labeled codes |
| --- | ---: | ---: |
| 3 | 1 | 1 |
| 4 | 1 | 2 |
| 5 | 5 | 20 |
| 6 | 4 | 32 |
| 7 | 2 | 32 |

In particular, the longest feasible block length is seven; every code attaining this endpoint is an affine translate of one of two three-dimensional linear subspaces, and the two subspaces are related by reversal of cyclic coordinate order.

## Assumptions and scope

Coordinates of \(\mathbb F_2^n\) are indexed by \(\mathbb Z/n\mathbb Z\). For any two words \(x,y\), define

\[
d_{\mathrm p}(x,y)=\left|\left\{i\in\mathbb Z/n\mathbb Z:\ (x_i,x_{i+1})\ne(y_i,y_{i+1})\right\}\right|.
\]

Codes are **unordered subsets of eight distinct words**; bit positions are fixed and labeled. There is no quotient by rotation, reflection, word permutation, or coordinate complement in the counts. The property \(d_{\mathrm p}(C)\ge n-1\) is required of every distinct pair; no assumption of linearity is made. The stated maximum distance always equals \(n-1\) for these codes.

## Proof

**1. Cardinality and length bounds.** If two words agree on three consecutive binary coordinates, they agree on at least two overlapping received pairs. Their pair-distance is at most \(n-2\). Consequently, projection of a code of minimum pair-distance at least \(n-1\) onto any three consecutive coordinates is injective, giving at most \(2^3=8\) codewords. Thus eight is the symbol-pair Singleton maximum.

For eight codewords there are \(\binom82=28\) unordered pairs of distinct words. At a fixed cyclic position, their observed two-bit symbols belong to four categories. The number of pairs with identical symbols is at least four: among eight objects and four categories, the number \(\sum_{j=1}^4\binom{m_j}{2}\) is at least four for nonnegative integer multiplicities summing to eight, with equality at \((2,2,2,2)\). Therefore, the sum of all pair-distances over the 28 word-pairs is at most \(24n\). The assumed lower bound gives \(28(n-1)\le24n\), whence \(n\le7\). This argument is valid for arbitrary nonlinear codes.

**2. Exact finite classification.** Translation \(C\mapsto C+z\), defined by coordinatewise XOR, preserves cyclic pair-distance. Translate any code to contain \(0\). For each \(n\in\{3,4,5,6,7\}\), put

\[
V_n=\{u\in\{1,\ldots,2^n-1\}:d_{\mathrm p}(u,0)\ge n-1\}.
\]

Represent integers by their \(n\)-bit binary expansions, with cyclic positions. Construct the simple graph on \(V_n\) with \(\{u,v\}\) an edge exactly when \(d_{\mathrm p}(u,v)\ge n-1\). A code containing \(0\) is exactly \(\{0\}\) together with a seven-vertex clique in this graph.

The standalone exhaustive verifier `verify_graph.py` enumerates **every** seven-vertex clique exactly once: it adds vertices in strictly increasing integer order and intersects remaining candidates with the new vertex's forward-neighbor set. It neither samples nor prunes a viable clique. The exact output is

| \(n\) | \(\lvert V_n\rvert\) | Seven-cliques | Every clique plus \(0\) XOR-closed? |
| --- | ---: | ---: | --- |
| 3 | 7 | 1 | Yes |
| 4 | 11 | 1 | Yes |
| 5 | 21 | 5 | Yes |
| 6 | 36 | 4 | Yes |
| 7 | 64 | 2 | Yes |

The verifier checks XOR closure for **each** code, not only one example. Eight distinct vectors closed under XOR form a three-dimensional subspace. Thus every translated optimal code is linear, and the original code is affine.

For the converse, the enumerated cliques themselves are witnesses of existence at each length. Independent enumeration over **all** three-dimensional subspaces, without using the clique routine, reproduces the five through-zero counts; see `verify_linear.py`. The following three generator rows give one example at each length (bits shown in cyclic coordinate order):

| \(n\) | Three generator strings |
| --- | --- |
| 3 | `001`, `010`, `100` |
| 4 | `0011`, `0101`, `1001` |
| 5 | `00101`, `01010`, `10011` |
| 6 | `001011`, `010101`, `100111` |
| 7 | `0010111`, `0101110`, `1001011` |

All pair-distances for their eight linear combinations can be checked directly by the supplied programs.

**3. Labeled multiplicities.** Every three-dimensional subspace has eight elements and exactly \(2^{n-3}\) distinct affine cosets. Cosets of distinct through-zero subspaces are distinct, since the unique coset containing zero identifies its parent subspace. Multiplying the through-zero counts by \(2^{n-3}\) yields \(1,2,20,32,32\), respectively. This accounts for all labeled codes.

**4. Separate endpoint check.** For \(n=7\), equality in the distance-sum inequality forces every distinct pair-distance to equal six, and every cyclic pair category to have multiplicity two. After translation so that \(0\) lies in the code, each of its seven nonzero words has exactly one cyclic occurrence of `00`, and each of the seven positions occurs for exactly one such word. For a specified `00` position, there are exactly five possible binary words with no second cyclic `00`. The separate verifier `verify_grouped.py` exhausts these \(5^7=78125\) selections and obtains exactly two codes through zero, each linear. This independently checks the most constrained endpoint without using the general clique recursion.

## Verification

Run with standard Python 3, in the folder containing the accompanying files:

```text
python3 verify_graph.py
python3 verify_linear.py
python3 verify_grouped.py
```

All three programs terminate with `VERIFY_OK` and their asserted exact counts. Their source code is included in full. The first performs an exhaustive unrestricted (not linear-only) code search. The second enumerates all possible binary three-dimensional subspaces; the third uses the endpoint's Plotkin-equality combinatorics. The independent methods provide different checks of the finite counts; the written reduction above justifies why they cover the specified domain.

## Relationship to prior work

The Singleton upper bound, pair-metric definitions, and existence of pair-MDS codes are established by Chee, Ji, Kiah, Wang and Yin (2013). Binary equiweight and Plotkin-type constructions have been studied since 2016. Luo, Ezerman, Güneri and Özbudak (2025 preprint) prove minimum possible lengths for **linear** binary three-dimensional pair codes and explicitly state that up to isomorphism there is one **linear** \([n,3,n-1]\) code for \(3\le n\le7\). Those linear-existence and linear-uniqueness facts are **not** claimed as new here. A previously recorded exact result also gives the length-six count 32 and affine rigidity; that isolated case is credited as preceding this unified classification.

What the present statement adds is the **unrestricted** conclusion: every eight-word code with the specified parameters, including all codes not assumed linear, is necessarily affine, and the exact numbers of labeled codes across the complete feasible length range are determined. Linear uniqueness up to isomorphism does not, on its own, preclude nonlinear codes. The independent graph enumeration supplies that missing universal quantifier.

## Limitations

This is a finite-alphabet, eight-word, pair-window-length-two classification, not a classification for arbitrary code sizes, alphabets, or longer read windows. It does not improve the already-known Singleton or Plotkin inequalities. It uses an exhaustive finite classification for lengths at most seven, with fully provided code and a proof of coverage; it does not present a standalone hand-enumeration of all cliques. Bibliographic residual risk includes possible equivalent nonlinear classifications in unindexed supplementary material or inaccessible literature, particularly the 2024 paper on equiweight codes.

## References

1. Y. M. Chee, L. Ji, H. M. Kiah, C. Wang, J. Yin, *Maximum Distance Separable Codes for Symbol-Pair Read Channels*, IEEE Transactions on Information Theory 59 (2013), 7259–7267, DOI 10.1109/TIT.2013.2276615, open text: https://ymchee66.github.io/home/PDF/symbolpairjournal.pdf.
2. G. Luo, M. F. Ezerman, C. Güneri, F. Özbudak, *Linear Codes for b-Symbol Read Channels Attaining the Griesmer Bound*, Section 4 and Theorem 4.2, open text https://epub.uni-bayreuth.de/8523/1/work_symbol_pair.pdf.
3. Y. Yang, W. Li, K. Feng, *Symbol-Pair Codes: Plotkin Bound and Constructions*, arXiv:1607.02677 (2016), https://arxiv.org/abs/1607.02677.
4. Y. Liang, Z. Liu, *The Plotkin-Type Bound on the Generalized Symbol-Pair Weight and Symbol-Pair Equiweight Codes*, IEEE Transactions on Information Theory 70 (2024), 4990–5001, DOI 10.1109/TIT.2024.3392744 (abstract examined; full text not obtained).
