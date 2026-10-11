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

The standalone script `theta_rips_verifier.py` is a Python 3 standard-library check. Run `python3 theta_rips_verifier.py` from the directory containing that file. Its correct completion line is `VERIFY_OK; complete equivariant Lefschetz traces=608`.

For each integer \(2\le m\le8\), the script constructs all \(2m+2\) graph vertices, computes their exact shortest-path distances by breadth-first search, enumerates all nonempty Vietoris–Rips simplices at thresholds one and two, and recomputes mod-two boundary ranks to check \(\widetilde\beta_1=m-1\) at scale one and \(\widetilde\beta_2=m-1\) at scale two. It separately reconstructs the internal simplicial complex and verifies it consists of precisely two full simplices and the matching bridges. For \(2\le m\le5\), it evaluates every \(608\) group-element reduced Lefschetz traces and compares them with the expected integral character.

This is an independent *computation* of finite tests, not independent peer review or a formal proof for all parameters. The uniform proof is the explicit distance classification, the exact simplicial join, a CW homotopy reduction, and the integral equivariant join isomorphism in `RESULT.md`. No finite enumeration or program termination is used to infer the infinite theorem. All group claims in the theorem exclude \(m=2\), whose automorphism group is larger.
