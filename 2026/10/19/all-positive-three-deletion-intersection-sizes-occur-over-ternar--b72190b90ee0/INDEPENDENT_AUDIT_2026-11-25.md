# Independent mathematical audit

## correctness

PASS

If the three-deletion intersection is nonempty but the two-deletion intersection is empty, the longest common subsequence length is exactly n-3. The number of distinct longest common subsequences of two words of lengths l+d and l+e and LCS length l is at most binomial(d+e,d): if the first symbols agree, all LCSs start with that common symbol (otherwise both suffixes would already have a subsequence of length l, which can be extended); stripping this symbol in both words reduces l by one. If the first symbols disagree, the LCSs come from the two first-symbol deletions, retaining only branches of LCS length l. The binomial recurrence bounds the union inductively, with bound 1 when either word has length l. Thus d=e=3 gives 20, agreeing with the cited theorem. An independent exact replay checked all 20 witness rows and verified the explicit ternary pair's 18 common words using deletion-position sets. Injections of the used symbols preserve all equality tests. The separate binary replay represented each deletion set as an integer bitmask and built all masks by the retain-or-discard-first-symbol recurrence; it checked every y<x at each length 3–13 using exact intersection and popcount. At n=13, 29,431,953 unordered pairs were admissible and their spectrum was 0–20 except 18, with no hits at 18 at earlier lengths either.

## originality

PASS

Applicable upper bounds and the extremal values 19 and 20 are prior work. The supported new scope is the complete realization of the intervening spectrum under two-deletion separation for q>=3, notably a ternary witness for 18, and the separate finite exclusion of binary 18 at the nontrivial lengths 10–13. Neither an extremal value nor an alphabet lift of known endpoint examples produces these results.

## value

PASS

Realizing, not just bounding, each cardinality closes the naturally posed order-three feasibility question for every alphabet with at least three symbols. The ternary value 18 is the one missing from the exhibited binary constructions, and the bounded binary exclusion records how far that obstruction is known, rather than treating an unbounded search as settled. The complete witness set is useful for arguments requiring specified feasible seed sizes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
