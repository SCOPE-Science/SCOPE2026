# Independent mathematical audit

## correctness

PASS

A uniform permutation factors bijectively as a uniform word of child labels of the prescribed multiplicities and independent uniform permutations within the children. Union greedy decisions are independent in those child permutations, and every maximal independent set is a product of child maximal independent sets. At a join the first letter is i with probability n_i/n; the first accepted vertex blocks all other children, leaving the independent uniform order in child i. Every maximal independent set at a nonempty join belongs to a unique child and is maximal within it. The flat law selects these children with weights m_i/m; within each, the law is flat. Comparing conditional laws and those two child-weight vectors gives exactly the positive n_i/m_i balance condition. At unions flatness is equivalent to flat marginals, which are the independent child laws. The base case is a leaf (the stated construction starts from single vertices). Multiplication/summation of counts and cross-multiplication for balance take a constant number of arithmetic operations per child edge, not necessarily constant bit complexity. This also makes clear which output is given exactly without listing every set.

## originality

PASS

The law coincides with independently stated exact laws on several subclasses and with a known sufficient criterion where that criterion applies, but the exact all-cograph cotree law and iff test are not covered by the compared statements. The probability recurrences are natural decomposition facts; their novel use here is a complete decision and probability rule on the whole hereditary class, including uniform graphs outside the older sufficient criterion.

## value

PASS

This gives a complete iff decision and exact individual-output laws across a canonical hereditary class without enumerating maximal sets to test uniformity. Comparing counts and vertex masses gives structural insight not captured by the old sufficient condition or by output-size statistics: K2 joined to two disjoint K2s is irregular and uniform despite outputs of different cardinalities. The short decomposition proof yields an exact algorithm on an unrestricted class rather than a tabulated case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
