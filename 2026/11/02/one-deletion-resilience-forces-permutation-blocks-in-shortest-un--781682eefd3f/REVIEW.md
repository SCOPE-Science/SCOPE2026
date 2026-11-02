# Self-review

## Correctness
PASS. A constant-symbol target survives any single deletion only when each letter has at least \(k+1\) occurrences; independent permutation blocks attain the resulting length bound. For \(k\ge2\), deleting the last copy of \(b\) and testing \(a^i b^{k-i}\) forces \(a_i<b_{i+1}\) for \(1\le i<k\); deleting the first \(a\) and testing \(a^{k-1}b\) forces the last case \(a_k<b_{k+1}\). This yields the exact consecutive-occurrence-level decomposition. The separate \(k=1\) argument counts all double-multiplicity arrangements. A separately implemented literal-subsequence verifier checked 413,244 eligible words, including every four-letter case at \(k=2\).

## Originality
PASS on the accessible evidence, with residual risk. The closest primary text is Day et al., *The Edit Distance to k-Subsequence Universality* (STACS 2021, Theorem 4.4), which computes deletion distances to a prescribed universality index, rather than the sharp classification of words universal after **each** deletion. Barker et al. describe arch factorization, and Adamson's counting algorithms address ordinary universality; these do not state the resilience-rigidity equivalence or the \(k=1\) boundary. Public mathematical-record and targeted textual searches located no dominating theorem. An unindexed equivalent derivation remains possible.

## Mathematical value
PASS. A one-symbol erasure is a canonical robustness test for a universal subsequence host. The theorem not only fixes the optimum redundancy but classifies all minimizers over every alphabet, discovers a rigidity transition between target lengths one and two, and turns the minimum-host resilience problem into an explicit factorial enumeration. Longer hosts and multiple deletions remain open to further treatment.

Self-review: passed. Independent audit: not yet performed.
