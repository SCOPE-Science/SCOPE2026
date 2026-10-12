# Seven Hamming-isometry classes of optimal \(q=4\) length-three \(2\)-traceability codes
## Finding
Let \(Q=\{0,1,2,3\}\). A code \(C\subseteq Q^3\) is \(2\)-traceability if, for every parent set \(P\subseteq C\) with \(|P|\le2\) and every descendant \(w\in\operatorname{desc}(P)\), every codeword nearest to \(w\) in Hamming distance belongs to \(P\).

The exact maximum is \(4\). There are exactly \(27{,}696\) literal maximum codes. Under the standard Hamming-isometry group
\[
(S_4)^3\rtimes S_3,
\]
of order \(82{,}944\), the maximum codes split into exactly seven orbits.

| Orbit size | Stabilizer order | Representative | Coordinate multiplicity profiles | Pair-distance profile |
|---:|---:|---|---|---|
| \(48\) | \(1728\) | `000,001,002,003` | \((4),(4),(1,1,1,1)\) | \(d=1\) six times |
| \(288\) | \(288\) | `000,011,022,033` | \((4),(1,1,1,1),(1,1,1,1)\) | \(d=2\) six times |
| \(576\) | \(144\) | `000,111,222,333` | \((1,1,1,1)^3\) | \(d=3\) six times |
| \(2592\) | \(32\) | `000,011,122,133` | \((2,2),(1,1,1,1),(1,1,1,1)\) | \(d=2\) twice, \(d=3\) four times |
| \(3456\) | \(24\) | `000,011,022,133` | \((3,1),(1,1,1,1),(1,1,1,1)\) | \(d=2\) three times, \(d=3\) three times |
| \(10368\) | \(8\) | `000,011,122,223` | \((2,1,1),(2,1,1),(1,1,1,1)\) | \(d=2\) twice, \(d=3\) four times |
| \(10368\) | \(8\) | `000,011,122,233` | \((2,1,1),(1,1,1,1),(1,1,1,1)\) | \(d=2\) once, \(d=3\) five times |

In particular, the diagonal distance-three code is only one of seven extremal Hamming-isometry types. The optimum also has equality cases of minimum Hamming distance \(1\) and \(2\).

## Assumptions and scope
A descendant of two parents is formed coordinatewise by choosing, independently in each coordinate, the symbol of one of those parents. A literal code means an unordered subset of \(Q^3\) with the alphabet symbols and coordinate positions fixed.

The equivalence group is the standard Hamming-space symmetry obtained from an arbitrary permutation of the four symbols in each coordinate and an arbitrary permutation of the three coordinates. Its order is \(24^3\cdot6=82{,}944\). Codeword order is never part of the data.

## Proof
A failure of the \(2\)-traceability condition is witnessed by three codewords: two parents and one outside codeword that ties or beats the nearest-parent distance for some descendant. Consequently a code is \(2\)-traceability exactly when every three-codeword subset is \(2\)-traceability. This reduces the finite classification to a three-uniform compatibility hypergraph on the \(4^3=64\) words.

The supplied verifier constructs that hypergraph directly from the definition. Of the \(\binom{64}{3}=41{,}664\) triples, exactly \(14{,}016\) are compatible. It then checks all \(\binom{64}{4}=635{,}376\) four-subsets and obtains exactly \(27{,}696\) valid codes. A separate recursive target-size search, pruning only when a newly formed triple is incompatible, proves that no five-code exists. Thus the maximum is \(4\) without using an external cardinality theorem.

For the equivalence classification, adjacent symbol transpositions in each coordinate together with adjacent coordinate transpositions generate \((S_4)^3\rtimes S_3\). Breadth-first orbit closure from the complete list of \(27{,}696\) maxima yields seven disjoint orbits with sizes
\[
48,\ 288,\ 576,\ 2592,\ 3456,\ 10368,\ 10368.
\]
Their sum is \(27{,}696\). Dividing the group order by the orbit sizes gives stabilizer orders \(1728,288,144,32,24,8,8\). The representatives and structural profiles in the table are recomputed from the same literal code sets.

## Verification
Run `python3 verify.py` with Python 3 and no third-party packages. The program reconstructs all words, descendants, nearest-codeword tests, compatible triples, all four-codeword maxima, a complete no-five-code search, and the symmetry orbit partition.

It also reruns the literal traceability definition on every enumerated maximum rather than relying only on the three-uniform reduction. The canonical newline-terminated census of all \(27{,}696\) literal maxima has SHA-256 `b22fb6b34d0cca55a2b161541233bcf81435a8d81d55122fc7c8e0c8263c9779`.

The expected first output line is:

`VERIFY_OK vertices=64 good_triples=14016 maximum=4 labeled_maxima=27696 natural_group=82944 orbits=7 orbit_sizes=48,288,576,2592,3456,10368,10368 stabilizers=1728,288,144,32,24,8,8 maxima_sha256=b22fb6b34d0cca55a2b161541233bcf81435a8d81d55122fc7c8e0c8263c9779`

## Relationship to prior work
Blackburn, Etzion, and Ng introduced the length-three construction \(3(q-1)/2\) for odd alphabets and established general asymptotic bounds for traceability codes. Their public preprint does not specialize to \(q=4\) or classify equality cases.

Owen and Ng reproduce the odd-alphabet length-three construction and then study length four. Their full text likewise does not give a four-symbol length-three extremizer classification.

A published 2026 exact-cardinality result proves
\[
M_{\mathrm{TA}}(3,q,2)=\max\bigl(q,\lfloor(3q-3)/2\rfloor\bigr),
\]
so it already implies the maximum value \(4\) at \(q=4\). Its statement, proof, constructions, and verification section do not enumerate the equality cases at \(q=4\), quotient them by Hamming isometries, or give the seven representatives above. The present finding is therefore an equality-case classification rather than a new cardinality formula.

## Limitations
The classification is only for strength two, length three, and alphabet size four. It does not classify extremizers for other alphabet sizes or longer codes. The originality assessment cannot exclude an obscure or unindexed historical enumeration under different terminology, although targeted searches for the exact parameter, equivalence formulation, and final numerical invariants found none.

## References
1. S. R. Blackburn, T. Etzion, S.-L. Ng, “Traceability Codes,” Cryptology ePrint Archive 2009/046; later *Journal of Combinatorial Theory, Series A* 117(8), 1049–1057 (2010), DOI 10.1016/j.jcta.2010.02.009. The ePrint history records 2009-01-29.
2. S. Owen, S.-L. Ng, “A note on an upper bound of traceability codes,” *Australasian Journal of Combinatorics* 62(1), 140–146 (2015).
3. “Exact maximum size of q-ary 2-traceability codes of length three,” published 2026-09-20; exact all-alphabet cardinality theorem and constructions.
