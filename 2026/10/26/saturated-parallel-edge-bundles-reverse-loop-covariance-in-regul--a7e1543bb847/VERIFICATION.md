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

The formula itself survives unchanged. If an elementary bundle is specified, conditioning leaves a uniform pairing with two residual degrees d−r and all others d. Exactly r(2d−r−1) eligible loop pairs are lost; the pair probability changes from 1/(nd−1) to 1/(nd−2r−1). Summing the bundle indicators gives E P_r=B_r p_r even at multiplicities above r; subtracting E L from the conditional expectation gives the displayed rational factor. For n≥3 all denominators are positive. The numerator bracket is d−1 at saturation and strictly negative otherwise because nd(d−r)≥3d. At n=2,r=d both means are positive but LP_d=0. At fixed d,r the mean has leading factor C(d,r)^2 r! n^(2−r)/(2d^r), and the covariance-to-mean ratio is asymptotic to −r(d−r)/(dn) or (d−1)/(dn²), giving the stated constants and rates. A fresh exact direct matching enumeration gave 4/25 at (n,d,r)=(3,2,2), −216/847 and 24/4235 at (4,3,2) and (4,3,3), and −768/4235 and 32/4235 at (3,4,3) and (3,4,4); the excluded (2,3,3) gave −12/25. The rewritten scope, proof, and contextual r=2 formula were checked against this derivation. The frozen checker was inspected, not executed or modified.

## originality

PASS

Pass for the repaired higher-bundle contribution only. A demonstrably earlier all-degree-sequence exact covariance and its regular corollary already cover the frozen theorem's full r=2 slice, including its signs and asymptotic rates by expansion. The repaired RESULT.md credits that coverage and retains r=2 solely for context; the new claim is the higher-bundle formula and saturation law for r≥3. No inspected stronger theorem states or directly implies that remainder. The pairing probability itself is standard.

## value

PASS

The higher-bundle sign is about a natural mixed defect statistic not measured by double-edge pairs. It distinguishes partially depleted endpoints from the formation of a saturated isolated two-vertex component, and it quantifies the positive effect at a smaller order than the negative one. That finite-size information is not available from the usual Poisson limits; it does not claim a dependence ordering or an irregular degree-sequence threshold. The known r=2 result is not counted toward the value of the repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
