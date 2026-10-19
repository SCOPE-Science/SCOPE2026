# Exact additive-one greedy assembly of DNA dinucleotide fragments

## Finding

Let \(\Sigma=\{\mathtt A,\mathtt C,\mathtt G,\mathtt T\}\), with Watson–Crick complementation \(\mathtt A\leftrightarrow\mathtt T\), \(\mathtt C\leftrightarrow\mathtt G\). For a word \(w\), let \(\operatorname{rc}(w)\) be its reversed complement. There are exactly ten equivalence classes of length-two words under \(w\sim\operatorname{rc}(w)\).

Take an arbitrary **nonempty subset** \(S\) of these ten classes, represented by one word per class. Define \(O(S)\) as the shortest length of a word containing, for every chosen class, one of its members as a contiguous factor. Define \(G(S)\) as the **largest** possible final length of the orientation-aware maximum-proper-overlap greedy merger, over every admissible tie and orientation choice. At each step it selects two different current components, chooses an orientation of each and an order achieving the globally largest *proper* suffix-prefix overlap, merges them, and continues. An overlap must leave a nonempty contribution from both components; zero-overlap joins are allowed.

Then, for **every** such \(S\),
\[
0\le G(S)-O(S)\le1.
\]
The inequality is sharp: precisely **282 of the 1023** possible nonempty class subsets have \(G(S)=O(S)+1\); the other **741** have equality. For a subset of cardinality \(n\), the exact worst length ratio is
\[
\max_{|S|=n}\frac{G(S)}{O(S)}=
\begin{cases}1,&n\in\{1,2\},\\ (n+2)/(n+1),&3\le n\le10.\end{cases}
\]
In particular the global maximum ratio is \(5/4\). One three-class witness consists of \(\mathtt{AA},\mathtt{AC},\mathtt{CA}\): \(\mathtt{AACA}\) is optimal of length four; a permitted greedy execution first merges reverse complements \(\mathtt{GT}\) and \(\mathtt{TG}\) to form \(\mathtt{GTG}\), then attaches \(\mathtt{AA}\) without overlap, obtaining \(\mathtt{GTGAA}\) of length five.

The full cardinality-wise enumeration is:

| Classes \(n\) | Instances | Instances with excess one | Sharp ratio |
|---:|---:|---:|---:|
|1|10|0|\(1\)|
|2|45|0|\(1\)|
|3|120|16|\(5/4\)|
|4|210|55|\(6/5\)|
|5|252|78|\(7/6\)|
|6|210|69|\(8/7\)|
|7|120|40|\(9/8\)|
|8|45|17|\(10/9\)|
|9|10|6|\(11/10\)|
|10|1|1|\(12/11\)|

## Assumptions and scope

The ten lexicographically canonical representatives, in order, are `AA,AC,AG,AT,CA,CC,CG,GA,GC,TA`. Every subset of these representatives is considered; input words have exactly two letters and no two selected words represent the same reverse-complement class. The greedy rule is a *direct pair-merging* rule, not a cycle-cover-based scheme such as MGREEDY-RC or TGREEDY-RC. The extremal greedy length is taken over all tie breaks, all allowed reversals/complementations and both concatenation orders. Strings with zero overlap can be joined in either order. This fixed, finite universe contains \(2^{10}-1=1023\) admissible inputs.

## Proof

**Lemma 1 (ten canonical classes).** The complement-reversal involution fixes the four dimers `AT,TA,CG,GC` and pairs the remaining twelve dimers into six two-element orbits. Hence the ten representatives shown above are exhaustive and pairwise distinct. This also shows that checking every nonempty subset of the ten is exhaustive.

**Lemma 2 (exact optimal-length recurrence).** For a chosen subset of \(n\) representatives \(s_1,\ldots,s_n\), let \(s_i^{(e)}\) denote the canonical or reversed-complemented orientation for \(e\in\{0,1\}\). For nonempty \(T\subseteq\{1,\ldots,n\}\), define \(D(T,i,e)\) as the least length of an ordered-overlap assembly containing exactly one chosen orientation of every indexed read in \(T\) and ending at \(s_i^{(e)}\). It satisfies
\[
D(\{i\},i,e)=2,
\]
\[
D(T,i,e)=\min_{\substack{j\in T\setminus\{i\}\\ f\in\{0,1\}}}
\bigl[D(T\setminus\{i\},j,f)+2-\operatorname{ov}(s_j^{(f)},s_i^{(e)})\bigr],
\]
where \(\operatorname{ov}\) is the largest proper suffix-prefix overlap (zero or one on distinct selected dimers). Any word satisfying all chosen classes contains occurrences of one chosen oriented dimer from each class. These occurrences start at distinct positions because different classes cannot yield the same length-two factor; sorting them from left to right gives an orientation/permutation order. Two successive starts either differ by one and match across a one-letter overlap, or differ by at least two and give zero overlap. Thus the recurrence constructs a word no longer than the original; conversely each recurrence path is a feasible word. Therefore
\[
O(S)=\min_{i,e} D(\{1,\ldots,n\},i,e).
\]

**Lemma 3 (exact worst-greedy recurrence).** Represent each current assembled component by the lexicographically lesser of it and its reverse complement, and sort the resulting multiset of components. This normalization cannot change available overlap lengths or final length, since each component may be reoriented freely at every merge. Let \(F(M)\) be the maximum final word length from a normalized multiset \(M\). For one component \(F(\{w\})=|w|\). Otherwise enumerate every unordered pair of *distinct component positions*, both orientations of each component, both concatenation orders, and each corresponding proper overlap. Retain just those pair-merges achieving the maximum overlap among **all** these choices; let \(\mathcal N(M)\) be their set of canonical successor multisets. Then
\[
F(M)=\max_{M'\in\mathcal N(M)}F(M').
\]
Every greedy execution has one of these first transitions, and every listed transition is legal. Each successor has one fewer component; induction on the number of components proves that this recurrence is exactly \(G(S)\), including adversarial tie breaking. Memoization merges repeated states but drops no choice. No heuristic pruning is employed.

**Finite exhaustive step.** The accompanying dependency-free `verify.py` implements the preceding two exact integer recurrences. It enumerates all \(1023\) input subsets and each possible first greedy transition recursively until one component remains. It checks the bound \(G(S)-O(S)\le1\) for **every instance** and accumulates the full nine-row-plus-singleton classification in the Finding section. It also checks the optimal-length recurrence independently against direct permutation-and-orientation enumeration for every input of up to four dimers, and checks greedy lengths by separately written uncached explicit recursion for every input of up to three dimers. All checks passed (see `verify-output.txt`). Consequently every table entry and both sharp bounds follow from Lemmas 1–3 and this exhaustive finite certificate.

**Sharpness.** For \(\{\mathtt{AA},\mathtt{AC},\mathtt{CA}\}\), any superstring has length at least four because three distinct length-two factors require at least three starting positions. The word \(\mathtt{AACA}\) realizes this bound. The first greedy choice \(\mathtt{GT}\) followed by \(\mathtt{TG}\) has overlap one, globally maximal for dimers; the resulting \(\mathtt{GTG}\) has zero proper overlap in either orientation with \(\mathtt{AA}\) or its reverse complement \(\mathtt{TT}\). Thus a legal greedy output of length five exists. The certificate additionally verifies sharp examples at every cardinality from three to ten.

## Verification

Run `python3 verify.py` with Python 3 and no third-party modules. Expected terminal output is exactly the embedded `verify-output.txt` (including the final `ALL_CHECKS_PASSED`). The checker enumerates \(638579\) canonical greedy states across all source inputs, uses exact integer comparisons, checks every admissible input and each greedy tied merge, and asserts the enumerated table, ratio and additive excess. The brute-force cross-checks use a separate implementation for small instances; neither those checks nor the witness alone replace the exhaustive recurrence. The finite proof does not rely on inference from sampled inputs.

## Relationship to prior work

Yamano and Shibuya (2026a, 2026b) analyze reverse-complement superstring approximation algorithms and give general cycle-cover-based guarantees. The first paper also describes the direct GREEDY-RC merger, citing the analogous reversal-based greedy treatment of Fici et al. (2015/2016). The present result is an exact finite-domain statement specifically about that **direct greedy** rule with reads of length two over the DNA alphabet, including all adversarial ties. Their general approximation/compression bounds do not imply the additive-one bound or the complete 1023-instance profile. Orenstein and Shamir (2013) optimize covering all \(k\)-mers with reverse complementation; covering the full set is different from classifying a greedy algorithm on **every subset** with adversarial tie-breaking. The ordinary binary length-four shortest-superstring exact ratio concerns a different alphabet, length, and absence of reverse complementations.

## Limitations

This is an exact finite-domain theorem for ten reverse-complement orbits, not a claim for longer reads, larger alphabets or arbitrary numbers of distinct input classes. All enumerated states were evaluated through deterministic code; exhaustive finite computation constitutes the numerical certificate, not a symbolic closed-form proof for an unbounded input family. The result distinguishes direct GREEDY-RC from the named cycle-cover-based variants. Despite literature and research-record searches, independent historical-priority assessment remains appropriate.

## References

- R. Yamano and T. Shibuya. *Improved Approximation Ratios for the Shortest Common Superstring Problem with Reverse Complements.* arXiv:2601.15814, first publicly submitted 2026-01-22; CPM 2026, DOI:10.4230/LIPIcs.CPM.2026.15.
- R. Yamano and T. Shibuya. *Improved Approximation Algorithms and Hardness Results for Shortest Common Superstring with Reverse Complements.* arXiv:2603.26176, first publicly submitted 2026-03-27; WABI 2026.
- G. Fici, T. Kociumaka, J. Radoszewski, W. Rytter and T. Waleń. *On the Greedy Algorithm for the Shortest Common Superstring Problem with Reversals.* arXiv:1511.08431, first publicly submitted 2015-11-26; Information Processing Letters 116 (2016), 245–251.
- Y. Orenstein and R. Shamir. *Design of shortest double-stranded DNA sequences covering all k-mers with applications to protein-binding microarrays and synthetic enhancers.* Bioinformatics 29 (2013), i71–i79, DOI:10.1093/bioinformatics/btt230.
