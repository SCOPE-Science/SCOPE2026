# Complete cyclic LZ78 phrase-spectrum of binary de Bruijn cycles of order five

## Finding
A binary de Bruijn cycle of order five is a cyclic binary word of length \(32\) in which every binary length-five block occurs once. There are \(2048\) such cycles modulo rotation. For a linear cut \(u\), let \(z_{78}(u)\) denote its LZ78 phrase count under the explicit end-of-input convention defined below. For a cycle \(C\), let \(m(C)\) and \(M(C)\) be respectively the minimum and maximum of \(z_{78}\) over its \(32\) rotations.

The exact joint frequency distribution is:

| \((m(C),M(C))\) | Number of cycles |
|:--|--:|
| \((11,13)\) | 6 |
| \((11,14)\) | 44 |
| \((12,13)\) | 746 |
| \((12,14)\) | 1172 |
| \((13,13)\) | 30 |
| \((13,14)\) | 50 |
| **Total** | **2048** |

Consequently, exactly \(50\) cycles admit a cut using only \(11\) phrases; exactly \(30\) have \(13\) phrases at *every* cut. The minimum-over-cuts distribution is \(50,1918,80\) at \(11,12,13\). The maximum-over-cuts distribution is \(782,1266\) at \(13,14\). In the unique cut beginning with \(00000\), the frequencies of phrase counts \(11,12,13,14\) are \(18,480,1508,42\), respectively.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\), the order is exactly five, and no end-of-string sentinel is appended. Rotations are distinct inputs to the parser but identify the same underlying cycle. Every order-five cycle has exactly one starting position whose next five symbols are \(00000\); this is its canonical cut.

For the LZ78 parse of a length-\(32\) linear word, begin with an empty dictionary of **complete preceding phrases**. At each stage take the shortest nonempty prefix of the unparsed suffix not equal to an existing dictionary entry, and add that phrase. If no such prefix fits because the input ends within a dictionary match, emit all remaining symbols as one final residual phrase. That residual counts as one phrase. This precisely fixes a boundary convention that otherwise changes small finite counts. This is the incremental-dictionary LZ78 rule, not the LZ76 exhaustive-history or LZ77 substring-source rule.

## Proof
First, enumerate *all* cycles without assuming a table. Represent the \(32\) binary five-bit blocks by integers from \(0\) to \(31\). At a four-bit vertex \(q\) there are exactly two incoming five-bit edges with first bit \(a\in\{0,1\}\), and two outgoing edges, indexed by their final bit. A transition joining a given incoming edge to an outgoing edge in a cyclic de Bruijn traversal must be a bijection at every vertex. Each such bijection is one of two possibilities, encoded by a switch \(f(q)\in\{0,1\}\). The resulting successor of five-bit edge \(e\) is

\[
F_f(e)=2(e\bmod16)+\big(\lfloor e/16\rfloor\mathbin{\mathrm{xor}}f(e\bmod16)\big).
\]

There are exactly \(2^{16}=65536\) switch maps. Every map is a permutation of the \(32\) edges: at any vertex its two entering edges are sent bijectively to its two leaving edges. An oriented edge sequence forms a single cyclic de Bruijn traversal precisely when that permutation has one orbit of length \(32\). The unique five-bit block \(00000\) therefore fixes its canonical starting edge; counting the single-orbit maps counts cycles without rotational multiplicity. Conversely, every de Bruijn cycle induces these local incoming-to-outgoing bijections, so this is exhaustive and injective.

The attached `verify.py` visits each switch map and each candidate edge at most once in testing its orbit. It finds exactly \(2048\) single-orbit maps, each yielding a distinct canonical \(32\)-bit word, and checks that all \(32\) circular five-bit factors are different. Independently it enumerates closed Euler tours beginning with the edge \(00000\) in the binary order-four de Bruijn graph, pruning repeated edges, and checks equality of the two complete sets of \(2048\) words. This second procedure does not use the switch maps.

For each canonical cycle and each of its \(32\) cuts, the verifier computes the LZ78 parse in two independent ways: (i) testing strings against a set of earlier complete phrases; (ii) following and updating an explicit dictionary trie until the next missing transition. Both implementations return *identical phrase sequences*, not only identical counts, for all \(2048\cdot32=65536\) cuts. These counts give the exact six joint frequencies above; summing their rows proves the displayed marginals. Finally the full canonically sorted \(2048\)-row `certificate.tsv` records the cycle string, its minimum and maximum phrase counts, and its canonical-cut phrase count. The verifier regenerates and byte-compares this entire file. All loops have fixed finite bounds, so together this is an exhaustive finite proof, not sampling or a claim inferred from examples.

## Verification
Run `python3 verify.py certificate.tsv` from the directory holding these two attached files. With Python 3 standard library and no third-party packages, the script independently enumerates cycles by the switch-permutation and Euler-tour methods, compares the two complete canonical sets, computes the two complete-phrase parsers on every rotation, compares exact phrase sequences, computes all claimed histograms, and confirms every certificate byte. Its success banner is `VERIFY_OK cycles=2048 cases=65536 rotations=65536`.

## Relationship to prior work
Ziv and Lempel (1978), pp. 531–533, define the incremental parsing principle and universal code construction. Ziv (2014), Introduction and Lemma 2 discussion, explicitly contrasts complete dictionary phrases and the possibly repeated final phrase. Köppl (2021), Sections 4.2–4.5, develops LZ78 factorization algorithms; its problem is algorithmic substring parsing, not the six-value enumeration of fixed de Bruijn cycles. Etzion and Lempel (1984) and follow-up work on the *complexity* of de Bruijn sequences concerns linear feedback/recurrence complexity, mathematically different from LZ78 phrase counts. None of the inspected sources directly states the joint table or implies it through a parameter substitution. A search result's failure to identify such a table is not a proof of publication priority.

## Limitations
This is a finite classification at order five, not a formula for arbitrary order, an assertion about coding bit lengths, or an optimality guarantee for selecting a rotation in general. Although the entire finite census is reproducible, independently performed mathematical audit has not occurred. Literature priority may be affected by unindexed tables, theses, implementations, or publications whose full content was not accessible; the inspection claim is restricted to the material actually read. The parent 1978 paper is dated only to September in reliable month-granularity bibliographic records, whereas the 2014 arXiv version has a verified exact public posting date; no particular day in 1978 is inferred.

## References
1. J. Ziv and A. Lempel, “Compression of individual sequences via variable-rate coding,” *IEEE Transactions on Information Theory* **24** (1978), 530–536, doi:10.1109/TIT.1978.1055934. Full seven-page scholarly paper inspected at https://www.philippe-fournier-viger.com/spmf/lz78.pdf.
2. J. Ziv, “A Constrained-Dictionary version of LZ78 asymptotically achieves the Finite-State Compressibility for any Individual Sequence with a Distortion measure,” arXiv:1409.1323, first posted 2014-09-04; https://arxiv.org/abs/1409.1323.
3. D. Köppl, “Non-Overlapping LZ77 Factorization and LZ78 Substring Compression Queries with Suffix Trees,” *Algorithms* **14** (2021), article 44, doi:10.3390/a14020044.
4. T. Etzion and A. Lempel, “On the distribution of de Bruijn sequences of given complexity,” *IEEE Transactions on Information Theory* **30** (1984), 611–614, doi:10.1109/TIT.1984.1056933; the 'complexity' there is linear complexity.
