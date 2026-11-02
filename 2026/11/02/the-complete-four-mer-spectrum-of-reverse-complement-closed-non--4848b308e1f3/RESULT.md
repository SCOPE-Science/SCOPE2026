# The complete four-mer spectrum of reverse-complement-closed non-overlapping DNA codes detecting one substitution

## Finding
Let \(\Sigma=\{A,C,G,T\}\), with Watson–Crick involution \(\overline A=T\), \(\overline C=G\), and \(\rho(w_1w_2w_3w_4)=\overline{w_4}\overline{w_3}\overline{w_2}\overline{w_1}\). A codebook is a subset \(C\subseteq\Sigma^4\) satisfying all three conditions:

1. \(\rho(C)=C\) (reverse-complement closure).
2. For every \(u,v\in C\), including \(u=v\), and \(1\le j\le3\), the length-\(j\) prefix of \(u\) differs from the length-\(j\) suffix of \(v\) (non-overlap).
3. Every two *distinct* words of \(C\) have aligned Hamming distance at least \(2\) (detection of one substitution).

The empty code is allowed. The exact cardinality-generating polynomial of all such **labeled** codebooks, without identifying nucleotide relabelings or reverse-complement orbits, is

\[
\boxed{H(z)=1+12z+88z^2+288z^3+584z^4+760z^5+688z^6+424z^7+160z^8+32z^9.}
\]

Consequently exactly \(3037\) codebooks satisfy the conditions, their sharp maximum word count is \(9\), and precisely \(32\) codebooks attain it. Under the group \(G=\{\pi\in S(\Sigma):\pi(\overline{x})=\overline{\pi(x)}\text{ for every }x\in\Sigma\}\) of the eight nucleotide relabelings preserving Watson–Crick complementation, the maxima form exactly **four orbits**, each of size eight. All four lexicographically least representatives are printed in `maxima_orbits.tsv`. Among the \(32\) maxima, \(24\) have five reverse-complement-fixed words and two two-word reverse-complement orbits; the other eight have one fixed word and four two-word orbits.

## Assumptions and scope
Words are aligned strings of **exactly four** nucleotides. All three non-overlap lengths \(1,2,3\) are forbidden, including self-overlaps. A reverse-complement-fixed word is permitted: closure under \(\rho\) is required, not a nonzero Hamming distance between a word and its *own* reverse complement. No fixed-GC-content condition is imposed. A Hamming distance of two detects, but does not necessarily correct, one substitution. Codebooks are sets (not ordered lists), and different labeled subsets count separately.

## Proof
**1. Orbit reduction is exact.** The \(256\) four-letter words split into \(136=(256+16)/2\) orbits of the involution \(\rho\), since there are \(16\) fixed words: in each of the two paired coordinate positions the first letter can be chosen in four ways. Any \(\rho\)-closed codebook is uniquely a union of such orbits. Call an orbit *admissible* if its own one or two words have no forbidden prefix/suffix overlaps and, when there are two, their Hamming distance is at least two. Exhaustive testing of the \(136\) explicitly defined orbits yields exactly \(56\) admissible orbits, of which \(12\) are singleton and \(44\) have two words. The complete, independently reconstructible list is provided in `adjacency.tsv`.

**2. Compatibility graph is equivalent to the original conditions.** Make one vertex for each admissible orbit. Join two distinct vertices precisely when every cross-orbit word pair satisfies both the oriented prefix/suffix exclusions and the Hamming-distance condition. This gives an explicitly specified undirected graph of \(56\) vertices and \(420\) edges. A valid codebook corresponds *bijectively* to a clique (including the empty clique): internal compatibility was verified at vertex construction, and all cross-orbit conditions are pairwise, so compatibility of every vertex pair is both necessary and sufficient. Assign vertex \(v\) weight \(s(v)=1\) for a fixed orbit, and \(s(v)=2\) otherwise.

**3. Exact finite recursion.** For any vertex subset \(S\), let \(F(S;z)\) be the sum of \(z^{\sum_{v\in K}s(v)}\) over all cliques \(K\subseteq S\). The base case is \(F(\varnothing;z)=1\). For any \(v\in S\), partition cliques according as they exclude or include \(v\):

\[
F(S;z)=F(S\setminus\{v\};z)+z^{s(v)}F((S\setminus\{v\})\cap N(v);z).
\]

Here \(N(v)\) is the neighbour set of \(v\). This recurrence strictly decreases the vertex set; hence it terminates and counts **all** cliques, without probability, sampling, an assumed cutoff on cardinality, or floating-point arithmetic. Applying the recurrence to all \(56\) vertices of the completely listed graph gives the displayed ten coefficients. The primary implementation visits \(1318\) distinct vertex-set recursion states. Its exact graph construction, recurrence, and expected coefficients are all in `verify_graph.py`; the 56 graph rows in `adjacency.tsv` can be checked byte-for-byte against independent regeneration.

**4. Maximizers and symmetries.** A second implementation independently generates every valid codebook by lexicographically increasing orbit insertion and directly rechecks all wordwise constraints at every extension. It obtains the same coefficients and all \(32\) distinct nine-word codebooks. The involution-preserving permutation group has order \(2^2\cdot2=8\): choose whether to swap the two complement pairs and whether to exchange the two letters inside each pair. Checking the images of every maximum shows four distinct classes, each containing eight codebooks. Direct counting of reverse-complement-fixed words gives the \(24+8\) split in the theorem. Since the second enumeration covers all codes by their unique increasing list of constituent orbits, the maximum and orbit classification are exhaustive.

## Verification
Execute with Python 3, using only the standard library:

```
python3 verify_graph.py adjacency.tsv
python3 crosscheck_direct.py
```

The first prints `GRAPH_VERIFY_OK`, coefficient vector \((1,12,88,288,584,760,688,424,160,32)\), \(56\) vertices, \(420\) edges and \(1318\) recurrence states; it also compares the recomputed adjacency representation byte-for-byte to `adjacency.tsv`. The second prints `DIRECT_CROSSCHECK_OK`, the same coefficient vector, the \(32\) maxima, their four symmetry orbits and the \(24+8\) structural split. `spectrum.csv` records every coefficient. `maxima_orbits.tsv` lists the four concrete maximum-code representatives. The direct implementation is not based on the primary graph recurrence or its memoization.

## Relationship to prior work
Blackburn's *Non-overlapping codes*, first released as arXiv:1303.1026 on 2013-03-05, establishes the classical prefix/suffix definition, synchronization motivation and general cardinality bounds. In particular it yields \(27\) as the unrestricted maximum at alphabet size and word length four, but does not impose reverse-complement closure or Hamming separation, and it does not enumerate this restricted cardinality spectrum. King's *Bounds for DNA codes with constant GC-content*, first publicly posted as arXiv:math/0306197 on 2003-06-12, treats DNA Hamming distance, GC content and **reverse-complement Hamming-separation** constraints. Its class differs from closure under reverse complementation and does not impose non-overlap. Mir et al. (2013) motivate short DNA barcodes with minimum-distance and biological constraints; their reported lengths are six to eight rather than this four-mer classification.

The present calculation combines *closure*, *strict non-overlap*, and *aligned Hamming distance at least two*, and counts every feasible cardinality and all maxima. Neither the unconstrained non-overlap maximum nor the classical reverse-complement-distance bounds logically determine these coefficients. A numerical literature search and targeted research-record searches did not identify an exact equivalent table; absence of a discovered table does not certify historical priority.

## Limitations
This is an exact **finite** classification for length four, not a general formula for longer words, larger alphabets or other distance thresholds. The mathematical proof is computer-assisted through a small, fully specified compatibility graph and a terminating exact-integer recursion; the two independent programs and full graph certificate are supplied for reproduction. Reverse-complement-fixed words are allowed, so the family must not be confused with codes requiring a positive distance from each word to its own reverse complement. Practical chemical constraints such as melting temperature, secondary-structure avoidance and GC balance are not modeled. Independently audited mathematical correctness and historical priority have not been established.

## References
1. O. D. King, *Bounds for DNA Codes with Constant GC-Content*, Electronic Journal of Combinatorics 10 (2003), R33, DOI: 10.37236/1726; first arXiv posting 2003-06-12, https://arxiv.org/abs/math/0306197 ; full journal text https://www.combinatorics.org/ojs/index.php/eljc/article/download/v10i1r33/pdf .
2. S. R. Blackburn, *Non-overlapping codes*, IEEE Transactions on Information Theory 61 (2015), 4890–4894, DOI: 10.1109/TIT.2015.2456634; first arXiv posting 2013-03-05, https://arxiv.org/abs/1303.1026 .
3. K. Mir, K. Neuhaus, M. Bossert and S. Schober, *Short barcodes for next generation sequencing*, PLoS ONE 8 (2013), e82933, published 2013-12-30, DOI: 10.1371/journal.pone.0082933, https://pmc.ncbi.nlm.nih.gov/articles/PMC3875435/ .
