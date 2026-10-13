# Sharp quaternary five-symbol synchronization codes detecting one substitution

## Finding

Let \(\Sigma=\{0,1,2,3\}\). A set \(C\subseteq\Sigma^5\) is **non-overlapping** if, for every \(x,y\in C\) (including \(x=y\)) and every \(j\in\{1,2,3,4\}\), the length-\(j\) prefix of \(x\) differs from the length-\(j\) suffix of \(y\). Additionally require the Hamming distance of any two distinct codewords to be at least \(2\), so one substitution can be detected.

The exact extremal cardinality is

\[
\boxed{\max |C|=32.}
\]

The bound is witnessed by a parity-lifted union of two binary non-overlapping synchronization templates. In contrast, imposing the same Hamming-distance condition within any *single* traditional Blackburn length-five family \(I^4J\) or its reversal permits at most \(27\) words, and \(27\) is attained. Thus the sharp construction necessarily departs from that single-template family.

## Assumptions and scope

Symbols, positions, prefixes, and suffixes are literal; coordinates are not identified under cyclic rotation. The restriction includes a word's own nontrivial prefix-suffix comparisons. The minimum Hamming distance is \(2\), which **detects**, but need not correct, one substitution. The result is specific to length \(5\), alphabet size \(4\), and these two simultaneous constraints. Its primary subject is MSC2020 94B50.

## Proof

### Constructing 32 words

For arbitrary binary variables \(a,b,t,u,v\in\{0,1\}\), put \(w=a\oplus b\oplus u\oplus v\) and take

\[
 c(a,b,t,u,v)=(a,\ b,\ 2t+u,\ 2(1-t)+v,\ 2+w).
\]

These are \(32\) distinct words: the first two symbols recover \(a,b\), the third and fourth identify \(t,u,v\), and the last coordinate is then determined. After replacing each symbol in \(\{0,1\}\) by \(0\) and each in \(\{2,3\}\) by \(1\), their group patterns are exactly \(00011\) and \(00101\). These two length-five binary patterns have no nontrivial prefix-suffix coincidences, within or across patterns. The original quaternary words are therefore non-overlapping.

If two words have different values of \(t\), they differ in positions three and four. If \(t\) is fixed, changing exactly one coordinate among the first four changes exactly one of \(a,b,u,v\), which must also change \(w\) and thus the fifth coordinate. No two distinct words can have Hamming distance one. This proves the lower bound \(32\).

### Universal upper bound by two explicit clique covers

Let \(C\ne\varnothing\) be any admissible code. Write \(A\) for its set of first-coordinate symbols and \(B\) for its set of fifth-coordinate symbols. The overlap exclusion at length one forces \(A\cap B=\varnothing\), so \(1\le |A|\le3\). Reversing all words preserves both constraints and exchanges \(A\) and \(B\). If \(|A|=3\), then \(|B|=1\), and reversal reduces to a first-coordinate set of size one. Accordingly, up to global alphabet relabeling and possible reversal, we may assume \(a=|A|\in\{1,2\}\), with first coordinate in \(\{0,\dots,a-1\}\) and last in \(\{a,\dots,3\}\).

For each \(a\in\{1,2\}\), define \(W_a\) to be the lexicographically ordered set of all such five-symbol words that have **no own nontrivial border**, i.e., no prefix of length \(1,2,3,4\) equals the suffix of the same length. Complete independent generation gives \(|W_1|=180\) and \(|W_2|=240\).

Make a conflict graph \(G_a\) on \(W_a\): distinct vertices are adjacent precisely if they have Hamming distance at most one **or** some proper prefix of either vertex equals a same-length suffix of the other. Every admissible \(C\), after the above normalization, is an independent set of the relevant \(G_a\).

The accompanying exact certificate, `artifacts/upper_certificate.json`, lists **32 vertex cliques covering all vertices** of \(G_1\) and **32 vertex cliques covering all vertices** of \(G_2\). Its vertex lists are explicit, and its clique indices are zero-based indices into those lists. The standalone programs `artifacts/verify.py` and `artifacts/verify_independent.py` each regenerate every vertex, verify the two exhaustive vertex lists, check every pair in each clique against the original conflict definition, and check that the 32 cliques together cover every vertex. The programs use independent string and integer encodings and only the Python standard library.

Because an independent set has at most one vertex in each clique of any clique cover, \(\alpha(G_a)\le32\) for both \(a=1,2\). Reversal and relabeling exhaust all possible nonempty admissible codes. Hence \(|C|\le32\), matching the explicit construction. This is a finite exhaustive proof: it does **not** infer the universal bound from a solver's report, a partial search, or probabilistic experiments. The small certificate is sufficient to reconstruct the complete upper bound by pairwise exact checks.

### Comparing the single-template construction

Suppose \(I,J\) partition \(\Sigma\), with \(|I|=\ell\in\{1,2,3\}\), and \(C\subseteq I^4J\) has minimum Hamming distance at least \(2\). Deleting the last coordinate is injective on \(C\), and so is deleting the fourth coordinate: otherwise a pair differs in only one position. Therefore

\[
 |C|\le \min\{\ell^4,\ \ell^3(4-\ell)\}\in\{1,16,27\},
\]

where the final three values correspond to \(\ell=1,2,3\). Reversal does not alter this inequality. The upper value \(27\) is attained by choosing \(I=\{0,1,2\}\), \(J=\{3\}\), allowing arbitrary first three symbols, and making the fourth their sum modulo \(3\). Hence the single-template maximum is exactly \(27\), strictly smaller than \(32\).

## Verification

Run, from any working directory, `python3 artifacts/verify.py` and `python3 artifacts/verify_independent.py` in the extracted package. Both are standard-library-only and read the bundled certificate using their own package-relative path. The first enumerates the \(180\) and \(240\) candidate words, checks all supplied clique pairs, all candidate coverage, the \(32\)-word construction, and the \(27\) single-template bound. The second independently reconstructs the complete vertex sets as base-four integers, checks every certificate clique and the entire construction. The exact observed outputs are retained in `artifacts/verification_output.txt`.

The upper-bound proof uses the explicit cliques as a fully checkable finite witness; finding the cliques need not be reproduced for correctness. No claim about codes of other lengths, alphabets, or minimum Hamming distances follows from this enumeration.

## Relationship to prior work

Blackburn introduced systematic non-overlapping-code constructions and bounds, but did not determine this Hamming-constrained length-five optimum. Levy and Yaakobi studied \((d_h,d_m)\)-mutually uncorrelated codes, including error detection and DNA storage, establishing general construction methods and non-sharp short-parameter bounds; their \((2,1)\) constraints include this problem. Stanovnik, Moškon, and Mraz studied unrestricted maximal non-overlapping codes; the later published length-five exact result gives the **unrestricted** four-symbol maximum \(81\), not the present distance-constrained value. The binary-template lifting idea is established in this literature and is **not** asserted to be new here.

Wang, Fang, and Feng (2025) also study error-correcting codes under restricted prefix-suffix overlap constraints and describe Gilbert–Varshamov-type lower bounds. Their accessible publisher material does not establish the exact numerical claim above; a complete independent comparison against that paper's unavailable full text remains a bibliographic limitation. The new claim is specifically the sharp \(32\) bound with its explicit universal clique-cover certificate and the strict separation from single-template \(I^4J\) designs.

## Limitations

The theorem neither classifies every \(32\)-word optimizer nor establishes optimal cardinalities outside \((q,n,d_H)=(4,5,2)\). The numerical proof is exact but finite; it relies on independently checkable bundled clique lists rather than a short structural inequality. One-substitution detection does not imply one-substitution correction. An unindexed or inaccessible earlier exact calculation could duplicate the result; public-source searching cannot prove absolute priority.

## References

1. S. R. Blackburn, “Non-Overlapping Codes,” arXiv:1303.1026v1 (first public 2013-03-05), *IEEE Transactions on Information Theory* 61 (2015), 4890–4894; https://arxiv.org/abs/1303.1026.
2. M. Levy and E. Yaakobi, “Mutually Uncorrelated Codes for DNA Storage,” arXiv:1804.05371 (2018), *IEEE Transactions on Information Theory* 65 (2019), 3671–3691; https://arxiv.org/abs/1804.05371.
3. L. Stanovnik, M. Moškon, and M. Mraz, “In search of maximum non-overlapping codes,” *Designs, Codes and Cryptography* 92 (2024), 1299–1326; https://doi.org/10.1007/s10623-023-01344-z.
4. X. Wang, Y. Fang, and T. Feng, “q-ary (1,k)-overlap-free codes with given restrictions,” *Discrete Mathematics* 348 (2025), 114236; https://doi.org/10.1016/j.disc.2024.114236.
5. “Exact size and enumeration of maximum length-five non-overlapping codes,” public mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-length-five-non-overlapping-code-optima--e8e2fd1a9e7a.
