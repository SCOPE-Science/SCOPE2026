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

# Verification

Run `python verify_affine_dodeca.py` using Python 3 and SymPy. The executable performs only current-result calculations: exact integer-pair arithmetic for \(\mathbb Z[\varphi]\), all 1,024 sign arrangements, all 90 oriented circle intersections, the twelve decagon chambers with sixty corners, the eight corner-type multiplicities, and all Taylor terms up to cubic order. Expected coefficients are hard-coded and verified by exact symbolic identities. This is a finite exhaustive certificate for the finite combinatorial component, supported by the analytic spherical excess proof in `RESULT.md`.

The analytic domain is every \(t>0\) and the expansion is local as \(t\to1\). Numerical tests are auxiliary, not proofs. This review is not an independent audit.
