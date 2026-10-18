# Circular Abelian-square spectrum of binary order-five de Bruijn cycles

## Finding

An **Abelian square** is a word \(uv\) whose two nonempty, equal-length halves \(u\) and \(v\) have the same number of each alphabet symbol. For binary words, it suffices that their counts of ones agree. A **circular** occurrence may cross the cut of a cyclic word, but has total length at most the circumference.

Let \(B\) be a binary de Bruijn cycle of order five: it has length \(32\) and every binary word of length five occurs in exactly one circular position. Identify cycles only up to cyclic rotation, and put

\[
A(B)=\sum_{d=1}^{16}\sum_{i=0}^{31}
\mathbf{1}\!\left[\sum_{j=0}^{d-1}B_{i+j}
=\sum_{j=d}^{2d-1}B_{i+j}\right],
\]

with every subscript read modulo \(32\). Thus \(A(B)\) counts starting positions and half-lengths, **not** Abelian-equivalence classes or just distinct factor strings.

**Complete order-five classification.** Among the \(2048\) rotation classes, \(A(B)\) takes exactly \(71\) values. Their full frequency distribution is in the embedded `spectrum.csv`. The sharp minimum and maximum are

\[
\min_B A(B)=73,\qquad \max_B A(B)=154.
\]

Each endpoint occurs for exactly four cycles, forming a single orbit under reversal and complementation. Their lexicographically least cyclic representatives (starting at the unique occurrence of `00000`) include, respectively,

`00000100011100110111110101001011`

and

`00000101110101000110110010011111`.

The unattained integers between the extremes are exactly \(134,136,138,143,144,148,149,150,151,152,153\). If the \(2048\) cycles are equally likely, then

\[
\mathbb E[A]=\frac{6597}{64},\qquad
\operatorname{Var}(A)=\frac{1097767}{4096}.
\]

**Occurrence/distinct-factor bridge.** Let \(D(B)\) count the number of different (as binary strings) Abelian-square circular factors of \(B\) with total length at most \(2^h\), for a de Bruijn cycle of arbitrary binary order \(h\). Defining \(A(B)\) analogously with \(1\le d\le2^{h-1}\), one has the exact identity

\[
A(B)-D(B)=\sum_{d=1}^{\lfloor h/2\rfloor}
\left(2^{h-2d}-1\right)\binom{2d}{d}.
\]

In particular at order five, \(D(B)=A(B)-20\), so the distinct-factor range is \(53\) through \(134\), with the same multiplicity distribution shifted by \(20\).

## Assumptions and scope

Binary alphabet \(\{0,1\}\), no sentinel, circular windows with total length between two and the circumference inclusive. Each occurrence is a pair (start, half-length). Rotations are identified, but neither reversal nor letter complementation is identified when counting the \(2048\) cycles; they are used only to describe the extremizers. Strings longer than the circumference are excluded. The finite histogram is only for order five; the occurrence/distinct identity holds for every binary order.

## Proof

**Universal short factors.** A binary de Bruijn cycle of order \(h\) contains each binary length-\(2d\) factor exactly \(2^{h-2d}\) times whenever \(2d\le h\). Richmond and Shallit's binomial count, or the direct Vandermonde identity \(\sum_{j=0}^d\binom dj^2=\binom{2d}d\), shows there are \(\binom{2d}d\) binary Abelian-square strings of length \(2d\). Once \(2d\ge h\), circular factors at two different starting positions are distinct as strings because their first \(h\) bits are distinct. Hence all repeated occurrences arise at lengths \(2d<h\), and summing multiplicity minus one proves the all-order bridge. At order five its value is \((8-1)\binom21+(2-1)\binom42=20\).

**Exhaustive cycle domain.** Use the directed binary de Bruijn graph with vertex set \(\{0,1\}^4\) and edge set \(\{0,1\}^5\), an edge from its four-bit prefix to its four-bit suffix. Every vertex has two incoming and two outgoing edges. A cyclic Eulerian tour induces, at each vertex, one of the two bijections from incoming to outgoing edges; conversely, any such \(16\) local pairings induces a permutation of the \(32\) edges. Exactly those pairings whose permutation is one \(32\)-cycle define a de Bruijn cycle. There are precisely \(2^{16}=65536\) pairings to inspect. Each true cycle contains `00000` exactly once, so choosing that edge as its first edge removes rotational duplication and establishes a one-to-one correspondence.

The `switch_cycles` routine in `verify.py` examines **every** pairing and accepts exactly the one-cycle permutations. It obtains \(2048\) distinct normalized cycles. Independently, the `euler_cycles` routine performs depth-first search through all unused-edge successor choices, beginning with edge `00000`, and accepts only closed Eulerian tours; it generates exactly the same \(2048\) strings. Its branching exhausts every Eulerian tour because a tour has exactly two possible next edges at each step, except edges already used. The two sets are compared as full string sets, not merely through cardinalities.

**Exact Abelian-square counts.** For every generated cycle and \(1\le d\le16\), \(0\le i<32\), `occurrences_by_half_fast` compares the two half sums using prefix sums of the doubled cycle. `occurrences_by_half_direct` independently compares the halves as literal slices and counts ones directly. Both agree at every half-length for every cycle. Sorting their totals yields the \(71\)-row frequency table in `spectrum.csv`, including the minimum, maximum, gaps, and moments above. Testing reversal and complementation of the normalized extremizers yields precisely four cycles at each endpoint, establishing the equality-class statement.

There is no sampling: the proof searches all \(65536\) local bijections and all accepted length-\(32\) cycles, and each has every one of the \(32\times16\) possible circular windows checked. The verifier repeats this through orders one to four and checks the all-order bridge at each tested order; the bridge itself was proved symbolically above.

## Verification

From the directory containing the embedded files, run `python3 verify.py`. The script uses only the Python standard library. It compares the independent Euler-tour and pairing enumerators at every order one through five, directly checks the de Bruijn property, compares independent square counters, checks the occurrence/distinct formula, and matches the complete order-five `spectrum.csv` numbers encoded as `EXPECTED_HIST` in the script.

Expected leading output: `VERIFY_OK orders=1..5 independent_generators=2 independent_abelian_tests=2`; subsequent lines give the extrema, moment fractions and the complete histogram. The full list of endpoint representatives is reproducible by filtering the cycles at totals \(73\) and \(154\).

## Relationship to prior work

Richmond and Shallit (2008/2009) count Abelian-square **strings** of each length over a given alphabet; their binary formula supplies the short-factor binomial term above but does not classify occurrences in constrained de Bruijn cycles. Fraenkel, Simpson and Paterson (1997; expanded 2002) study **inequivalent** Abelian circular squares under identification by length and symbol composition, rather than the present number of (start, half-length) occurrences across all order-five universal cycles. The obtainable abstract does not settle whether their inaccessible full text contains a related supplementary census. Fici and Mignosi (2015) treat Abelian-square-rich infinite words (notably Thue–Morse and Sturmian words). Kociumaka, Radoszewski, Rytter and Waleń (2016) give general extremal bounds for distinct and nonequivalent nonstandard squares in unconstrained words; neither gives this conditional finite occurrence histogram.

## Limitations

The \(71\)-cell order-five census does not imply a uniform formula for higher de Bruijn orders or a general bound sharp at all orders. It concerns **all occurrences**, not the number of Abelian equivalence classes; the latter is a different invariant. The all-order occurrence/distinct bridge is a direct consequence of previously known short-word counting and de Bruijn factor uniqueness, and is offered as a useful structural identity, **not** as a separate historical novelty claim. A directly relevant 1997/2002 circular-square paper was accessible in abstract/repository form but not complete full text; unseen supplementary data might affect priority.

## References

1. L. B. Richmond and J. Shallit, *Counting Abelian Squares*, arXiv:0807.5028 (first public arXiv version July 31, 2008); Electronic Journal of Combinatorics 16 (2009), R72. https://arxiv.org/abs/0807.5028
2. A. S. Fraenkel, J. Simpson and M. Paterson, *On Weak Circular Squares in Binary Words*, Combinatorial Pattern Matching, LNCS 1264 (1997), 76–82. https://doi.org/10.1007/3-540-63220-4_51
3. G. Fici and F. Mignosi, *Words with the Maximum Number of Abelian Squares*, arXiv:1506.03562 (2015). https://arxiv.org/abs/1506.03562
4. T. Kociumaka, J. Radoszewski, W. Rytter and T. Waleń, *Maximum Number of Distinct and Nonequivalent Nonstandard Squares in a Word*, arXiv:1604.02238 (2016). https://arxiv.org/abs/1604.02238
