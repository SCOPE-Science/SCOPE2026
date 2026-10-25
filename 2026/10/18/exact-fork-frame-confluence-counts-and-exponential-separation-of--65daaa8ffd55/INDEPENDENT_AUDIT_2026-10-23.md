# Independent mathematical audit

## correctness

PASS

On a rooted fork the only proper order comparisons are o<=a for each leaf a. Universal FC means each root-arrow oRb to a leaf must repeat in every leaf row, while a root loop requires every leaf row nonempty. Universal BC means a leaf-to-root arrow forces that leaf row to contain all leaves, and a root loop requires the union of root/leaf leaf-successors to cover the leaves. Splitting by root loop e and root outgoing leaf set J gives exact F_k and I_k inclusion-exclusion formulas. For k large, zero-J cases give F_k=2*2^(k(k+1))(1+O(k2^-k)), I_k=2*2^(k*k)(1+O(k2^-k)), while j>=1 is negligible, proving 2^k I_k/F_k -> 1. Independently checked all 2^((k+1)^2) arbitrary labelled relations for k=1,2,3 against quantified FC and BC, obtaining (11,9),(185,81),(10943,2043), precisely the formulas; k=6,10,14 normalized ratios tend 1.

## originality

PASS

FC and BC are foundational FIK/IK semantic conditions and not new. Published exact FIK and KI relation censuses for finite CHAINS concern totally ordered worlds rather than forks with incomparable leaves; their row monotonicity reduces differently. The present exact normal form and asymptotic exponential ratio for unrestricted labelled fork frames were not found as a corollary of the general logical axioms or chain counting formulas.

## value

PASS

A fork is the first natural branching information order; its unrestricted modal relation census directly measures the quantitative gap between forward and backward confluence. Explicit all-k labelled formulas and asymptotic 2^-k separation provide structural semantics, not a small finite catalog.

The dated certificate retains the supplied scientific assessment, sources and limitations.
