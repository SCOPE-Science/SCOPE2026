# Every binary order-five de Bruijn unfolding has an optimal seven-position string attractor

## Finding

**Theorem.** Let \(b\) be any binary de Bruijn cycle of order \(5\), so its cyclic length is \(32\). For any cut \(t\), let \(T_{b,t}\) be the length-\(36\) word consisting of the corresponding length-\(32\) linear rotation followed by its first four symbols. Every such unfolded word satisfies
\[
\gamma^*(T_{b,t})=7.
\]
If \(M(T)\) counts distinct position sets of cardinality seven that attract every nonempty factor of \(T\), then
\[
30\le M(T_{b,t})\le120.
\]
Both bounds are sharp: among the \(65{,}536\) unfoldings, precisely four have \(M=30\), and precisely twenty-two have \(M=120\).

## Assumptions and scope

A cyclic binary word is a de Bruijn cycle of order \(5\) if each of the \(32\) binary words of length \(5\) occurs exactly once as a cyclic factor. A *full string attractor* of a finite word \(T\) is a set \(P\) of zero-based letter positions such that every distinct nonempty factor of \(T\) has at least one occurrence containing a position in \(P\). Denote the smallest cardinality by \(\gamma^*(T)\). The theorem concerns all cyclic order-five de Bruijn words, all choices of cut, and the ordinary, noncircular attractor of the resulting linear word. Complementing, reversing, or rotating a word is not used to discard any cut during the census.

## Proof

**Lower bound.** All \(32\) length-five factors of an unfolding are distinct and occur at the \(32\) starting positions \(0,\ldots,31\). A marked letter position can lie in at most five of these length-five occurrences. Therefore any attractor has at least \(\lceil32/5\rceil=7\) marks.

**Exact reduction to a finite collection of position sets.** Let the proposed seven positions be \(0\le p_1<\cdots<p_7\le35\). Since each length-five factor has exactly one occurrence, a necessary condition for these positions to form a full attractor is that they intersect every interval \([i,i+4]\), for \(0\le i\le31\). This is equivalent to the three constraints
\[
p_1\le4,\qquad p_7\ge31,\qquad p_{j+1}-p_j\le5\quad(1\le j<7).
\]
Conversely, any set satisfying these constraints intersects all length-five windows. Each occurrence of any factor of length at least five contains at least one length-five window, so every such factor is automatically attracted. It remains only to check factors of lengths one through four. These constitute exactly \(2+4+8+16=30\) distinct binary factors in every unfolding. For each such factor \(u\), form the union \(I(u)\) of the letter-position intervals covered by all its occurrences. It is attracted precisely when \(P\cap I(u)\ne\varnothing\). Thus a seven-position set is a full attractor if and only if it satisfies the displayed spacing constraints and all thirty interval-union tests.

**Exhaustive finite certificate.** The program `verify_order5.cpp` enumerates every strictly increasing seven-position set satisfying the spacing and endpoint constraints, finding exactly \(120\). It independently verifies that every set meets each length-five window. It then enumerates edge-distinct Euler circuits in the binary order-four de Bruijn digraph: there are sixteen vertices (four-bit words), and thirty-two directed edges (five-bit words). The unique edge labeled `00000` is prescribed as the first edge, eliminating cyclic rotation without losing any cycle. Every binary order-five de Bruijn cycle contains that edge once and corresponds to a unique such anchored circuit. The exhaustive depth-first traversal enumerates exactly \(2{,}048\) anchored circuits, consistent with the classical binary de Bruijn enumeration \(2^{2^{4}-5}=2{,}048\). For each circuit the program tests all \(32\) cuts, i.e. all \(65{,}536\) unfoldings.

For each unfolding, the thirty short-factor interval masks are constructed directly from its characters, and every one of the \(120\) candidate seven-sets is tested. The number passing is between \(30\) and \(120\) in every case. The extrema occur with frequencies \(4\) and \(22\), respectively. Furthermore, for one successful seven-set in every unfolding, the same program performs a separate *full-factor* check for every length from one through thirty-six by comparing the sets of distinct factors with and without a marked occurrence. Every such witness passes. The lower bound and exhaustive upper-bound certificate establish the claimed exact minimum, while the complete list of necessary seven-set candidates makes the multiplicity counts exhaustive.

## Verification

Compile the included standalone certificate with

```sh
c++ -O2 -std=c++17 -Wall -Wextra -pedantic verify_order5.cpp -o verify_order5
./verify_order5
```

The executed source prints

```text
VERIFY_OK cycles=2048 unfoldings=65536 candidates=120 full_factor_witnesses=65536 min_seven_attractors=30 max_seven_attractors=120 cuts_with_30=4 cuts_with_120=22
```

The certificate checks both the exact thirty-short-factor reduction for every candidate and all nonempty factors for an actual witness in every unfolding. The Euler traversal has an explicit edge-use mask, and each cut's factor data are recomputed from the cut word. Completeness follows from the graph/cycle bijection proved above, not merely from the numerical agreement with the known \(2{,}048\)-cycle count.

## Relationship to prior work

Mantaci, Restivo, Rosone, Romana and Sciortino [1, Proposition 41] derive general lower and upper bounds for linear de Bruijn attractors, and their Proposition 9 gives the basic factor-complexity lower bound. The lower bound specializes to \(\lceil32/5\rceil=7\) here, without providing the universal attaining construction. Whittington [2, Section on optimal attractors for de Bruijn sequences, Theorem 29] proves that a specially chosen Lyndon-generated unfolding attains the appropriate lower bound at prime order; the inspected theorem does not cover **every** binary order-five cycle and **every** cut. His discussion explicitly highlights the difficulty of extending sharp-window coverage to short factors and poses questions about general de Bruijn sequences. Béal, Crochemore and Romana [3] give algorithms and one-family experimental attractor sizes, not the complete all-cycle/all-cut classification. The present finite census proves the stronger order-five universal assertion and sharp multiplicity extrema, without claiming a corresponding theorem for arbitrary orders.

## Limitations

The result is confined to binary order-five cycles and their standard four-symbol linear unfoldings. It does not establish uniform optimality at other orders, over larger alphabets, or for circular rather than ordinary full string attractors. The coverage is an exhaustively reproducible finite proof, not a symbolic formula for arbitrary order. Literature searches cannot exclude every unpublished or unindexed equivalent treatment.

## References

1. S. Mantaci, A. Restivo, G. Rosone, G. Romana and M. Sciortino, *A Combinatorial View on String Attractors*, Theoretical Computer Science (2021). Full text: https://pages.di.unipi.it/rosone/Papers/MRRRS_TCS2021.pdf, especially Section 6.2 and Proposition 41.
2. P. Whittington, *Online String Attractors*, arXiv:2407.15599v1, initially public 2024-07-22. Full text: https://arxiv.org/pdf/2407.15599, especially pp. 16–18 and Theorem 29.
3. M.-P. Béal, M. Crochemore and G. Romana, *Checking and Producing Word Attractors*, arXiv:2509.08503v1 (2025). Full text: https://arxiv.org/pdf/2509.08503, especially the experimental de Bruijn table.
