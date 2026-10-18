---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For C=u^(1+a(v^-s-1))*v^(1+b(u^-s-1)) on 0<u,v<1, the logarithmic mixed derivative yields c=C/(uv)(PQ-s(a v^-s+b u^-s)). The product PQ is bounded below by [1+a(v^-s-1)][1+b(u^-s-1)] and hence c>=0 on s(a+b)<=1; strict interior positivity includes endpoints by positive log terms or independence. Near (1,1) c tends to 1-s(a+b); a negative limit invalidates the copula. Boundaries have uniform margins and continuous zero axes. Opposite conditional tails are 1-e^-b and 1-e^-a for s=1, zero for s<1; inversion gives (1-x)(1-y)>=e^-1. Diagonal depends only on r=a+b and upper-right joint exceedance is (1-sr)t²+O(t³), or (1-s/2)t³+O(t⁴) at sr=1. Finite density/limit tests independently checked and do not replace proof.

## originality

PASS

Chesneau 2023 VP2 establishes the symmetric slice a=b up to 1/2 and another Khoudraji asymmetric deformation with powers tied to transformed arguments. The Stingray preprint gives a symmetric reciprocal construction and proposes a one-sided candidate. The audited theorem treats independently weighted common-power exponents with sharp simplex and exact two-tail region; those results are not established by the inspected earlier statements. Full text of the most plausible 2024 paper could not be obtained, so this is qualified best-of-knowledge originality.

## value

PASS

Sharp full-support admissibility for the natural independently weighted reciprocal-power copula, an attainable two-dimensional opposite-tail tradeoff, and the fact that the diagonal hides allocation of the two weights solve meaningful dependence-model parameter and identifiability questions. This is not a gratuitous slice or a numerical experiment; theorem handles the entire stipulated parameter region, with a boundary order change.

The dated certificate retains the supplied scientific assessment, sources and limitations.
