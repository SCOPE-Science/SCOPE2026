---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The untouched count U has variance at most its mean u by negative pairwise occupancy covariance, and U/n tends to zero for r/n→∞. Exchangeability in the order of last selection gives a uniform ordered prefix conditional on the number touched; the untouched suffix stays sorted. Compare with an independent uniform permutation before sorting that suffix. The descents change by a tail sum of mean U/2 up to a bounded endpoint/interface term, with conditional variance O(U), whereas inversions change only within the suffix, with conditional mean U(U−1)/4 and variance U(U−1)(2U+5)/72 from the independent Lehmer digits. Thus the centered perturbations vanish on the respective √n and n^(3/2) scales, and the stationary 1-dependent and independent-summand CLTs supply variances 1/12 and 1/36. The subsequence argument handles oscillating ratios in the iff statements, including divergence to minus infinity. At the critical windows the occupancy limits are e^(−c); uniform convergence to continuous CDFs and the midpoint of the two equal-variance normal CDFs give both Kolmogorov constants. Independently checked the conditional prefix counts and inversion mean over 3,906 histories (n=5, r=0..5); replay: python -B /workspace/branches/audit-replay.py 3. This checks finite identities, not the limits.

## originality

PASS

The best-supported distinct claim is the critical-window scalar Gaussian shifts, their exact Kolmogorov profiles and necessity over all r/n→∞. The ordered-suffix law, fixed linear-time CLTs and above-window sufficient conditions are prior work; no inspected source already covers the distinct claim.

## value

PASS

These natural observables become effectively stationary at different times well before full-deck mixing. The exact shifts identify the mechanisms (linear missing-card penalty versus quadratic lost inversions), and the Kolmogorov profiles and iff conditions distinguish delays that an above-window sufficient CLT does not. The contribution is precise scalar relaxation, not a full-deck, local-limit or joint-limit theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
