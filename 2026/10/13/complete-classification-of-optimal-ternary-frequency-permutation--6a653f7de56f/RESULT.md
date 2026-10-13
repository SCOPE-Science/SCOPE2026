# Complete classification of optimal ternary frequency-permutation codes of length six and distance four
## Finding
Let \(\mathcal W\) be the set of the \(90=6!/(2!)^3\) ternary words of length \(6\) with composition \((2,2,2)\). For every \(C\subseteq\mathcal W\) whose distinct words have Hamming distance at least \(4\),
\[
|C|\le 15.
\]
Exactly 12 labeled unordered codes attain equality. The group \(S_6	imes S_3\), acting by coordinate permutations and a common permutation of the three symbols, acts transitively on these 12 codes. Thus every maximum has stabilizer order \(4320/12=360\).

Every maximum is coordinate-balanced: in each of its six coordinates, each symbol occurs five times. Its pairwise-distance multiset consists of 90 pairs at distance \(4\) and 15 pairs at distance \(6\). One representative is
\[
\{001122, 010212, 012021, 021201, 022110, 100221, 102012, 112200, 120102, 121020, 201210, 202101, 210120, 211002, 220011\}.
\]
## Assumptions and scope
Words are ordinary length-six sequences over \(\{0,1,2\}\). Each word contains exactly two copies of each symbol. Distance is Hamming distance, and the code condition is minimum distance at least \(4\), not exact pairwise distance \(4\). Codes are unordered sets without repeated words. “Labeled” keeps the six coordinate labels and the three symbol labels fixed. Equivalence is only under the stated natural action of \(S_6	imes S_3\).

## Proof
Construct the compatibility graph \(G\) whose 90 vertices are the words in \(\mathcal W\), joining two vertices exactly when their Hamming distance is at least \(4\). Then codes in scope are precisely cliques of \(G\). The supplied verifier constructs all 90 vertices directly from the multiset \((0,0,1,1,2,2)\), obtains 2745 compatibility edges, and exhaustively enumerates every maximal clique by a pivoted Bron–Kerbosch recursion. The complete maximal-clique size distribution is
\[
6:38895,\quad 7:20160,\quad 8:20520,\quad 9:10320,\quad 11:720,\quad 15:12.
\]
Hence the maximum is 15 and there are exactly 12 labeled unordered maxima.

For every one of the 12 maxima, the verifier directly rechecks all pairwise distances and all six coordinate symbol counts. For one maximum it then applies all \(6!\,3!=4320\) coordinate/symbol transformations. The resulting orbit contains exactly the 12 enumerated maxima and the representative is fixed by exactly 360 transformations. This proves transitivity and the stabilizer count by direct finite exhaustion.

## Verification
Run `python3 verify.py`. The expected output begins with `VERIFY_OK` and records 90 vertices, 2745 compatibility edges, 90627 maximal cliques, maximum 15, 12 maximum codes, one natural orbit of size 12, stabilizer 360, and census digest `65b3cfc15c29027b96d96a9b3fb72f83d7374b00b975eb9f7b33c574234b8da7`.

The verifier uses only the Python standard library. Its exhaustive recursion terminates after enumerating every maximal clique; the conclusion is not inferred from a timeout, random search, or partial sample.

## Relationship to prior work
Huczynska and Mullen introduced frequency permutation arrays and the notation \(M_\lambda(n,d)\), together with general constructions and bounds. Their publicly available 2005 preprint was inspected through the sections defining FPAs, the elementary bounds, constructions, and special cases; it does not state the above length-six, frequency-two equality classification. The 2009 constraint-programming paper studies the stricter *equidistant* FPA problem. It explicitly displays the parameter choice \(q=3\), \(\lambda=2\), \(d=4\) with five codewords, but its condition requires every pair to have distance exactly \(4\), whereas the present finding concerns minimum distance at least \(4\) and every maximum here necessarily has 15 pairs at distance \(6\). Thus that displayed EFPA is not a statement implying the present maximum-code classification.

Constant-composition-code literature supplies the broader coding framework and constructions. Exact-parameter searches using FPA, constant-composition, and multipermutation aliases did not locate a published statement of the 12-code census or the single-orbit equality classification. This absence is evidence from the searches performed, not a proof that no obscure source exists.

## Limitations
The result is finite and parameter-specific. It does not classify submaximum codes, equidistant FPAs, other compositions, or other lengths/distances. Originality risk remains from a possible unindexed historical table, thesis, or computational census of the same equality layer. The finite verifier establishes the mathematical census independently of that literature risk.

## References
1. S. Huczynska and G. L. Mullen, “Frequency permutation arrays”, arXiv:math/0511173v1 (2005-11-07); later J. Combin. Des. 14 (2006), 463–478, DOI 10.1002/jcd.20096.
2. S. Huczynska, P. McKay, I. Miguel, and P. Nightingale, “Modelling Equidistant Frequency Permutation Arrays: An Application of Constraints to Mathematics”, CP 2009, DOI 10.1007/978-3-642-04244-7_7.
3. W. Chu, C. J. Colbourn, and P. Dukes, “On constant composition codes”, Discrete Appl. Math. 154 (2006), 912–929, DOI 10.1016/j.dam.2005.09.009.
