# Independent mathematical audit

## correctness

PASS

Let \(e_j=F(j/N)\) and \(m=\min_j e_j\). Exact decision preservation forces the first \(k\) values to be at least \(1/\alpha\), while every tail value is at least \(m\). Exact e-validity on the uniform rank grid gives \(N=\sum_j e_j\ge k/\alpha+(N-k)m\), hence the stated \(m^*\). Equality forces every head value to equal \(1/\alpha\) and every tail value to equal the common minimum, so the optimizer is unique on the grid. When \(\alpha N\) is integral, the first \(k\) values already exhaust the total expectation, forcing every tail value to zero. The bundled rational checker validates representative lattice and nonlattice cases; the theorem itself is the exact normalization argument.

## originality

PASS

The 2026 PMLR paper introduces the same set-preserving p-to-e problem and motivates strictly positive calibration, but the accessible primary page states construction and efficiency results rather than the max-min grid frontier. The audited theorem optimizes over the larger class of all positive exact grid calibrators and produces a sharp worst-rank ceiling and the lattice impossibility. The PDF link returned an unsupported-content transport error in this run, so full-body noncoverage is not claimed and overlap remains a residual risk.

## value

PASS

The worst-rank reserve is directly motivated by the source's positivity/anti-collapse goal: a single zero can collapse products of e-values. The exact max-min frontier quantifies how much uniform positivity is fundamentally possible, shows unavoidable \(O(N^{-1})\) decay, and identifies the unique grid optimizer. Although the proof is elementary normalization, the invariant is natural for the motivating application and the result is a sharp finite-sample boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
