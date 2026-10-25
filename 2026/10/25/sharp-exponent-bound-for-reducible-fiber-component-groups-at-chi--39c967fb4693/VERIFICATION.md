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

The numerical domain is exhaustively bounded: \(c(13)=42/13>3\) and \(c(n)\) is increasing, so every entry is at most \(12\); each entry costs at least \(1/2\), so there are at most \(6\) entries. The included verifier enumerates all nondecreasing multisets in that domain with exact rational arithmetic. It returns \(78\) feasible multisets and the unique maximum \(\operatorname{lcm}=60\) at \((3,4,5)\). An independent recursive enumeration reproduced the result. The component-group exponent identity is \(\operatorname{exp}(\prod_i \mathbf Z/n_i\mathbf Z)=\operatorname{lcm}(n_i)\).

Limits: no geometric existence proof for the extremal configuration; no claim for \(\chi>3\); the earlier source full text was not retrieved; independent audit remains unperformed.
