# Independent mathematical audit

## correctness

PASS

At a prefix, the number of copies that could emit the next block is at most the floor of the previous-stage count divided by its block length. Conversely assign successive occurrences of each letter to the numbered copies in full batches: each batch's first and all subsequent occurrences are read only after the preceding block of that copy has completed by the inequality at that prefix. The specified terminal counts complete all copies. Feasible count vectors are all reachable by sorted prefixes and have accepting completions by appending the missing occurrences in stage order. Distinct vectors require different suffix Parikh vectors, so these residuals and the dead residual are all distinct. Writing counts as p_j t_j+r_j gives decreasing weak levels; equality of adjacent levels forces residue zero at the lower stage, while a strict drop allows all residues. For a drop set J, if t_1<k the multiplicity is p_1 times the product over J with binomial(k,|J|+1) choices of levels, and if t_1=k the multiplicity is just the product over J with binomial(k,|J|) choices. This enumerates all subsets with and without stage 1, giving the elementary-symmetric sum plus one sink. For k=0 there is precisely an accepting start and sink since d>=1; d=1 gives the singleton one-letter chain and sink. The unit case follows by Vandermonde and all claimed corollaries follow algebraically.

## originality

PASS

The inspected overlap concerns two-copy special cases and bounds, or a restricted membership implication, not the exact arbitrary-k complete-minimum law with positive ordered-block lengths.

## value

PASS

An exact minimum for a natural parametrized family of finite shuffle languages improves on a size estimate and explains the symmetry under block permutations despite ordered membership. The prefix test and residual characterization give both recognition and a sharp automaton lower bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
