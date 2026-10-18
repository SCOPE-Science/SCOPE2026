# Rotation-resolved Lempel–Ziv complexity of order-five binary de Bruijn cycles

## Finding
A binary de Bruijn cycle of order five is an oriented circular binary word of length \(32\) in which every binary word of length five occurs once as a circular factor. Two cycles are identified only under rotation, not under reversal or complement. There are \(2048\) such cycles. For a linear word \(u\), let \(c(u)\) be the number of components of its full Lempel–Ziv 1976 exhaustive history, including the final component even if it is fully reproducible from earlier symbols. Over all \(2048\cdot32=65536\) rooted linearizations \(u\) of these cycles, the exact distribution is

| \(c(u)\) | Number of rooted linearizations |
|:--:|--:|
| 8 | 6766 |
| 9 | 34836 |
| 10 | 23208 |
| 11 | 726 |

No other value occurs. More strongly, for a circular de Bruijn cycle \(B\), let
\[
m(B)=\min_{0\le i<32} c(\operatorname{rot}_i B),\qquad
M(B)=\max_{0\le i<32} c(\operatorname{rot}_i B).
\]
The exact distribution over cycles is

| \((m(B),M(B))\) | Number of cycles |
|:--:|--:|
| \((8,10)\) | 1228 |
| \((8,11)\) | 502 |
| \((9,10)\) | 226 |
| \((9,11)\) | 92 |

Thus every order-five binary de Bruijn cycle admits some cut with at most nine exhaustive-history components and another cut with at least ten components. The complete rooted population has mean \(303859/32768\) and variance \(458624343/1073741824\).

## Assumptions and scope
The alphabet is labeled \(\{0,1\}\). Positions are numbered \(0,\ldots,31\), and \(\operatorname{rot}_i B\) starts at circular position \(i\). The de Bruijn condition concerns contiguous circular length-five factors, not scattered subsequences. Every such cycle is aperiodic because its length-five factors are all distinct, so all 32 roots are different.

For precision, define the Lempel–Ziv parsing algorithm rather than relying on a potentially ambiguous name. Given a length-\(L\) word \(u\), initialize \(p=0\). At each \(p<L\), put
\[
\lambda_u(p)=\max_{0\le q<p}\operatorname{LCP}(u[q:L],u[p:L]),
\]
where \(\operatorname{LCP}\) is the longest common-prefix length and a maximum over an empty set is zero. The earlier source need only START before \(p\); matching is allowed to overlap its destination. The next phrase ends at
\[
p'=\min\{L,p+\lambda_u(p)+1\}.
\]
Set \(p=p'\) and repeat. Count all nonempty phrases, including a final phrase lacking a new symbol. This is the full-component convention for the LZ76 exhaustive history, not LZ78, an LZ77 code length, a nonoverlapping-copy variation, or a convention that discards a fully reproductive final phrase.

## Proof
**Exact enumeration of cycles.** Use the directed binary de Bruijn graph with vertices the \(16\) four-bit strings and edges the \(32\) five-bit strings. An edge \(x_1\ldots x_5\) goes from \(x_1\ldots x_4\) to \(x_2\ldots x_5\). At each vertex there are precisely two incoming and two outgoing edges. Any Eulerian circuit induces a bijection pairing each incoming edge with the outgoing edge immediately following it. Each vertex has exactly two possible such pairings, so every circuit induces one of \(2^{16}=65536\) complete pairing assignments.

Conversely, an assignment of one incoming-to-outgoing pairing at each vertex induces a permutation \(P\) of the \(32\) directed edges, and it represents one de Bruijn cycle if and only if \(P\) is a single cycle of length \(32\). This is a bijection between admissible pairing assignments and de Bruijn cycles modulo rotation: every de Bruijn cycle contains the edge `00000` exactly once, so choose that edge as the unique origin of the circuit. There is no quotient by reversal or symbol complement.

The standalone enumerator checks all \(65536\) assignments. At a vertex with integer representation \(v\in\{0,\ldots,15\}\), incoming edge integers are \(v\) and \(16+v\), while outgoing edge integers are \(2v\) and \(2v+1\). Selector bit \(s_v\) sets
\[
P(v)=2v+s_v,\qquad P(16+v)=2v+1-s_v.
\]
The code traverses \(P\) starting at edge zero, accepts only assignments whose traversal visits all 32 edges before returning to zero, and reads the last bit of each edge to obtain a cycle representation. The result is exactly 2048 different accepted words. Each candidate also passes the independent de Bruijn-factor uniqueness check.

**Independently complete enumeration.** A second generator does not use pairings. It fixes `00000` as the first directed edge and recursively tries both unused outgoing edges at each of the 16 vertices, accepting precisely closed walks after all 32 different edges have been used. Every Eulerian circuit has one and only one rooted representation with `00000` first, so this depth-first enumeration is complete. It produces 2048 words, and its complete word set equals the first generator's word set.

**Exact LZ76 counts.** For each of the 2048 cycles the verifier forms all 32 rotations. It parses every resulting linear word by two independent finite algorithms: (i) the longest-previous-factor formula defining \(\lambda_u(p)\), and (ii) at every position, a literal search for the *shortest* next phrase absent from all matches starting at an earlier position, with the entire remaining suffix used when no such phrase exists. The algorithms agree for all 65536 rooted words. Their computed histogram and cyclewise minimum/maximum histograms are exactly the two tables in the Finding section.

To justify that both algorithms compute the stated invariant, note that if a prefix of length \(h\) of the next phrase matches a source starting at some \(q<p\), then those \(h\) symbols can be copied recursively, even when \(q+h>p\). The maximum possible copy length is \(\lambda_u(p)\); the following symbol, when it exists, is the first innovation. Thus the next exhaustive phrase has length \(\lambda_u(p)+1\), truncated at the end of the word. The second algorithm locates this same first innovation without using longest-match lengths. A final fully copied suffix is still one component by the explicit convention. Because the finite programs inspect every possible pairing, every rooted cut, and every candidate previous source, the exact finite classifications follow.

For the claimed mean and variance, write \(h_8=6766\), \(h_9=34836\), \(h_{10}=23208\), and \(h_{11}=726\). Compute \(\sum_k k h_k/65536=303859/32768\) and \(\sum_k k^2h_k/65536-(303859/32768)^2=458624343/1073741824\).

## Verification
Run `python3 verify.py` from the directory containing this document. It uses Python's standard library only. The script regenerates the full lists from the two distinct enumerators, checks uniqueness and equality, rechecks the de Bruijn property, compares both exhaustive-history parsers on each rooted word, and asserts each numerical table. It also checks two independently published sample parsings. The expected final output begins with `VERIFY_OK` and reports `debruijn_order5_cycles=2048`, `rooted_words=65536`, and the four-cell histogram.

The enumeration loops have explicit finite limits: \(2^{16}\) pairing assignments; 32 edges per accepted circuit; 32 cuts per accepted cycle; and previous-match searches only at earlier word positions. The computational proof is exhaustive for the stated finite universe. Neither its runtime nor sampling is used as evidence for an all-order theorem.

## Relationship to prior work
Lempel and Ziv (1976) introduced the exhaustive-history complexity measure. Szczepanski (arXiv:math/0009084, first publicly submitted 2000-09-08) proves identities for the LZ76 complexity distribution over *all* words under a uniform source and introduces exact terminal components; those formulas do not evaluate the distribution conditional on being a rooted de Bruijn word. Nunes, Estevez-Rams, Aragón Fernández and Lora Serrano (arXiv:1311.0822, first publicly submitted 2013-11-04) study strings with globally maximal LZ76 complexity; their unrestricted extremal construction does not classify order-five de Bruijn cycles or their cuts.

The similarly titled paper by Etzion and Lempel (1984), *On the Distribution of de Bruijn Sequences of Given Complexity*, concerns **linear feedback recurrence complexity** of periodic sequences, a mathematically different invariant. In particular, that notion does not imply any of the LZ76 phrase counts recorded here. Ruskey, Sawada and Williams (2012) study de Bruijn sequences for fixed-weight binary strings, not the present parse-count distribution.

## Limitations
All assertions concern binary de Bruijn order five, length 32, and the exact full-component LZ76 convention. The result does not state an asymptotic limit, an all-order formula, a compression bit-rate estimate, or an optimal LZ77/LZ78 coding claim. The counts are not invariant under changing the parsing convention, and the cyclewise results must not be interpreted as rotation-invariant individual phrase counts. Search of accessible sources is not a guarantee of historical priority; an earlier unindexed equivalent computation is possible.

## References
1. A. Lempel and J. Ziv, *On the Complexity of Finite Sequences*, IEEE Transactions on Information Theory 22 (1976), 75–81. DOI: 10.1109/TIT.1976.1055501.
2. J. Szczepanski, *On the Distribution Function of the Complexity of Finite Sequences*, arXiv:math/0009084 (first submitted 2000-09-08), https://arxiv.org/abs/math/0009084.
3. C. A. J. Nunes, E. Estevez-Rams, B. Aragón Fernández and R. Lora Serrano, *Properties of Maximum Lempel-Ziv Complexity Strings*, arXiv:1311.0822 (first submitted 2013-11-04), https://arxiv.org/abs/1311.0822.
4. T. Etzion and A. Lempel, *On the Distribution of de Bruijn Sequences of Given Complexity*, IEEE Transactions on Information Theory 30 (1984), 611–614. DOI: 10.1109/TIT.1984.1056933 (linear recurrence complexity, not LZ76).
5. F. Ruskey, J. Sawada and A. Williams, *De Bruijn Sequences for Fixed-Weight Binary Strings*, SIAM Journal on Discrete Mathematics 26 (2012), 605–617. DOI: 10.1137/100808782.
