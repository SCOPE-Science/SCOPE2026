# Seven collineation types and order \(105\) of Fano-incidence rowmotion

## Finding

Let \(P\) be the height-two point–line incidence poset of the Fano plane. On its set \(J(P)\) of lower order ideals, classical rowmotion \(\rho\) has precisely \(458\) states and cycle-count generating polynomial

\[
29t^3+35t^5+28t^7.
\]

Thus \(\rho\) has order \(\operatorname{lcm}(3,5,7)=105\); all its cycles have odd length. The collineation group \(G=\operatorname{GL}_3(\mathbb F_2)\) commutes with \(\rho\) and has exactly seven orbits on the \(92\) rowmotion cycles.

For the explicit point/line encoding below, each row of this table gives one representative ideal, its rowmotion period, the number of rowmotion cycles in its collineation orbit, the sum of ideal cardinalities along the representative cycle, and the stabilizer order in \(G\):

| Point mask | Line mask | Period | Number of cycles | Cardinality sum | Stabilizer order |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 0 | 3 | 1 | 21 | 168 |
| 47 | 1 | 3 | 14 | 18 | 12 |
| 63 | 3 | 3 | 14 | 24 | 12 |
| 1 | 0 | 5 | 7 | 38 | 24 |
| 3 | 0 | 5 | 21 | 35 | 8 |
| 7 | 0 | 5 | 7 | 32 | 24 |
| 11 | 0 | 7 | 28 | 49 | 6 |

In particular, the cardinality statistic is not homomesic: distinct orbits of period \(3\) have cardinality averages \(6,7,8\), and distinct orbits of period \(5\) have averages \(32/5,7,38/5\). All period-\(7\) orbits average \(7\).

## Assumptions and scope

Write \(V=\mathbb F_2^3\). Label its seven nonzero vectors, interpreted as the seven projective points, by the integers \(1,\ldots,7\) according to their three binary coordinates. For each nonzero coefficient vector \(a\), define a projective line

\[
L_a=\{v\in V\setminus\{0\}:a\cdot v=0\}.
\]

The dot product is computed modulo \(2\). Every \(L_a\) consists of three points; the seven lines and seven points constitute the Fano plane. Define \(P\) to have fourteen elements, with seven points minimal, seven lines maximal and \(v<L_a\) if and only if \(v\in L_a\). This is not the vertex–edge incidence poset of the Heawood graph; the Heawood graph is the undirected Hasse diagram of \(P\).

Encode a lower ideal as a pair \((A,B)\), where \(A\) is a subset of the seven points and \(B\) a subset of the seven lines. It is an ideal exactly when \(L_a\subseteq A\) for every \(a\in B\). Point and line masks give the binary incidence vectors of \(A\) and \(B\) in label order, with label \(1\) at the least-significant bit. Rowmotion is defined, with no normalization ambiguity, by

\[
\rho(I)=\langle\operatorname{Min}(P\setminus I)\rangle,
\]

where the angle brackets denote the generated lower ideal. The claim concerns this exact finite poset, not arbitrary projective planes or all subspace lattices.

## Proof

**Step 1: Exact recurrence.** For a lower ideal \((A,B)\), define

\[
N(A,B)=\{a:L_a\subseteq A,\ a\notin B\}.
\]

A missing point is automatically a minimal element of the complement. A missing line is minimal in the complement precisely when all its incident points are already in \(A\), which is the defining condition for \(a\in N(A,B)\). Generating the lower ideal of those minimal complementary elements therefore gives

\[
\rho(A,B)=\left((V\setminus\{0\}\setminus A)\cup\bigcup_{a\in N(A,B)}L_a,\quad N(A,B)\right).
\]

This identifies every transition directly and proves that the recurrence implements the standard order-ideal definition. It also agrees with the independent toggle implementation: toggle all upper elements, then all lower elements.

**Step 2: Exact state count.** For a point subset \(A\), let \(e(A)=|\{a:L_a\subseteq A\}|\). An ideal with lower part \(A\) may select any subset of the \(e(A)\) available lines, whence

\[
|J(P)|=\sum_{A\subseteq V\setminus\{0\}}2^{e(A)}=458.
\]

The right side is evaluated exhaustively by the reproducible certificate \(\texttt{verify.py}\), which iterates over all \(128\) point masks. The separate \(\texttt{verify_alt.cpp}\) iterates over all \(2^{14}\) possible point–line bit masks, filtering by downward closure; it obtains the same \(458\).

**Step 3: Collineation certificate.** Each invertible binary linear transformation permutes the seven points and, by mapping each three-point line to another three-point line, induces an order automorphism of \(P\). Conversely these transformations supply a group of order

\[
|\operatorname{GL}_3(\mathbb F_2)|=(8-1)(8-2)(8-4)=168.
\]

Any order automorphism commutes with rowmotion, since it preserves complements, minimal elements and downward closure. It therefore acts on the rowmotion cycles, preserving cycle length and the sum of the ideal cardinalities.

For each of the seven mask pairs in the table, compute its orbit by repeatedly applying the explicit recurrence. The periods and cardinality sums are exactly those shown. Next apply each of the \(168\) invertible linear transformations to the entire cycle and deduplicate the resulting cycles. The seven group-orbit sizes are

\[
1,14,14,7,21,7,28.
\]

The pair (period, cardinality sum) differs across all seven rows, so their \(G\)-orbits are pairwise disjoint. Their total number of ideal states is exactly

\[
3(1+14+14)+5(7+21+7)+7(28)=458.
\]

They are all valid lower ideals, and each is a complete rowmotion cycle by direct recurrence. Because the disjoint cycles already exhaust the entire set of \(458\) ideals, **there are no other cycles**. This is a finite exhaustive proof of the complete cycle and symmetry classification; the full permutation order and orbitwise cardinality averages follow immediately.

**Step 4: Independently reconstructed check.** The alternate certificate builds the seven Fano lines by \(\{p,q,p+q\}\) for distinct nonzero binary vectors, rather than by the orthogonality construction above. It then computes rowmotion by the full sequence of upper-rank and lower-rank toggles on all valid ideals. It independently reproduces the state total and the complete cycle-length and cardinality-sum distributions.

## Verification

Files \(\texttt{verify.py}\) and \(\texttt{verify_alt.cpp}\) contain standalone exact certificates requiring only Python 3 and, for the second implementation, a C++17 compiler. Reproduce with

```sh
python3 verify.py
g++ -std=c++17 -O2 -Wall -Wextra verify_alt.cpp -o fano_check
./fano_check
```

The Python program verifies all \(458\) ideals, the recurrence–toggle equivalence on each state, all \(168\) transformations, their commutation with rowmotion, the seven representative-orbit certificates, the complete orbit partition and the order \(105\). The C++ program reconstructs the incidence relation by different code, enumerates the \(2^{14}\)-bit universe and independently certifies the cycle histogram. Each prints an explicit success marker, and assertions terminate execution on failure. No numerical tolerance, random search, unproved infinite extrapolation or outside dataset is used.

## Relationship to prior work

Striker and Williams define rowmotion on order ideals and develop promotion–rowmotion relations for families such as products of chains, root posets and alternating-sign-matrix posets. Striker extends the toggle-group viewpoint and gives general structure theorems for generalized toggle groups. Einstein and Propp study cardinality homomesy for products of two chains. These sources explain the classical operation and the homomesy question, but their inspected statements do not determine the Fano incidence-poset permutation. In particular, a projective incidence poset is not a product of two chains and the finite seven-orbit classification does not follow from the cited product-of-chains theorems.

The result here concerns the exact distribution of periods and the collineation types for this specific fourteen-element poset, not the already-known definition or general toggle-group theory. It is distinct from dynamics on vertex–edge incidence posets of unrelated graphs and from homology or domination invariants of the undirected Heawood graph.

## Limitations

This is a finite exact theorem for the Fano plane only. No formula is established here for general projective-plane orders, for other field sizes, or for a family of incidence posets. Full mathematical novelty beyond the inspected literature is not guaranteed: equivalent results under other names or in unindexed literature remain possible. The computational certificate is exhaustive for the \(458\)-state finite universe and supports the complete enumeration; its execution is not an independent scholarly audit.

## References

1. Jessica Striker and Nathan Williams, *Promotion and Rowmotion*, arXiv:1108.1172 (public preprint first submitted August 4, 2011), https://arxiv.org/abs/1108.1172.
2. Jessica Striker, *Rowmotion and generalized toggle groups*, arXiv:1601.03710 (first submitted January 14, 2016), https://arxiv.org/abs/1601.03710.
3. David Einstein and James Propp, *Combinatorial, piecewise-linear, and birational homomesy for products of two chains*, arXiv:1310.5294 (first submitted October 2013), https://arxiv.org/abs/1310.5294.
