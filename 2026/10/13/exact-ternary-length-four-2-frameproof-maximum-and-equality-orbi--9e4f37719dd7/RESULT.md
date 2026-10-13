# Exact ternary length-four \(2\)-frameproof maximum and equality orbits
## Finding
Let \(C\subseteq\{0,1,2\}^4\). Call \(C\) a ternary length-four \(2\)-frameproof code when, for any distinct \(x,y,z\in C\), the word \(z\) is not in the descendant of \(\{x,y\}\); equivalently, for each choice of one word against the other two there is a coordinate where its symbol differs from both opposing symbols. This is exactly an \(\mathrm{SHF}(4;|C|,3,\{1,2\})\).

The exact maximum is
\[
|C|=12.
\]
There are exactly \(5{,}616\) labeled unordered maximum codes. Under the natural Hamming-isometry group
\[
(S_3)^4\rtimes S_4,
\]
of order \(31{,}104\), the maxima split into exactly two orbits, of sizes \(432\) and \(5{,}184\), with stabilizer orders \(72\) and \(6\), respectively.

A representative of the orbit of size \(432\) is
\[
\{0000,0011,0101,0222,1001,1112,1120,1210,2022,2110,2202,2221\}.
\]
Every coordinate of this type has symbol multiplicities \(4,4,4\), and its pairwise Hamming-distance distribution is \(18\) pairs at distance \(2\), \(36\) at distance \(3\), and \(12\) at distance \(4\).

A representative of the orbit of size \(5{,}184\) is
\[
\{0000,0011,0022,0101,0202,1001,1112,1120,1210,2002,2110,2221\}.
\]
For this type, exactly one coordinate has multiplicities \(4,4,4\), while the other three have multiplicities \(5,4,3\), up to relabeling. Its pairwise Hamming-distance distribution is \(21\) pairs at distance \(2\), \(33\) at distance \(3\), and \(12\) at distance \(4\).

## Assumptions and scope
Codes are unordered sets of distinct words. “Labeled” means that the four coordinates and the three symbols in every coordinate are fixed. The equivalence group in the orbit statement consists only of coordinate permutations and independent symbol permutations in each coordinate.

The result is specific to alphabet size \(3\), length \(4\), and coalition size \(2\). It does not assert a formula for larger alphabets or lengths.

## Proof
There are \(3^4=81\) possible words. For three distinct words, the frameproof condition is symmetric: each of the three words must have some coordinate whose symbol occurs in neither of the other two words at that coordinate. Direct reconstruction gives \(18{,}792\) forbidden triples.

Independent symbol permutations can map any selected codeword to \(0000\) while preserving the frameproof property. Therefore an alleged code of size \(13\) can be normalized to contain \(0000\). The verifier enumerates all increasing subsets containing \(0000\). At each node it keeps exactly those later words that make a legal triple with every pair already selected; hence no valid extension is discarded. The exhaustive normalized search visits \(936{,}713\) nodes and finds no size-
\(13\) code. This proves \(|C|\le12\). The displayed representatives are directly checked and give the matching lower bound.

The same exhaustive recursion enumerates exactly \(832\) size-
\(12\) codes containing \(0000\). Coordinatewise translations modulo \(3\) form a transitive subgroup of the natural symbol action on the \(81\) words. Translating the \(832\) normalized maxima and deduplicating yields exactly \(5{,}616\) labeled maxima. The incidence identity
\[
832\cdot81=5{,}616\cdot12
\]
independently checks the count, since every labeled maximum contains exactly \(12\) choices of a word that can be translated to \(0000\).

Finally, adjacent coordinate swaps and adjacent symbol transpositions generate the full group \((S_3)^4\rtimes S_4\). Breadth-first orbit enumeration over the complete maximum-code census gives orbit sizes \(432\) and \(5{,}184\). Orbit-stabilizer then gives stabilizer orders \(31{,}104/432=72\) and \(31{,}104/5{,}184=6\). Direct checks on the orbit representatives give the stated coordinate multiplicity and Hamming-distance profiles.

## Verification
The standalone `artifacts/verify.py` uses only the Python standard library. It reconstructs all words and forbidden triples from the definition, performs the complete normalized size-
\(13\) exclusion, enumerates all normalized and labeled size-
\(12\) maxima, reconstructs both natural-equivalence orbits, and verifies the two structural profiles.

A fresh replay returned:

`VERIFY_OK maximum=12 normalized_maxima=832 labeled_maxima=5616 size13=0 natural_group=31104 orbits=2 orbit_sizes=432,5184 stabilizers=72,6 bad_triples=18792 nodes12=1354177 nodes13=936713 census_sha256=b064067a522954ba8b0f3150ebc11b264dc601831ded0e41b0baa614e7bdc293`

## Relationship to prior work
Li, van Rees, and Wei posed the problem of maximizing the number of columns in \(\mathrm{SHF}(4;m^2+a,m,\{1,2\})\) and exhibited only \(10\) columns for \(m=3\). Their 2006 paper did not claim that example optimal. Bazrafshan’s 2011 dissertation repeats the same open question and again records the ternary example with \(10\) columns, while explicitly labeling only the binary five-column example as optimal. Thus the present equality \(12\) closes that smallest unresolved ternary instance and improves the historical construction by two columns.

Blackburn’s general length-four frameproof bound gives \(2q^2-2\), which is \(16\) at \(q=3\), so it does not imply the exact value. Later length-four improvements cited in the checked literature apply only for much larger alphabets, for example \(q>48\), and therefore do not cover the ternary case.

Exact-parameter searches for the aliases “separating hash family,” “2-frameproof code,” and the parameters \(4,12,3,\{1,2\}\), together with searches for the final counts and orbit sizes, found no published statement implying the exact maximum or equality classification.

## Limitations
The upper bound is a complete finite enumeration after a symmetry normalization, not a general symbolic bound in the alphabet size. The equality census is under the stated natural Hamming-isometry group only. An obscure or unindexed historical enumeration of the ternary instance remains a residual originality risk, but the two directly relevant full-text sources inspected both present the case as unresolved at \(10\) columns rather than as a solved \(12\)-column optimum.

## References
1. P. C. Li, G. H. J. van Rees, and R. Wei, “Constructions of 2-Cover-Free Families and Related Separating Hash Families,” *Journal of Combinatorial Designs* 14 (2006), 423–440, DOI 10.1002/jcd.20109. First published online 21 April 2006.
2. Marjan Bazrafshan, *Separating Hash Families*, doctoral dissertation, Universität Duisburg-Essen, 2011, URN urn:nbn:de:hbz:464-20110823-103007-8.
3. Simon R. Blackburn, “Frameproof Codes,” *SIAM Journal on Discrete Mathematics* 16 (2003), 499–510, DOI 10.1137/S0895480101384633.
4. Minquan Cheng, Jing Jiang, and Qiang Wang, “Improved bounds on 2-frameproof codes with length 4,” *Designs, Codes and Cryptography* 87 (2019), 97–106, DOI 10.1007/s10623-018-0490-5.
