# Sharp six-request all-symbol batch capacity of the binary length-16 first-order Reed–Muller code

## Finding
Let \(C=\operatorname{RM}_2(1,4)\) be the binary linear \([16,5,8]\) code with generator columns \(g_x=(1,x)\), indexed by \(x\in\mathbb F_2^4\). A recovery set for coordinate \(x\) is a subset \(R\subseteq\mathbb F_2^4\) such that \(g_x\) lies in the binary span of \(\{g_y:y\in R\}\). Define \(t_{\mathrm{ASB}}(C)\) to be the largest integer \(t\) for which *every multiset of \(t\) codeword-coordinate requests* admits \(t\) pairwise disjoint recovery sets, one for each occurrence. Then

\[
\boxed{t_{\mathrm{ASB}}(\operatorname{RM}_2(1,4))=6.}
\]

Moreover, every six-request multiset has a disjoint recovery realization using only singleton and three-coordinate sets. Thus the same conclusion holds when each request is constrained to read at most three codeword coordinates.

## Assumptions and scope
All algebra is over \(\mathbb F_2\), each of the sixteen stored coordinates can be read by at most one request, and repeated requests for the same stored symbol are allowed. Recovery sets may contain the requested coordinate, but different recovery sets must be disjoint. The result concerns *stored codeword symbols*, not just independent input-message symbols. The statement does not address longer Reed–Muller codes or simultaneous recovery with smaller helper sets.

## Proof
**Upper bound.** The sixteen generator columns are pairwise distinct and each has leading entry one. A binary representation of a generator column by other generator columns must use an odd number of them. A singleton different from the target cannot represent it, and a pair has leading entry zero; consequently any recovery set avoiding the target has at least three coordinates. If seven copies of one target \(x\) had disjoint recovery sets, at most one could contain \(x\); the other six would require at least eighteen different coordinates among the fifteen coordinates other than \(x\). This is impossible. Therefore \(t_{\mathrm{ASB}}(C)\le6\).

**Lower bound by a complete finite witness construction.** Regard the coordinate indices as integers \(0,\ldots,15\) encoding their four binary coordinates. For a target \(x\), use the singleton \(\{x\}\) and every unordered triple \(\{a,b,c\}\) of distinct indices satisfying \(a\oplus b\oplus c=x\), where \(\oplus\) is bitwise XOR. Each such triple is a legitimate recovery set because
\[
 g_a+g_b+g_c=(1,a\oplus b\oplus c)=g_x.
\]
There are precisely thirty-five different admissible triples per target: among the fifteen other indices, choose two of the fifteen; their unique third completion is distinct from both and the target, and each resulting triple is counted three times. Hence each target has thirty-six candidate sets, including its singleton.

The accompanying standard-library program `verify.py` defines the generator columns independently, generates these candidates by looping through all \(\binom{16}{3}=560\) triples, and loops through *every* nondecreasing six-tuple of indices in \(\{0,\ldots,15\}\). This visits exactly
\[
\binom{16+6-1}{6}=\binom{21}{6}=54{,}264
\]
multisets. For each tuple it constructs six disjoint candidate sets by exact recursive search over a state comprising the remaining target multiplicities and a sixteen-bit used-coordinate mask. Once a witness is returned, a separate check verifies the six target occurrences, the disjointness of every support, and equality between the XOR of the actual generator columns in each support and the requested column. All \(54{,}264\) witnesses pass these assertions. Because the iteration is an exhaustive enumeration of the finite domain of six-request multisets, this proves \(t_{\mathrm{ASB}}(C)\ge6\). Combining with the upper bound yields the claimed equality.

## Verification
Run `python3 verify.py` with Python 3 and no third-party dependencies. It regenerates all possible requests and validates every returned witness, not merely a log or a checksum. The expected final marker is `VERIFY_OK` following `CHECKED_REQUEST_MULTISETS 54264` and `UPPER_BOUND 6`. The test additionally confirms that no two distinct generator columns can represent a column by binary sum. The computer-assisted component proves only this finite length-sixteen statement; its coverage does not extend to other lengths.

## Relationship to prior work
Boruchovsky, Gruica, Niemann and Yaakobi introduced the all-symbol batch/PIR framework, proved a general dual-distance bound and analyzed MDS and simplex families. Their 2026 paper explicitly identifies Reed–Muller families as a direction for subsequent work. Baumbaugh, Diaz, Friesenhahn, Manganiello and Vetter studied batch properties of Reed–Muller codes and gave a four-request result for \(\operatorname{RM}_2(1,4)\); it does not establish the arbitrary *six*-request property under the present per-coordinate disjointness convention. Standard all-symbol PIR availability for six repetitions of one coordinate is weaker than the all-symbol batch assertion for every multiset of six possibly different coordinates.

## Limitations
This is an exact finite-code classification, not an all-length theorem, a runtime-complexity guarantee for online recovery, or a claim of six-request optimality for other code families. The exhaustive certificate is plain Python and depends on the stated generator normalization, which is equivalent under row operations to any generator for this code. The underlying family, the general recovery framework and the earlier four-query construction are established literature; novelty is claimed solely for the sharp six-request all-symbol batch assertion.

## References
1. A. Boruchovsky, A. Gruica, J. Niemann and E. Yaakobi, *Serving Every Symbol: All-Symbol PIR and Batch Codes*, arXiv:2601.04041 (first submitted 7 January 2026), particularly Definition 2, Proposition 29 and Section 5; https://arxiv.org/html/2601.04041v2.
2. T. Baumbaugh, Y. Diaz, S. Friesenhahn, F. Manganiello and A. Vetter, *Batch Codes from Hamming and Reed–Muller Codes*, arXiv:1710.07386, Journal of Algebra Combinatorics Discrete Structures and Applications 5 (2018), 153–165, particularly Theorems 4.11–4.14; https://doi.org/10.13069/jacodesmath.466634.
3. H. Ly and E. Soljanin, *Optimum 1-Step Majority-Logic Decoding of Binary Reed–Muller Codes*, arXiv:2508.08736 (first submitted 12 August 2025), Sections III–V; https://arxiv.org/html/2508.08736v3.
