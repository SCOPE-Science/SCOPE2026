# Review

## Correctness

PASS. The sign-flip state is obtained by exact substitution. The two phase Jacobians are computed in normalized coordinates, their product gives the stated Floquet polynomial, and the complete Jury test reduces to the single nontrivial condition \(c<1/2\). This yields the exact window \(2\varepsilon<\alpha\lambda<4\varepsilon\).

Risk: the theorem classifies local orbital stability rather than global attraction.

## Originality

PASS. The defining AdaShift paper develops temporal decorrelation and reports instability of the temporal-only variant on some tasks. The later asynchronous-optimizer analysis studies convergence conditions and delay sensitivity. Neither inspected source states the constant-step scalar period-two orbit, its sharp epsilon-dependent stability window, or the exact zero-epsilon Floquet modulus. Focused published-record searches found no implication-equivalent result.

Residual risk: an equivalent calculation may exist in unindexed delayed-RMSProp analyses.

## Value

PASS. AdaShift's defining modification is to delay the second-moment information. The finding isolates a precise nonlinear consequence of that delay and shows that the denominator constant controls a genuine bifurcation between stable and unstable oscillation. This gives a concrete explanation for why temporal-only adaptive normalization can remain sensitive to learning-rate scale even after decorrelation removes the Adam correlation pathology.

Same-model review: passed. Independent audit: not yet performed.
