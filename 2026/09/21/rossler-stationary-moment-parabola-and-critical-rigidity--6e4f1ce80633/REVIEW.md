# Review status

Mathematical audit date: 2026-10-01 UTC.

Disposition: **repaired**.

Correctness: PASS. For every smooth compactly supported \(\psi\), invariance gives \(\int\psi'(z)[b+z(x-c)]\,d\mu=0\). Conditioning on height defines a compactly supported signed measure with zero distributional derivative, so it must vanish. This forces zero mass at \(z=0\) and \(\mathbb E[x\mid z]=c-b/z\) almost surely. Compact support makes the conditional mean bounded, which also justifies the integrated reciprocal-height consequence.

Originality: PASS. PASS to the best of current knowledge on the repaired claim. The original package substantially overlapped a published 20 September 2026 Rössler theorem: that earlier complete result already contains the mean/variance parabola, covariance identities, compact-recurrence threshold, harmonic-height identity, endpoint rigidity, and critical unique invariant probability. The repair removes all of those as contributions. The earlier theorem does not state the conditional law \(\mathbb E[x\mid z]=c-b/z\), and its single integrated harmonic identity does not imply the family of test-function identities that determine the conditional mean.

Scientific value: PASS. The conditional law is a natural structural refinement of the stationary moment equations for a canonical chaotic flow. It identifies the mean horizontal coordinate at every occupied height of any compact stationary state and can be used as a height-resolved diagnostic rather than only a global moment check.

Evidence: `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
