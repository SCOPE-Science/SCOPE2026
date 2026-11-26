# Independent mathematical audit

## correctness

PASS

For y in [0,1/k], exactly the inverse branches 1/(j+y), j≥k, stay in the observation interval, apart from null boundary points. Applying the Jacobians n−1 times and integrating also gives the exact n=1 normalization. Independently normalize the operator by p and write it as expectation over J with mass J^(−2)/p. Put d=q/p=E(1/J)≤1/k and test h(y)=1−2dy. Uniformly in y and J, (1+y/J)^(−2)=1−2y/J+O(k^(−4)) and 1−2d/(J+y)=1−2d/J+O(k^(−4)); the product of the two linear defects is also O(k^(−4)). Averaging gives Lh/p=1−2dy−2d²+O(k^(−4))=(1−2d²)h+O(k^(−4)). Both h and 1−2d² are bounded below by 1−2/k². Positivity iterates the relative O(k^(−4)) error, and endpoint integration and replacing h by 1 cost O(k^(−2)). This yields the asserted uniform relative error for n≤Ck². Since d=1/(2k)+O(k^(−2)), the log of the independent-digit-normalized rate is −1/(2k²)+O(k^(−3)); multiplying by n−1 gives the limit, including τ=0. The frozen checker was inspected, not executed: its rational-cylinder, digamma, sampled residual and zeta-tail checks are finite corroboration, not the proof.

## originality

PASS

The inspected sources share the Gauss branches, the hole, or the transfer-operator method, but do not provide the claimed finite-horizon Lebesgue asymptotic or mechanically imply its uniform error and crossover coefficient. Pass is limited to that combined finite-time claim, not the symbolic cutoff, pressure construction, or transfer operator.

## value

PASS

The result quantifies when multiplication of the zero-endpoint branch Jacobians ceases to approximate the actual Lebesgue survival mass by a factor tending to one. At a natural diverging horizon O(k²), O(k⁻²) per-observation dependence accumulates into a nontrivial loss whose sign and coefficient are determined, while the corrected law retains a uniform relative error. A dimension or escape-rate-only result does not answer this finite-observation question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
