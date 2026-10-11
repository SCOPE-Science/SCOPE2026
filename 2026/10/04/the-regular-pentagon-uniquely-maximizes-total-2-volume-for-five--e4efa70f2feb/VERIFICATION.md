---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

Writing the two synthesis rows as an orthonormal pair \(u,v\) converts the sum of absolute Pluecker coordinates into \(\max_S u^{\mathsf T}Sv\) over skew sign matrices. For fixed \(S\), the orthonormal-pair maximum is its top singular value because \(Sv/\sigma_1\) is orthogonal to \(v\). For order five, the nonzero singular squares sum to 10 and their product is the sum of squared principal Pfaffians. A fresh exhaustive replay over all 1024 sign patterns gives exactly 384 cases with \(C=5\) and 640 with \(C=21\); the former yield top singular square \(5+2\sqrt5\). The package's exact signed-permutation orbit census plus the strict top spectral gap gives equality rigidity. The regular-pentagon frame attains the bound analytically.

## originality

PASS

Cahill and Casazza prove that equiangular Parseval frames maximize total volume when they exist, explicitly note that they need not exist, and end with extensive optimization questions. A real five-vector equiangular tight frame in dimension two does not exist, so that theorem does not solve this case. Searches under Parseval-frame, Pluecker \(\ell^1\), Grassmannian and skew-sign spectral formulations found no prior exact value plus equality classification.

## value

PASS

This solves a natural first small non-equiangular instance of a published Parseval-frame optimization problem, with both a sharp value and full equality classification. The optimizer's regular-pentagon geometry also identifies concrete structure beyond the finite enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
