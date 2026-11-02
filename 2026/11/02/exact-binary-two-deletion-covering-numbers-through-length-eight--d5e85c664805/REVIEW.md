# Scientific review — exact binary two-deletion covering numbers through length eight

## Correctness

**PASS.** The claim is quantified only over the seven fixed lengths \(2\) through \(8\). Each upper bound is an explicit family of words whose deletion descendants are checked against the entire target space. For the nontrivial lower bounds, a nonnegative integer weight on target words implies that any covering family has at least total-weight/max-single-shadow-weight members. The three numerical certificates have independently recomputable totals and maxima of \((8,3)\), \((10,3)\), and \((74,12)\). Exhaustion of all 64, 128, and 256 corresponding source words is complete, not a probabilistic experiment. The separate subsequence predicate checks the shadow generator. The elementary \(n=5\) obstruction follows from the simultaneous need for three zeros and three ones. The program is self-contained and was replayed from its actual file.

## Originality

**PASS on the inspected literature and relevant exact-record comparison; residual priority risk remains.** Two primary articles were inspected for the relevant subsequence-covering definitions, lower bounds, general two-deletion arguments and distinctions from burst deletion. Neither specifies the seven-entry exact profile or a lower certificate that implies its terminal value. The closest earlier exact small covering record concerns ternary one-deletion codes, with no parameter reduction covering the binary radius-two claim. Searches for the seven-word cover, its incidence interpretation, the notation \(D(2,8,2)\), and alternative descriptions returned no matching exact result. This is evidence of noncoverage among inspected results, not proof of publication uniqueness.

## Value

**PASS.** Determining the minimum number of short templates needed to contain every shorter binary word as a scattered subsequence is the defining finite covering-code optimization. The complete initial radius-two profile supplies an exact benchmark, and the jump from four at length seven to seven at length eight is not obtained from the elementary volume lower bound, which yields only three at length eight. The small integer-weight certificates make the nontrivial lower bounds transparent and reusable as finite test instances for future covering-code bounds and algorithms; no unsupported asymptotic or downstream theorem is asserted.

## Closest sources and limitations

The general covering-code theory is due to Lenz et al., arXiv:1911.09944, especially Theorem 14 and the multiple-deletion section. Xie et al., arXiv:2606.15379, Section V proves large-alphabet asymptotic deletion-covering bounds and Section VI treats adjacent burst deletions, not all arbitrary two-deletion positions. The related short ternary single-deletion covering result is not a stronger bound in the present parameters. Unindexed tables or earlier exact calculations remain possible; independent priority verification and independent mathematical audit have not been conducted. No result for length nine or larger, or for nonbinary alphabets, is proved here.

Self-review: passed. Independent audit: not yet performed.
