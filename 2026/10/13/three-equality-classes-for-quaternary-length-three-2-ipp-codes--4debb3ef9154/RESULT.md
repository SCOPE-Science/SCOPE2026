# Three equality classes for quaternary length-three \(2\)-IPP codes
## Finding
For length-three 2-identifiable-parent codes over a four-symbol alphabet, the known optimum is \(F(3,4)=5\). The full equality layer consists of exactly \(55{,}296\) labeled unordered codes and exactly three equivalence classes under coordinate permutations and independent symbol permutations in each coordinate. Their orbit sizes are \(20{,}736\), \(13{,}824\), and \(20{,}736\), with stabilizer orders \(4\), \(6\), and \(4\). Representatives are `{000,011,022,103,230}`, `{000,011,102,220,333}`, and `{000,011,102,223,333}`. The first and third realize the published partial-order-minimal type-IV and type-III shapes, while the middle class is a genuine nonminimal maximum whose code graph is a three-color binding of three 2-cliques together with one isolated vertex.

## Assumptions and scope
A code is an unordered subset \(C\subseteq\{{0,1,2,3\}}^3\). For every coalition \(X\subseteq C\) with \(1\le |X|\le2\), its descendant set consists of the words whose coordinate symbols are chosen coordinatewise from the symbols appearing in \(X\). The code has the \(2\)-identifiable-parent property when, for every descendant word, the intersection of all coalitions of size at most two that can generate it is nonempty. Equivalence means arbitrary permutation of the three coordinates together with an independent permutation of the four alphabet symbols in each coordinate.

The statement is finite and only concerns alphabet size four, length three, and coalition size two. The scalar optimum \(F(3,4)=5\) is prior work; the equality census and orbit classification are the contribution assessed here.

## Proof
The published length-three structure theorem selects, among maximum code graphs, one that is minimal for a partial order based first on alphabet usage and then on the number of three-color parts. For \(q=4\), its classification excludes type I and type II. A type-III selected maximum has at most \(2q-3=5\) vertices, while a type-IV selected maximum has exactly \(q+1=5\) vertices. The source also gives a five-word witness, hence \(F(3,4)=5\).

For the complete equality layer, fix a maximum codeword and use independent symbol permutations to send it to `000`. There are \(\binom{{63}}{{4}}=595{,}665\) five-word subsets containing `000`. The verifier examines all of them directly from the descendant definition, with no probabilistic or heuristic pruning. Exactly \(4{,}320\) are \(2\)-IPP.

To quotient by the natural equivalence relation, the verifier canonically records, for each coordinate, the equality partition induced on the five codewords. It minimizes the resulting triple of partitions over all five-word orderings and all coordinate permutations. This produces exactly three canonical forms, with respectively \(1{,}620\), \(1{,}080\), and \(1{,}620\) normalized codes containing `000`.

The full natural group has order \(6\cdot24^3=82{,}944\). It is transitive on the \(64\) ambient words. Double-counting incidences between an equality code and its five codewords gives
\[
N\cdot5=64\cdot4{,}320,
\]
so the complete labeled census is \(N=55{,}296\). Applying the same incidence count within each equivalence orbit yields orbit sizes \(20{,}736\), \(13{,}824\), and \(20{,}736\). Orbit-stabilizer then gives stabilizer orders \(4\), \(6\), and \(4\).

For the three representatives, the code graph joins two codewords in color \(i\) when they agree in coordinate \(i\). The first representative is a type-IV binding of one 3-clique and two 2-cliques at a common vertex. The third is a type-III union of a two-color three-vertex part and a monochromatic 2-clique. The middle representative consists of a three-color binding of three 2-cliques at a common vertex together with one isolated vertex. This last shape is maximum but is excluded only after the source's partial-order minimization, so it is not among the two minimal shapes displayed for \(q=4\).

## Verification
Compile `verify.cpp` with a C++17 compiler and run it without arguments. It independently constructs every normalized five-word candidate, forms every descendant of every one- or two-word coalition, intersects all possible parent sets for each descendant, and retains exactly the valid codes. It then recomputes the canonical equivalence classes and the incidence/orbit counts.

The reviewed run returned `VERIFY_OK containing_zero=4320 labeled_maxima=55296 classes=3 group=82944`, followed by normalized class counts `1620,1080,1620`, orbit sizes `20736,13824,20736`, stabilizers `4,6,4`, and `orbit_sum=55296`.

## Relationship to prior work
Hollmann, van Lint, Linnartz, and Tolhuizen introduced and bounded identifiable-parent codes. Tô and Safavi-Naini subsequently solved the relevant small length-three cardinality problem and prove \(F(3,4)=5\). Their structural analysis explicitly first chooses a partial-order-minimal maximum graph; for \(q=4\), the paper displays type-III and type-IV minimal maximum graphs. The present equality census does not change that optimum. It instead classifies all maximum codes and shows that a third, nonminimal equality orbit survives before the minimization step.

Exact-parameter searches using identifiable-parent, \(2\)-IPP, graph-equivalence, orbit, and equality-census formulations found no source stating the three-orbit classification, the count \(55{,}296\), or stabilizers \(4,6,4\). A nearby exact result for length-three \(2\)-traceability codes concerns a strictly stronger tracing property and therefore does not imply the five-word \(2\)-IPP equality layer.

## Limitations
This is a finite classification for one natural small parameter. It does not classify maximum \(2\)-IPP codes for other alphabet sizes or lengths. The foundational 1998 article was checked as the source of the object and historical bounds but was not used for a whole-document negative originality claim; the decisive comparison is the later full length-three maximum-code article. An obscure unindexed historical enumeration of the same \(q=4\) equality layer remains a residual originality risk.

The earliest day-resolved public record found for the foundational source is 1998-05-01; no earlier public posting day was verified, and no date was inferred from a later revision.

## References
1. H. D. L. Hollmann, J. H. van Lint, J.-P. M. G. Linnartz, and L. M. G. M. Tolhuizen, *On Codes with the Identifiable Parent Property*, Journal of Combinatorial Theory, Series A 82 (1998), 121–133. DOI: `10.1006/jcta.1997.2851`.
2. Vu Dong Tô and Reihaneh Safavi-Naini, *On the Maximal Codes of Length 3 with the 2-Identifiable Parent Property*, SIAM Journal on Discrete Mathematics 17 (2004), 548–570. DOI: `10.1137/S0895480102400424`.
