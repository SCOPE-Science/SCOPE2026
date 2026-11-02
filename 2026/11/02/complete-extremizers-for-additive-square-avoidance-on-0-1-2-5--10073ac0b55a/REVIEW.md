# Scientific review

## Correctness — PASS

The end-square extension identity follows directly from prefix sums. Induction proves that the recurrence is exhaustive and neither creates nor omits a valid word. The two embedded programs implement dissimilar extension checks (a forbidden-letter identity versus literal sliding block sums) and agree on all \(299596819\) visited prefixes, the eight depth-86 words and zero depth-87 words. The four reversal pairings and three Parikh profiles are checked from the complete list. Arithmetic ranges are bounded. This is a finite computer-assisted result, not a claim proved from a sample.

## Originality — PASS, with risk

Zhang's arXiv:2610.02215v1 and its technical supplement were inspected: the paper proves the sharp length \(86\), exhibits one word and records total search visits, but does not give an eight-word census or reversal/Parikh classification. Searches under the exact alphabet, extremal length, additive-square and equivalent terminology did not reveal an identical assertion in the published literature or searchable mathematical research records. The older endpoint-sum result is inapplicable to this isolated alphabet. Risk: the separate electronic source archive could not be read, so its unpublished raw logs might implicitly expose the same endpoint count; there has been no independent priority audit.

## Value — PASS

The alphabet \(\{0,1,2,5\}\) is the first isolated four-letter finite-spectrum class immediately beyond the previously studied endpoint-sum family in Zhang's sharp classification. Determining **all** equality cases refines the natural exact extremal length problem and shows marked rigidity: only eight words and four reversal orbits survive an exhaustive search of nearly 300 million valid prefixes. Their distinct Parikh profiles distinguish three types invisible from the published existence example and sharp bound. The new assertion is an exact complete classification of the natural extremizers, not a routine reformulation of the maximum-length result.

## Limits and closest work

The primary result is finite, for the stated integer alphabet only. The original maximum length and example are credited to Zhang; the new part is the complete optimizer census. External independent verification and supplementary-archive priority comparison remain outstanding.

Self-review: passed. Independent audit: not yet performed.
