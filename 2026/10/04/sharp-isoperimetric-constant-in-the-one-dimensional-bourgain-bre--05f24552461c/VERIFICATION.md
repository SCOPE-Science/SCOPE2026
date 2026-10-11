---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

With the stated Fourier convention, the inverse transform of the principal-value multiplier \(1/\xi\) is \((i/2)\operatorname{sign}x\); mean zero therefore turns \(|D|^{-1}\operatorname{sign}(D)f\) into \(iF\). The Hermitian pairing is twice the signed area of the closed primitive curve, and the sharp signed isoperimetric inequality gives \(2|\mathcal A(F)|\le \|f\|_1^2/(2\pi)\), with circles as the equality cases. The argument also lets a finite regularized difference transfer finiteness from one half-frequency energy to the other. A local proof typo was detected in RESULT.md: it prints a minus sign in the displayed formula for \(\operatorname{Im}(F'\overline F)\); direct multiplication gives the positive area integrand. The immediately following pairing and final identity use the correct sign, so the theorem and sharp constant are unchanged. This is treated as a non-substantive proof-line defect, not a false final claim.

## originality

PASS

The closest source is Arsénio's one-dimensional Hilbertian Bourgain--Brezis model. Public arXiv/full-text routes did not yield usable complete text in this run, and after those failures the authorized institutional retrieval returned an Oxford-worker-unavailable/request-invalid error; it was not retried or bypassed. Accessible source material describes the nonsharp comparison, while the submitted argument identifies the endpoint pairing with signed area and then imports the classical sharp isoperimetric constant and equality cases. Resultary search for the exact Hardy-projection imbalance and \(1/(2\pi)\) constant returned only the submitted exact formulation among the relevant hits. The inaccessible same-paper remainder is retained as a priority risk rather than treated as automatic failure.

## value

PASS

The result sharpens a current one-dimensional Bourgain--Brezis model from an unspecified comparison to the exact constant and complete equality geometry. Identifying the operator imbalance with signed area gives a structural explanation, not merely a better numerical coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
