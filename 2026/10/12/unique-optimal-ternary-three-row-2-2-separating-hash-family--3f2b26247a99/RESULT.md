# Unique optimal ternary three-row \(\{2,2\}\)-separating hash family

## Finding
For a ternary three-row separating hash family of type \(\{2,2\}\), the known optimum is five columns. Among unordered five-column families in \(\{0,1,2\}^3\), exactly \(54\) attain the separating property, and all \(54\) lie in one orbit under the natural Hamming-isometry group \((S_3)^3\rtimes S_3\) of order \(1296\). Thus every optimum has stabilizer order \(24\).

Equivalently, every optimum can be relabeled to
\[
\{000,011,101,110,222\}.
\]
In every optimum each row has symbol multiplicities \((2,2,1)\), the three row-singleton symbols occur in the same column, and after deleting that column the remaining four columns are one parity class of \(\{0,1\}^3\). Every optimum therefore has six unordered codeword pairs at Hamming distance \(2\) and four at distance \(3\).

## Assumptions and scope
A family is represented by an unordered set \(C\subseteq\{0,1,2\}^3\) of distinct columns. It is separating of type \(\{2,2\}\) when, for every two disjoint two-element subsets \(A,B\subseteq C\), at least one of the three coordinates has disjoint symbol sets on \(A\) and \(B\). The classification is only for three rows, alphabet size three, and type \(\{2,2\}\); no claim is made for larger alphabets, more rows, ordered columns, or other separating types.

## Proof
Bazrafshan proved that an \(\operatorname{SHF}(3;n,3,\{2,2\})\) has \(n\le 5\) and displayed a five-column construction, so the optimum cardinality is already known. The new part is the equality classification.

The independent verifier derives the forbidden four-column configurations directly from the definition. A four-set is forbidden when one of its three partitions into two unordered pairs is not separated by any coordinate. It then checks every one of the \(\binom{27}{5}=80730\) five-column subsets and every one of the \(\binom{27}{6}=296010\) six-column subsets. Exactly \(54\) five-sets are admissible and no six-set is admissible.

For each of the \(54\) maxima, the verifier checks that every row has multiplicity pattern \((2,2,1)\) and that the singleton position is the same column in all three rows. Delete this common singleton column. Relabel the two remaining symbols in each row by \(0\) and \(1\). The four surviving columns are then exactly one of the two parity classes in \(\{0,1\}^3\). Independent symbol swaps move the odd parity class to the even one, so every maximum is equivalent to \(\{000,011,101,110,222\}\).

For labeled symbols, the common singleton column has \(3^3=27\) possible symbol triples. Once those singleton symbols are fixed, the four-column binary block has two parity choices, giving \(27\cdot2=54\) labeled maxima. Direct generation of the full group \((S_3)^3\rtimes S_3\) confirms that the orbit of the canonical family has size \(54\), so the stabilizer order is \(1296/54=24\).

## Verification
Run `python3 verify.py`. The verifier reconstructs the \(27\) ternary columns, derives every forbidden four-set from the separating definition, exhausts all five- and six-column subsets, checks the structural singleton/parity description, constructs all \(1296\) natural Hamming isometries, and verifies the orbit and stabilizer counts from scratch.

## Relationship to prior work
Bazrafshan's 2011 dissertation proves the sharp bound \(n\le5\) for \(\operatorname{SHF}(3;n,3,\{2,2\})\) and gives the canonical five-column example, but the inspected equality-case section does not state that every optimum is isomorphic to that example or count the labeled optima. Blackburn, Etzion, Stinson, and Zaverucha give the general separating-hash-family definition and explain that type \(\{2,2\}\) is the secure-frameproof side of the standard coding-theoretic dictionary. Bazrafshan and van Trung develop bounds for separating hash families under MSC \(94A60\). Semantic searches for the exact parameter, uniqueness up to isomorphism, the number \(54\), and the secure-frameproof alias found no source implying this equality classification.

## Limitations
The computation is finite and exhaustive for exactly this parameter set; it is not evidence for any asymptotic statement. The literature search cannot rule out an obscure unindexed equality classification. The group used here is the explicit natural row-permutation and independent row-symbol-permutation group; no assertion is needed about automorphisms outside this action.

## References
1. M. Bazrafshan, *Separating Hash Families*, dissertation, Universität Duisburg-Essen, 2011; Proposition 5.2.3 and Example 5.2.4.
2. S. R. Blackburn, T. Etzion, D. R. Stinson, G. M. Zaverucha, *A bound on the size of separating hash families*, Journal of Combinatorial Theory, Series A 115 (2008), 1246–1256, doi:10.1016/j.jcta.2008.01.009.
3. M. Bazrafshan, Tran van Trung, *Improved bounds for separating hash families*, Designs, Codes and Cryptography, doi:10.1007/s10623-012-9673-7.
