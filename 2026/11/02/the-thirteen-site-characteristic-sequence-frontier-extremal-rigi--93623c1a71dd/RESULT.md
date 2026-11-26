# The two largest characteristic sums of thirteen-site cycles

## Finding

Let \(\pi\) be a single cycle on the ordered set \(\{1,\ldots,13\}\). Set \(A_i=\{i,i+1\}\) for \(1\le i\le12\), let \(T_\pi(S)\) be the integer convex hull of \(\pi(S)\), and define the positive return characteristics and their sum by
\[
c_i(\pi)=\min\{\ell\ge1:T_\pi^\ell(A_i)\supseteq A_i\},\qquad S(\pi)=\sum_{i=1}^{12}c_i(\pi).
\]
The cycles with \(S(\pi)=78\) are **exactly** the twelve nonzero modular translations
\[
\pi(j)=1+((j-1+q)\bmod13),\qquad 1\le q\le12.
\]
Among the remaining cycles the largest sum is \(77\), attained by **exactly two** permutations. In one-line notation they are
\[
(3,4,5,6,7,8,9,10,11,13,12,2,1),\qquad
(13,12,2,1,3,4,5,6,7,8,9,10,11).
\]
Each has sorted profile \((1,2,3,4,5,6,6,8,9,10,11,12)\). Every other nontranslation has sum at most \(76\).

## Assumptions and scope

The sites are ordered and labeled; the count is over all single cycles, not over representatives modulo conjugacy. Convexification is performed **after each** application of the permutation; the sum uses all twelve adjacent-pair returns, not permutation cycle lengths. The extremal classification is for order thirteen only.

## Proof

**Known upper bound and attaining examples.** Wang's *On Periodic Points in Covering Systems*, Lemma 1.6, proves \(c'_k\le k\) for the sorted characteristics of **every** cyclic permutation, with the same definition of integer convexification. Thus \(S(\pi)\le78\), and equality requires the entire profile \((1,2,\ldots,12)\). Wang's Example 3.6(1) already gives this profile for every modular shift coprime to the order. These facts do not classify equality among all thirteen-cycles or determine the next-largest level.

**Interval graph.** On vertices \(1,\ldots,12\), put an arrow \(i\to j\) when
\[
\min\{\pi(i),\pi(i+1)\}\le j<\max\{\pi(i),\pi(i+1)\}.
\]
For \([a,b]\cap\mathbb Z\) with \(a<b\), the real closed intervals joining consecutive images \(\pi(j),\pi(j+1)\), \(a\le j<b\), overlap at consecutive endpoints. Their union is the interval between the least and greatest image of an integer in \([a,b]\). All endpoints are integers. It follows by induction that the unit cells covered by \(T_\pi^\ell(A_i)\) are exactly those at the ends of walks of length \(\ell\) from \(i\). In particular \(c_i\) is the length of a shortest positive closed walk rooted at \(i\). Such a walk exists since \(T_\pi^{13}(A_i)\supseteq\pi^{13}(A_i)=A_i\); a shortest one is simple, so has length at most twelve. This correspondence is the graph interpretation in Wang's work.

**Exhaustive count.** Use zero-based labels for the computation. A cyclic orbit sequence starting with \(0\) determines the permutation uniquely. For each successor \(q\in\{1,\ldots,12\}\), generate all \(11!\) orderings of the remaining sites; append the closing arrow to \(0\). In `verify_characteristic13.cpp`, build the twelve adjacency masks from the formula above. For each graph vertex \(i\), start with its out-neighbors at distance one; check for \(i\) before dropping previously expanded vertices, and form the next layer by taking the union of out-neighbors of the newly reached vertices. Skipping previously expanded vertices other than the checked return does not affect shortest return distances: a shortest positive closed walk has no repeated interior vertex, and a shorter path to an interior vertex would give a shorter return. Sort the twelve return lengths and count maximal profiles and the least positive deficit \(78-S(\pi)\) with its multiplicity in each block.

The exact outputs in `census.tsv` report \(39{,}916{,}800\) cycles in each block and one and only one maximal profile in each, always the modular translation. The least positive deficit is \(1\) only in the blocks \(q=2\) and \(q=12\), and has multiplicity one in each. The one-based representatives are the two permutations displayed above. Their profiles also follow by direct convexification, independently of the graph interpretation. The enumeration exhausts \(12!=479{,}001{,}600\) cycles and proves the two classifications.

## Verification

Compile `verify_characteristic13.cpp` with a GCC-compatible C++17 compiler, for example `g++ -O3 -std=c++17 -Wall -Wextra -pedantic verify_characteristic13.cpp -o verify_characteristic13`. Run `./verify_characteristic13 "$q"` for each integer \(q=1,\ldots,12\). The output can be compared with the accompanying `census.tsv` (the first-successor and witness columns use zero-based labels). `check_direct.py` separately compares repeated integer convexification with the graph method for all cycles of orders 3 through 8 and 10,000 seeded thirteen-site samples; it also checks both witnesses and all twelve translations. Those sampled comparisons check the two implementations; they are not the source of the exhaustive exclusion.

## Relationship to prior work

Wang's 2022 manuscript defines the characteristic sequence, states the sorted inequality as Conjecture 1.7 and reports computation through order twelve in Example 3.7. The subsequent 2023 paper proves the all-order inequality (Lemma 1.6 and §4), proves the covering-system result (Theorem 1.2), and states the coprime modular-shift profiles (Example 3.6(1)). Consequently neither the order-thirteen inequality nor the attainment of \(78\) by the translations is a new theorem here. The distinct contribution is the exhaustive **exclusion of every other maximizer** at order thirteen and the explicit, complete description of the next level.

## Limitations

This is a finite computer-assisted classification for thirteen sites. It does not give a general rigidity or stability theorem for equality or near equality in Wang's bound. An equivalent classification in other sources is not ruled out by the comparisons above.

## References

1. Yihan Wang, *On an existence problem of periodic points in intervals whose images cover themselves*, [arXiv:2205.07225v1](https://arxiv.org/abs/2205.07225), 2022, Definition 1.6, Conjecture 1.7, Proposition 3.5, Example 3.7.
2. Yihan Wang, *On Periodic Points in Covering Systems*, [arXiv:2306.10523v1](https://arxiv.org/abs/2306.10523), 2023, Theorem 1.2, Definition 1.4, Lemma 1.6, Proposition 3.4, Example 3.6(1), and §4.
