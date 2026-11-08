# Independent mathematical audit

## correctness

PASS

From renewal-event recursion ν_k=Σ_{j≤k}S_{j-1}r_j ν_{k-j} with ν_0=1, last-reset conditioning gives Φ_t(X)=S_t U^t X U^{-t}+tr(X)A_t, tr A_t=1−S_t. On traceless operators Φ_s is S_s Ad(U^s) and preserves trace, so for S_s>0 its unique inverse exists. Φ_t Φ_s^{-1}(Y)=a Ad(U^{t−s})Y+tr(Y)Q, a=S_t/S_s>0; Q≥0 makes a CPTP unitary/replacement mixture, while any negative Q eigenvector can be exposed by an input rank-one projector orthogonal to it (d≥2), proving positive iff CP iff Q≥0. Adjacent Q expands to ν_{t+1}τ+Σ_{k=1}^t ν_k S_{t−k}(r_{t+1}−r_{t+1−k})Ad(U^{t+1−k})τ, nonnegative for nondecreasing hazards; composition handles all intervals. For qubit bit-flip, pure τ, p=r1>r2=q, Q has negative eigenvalue p(q−p) while every trace distance contracts by S_t. Domain d≥2, r_j<1 at each finite age, fixed unitary/reset density. No conclusion on process tensors, sure resets or nonunitary gates.

## originality

PASS

Best-of-knowledge model-specific renewal last-reset Loewner criterion and all-dimensional rising-hazard guarantee survive comparison with general quantum semi-Markov and discrete resetting literature. Published 2026 Carollo–Wald introduces same discrete resetting system and a ramp, so novelty excludes the renewal map and ramp definition. Its full text remained inaccessible: only abstract/metadata and source-package quotations were readable; it could contain relevant sufficient conditions. No full-document noncoverage claim is made. The exact two-step trace-distance-invisible failure is an independent structural witness.

## value

PASS

The exact necessary-and-sufficient operator-order criterion replaces sample numerical divisibility witnesses by a concrete test in any finite dimension. The hazard monotonicity theorem gives a simple noncommuting-reset CPTP design guarantee, and the p>q qubit example shows that trace-distance monotonicity alone cannot diagnose failure. Both are motivated by physical renewal resetting rather than arbitrary parameter slicing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
