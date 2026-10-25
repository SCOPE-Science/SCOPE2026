# First primitive-necklace packing deficit for constant-weight-four non-overlapping binary codes

## Finding
For a positive integer \(n\), let \(M_4(n)\) be the maximum number of distinct binary words of length \(n\) and Hamming weight four in a *non-overlapping code*: no nonempty proper prefix of one selected word equals a suffix of another selected word, including when both words are the same. Then the exact values at lengths \(5\) through \(12\) are
\[
\begin{array}{c|rrrrrrrr}
n&5&6&7&8&9&10&11&12\\\hline
M_4(n)&1&2&5&8&14&20&30&39.
\end{array}
\]
At lengths \(5\) through \(11\) these optima meet the primitive-cyclic-necklace packing bound; at length \(12\) that bound equals \(40\), but the optimum is \(39\). Thus length \(12\) is the first strict deficit in this natural fixed-weight family (at length \(4\), the only word is bordered, so both bounds are zero).

## Assumptions and scope
The alphabet is \(\{0,1\}\); every codeword has exactly four ones and length \(n\). A proper prefix/suffix has length \(j\) with \(1\le j<n\). The constraint includes self-overlap. Two different words conflict if a proper prefix of either equals a suffix of the other. Words with self-overlap are never eligible. Results are only asserted for \(4\le n\le12\); no statement about larger lengths or unrestricted-weight non-overlapping codes is implied.

## Proof
**Necklace upper bound.** A word with a nontrivial period dividing its length has a nonempty proper border, hence no codeword can be nonprimitive. If distinct primitive length-\(n\) codewords are cyclic rotations of each other, a nontrivial rotation equates a proper prefix of one to a suffix of the other (or conversely). Therefore each codeword occupies a separate *primitive rotation orbit*. A primitive orbit has \(n\) members. The number of primitive weight-four orbits is
\[
N_4(n)=\frac1n\sum_{d\mid\gcd(n,4)}\mu(d)\binom{n/d}{4/d},
\]
where \(\mu\) is the Möbius function. For \(n=5,6,7,8,9,10,11,12\), respectively, direct substitution gives \(1,2,5,8,14,20,30,40\). Hence \(M_4(n)\le N_4(n)\) throughout.

**Attainment through length eleven.** The accompanying `certificate.json` provides a complete list of selected words for each length from \(5\) to \(11\), containing respectively \(1,2,5,8,14,20,30\) words. The standalone `verify.py` tests every prefix-suffix length for every ordered pair (including equal pairs), establishing their admissibility. These lists attain the necklace bound.

**Sharp upper bound at length twelve.** There are exactly \(128\) binary length-\(12\), weight-four words with no proper border. The `overlap_cliques_12` array in `certificate.json` partitions this entire set into exactly \(39\) nonempty groups, and any two *distinct* words within any one group conflict by a proper prefix-suffix equality. Every eligible codeword lies in this enumerated set, and an admissible code can choose at most one element from any group. Hence \(M_4(12)\le39\). The same certificate includes a \(39\)-word admissible code, so \(M_4(12)=39\). In contrast, the primitive-necklace bound equals \(40\) (there are \(480\) primitive weight-four words among \(\binom{12}{4}=495\)). Together with the earlier equalities, this establishes the claimed first deficit.

## Verification
The attached `verify.py` uses only the Python standard library and reads `certificate.json` from the same directory. Run `python verify.py` in the directory holding both files. The checker independently enumerates every binary weight-four word of each relevant length; recomputes full cyclic-rotation orbits; validates every codeword and every possible oriented proper overlap; recomputes the length-twelve universe of unbordered candidates; tests that the \(39\) supplied cliques partition all \(128\) candidates exactly; and checks that every pair within a clique conflicts. All assertions pass with the supplied certificate. The finite exhaustive verification establishes the stated finite optimum without extrapolating from empirical trials.

## Relationship to prior work
Bilotta–Pergola–Pinzani introduce constructions of cross-bifix-free binary sets (arXiv:1112.3168). Chee–Kiah–Purkayastha–Wang provide general cross-bifix-free code constructions and size bounds (arXiv:1209.0236). Blackburn develops general non-overlapping-code bounds and constructions (arXiv:1303.1026). Those general results provide the motivating framework but do not, in the inspected formulations, supply this exact *fixed-weight-four* optimum at length \(12\) or a \(39\)-clique upper certificate. The standard primitive-necklace count alone permits \(40\); the extra obstruction requires the cross-orbit overlap constraints. Harju–Nowotka study enumeration of fixed-weight primitive and bordered words, and OEIS A099766 records the fixed-weight unbordered counts (including the already-known count \(128\) for length \(12\), weight four). Neither the individual-word enumeration nor that table determines the packing optimum under pairwise cross-overlap restrictions.

## Limitations
This is an exact finite theorem through length \(12\), not an all-length formula. The novelty comparison is based on inspected accessible literature and searchable records; an equivalent restricted result could be present in unindexed or uninspected sources. The certificate is an exhaustively checkable finite combinatorial proof, not an external independent mathematical review. No claim is made about uniqueness or classification of optimal codebooks.

## References
1. S. Bilotta, E. Pergola, R. Pinzani, “A new approach to cross-bifix-free sets,” arXiv:1112.3168, publicly posted 2011-12-14.
2. Y. M. Chee, H. M. Kiah, P. Purkayastha, C. Wang, “Cross-bifix-free codes within a constant factor of optimality,” arXiv:1209.0236 (2012).
3. S. R. Blackburn, “Non-overlapping codes,” arXiv:1303.1026 (2013).
4. T. Harju, D. Nowotka, “Counting bordered and primitive words with a fixed weight,” Theoretical Computer Science 340 (2005), DOI:10.1016/j.tcs.2005.03.040.
5. OEIS A099766, fixed-weight unbordered-word count table, first posted 2004-11-11, https://oeis.org/A099766.
