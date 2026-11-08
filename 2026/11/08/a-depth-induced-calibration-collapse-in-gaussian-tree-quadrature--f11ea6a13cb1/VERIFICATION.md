---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification of the Gaussian tree-recombination depth theorem

## Exact algebra

The standalone checker `verification/check.py` uses only `fractions.Fraction`, with six positive rational variance ratios, all heights from \(0\) to \(8\), and six deterministic observation vectors at each configuration. At each internal tree node it evaluates the same Schur-complement merge weights and reported posterior variance as the theorem, rather than a closed-form shortcut. It verifies the exact formula for the root mean, root variance, coherent posterior mean and variance, coherent/reported variance ratio, and normalized true mean-square error. The script reported `PASS 2268 exact rational identities`.

Run using `python verification/check.py` from the extracted package root.

## Independent proof checks

The leaf integral and midpoint observation reduce to independent Gaussian coordinates; no numerical integration approximation enters the proof. Every parent prior covariance is the true \(mI_2\) under independent cells. The denominators remain positive for all \(v>0\), and the base case \(h=0\) matches the coherent posterior exactly. The asymptotic claim is restricted to fixed \(v,z>0\) and \(h\to\infty\); the Gaussian coverage formula is exact at each finite height.

## Boundaries and unproved claims

The finite checker does not certify arbitrary depth, coverage, or Gaussianity; those statements rely on the analytical proof. It tests no software implementation, kernel fitting, adaptive domain partitioning, or floating-point effects. Independent mathematical audit has not been performed.
