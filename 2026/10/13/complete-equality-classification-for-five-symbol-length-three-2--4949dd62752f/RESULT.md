# Complete equality classification for five-symbol length-three 2-IPP codes
## Finding
For a five-symbol alphabet \(A=\{0,1,2,3,4\}\), consider length-three codes \(C\subseteq A^3\) with the \(2\)-identifiable-parent property. The known optimum is \(F(3,5)=7\). Among all seven-codeword optimum codes there are exactly two equivalence classes under permutations of the three coordinates and independent permutations of the five symbols in each coordinate.

Representatives are
\[
C_A=\{000,011,022,103,204,330,440\}
\]
and
\[
C_B=\{000,011,022,133,234,343,444\}.
\]

As unordered subsets of \(A^3\), there are exactly \(432{,}000\) optimum codes. Under \((S_5)^3\rtimes S_3\), the two classes are orbits of size \(216{,}000\) each, and each representative has stabilizer order \(48\).

The equality graph of \(C_A\) is a binding of three monochromatic \(3\)-cliques with one common vertex. The equality graph of \(C_B\) is the disjoint union of a monochromatic \(3\)-clique and an alternating two-color \(4\)-cycle. The pairwise Hamming-distance profiles are, respectively, \(9\) pairs at distance \(2\) and \(12\) at distance \(3\), and \(7\) pairs at distance \(2\) and \(14\) at distance \(3\). Every optimum code uses all five symbols in each coordinate.

## Assumptions and scope
For \(X\subseteq C\), define \(\operatorname{desc}(X)\) to be the words whose symbol in every coordinate occurs among the symbols used in that coordinate by a member of \(X\). A code is \(2\)-IPP when, for every word obtainable from a coalition of at most two codewords, the intersection of all coalitions of size at most two that can produce that word is nonempty.

The equivalence relation is the standard one used in the primary literature: permute coordinates and independently relabel the alphabet in each coordinate. The statement classifies unordered seven-word codes. It does not assert a classification for other alphabet sizes, other lengths, or coalition sizes greater than two.

## Proof
Tô and Safavi-Naini prove \(F(3,5)=7\) in their small-alphabet theorem. For the equality classification, label the seven codewords temporarily by \(0,\ldots,6\). Each coordinate induces a set partition of these seven labels into at most five blocks, according to equality of the coordinate symbol. Conversely, a triple of such partitions determines a code up to independent symbol relabeling.

For length three, the standard characterization of the \(2\)-IPP property gives two finite families of conditions. For each triple of distinct codeword labels, at least one coordinate must place the three labels in three different blocks. There are \(\binom{7}{3}=35\) such conditions. For each two disjoint unordered pairs of labels, at least one coordinate must give the two pairs disjoint sets of block labels. There are \(3\binom{7}{4}=105\) such conditions.

There are exactly \(855\) set partitions of seven labeled points into at most five blocks. Exhaustively testing triples of coordinate partitions against the \(140\) conditions yields exactly \(210\) valid triples after forgetting coordinate order. Quotienting those \(210\) triples by all \(7!\) relabelings of the temporary codeword labels yields exactly two classes, each containing \(105\) of the \(210\) labeled partition structures. Canonical representatives convert to \(C_A\) and \(C_B\) above.

Every valid equality structure has exactly five blocks in every coordinate. Thus each coordinate partition admits \(5!\) assignments of the five alphabet symbols. Restoring coordinate order contributes a factor of \(3!\), while forgetting the temporary labeling of the seven distinct codewords divides by \(7!\). Hence the number of literal optimum codes is
\[
210\,\frac{3!(5!)^3}{7!}=432{,}000.
\]
Each of the two classes contributes half of this number. Since \(|(S_5)^3\rtimes S_3|=3!(5!)^3=10{,}368{,}000\), each orbit has stabilizer order \(10{,}368{,}000/216{,}000=48\). A direct automorphism count gives the same value for both representatives.

## Verification
The accompanying `verify.py` regenerates all \(855\) allowed coordinate partitions, encodes the \(35+105\) characterization conditions, enumerates all \(210\) valid unordered coordinate triples, and quotients them by all \(7!\) codeword relabelings. It also checks the two representatives directly from the descendant definition, checks every enumerated equality structure directly from that definition, recomputes both stabilizers, and verifies the Hamming-distance profiles.

Run `python3 verify.py`. The expected line begins `VERIFY_OK` and reports `equivalence_classes:2`, `class_partition_counts:[105,105]`, `literal_maximum_codes:432000`, `orbit_sizes:[216000,216000]`, and `stabilizers:[48,48]`.

## Relationship to prior work
Hollmann, van Lint, Linnartz, and Tolhuizen introduced and developed identifiable-parent codes. Tô and Safavi-Naini later studied maximum length-three \(2\)-IPP codes directly. Their paper defines the same equivalence relation and the two finite IPP conditions used here, and its Theorem 34 establishes \(F(3,5)=7\). Their structural analysis first selects, among maximum graphs, one that is minimal in a partial ordering; for \(q=5\) their proof then exhibits a type-III maximum graph. That establishes the optimum but does not enumerate all equality cases under code equivalence. The classification above shows that a second, nonminimal equality type survives: the binding of three \(3\)-cliques.

A semantic search of published mathematical findings found a nearby exact result for length-three \(2\)-traceability codes, a strictly stronger tracing condition, but its bound does not imply this equality classification for \(2\)-IPP codes.

## Limitations
The finite census relies on the standard length-three IPP1/IPP2 characterization from the primary paper and on the published proof that the maximum size is seven. The verifier independently reconstructs the complete equality census conditioned on seven codewords, but it does not re-prove the published upper bound from first principles. No claim is made that no obscure unindexed historical source contains the same equality classification; exact-parameter and structural searches did not locate one.

## References
H. D. L. Hollmann, J. H. van Lint, J.-P. M. G. Linnartz, and L. M. G. M. Tolhuizen, “On Codes with the Identifiable Parent Property,” Journal of Combinatorial Theory, Series A 82 (1998), 121–133. DOI: 10.1006/jcta.1997.2851.

V. D. Tô and R. Safavi-Naini, “On the Maximal Codes of Length 3 with the 2-Identifiable Parent Property,” SIAM Journal on Discrete Mathematics 17 (2004), 548–570. DOI: 10.1137/S0895480102400424.
