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

Exact dynamic-programming coefficients of the product generating function were computed for the four integer parameters \(u=2,3,4,5\) using `verify.py`. The script independently verifies every proposed Apéry threshold value by counting representations, checks the distinct residues, and recomputes the number of holes and maximal hole. The theoretical proof relies instead on a complete classification of possible coefficients of \(P_9(u)\) in each residue: they differ by multiples of \(u\), and a sharp two-block inequality limits this multiple to \(0\) or \(1\). Verification does not cover any parameter beyond the finite tested range or establish mathematical originality. No independent audit has been performed.
