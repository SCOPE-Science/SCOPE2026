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

# Reproduction
Run `python3 checker.py` using only Python 3 standard-library modules. It must print the six indices \(2,3,6,7,8,18\) and PASS for each of the three advertised checks. It enumerates every coefficient in \(C=uA/d+vB/d\), not just a bounded sample, for all \(n\in[2,124]\). Exact gcd and minimality checks accompany the loop. A separate Dijkstra calculation of minimum semigroup representatives modulo the least generator supplies Apéry-set Frobenius and gap counts through \(n=60\).

# Proof scope
The integral-inequality argument for \(n\ge125\) is symbolic and covers infinitely many remaining indices. The theorem depends on the classical three-generator symmetry/gluing characterization quoted in the main proof. Computational checks alone would not justify the infinite conclusion. This verification is not an independent audit or external certification.
