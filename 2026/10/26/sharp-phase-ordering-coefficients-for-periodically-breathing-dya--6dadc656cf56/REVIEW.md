# Scientific review of the periodic dyadic-hole phase-ordering result

## Correctness
The binary-to-zero-run equivalence is exact, and each complete safe run is represented by one weighted transition in the finite \(q\)-phase renewal matrix. Perron renewal asymptotics give the infinite-time escape rate. Perturbing the explicitly known unconstrained matrix about its simple eigenvalue at one yields the displayed \(O(m4^{-m})\) estimate. The all-period minimum follows from a pointwise erosion inequality, with equality characterized by the unique cyclic descending permutation. The finite maxima and maximizing counts through eight phases are established by exhaustive enumeration of precisely \((q-1)!\) cyclic classes using exact rational arithmetic. The attached standard-library checker was executed and printed `VERIFY_OK`.

## Originality
The closest direct mathematical antecedent is Poo–Marcus (2006), which treats equivalent phase-dependent maximum-run constraints, reduces vectors to canonical tight forms, gives exact characteristic methods, and compares capacity through period four. This general method determines individual capacities in principle, but the inspected text does not formulate the small-hole coefficient or the complete extremal finite enumeration for periods five through eight. Livorati et al. (2013/2014) motivate time-dependent holes and short-orbit overlaps, without these exact permutation-optimization results. The 2011 periodic-finite-type formalism is broader, and the 2010 escape-rate asymptotics concern stationary holes. These are bounded comparisons, not proof of global literature uniqueness. The equivalent coding-theoretic setting is explicitly acknowledged; unindexed follow-up calculations and unread equations in one HTML transcription are residual risks.

## Mathematical value
For a fixed multiset of periodic hole sizes, rearrangement changes the leading escape rate rather than merely a finite-time constant. The all-period unique optimum is a structural ordering principle, while the exact periods five to eight include the first periods beyond the earlier low-period capacity order and disprove an attractive first-six-period linear extremal extrapolation. The finite enumeration is a natural initial optimization census in the relevant periodic family, not an arbitrary parameter slice.

## Limits
Only small-hole leading coefficients are classified. At finite hole size the total ordering can differ, and the maximum is not determined for arbitrary period. The same source's general capacity algorithm could allow further related results to be derived; independent literature assessment is still needed.

Self-review: passed. Independent audit: not yet performed.
