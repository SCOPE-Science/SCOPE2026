# Scientific review: mixed length-two duplication spheres

## Correctness

PASS. The two same-type collision lemmas account for all repeated positions. A source substring \(abba\) with \(a\ne b\) gives precisely the new cross-type equality \(P_i=T_{i+2}\); necessity follows by comparing shifted output coordinates and excluding tandem sites to the left. Adding nonconstant palindromic outcomes to the distinct tandem outcomes and subtracting exactly these collisions gives the pointwise formula. Two positive comparison sums yield the sharp nonbinary upper bound and exact extremizers. In the binary case, the transition-word deficiency is a nonnegative sum over maximal zero-runs; its zero cases give the classification and rational generating function. Direct full-set enumeration agrees for 79,073 tested words. The logical quantifiers cover all \(q\ge2\), \(n\ge2\); the test range is not substituted for a proof.

## Originality

PASS, subject to the stated literature risk. Lenz–Wachter-Zeh–Yaakobi, arXiv:1707.00052, Section 3, treats tandem spheres and palindromic spheres separately; it provides neither a mixed-channel union count nor the \(abba\) intersection correction or tribonacci binary extremizers. Zeraatpisheh–Esmaeili–Gulliver, DOI:10.1109/ACCESS.2020.2995812, develops duplication code constructions including mixed mechanisms but does not give the exact one-error mixed descendant sphere in the inspected sections. Yohananov–Schwartz, arXiv:2312.00394, treats reverse-complement/palindromic capacities rather than this mixed one-step channel. The closest publicly indexed calculations count confusable pairs under a fixed tandem length or code sizes for two palindromic errors, not the source-wise mixed sphere. A differently phrased exact identity in unindexed literature remains possible.

## Mathematical value

PASS. A channel that permits either of two biologically motivated duplication mechanisms has a different one-step output sphere from either mechanism alone. The pointwise correction isolates the precise overlap pattern, while the sharp transition from binary to larger alphabets and the tribonacci number of binary maximizers determine nontrivial extremal structure for every block length \(n\). These properties are directly relevant to sphere-counting and packing analyses, although no code-rate improvement or multi-error claim is established.

## Scope and uncertainty

Only exact-one length-two copy operations, without complementation, are covered. The unrestricted proof is a direct word-comparison argument; finite checker agreement adds reassurance without proving all instances. The originality review is bounded by located accessible sources, and independent mathematical validation is outstanding.

Self-review: passed. Independent audit: not yet performed.
