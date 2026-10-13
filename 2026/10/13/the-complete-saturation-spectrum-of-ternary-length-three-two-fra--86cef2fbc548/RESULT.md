# The complete saturation spectrum of ternary length-three two-frameproof codes

## Finding

Let \(Q=\{0,1,2\}\). A code \(C\subseteq Q^3\) is *two-frameproof* when no word of \(C\) outside any pair of its codewords can be manufactured coordinatewise from that pair. Call \(C\) *inclusion-maximal* when it is two-frameproof and adding any other word of \(Q^3\) destroys two-frameproofness.

**Theorem.** The cardinality enumerator of all labeled inclusion-maximal two-frameproof codes is exactly
\[
  S(t)=27t^3+162t^4+540t^5+27t^6+324t^7+12t^9.
\]
Consequently there are precisely 1,092 inclusion-maximal codes, with possible sizes \(3,4,5,6,7,9\). In particular, none has size \(8\), and the smallest inclusion-maximal codes contain only three words, whereas the largest contain nine.

The full group of independent alphabet permutations in the three coordinates and permutations of those coordinates, of order \((3!)^4=1296\), partitions these 1,092 codes into exactly nine orbits. At sizes \(3,4,5,6,7,9\), respectively, the lists of orbit sizes are \((27)\), \((162)\), \((54,162,324)\), \((27)\), \((108,216)\), and \((12)\).

There are exactly 108 feasible eight-word codes. Each is contained in exactly one nine-word two-frameproof code; hence no eight-word code is inclusion-maximal.

## Assumptions and scope

All codewords are distinct labeled words in the fixed universe \(Q^3\), with three ordered coordinates. There is no quotient by symbol or coordinate permutations in the cardinality enumerator. Write
\[
\operatorname{desc}(X)=\{w\in Q^3:w_i\in\{x_i:x\in X\}\text{ for }i=1,2,3\}.
\]
The two-frameproof condition is \(\operatorname{desc}(X)\cap C=X\) for every \(X\subseteq C\) with \(|X|\le2\). This is distinct from the stronger two-identifiable-parent and traceability properties. The theorem is a finite complete classification for alphabet size three, block length three and coalition bound two; it is not a statement for arbitrary code lengths.

## Proof

**1. Forbidden-triple reduction.** For three pairwise distinct words \(a,b,c\in Q^3\), declare the unordered set \(\{a,b,c\}\) forbidden when one of its members belongs to the coordinatewise descendant set of the other two. A code is two-frameproof if and only if it contains no forbidden triple: coalitions of size zero or one cannot frame a *distinct* word, and every violation for a coalition of size two is precisely such a triple. Thus a code is a subset of the 27-element universe avoiding a fixed three-uniform hypergraph of forbidden triples.

For an independent count of forbidden triples, each coordinate permits 15 ordered assignments of values to a target and two parents, so there are \(15^3=3375\) ordered descendant triples. Removing cases where at least two whole words coincide leaves \(1944\). For three distinct words at most one can be descended from the other two (if two could be, those two would agree in all coordinates). Dividing by the two orders of the parent pair gives \(|B|=972\).

The triple \(\{000,001,002\}\) is an explicit inclusion-maximal code of size three. Conversely, the nine-word code \(\{(i,j,i+j\bmod3):i,j\in Q\}\) attains the largest size, which the exhaustive census confirms is nine.

**2. Exact enumeration.** Index the words lexicographically, \(000,001,\ldots,222\), by integers \(0,\ldots,26\). Let \(B\) be the complete forbidden-triple set computed from the above definition. The checker `verify_python.py` explicitly tests each unordered triple and obtains \(|B|=972\). Starting with the empty set, recursively append only indexes greater than every already chosen index. Append \(j\) precisely when no pair from the current set, together with \(j\), forms a triple of \(B\). By induction, every generated set is feasible. Conversely, each feasible set has a unique sorted sequence of indices, and every prefix passes the append test; therefore every feasible code is generated exactly once. This is exhaustive, not random sampling.

**3. Inclusion-maximality test.** For every generated feasible code \(C\), test all \(w\in Q^3\setminus C\). No extension is feasible if and only if \(C\) is inclusion-maximal by definition. The direct triple checker gives the feasible-code rank counts, for ranks \(0\) through \(9\),
\[
 (1,27,351,1953,4455,4482,2439,756,108,12),
\]
with no larger feasible codes; the total is 14,584. The maximal-code rank counts are, in the same range,
\[
 (0,0,0,27,162,540,27,324,0,12).
\]
These are the coefficients of \(S(t)\). The full codeword lists for all 1,092 maximal codes appear in `maximal_codes.txt`.

**4. Independent exhaustive route.** The C++ checker `verify_cpp.cpp` represents codes by 27-bit masks and, for each ordered pair of index values, constructs a bitmask of forbidden third words using base-three digit comparisons. Its increasing-index recursion removes incompatible future choices by bitwise intersection. Its global maximality test considers *every* unchosen word, not merely later indices. This implementation reproduces all 14,584 feasible subsets and all 1,092 maximal subsets. Its independently emitted `maximal_codes_cpp.txt` is byte-for-byte equal to the Python catalogue after accounting for opposite base-three digit significance. The two algorithms implement different forbidden-triple and extension tests.

**5. Symmetries and the eight-word gap.** The Python checker generates the action of each independent symbol transposition and cycle together with adjacent coordinate transpositions. These generate \((S_3)^3\rtimes S_3\). Breadth-first orbit closure of every maximal-code bitmask gives the nine orbit sizes in the theorem, accounting for all 1,092 codes exactly once. The 12 nine-word codes have exactly \(12\cdot9=108\) distinct one-word deletions, which equals the complete number of eight-word feasible codes. Thus every eight-word feasible code admits a unique ninth word and cannot be maximal.

## Verification

Run, from a directory containing the named source files, `python3 verify_python.py`. For independent verification, compile `verify_cpp.cpp` with `g++ -O2 -std=c++17 verify_cpp.cpp -o checker` and execute `./checker`, then compare `maximal_codes.txt` and `maximal_codes_cpp.txt` with `cmp`. Both verifiers assert the claimed exact cardinalities. The SHA-256 checksum of `maximal_codes.txt` is `e9e663390cc753c2789547540be9174e2075f3b11b9b2b316f35a450610e7728`; it has 1,092 UTF-8 newline-terminated records.

## Relationship to prior work

Chee and Zhang [1] define frameproof codes in precisely the descendant sense used here and develop large-code constructions and asymptotic cardinality bounds; their paper does not enumerate inclusion-maximal ternary length-three codes. Guo [2] surveys finite frameproof codes and small examples but the inspected sections do not present this saturation polynomial. Blackburn [3] treats upper bounds and extremal constructions, a different task from enumerating all terminal configurations under codeword addition. Tô and Safavi-Naini [4] study length-three codes with the stronger two-identifiable-parent property and use 'maximal' in connection with maximum codeword counts, not the inclusion-maximal two-frameproof census stated here. Their Theorem 34 gives a maximum of four words when the alphabet is ternary, compared with nine for the present weaker property. The distinction from two-identifiable-parent is strict even in this universe: the two-frameproof code \(\{012,021,100,200\}\) has descendant intersection at \(000\) between the disjoint parent pairs \(\{012,100\}\) and \(\{021,200\}\), so it is not two-identifiable-parent. Those distinctions concern implications of the published claims, not matching titles.

The 12 maximum-size codes are a proper subcollection of the 1,092 inclusion-maximal codes. The novelty claim concerns the saturation spectrum, full orbit structure and eight-word extension phenomenon; it does not claim the maximum cardinality nine or its 12 optimizers as independently new results.

## Limitations

This is finite, exhaustive and fully reproducible, but it does not produce a closed formula at variable alphabet size or length. Unindexed earlier enumerations might duplicate all or part of the census. The older Blackburn paper could not be inspected in full, so originality remains subject to further bibliographic checking. All computational upper bounds rely on complete finite search justified above, not an infinite theorem.

## References

[1] Y. M. Chee and X. Zhang, *Improved Constructions of Frameproof Codes*, arXiv:1206.5863v1 (26 June 2012), https://arxiv.org/pdf/1206.5863.

[2] C. Guo, *Fingerprinting Codes and Related Combinatorial Structures*, University of Waterloo thesis (2015), https://uwspace.uwaterloo.ca/handle/10012/9260.

[3] S. R. Blackburn, *Frameproof Codes*, SIAM Journal on Discrete Mathematics 16 (2003), 499–510, DOI:10.1137/S0895480101384633.

[4] V. D. Tô and R. Safavi-Naini, *On the Maximal Codes of Length 3 with the 2-Identifiable Parent Property*, SIAM Journal on Discrete Mathematics 17 (2004), 548–570, DOI:10.1137/S0895480102400424.
