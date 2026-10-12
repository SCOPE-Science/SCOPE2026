# Bounded-run synchronization of the Černý automata through order twenty-four
## Finding
For the standard \(n\)-state Černý automaton \(C_n\) with \(n\ge3\), impose the input-language constraint that no three successive input letters equal \(a\). Then the smallest achievable maximum run of \(a\) in a reset word is exactly two, for **every** \(n\ge3\). Moreover, for each integer \(3\le n\le24\), the shortest reset-word length subject to this constraint is exactly
\[
L_n=(n-1)(n-2)+\left\lceil\frac{(n-1)^2}{2}\right\rceil
=\left\lfloor\frac{3n^2-8n+6}{2}\right\rfloor.
\]
The stated exact formula is **proved only for the 22 integers** \(3\le n\le24\); it is not asserted for all orders. Explicit optimal words at all these orders are in `artifacts/exact_profile.csv`.

## Assumptions and scope
The state set is \(Q=\{0,1,\ldots,n-1\}\). Words act from left to right; \(a\) maps state \(i\) to \(i+1\) modulo \(n\), while \(b\) fixes every state except \(n-1\), which it sends to \(0\). A reset word \(w\) satisfies \(|Qw|=1\). Admissible words are precisely those over \(\{a,b\}\) with no contiguous factor `aaa`, with no cyclic wraparound convention. Word lengths count individual letters; the empty word and words without \(b\) do not reset. The all-order part determines whether zero, one, or two consecutive \(a\)'s suffice, and supplies an all-order quadratic upper bound. The length formula is finite-range only.

## Proof
**All-order run threshold and witness.** Until the first \(b\), the image of \(Q\) is \(Q\), because \(a\) is a permutation. The first \(b\) gives \(S=\{0,\ldots,n-2\}\), and \(b\) is idempotent. For a shortest reset word it is therefore sufficient to consider words starting in \(b\), without `bb`, and ending in \(b\): remove initial \(a\)'s, redundant adjacent \(b\)'s and final \(a\)'s without affecting the reset property or violating the constraint. Every such admissible word has the form \(b\{ab,aab\}^{*}\). If no `aa` is allowed, only blocks `ab` occur after the first \(b\); the map `ab` cyclically permutes the \(n-1\) elements of \(S\), so the image cardinality stays \(n-1\). Consequently no word having at most one consecutive \(a\) can reset.

Let \(m=n-1\). On \(S\), write \(f=ab\) and \(g=aab\). Then \(f\) is the cycle \(i\mapsto i+1\pmod m\), and \(g\) maps \(0\le i\le m-3\) to \(i+2\), and maps \(m-2,m-1\) to \(0\). Consequently \(h=g f^{m-1}\) maps \(i\mapsto i+1\) when \(i<m-1\), while fixing \(m-1\). The word
\[
 b\bigl(aab(ab)^{n-2}\bigr)^{n-2}
\]
therefore sends \(Q\) to a singleton. It has no `aaa` and has length \(2n^2-5n+3\). This proves that the exact minimum permitted maximum run is two at **all** orders \(n\ge3\), and the upper bound is unconditional.

**Finite exact length determination.** The normal form above reduces shortest admissible synchronization to the minimum-cost path from \(S\) to any singleton in the graph of nonempty subsets of \(S\), with edges \(T\xrightarrow{f}Tf\) of cost \(2\), and \(T\xrightarrow{g}Tg\) of cost \(3\); the initial \(b\) contributes exactly \(1\). Every nonempty subset (at most \(2^{n-1}-1\)) is represented by its bitmask, including those not reached. Complete weighted shortest-path enumeration in `artifacts/cerny_block_dijkstra.cpp` proves the minimum, as all costs are positive and every reachable subset is processed before termination at a singleton. Independently, `artifacts/cerny_run2_bfs.cpp` carries out ordinary unweighted breadth-first search on the full product of all nonempty subsets of \(Q\) and a three-state counter for the current trailing \(a\)-run; `a` is prohibited when the counter equals two. This independently checks the unrestricted start, transition normalization, and every shorter admissible word. For each of the 22 orders \(3\) through \(24\), both exhaustive methods give the same minimum, precisely the claimed formula. No extrapolation of a finite numerical pattern is used to prove an infinite length law.

## Verification
Compile both programs with a C++17 compiler, e.g. `g++ -O3 -std=c++17 artifacts/cerny_run2_bfs.cpp -o bfs` and analogously `artifacts/cerny_block_dijkstra.cpp -o shortest`; invoke `./bfs 24` and `./shortest 24` from the directory containing the code and compare the reported minimum lengths to `artifacts/exact_profile.csv`. Then invoke `python3 artifacts/verify_witnesses.py`. Both independently exhaustive programs were run through \(n=24\), and agree in all 22 minimum lengths. The independent product-state BFS processed \(25{,}165{,}756\) states at \(n=24\); the weighted subset search processed \(8{,}388{,}585\). The stored word witnesses and independently produced BFS words have each been directly replayed and checked to reset the defined DFA without `aaa`. Optimal witnesses from the two searches need not be identical. The direct witness program also replays the constructive all-order witness for \(3\le n\le100\), which is a numerical check, not the all-order proof.

The full recorded exact profile (order: minimum length) is

`3:4, 4:11, 5:20, 6:33, 7:48, 8:67, 9:88, 10:113, 11:140, 12:171, 13:204, 14:241, 15:280, 16:323, 17:368, 18:417, 19:468, 20:523, 21:580, 22:641, 23:704, 24:771`.

## Relationship to prior work
Classical Černý automata have unconstrained reset threshold \((n-1)^2\); that result and the standard unconstrained constructions are not presented as new. Grech and Kisielewicz study Černý-type reset bounds for automata respecting directed graph intervals [1]; Kowalski and Szykuła examine unconstrained reset lengths experimentally [2]. Hoffmann's papers on constrained synchronization [3,4] give general complexity and decision frameworks, including simple-idempotent families, rather than this explicit input-language threshold and the complete 22-order exact profile. A constraint on the *input word* is different from a prescribed subset that the reset word avoids in its *state image*. Indexed published mathematical findings were also compared for this difference. This report makes no claim of a uniqueness or exhaustive literature search.

## Limitations
The closed quadratic formula for the shortest admissible reset length is an **exact finite statement** for \(3\le n\le24\); its extension to \(n>24\) is unproved. The maximum-run-two threshold and the constructive upper bound are proved for every \(n\ge3\). The exponential exhaustive computations are reproducible finite proofs only for the recorded orders, subject to verification of the short supplied programs. General algorithmic frameworks could subsume the computation in principle without publishing the exact numbers. Earlier unindexed tables or results may already contain some of these lengths. No independent scientific audit has been performed.

## References
[1] M. Grech and A. Kisielewicz, *The Černý conjecture for automata respecting intervals of a directed graph*, arXiv:1207.2556v1, 2012-07-11. https://arxiv.org/html/1207.2556v1

[2] J. Kowalski and M. Szykuła, *Experiments with Synchronizing Automata*, arXiv:1607.04025v1, 2016. https://arxiv.org/html/1607.04025v1

[3] S. Hoffmann, *Ideal Separation and General Theorems for Constrained Synchronization and their Application to Small Constraint Automata*, arXiv:2005.05907v2. https://arxiv.org/html/2005.05907v2

[4] S. Hoffmann, *Constrained Synchronization for Commutative Automata and Automata with Simple Idempotents*, arXiv:2109.02743v1. https://arxiv.org/html/2109.02743v1
