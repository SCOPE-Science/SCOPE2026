# Scientific assessment

## Correctness — PASS

For each fixed \(n\ge4\), the normalization to a common endpoint orientation is forced by length-one overlaps. The exact criterion \(\min i+\min j>n\) has been proved in both directions by comparing one-counts of possibly matching prefix/suffix pairs. It yields a complete containing-family upper bound; an elementary integer quadratic maximization proves the size and, by equality rigidity, the complete optimum classification. The independent finite code `verify.py` rechecks pairwise overlap, every oriented subset through length nine, and the general construction through length thirty. Finite checks do not replace the all-length proof.

## Originality — PASS, qualified

Relevant primary works on unrestricted non-overlapping code sizes, generating functions, and non-expandability were inspected at material level. They address unrestricted code design or other extremality notions; none of the inspected main results gives a weight-three optimum for every \(n\) and a complete labeled classification. The closest known length-five unrestricted size of two does not imply the theorem at all other lengths and cannot establish rigidity. The two-interior-one threshold reduction is a direct new derivation rather than an application of an asserted prior classification. The residual risk is that an equivalent constant-composition result is embedded in unsurveyed literature or obtainable as a special instance of a sufficiently strong general characterization.

## Mathematical value — PASS

Fixed Hamming-weight synchronization codes are a natural sparse signaling constraint, and weight three is the first nontrivial interior-pair layer after endpoint normalization. The result determines a whole infinite-family exact zero-error capacity, all labeled maximum codebooks and an explicit period-three size law. It is not a mere finite example or a recomputation of the unrestricted binary result.

## Constraints and external review

The theorem does not cover higher weights, mixed-weight words, or unrestricted optimal code size. The finite verification uses exhaustive enumeration only for specified bounded lengths. The review is not an independent peer assessment, and the possibility of unindexed equivalent claims remains.

Self-review: passed. Independent audit: not yet performed.
