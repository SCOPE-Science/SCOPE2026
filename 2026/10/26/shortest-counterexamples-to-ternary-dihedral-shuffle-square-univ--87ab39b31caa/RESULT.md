# Complete classification of the shortest ternary dihedral-shuffle obstructions

## Finding

Among the 1,641 indexed even ternary words of length eight, exactly **48** are not dihedral shuffle squares. They are exactly the orbit of `00011022` under alphabet relabeling, cyclic rotation of the entire word, and reversal. Because all shorter even words admit dihedral shuffle decompositions, this is the complete set of shortest obstructions to Conjecture 2 of Grytczuk, Pawlik and Pleszczyński [1]. The specific witness `00011022` is already implied by the exhaustive neighborhood table in [2]; the contribution here is the complete census and orbit classification.

| Word length | Even ternary words | Non-dihedral-shuffle words |
| ---: | ---: | ---: |
| 2 | 3 | 0 |
| 4 | 21 | 0 |
| 6 | 183 | 0 |
| 8 | 1641 | 48 |

## Assumptions and scope

Words use the alphabet \(\{0,1,2\}\); a word is even when each letter has even multiplicity. A dihedral shuffle square is a word of length \(2h\) whose positions partition into two increasing subsequences of length \(h\), with one subsequence a rotation or reflected rotation of the other. Counts are for indexed linear words, before taking any quotient. The symmetry of the full words is separate from the dihedral test on the two subsequences.

## Proof

At lengths \(2h\le 6\), assign half of each letter's occurrences to each part. This gives two anagrams, and every permutation of at most three positions is dihedral. The exact numbers of even words at length \(2h\) are \((3^{2h}+3)/4\): filtering by the three parity characters gives \(2^{-3}\sum_{\epsilon_0,\epsilon_1,\epsilon_2\in\{1,-1\}}(\epsilon_0+\epsilon_1+\epsilon_2)^{2h}\), with two terms \(3^{2h}\) and six terms 1.

For context, a direct proof of the known witness is short. Any successful partition of `00011022` puts two zeros, one one and one two in each part. One part takes two of the first three zeros and reads `0012`; the other takes the late zero and reads `0102`. Their two zeros are adjacent on one four-cycle and opposite on the other, so the parts cannot be dihedrally equivalent. Equivalently, [2] lists only `1324` and `2314` up to inversion; neither preserves adjacency of a four-cycle.

For completeness at length eight, `verify.py` filters all \(3^8\) words to the even ones. For each it checks all \(\binom84=70\) position subsets with their complements. After testing the necessary equality of letter multiplicities, it checks whether one subsequence occurs as a length-four substring in the other doubled or in its reversal doubled. Every rotation or reflected rotation occurs in these doubled words, and no other length-four words occur. This tests all possibilities exactly. On each even word of multiplicity pattern \((4,2,2)\) it also tests independently whether the repeated symbol has the same cyclic adjacency type in the two parts. For parts of type \((2,1,1)\), adjacency and opposition are the two dihedral classes: dihedral symmetry is transitive on adjacent pairs and on opposite pairs, and the stabilizer of either pair can swap the two remaining positions. The checker then constructs the orbit of `00011022` by all six relabelings and all rotations and reflections of the eight positions. The two resulting sets are equal and have cardinality 48. Thus there are no other shortest obstructions.

## Verification and limits

Run `python3 verify.py` with the standard library; the final output includes `DIHEDRAL_SHUFFLE_COUNTEREXAMPLE_PASS`, the table above and the orbit size. An alternative exhaustive construction is to generate all ternary half-words, pair each with all its cyclic and reflected shifts, interleave each pair over all complementary position subsets, and subtract the set of resulting strings from the set of even words. This construction counts 1,593 successes and 48 failures at length eight and gives the same orbit. No claim is made about the obstruction sets at larger lengths.

## Relationship to prior work

In §2.3 of [1], Conjecture 2 concerns subsequence partitions, not the separate whole-word statement refuted there by `001221`. The earlier record [2] already determines the admissible permutations for `00011022`; it also counts all even eight-letter words and proves an optimal cover by seven unrestricted permutations. Its seven-permutation coverage counts do not determine how many words are covered by the dihedral subgroup, and its table of complete neighborhoods is only for seven selected words. Reference [3] studies ordinary shuffle squares (identical subsequences), not the complete dihedral obstruction set. The originality comparison concerns the 48-word classification only; it does not assert that no other account exists.

## References

1. J. Grytczuk, B. Pawlik and M. Pleszczyński, *Variations on shuffle squares*, [arXiv:2308.13882v2](https://arxiv.org/abs/2308.13882v2), §2.3, Conjecture 2.
2. *Seven permutations suffice and are necessary for ternary length-four shuffle coverings*, [Resultary record 07a749473b9e](https://github.com/Resultary/2026/blob/main/2026/10/12/SCOPE-seven-permutations-suffice-and-are-necessary-for-ternary-length--07a749473b9e/RESULT.md), lower-bound witness neighborhood table.
3. J. Grytczuk, B. Pawlik and A. Ruciński, *Shuffle squares and ordered nest-free graphs*, [arXiv:2503.22043v2](https://arxiv.org/abs/2503.22043v2).
