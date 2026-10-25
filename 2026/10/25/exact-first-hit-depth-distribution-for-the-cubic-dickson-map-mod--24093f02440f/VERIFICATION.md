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

# Verification and limits

Run `python3 verify.py` with Python 3 standard library. The script independently computes actual orbits of the cubic map for every residue modulo \(3^k\), for \(1\le k\le8\), terminating only upon entering the uniquely determined fixed point. For every one of the 9,840 residues it checks that the actual first-hit time equals the capped-valuation formula. It independently builds the closed-sum histogram and compares all coefficients, checks total mass \(3^k\), and checks the three sharp basin heights, including \(k=1\). The successful output ends with `VERIFY_OK`.

No finite check proves the statements for arbitrary \(k\); the mathematical proof is the factorizations, exact valuation increments, finite residue partition valid for every precision, and sharp witness construction given in RESULT.md. External independent auditing has not been performed.
