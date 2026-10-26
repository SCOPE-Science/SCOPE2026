# Shortest counterexamples to ternary dihedral shuffle-square universality

## Finding
A word over \(\{0,1,2\}\) is **even** if every letter occurs an even number of times. A **dihedral shuffle square** of length \(2h\) can be partitioned into two disjoint, order-preserving subsequences \(A,B\), each of length \(h\), with \(B\) a rotation of \(A\) or of the reversal of \(A\).

The assertion that every even ternary word is a dihedral shuffle square is false. The word \(\mathtt{00011022}\) is an eight-letter counterexample, and eight is the shortest possible positive length. Moreover, among all \(1641\) even ternary words of length eight, **exactly \(48\)** are counterexamples. They are precisely the words obtained from \(\mathtt{00011022}\) by alphabet relabeling, cyclic rotation of the entire word, and reversal. Thus the complete shortest-obstruction set forms one symmetry class.

The exact length-by-length census through the first failure is:

| Word length | Even ternary words | Non-dihedral-shuffle words |
| ---: | ---: | ---: |
| 2 | 3 | 0 |
| 4 | 21 | 0 |
| 6 | 183 | 0 |
| 8 | 1641 | 48 |

## Assumptions and scope
The alphabet is exactly \(\{0,1,2\}\), with indexed linear words and with no equivalence relation imposed until the final symmetry classification. A partition is a two-coloring of every position, read in increasing order within each color; it is not a split into two contiguous halves. Anagram equality of the two subsequences is necessary but not sufficient for dihedral similarity. The dihedral group on \(h\) positions acts by cyclic rotations and reflected rotations (for \(h=1,2\), use the resulting permutation action). The census is exactly for lengths \(2,4,6,8\); no general length distribution is asserted.

## Proof
**1. No smaller counterexample.** Every even word of length \(2h\) admits a partition into two anagrams of length \(h\): allocate exactly half the occurrences of each letter to each subsequence. For \(h\le3\), the induced dihedral permutation action is the full symmetric group on \(h\) positions. Every two anagrams are therefore dihedrally equivalent. This proves all even ternary words of lengths \(2,4,6\) satisfy the property.

**2. An explicit counterexample without computational assumptions.** In \(W=\mathtt{00011022}\), there are four zeros, two ones and two twos. Any admissible partition must put two zeros, one one and one two into each four-letter subsequence. The four zeros occur in positions \(1,2,3,6\), the ones in \(4,5\), and the twos in \(7,8\). Consequently, whichever two zeros are assigned to the first part, every balanced partition yields the pair \((\mathtt{0012},\mathtt{0102})\), in one order or the other. Indeed, selecting two of the initial three zeros gives \(\mathtt{0012}\); selecting the late zero gives \(\mathtt{0102}\). There are \(\binom42\cdot2\cdot2=24\) labeled balanced partitions, exactly twelve of each ordered type.

In the cyclic four-position arrangement of \(\mathtt{0012}\), the two zero positions are adjacent. In the cyclic arrangement of \(\mathtt{0102}\), they are opposite. A dihedral permutation of a four-cycle preserves adjacency. Hence those two four-letter words are not dihedrally equivalent, and no balanced partition of \(W\) is a dihedral shuffle square.

**3. Exact enumeration and symmetry completeness.** The standalone `verify.py` enumerates every one of the \(3^m\) labeled ternary words of each \(m\in\{2,4,6,8\}\). For an even word of length \(2h\), it enumerates all \(\binom{2h}{h}\) position subsets, constructs their two complementary subsequences, and tests all cyclic and reverse-cyclic agreements. There is no sampling: each possible partition corresponds to exactly one of these subsets, and the string-in-doubled-string test enumerates every rotation. Independent of the rotation test, the checker exploits the exact structural classification of dihedral orbits of four-letter words with multiplicities \((2,1,1)\): the two occurrences of the repeated letter are either adjacent or opposite on a four-cycle, and those are the only two dihedral types. It checks agreement of these independently computed decisions on every eight-letter word with multiplicity pattern \((4,2,2)\).

The certificate returns zero failures at lengths \(2,4,6\), and exactly \(48\) failures at length eight. It independently generates all permutations of the alphabet and all reversals and cyclic rotations of \(\mathtt{00011022}\), verifies this orbit has \(48\) distinct members, and checks that it equals the complete enumerated failure set. This supplies a finite exhaustive proof of the census and orbit statement, without extrapolating beyond eight letters.

## Verification
Execute `python3 verify.py` using Python 3 and its standard library. The program checks both the complete partition enumeration and a separate four-position zero-adjacency criterion. It asserts the length counts, all \(48\) exceptions, their single orbit, the witness's complete set of balanced pairs, and the distribution of the exceptions among the three possible majority letters. The success message is `DIHEDRAL_SHUFFLE_COUNTEREXAMPLE_PASS`. The proof of the witness and minimality above is independent of the program; the finite exhaustive computation certifies the exact total \(48\).

## Relationship to prior work
Grytczuk, Pawlik and Pleszczyński, *Variations on shuffle squares*, arXiv:2308.13882, publicly available August 26, 2023, Conjecture 2, proposes that every even ternary word admits such a dihedral shuffle decomposition. Its Theorem 2 establishes a weaker cyclic-shuffle theorem for binary words; neither that theorem nor its ternary conjecture supplies this counterexample or the complete first-failure census. The 2025 work of Grytczuk, Pawlik and Ruciński on ordered nest-free graphs analyzes ordinary, mainly binary, shuffle squares, not the present ternary dihedral property. Published-source and semantic research-record searches did not locate an earlier statement of this exact obstruction or its \(48\)-word classification; this absence is not a proof of absolute uniqueness.

## Limitations
The classification is of the **shortest** counterexamples only. It does not enumerate or characterize counterexamples at larger lengths and does not settle broader covering-set conjectures for arbitrary permutation families. The short finite computation is exhaustive for the specified domain, while originality remains subject to independently locating unindexed literature. No independent mathematical audit has been performed.

## References
1. J. Grytczuk, B. Pawlik and M. Pleszczyński, *Variations on shuffle squares*, arXiv:2308.13882 (first public version August 26, 2023; inspected revised 2024 text), especially Section 2.3, Conjecture 2. https://arxiv.org/abs/2308.13882
2. J. Grytczuk, B. Pawlik and A. Ruciński, *Shuffle squares and ordered nest-free graphs*, arXiv:2503.22043 (2025), especially Sections 1–3. https://arxiv.org/abs/2503.22043
3. Standalone complete verifier supplied as `verify.py`.
