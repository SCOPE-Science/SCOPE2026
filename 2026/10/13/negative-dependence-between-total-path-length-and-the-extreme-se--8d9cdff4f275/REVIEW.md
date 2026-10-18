# Independent mathematical audit

## correctness

PASS

For uniform permutation insertion BST, P_n is internal path length and R_n rightmost spine node count = strict upper records, with empty-subtree P_0=R_0=0. Conditioning on uniform right subtree size J yields P_n=n−1+P_J^r+P_{n−1−J}^l and R_n=1+R_J^r; conditional independence gives covariance recurrence K_n=(Σ_{j<n}K_j)/n+g_n. The manuscript derives exact g_n=(n+1)(3/2−H_n^(2))−H_n/n from a harmonic convolution and weighted-square identity, hence K_n=3n+H_n−2(n+1)H_n^(2). Reflection/strict convexity of subtree mean path length and concavity of averaged record means show g_n<0 for n≥3 (zero n1,n2). Harmonic expansions and the classical independent record/Quicksort variances yield correlation ~−0.4471358767/sqrt(log n). Independently computed exact rational recurrence n≤50 and built 5913 BSTs over all permutations n≤7, obtaining identical covariances. The result is only for successful maximum search, not arbitrary selected key.

## originality

PASS

Classical Quicksort means/variances and BST right-spine record identity supply the marginals, not their cross covariance. Grübel treats normalized internal path length and its strong limits; Corsini studies height of record-biased trees; selected-node weighted-depth literature is not this unweighted mixed covariance. Related Resultary squared root-split imbalance and recursive-tree root-degree covariance are different pairs of functionals. The exact n-dependence and strict sign were not found in inspected materials; residual possibility of earlier record-weighted mixed-moment formula.

## value

PASS

Two natural cost metrics of the same insertion order are often presumed positively linked. Exact strict negative finite-n dependence and asymptotically vanishing negative correlation expose a structural tradeoff and quantify the joint fluctuations for maximum-key searches versus total construction comparisons. The mixed covariance is a useful stand-alone algorithmic statistic even without a full joint law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
