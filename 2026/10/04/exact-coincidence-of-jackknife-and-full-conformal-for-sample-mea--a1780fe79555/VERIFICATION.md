---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The leave-one-out mean is \(\bar Y-d_i/(n-1)\) and its residual is \(n|d_i|/(n-1)\), giving the stated jackknife+ endpoints. For a candidate offset \(x=y-\bar Y\), fresh symbolic expansion verifies exactly \(((n+1)d_i-x)^2-n^2x^2=(n+1)(n-1)(d_i-x)(x+c_nd_i)\). Therefore the candidate residual is no larger than training residual i exactly when y lies in the corresponding endpoint interval. Every such interval contains \(\bar Y\), so the points lying in at least \(j=\lfloor\alpha(n+1)\rfloor\) intervals form one interval with endpoints \(\ell_{(j)}\) and \(u_{(n-j+1)}\); the integer identity \(n-j+1=\lceil(1-\alpha)(n+1)\rceil\) gives exact equality. Exact-rational spot checks independently matched full-conformal membership, including the infinite-interval convention.

## originality

PASS

Barber et al. define jackknife+ and full conformal separately and emphasize their different generic guarantees and computational behavior; the complete inspected text contains no sample-mean, intercept-only, or location-model specialization. A later tutorial explicitly works through full conformal with the sample mean and separately presents jackknife+, but does not state their deterministic equality. Later relationship papers discuss generic or asymptotic equivalences, not this exact finite-sample identity. No exact Resultary match was found.

## value

PASS

The intercept-only location model is the canonical exact benchmark for regression conformal methods. Showing that jackknife+ recovers full conformal samplewise—thereby improving its generic worst-case guarantee from \(1-2\alpha\) to the full conformal grid in this model—clarifies a real boundary between the two procedures and supplies a clean test case for approximation and stability theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
