---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The positive nearest-neighbor rates give irreducibility. Multiplying the forward/backward rate ratios yields the stated stationary weights including the squared binomial, with one overall normalization. The ratio of adjacent ratios at index k is F_k(a)F_(n-k)(b); the geometric tilt r cancels. For j>=2 the positive difference between denominator and numerator of F_j is j^2-j-1+(2j+1)u, so only the two boundary inequalities can fail, and they coincide at n=2. F_1(u)=(1+u)/(4u) has cutoff 1/3; since F_(n-1)(u) tends to 1, both shape cutoffs are necessary as well as sufficient for every size. For the symmetric modes, R_0 crosses 1 exactly at u=1/(n+1), R_1>1 for n>=4, and the interior ratios strictly decrease and are paired by reflection as reciprocals. This gives the exact central peak or central plateau and the strict endpoint peaks, with the claimed equality interpretation. The symmetric log-concavity product decreases continuously from infinity to a value below 1 at u=1/3, and it exceeds 1 at the endpoint-mode threshold (R_0=1<R_1). At its unique root, write A=F_(n-1)(u_n) and u_n=A/(4-A); the uniform expansion A=1-1/n+O(n^-2) on 0<u_n<1/3 yields the claimed -4/(9n) correction. An independently coded exact replay from the generator checked 2052 rate-built laws and symmetric shape around the mode threshold through n=32.

## originality

PASS

The squared-binomial law, its detailed-balance ratio, and its binomial times beta-binomial factorization were already in arXiv:2610.17775 Appendix C and are not new. The distinct checked contribution is the exact weighted-law boundary-only classification and its sharp all-size 1/3 threshold, together with the separation of the finite-size mode and log-concavity thresholds in the symmetric system. The inspected source for the same chain studies mixing, includes ordinary stationary weights, and uses unimodality for a different ratio (transient probability divided by stationary probability); it does not supply the claimed sharp inequalities. Related indexed and primary single-binomial laws change the second ratio and do not supply the same classification. The stated pass is bounded by the specific compared evidence, not proof of publication priority.

## value

PASS

The proof is elementary once the weights are known, but the result is a complete finite-size and sharp population-uniform shape classification of an independently motivated stationary law. It identifies exactly where curvature can fail (only the endpoints), gives a uniform threshold with necessity, and quantifies a centrally unimodal region that would be misclassified by equating loss of boundary peaks with onset of log-concavity. These statements give usable information for future analyses of this specific chain and do not rely on asserting value for the already known invariant weights.

The dated certificate retains the supplied scientific assessment, sources and limitations.
