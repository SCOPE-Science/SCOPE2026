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

The theorem is proved in `RESULT.md`; the included `verifier.py` is an ordinary executable cross-check. Execute `python3 verifier.py` under Python 3 without external dependencies.

The program independently iterates \(v\mapsto v+\nu_2(v)-1\), detects cycles, and checks that the least period agrees with the recursive label for all integer exponents \(2\le m\le100000\). It also checks the recursive membership law through \(100000\), verifies the resulting finite count \(29705\), and constructs a rational interval of width \(2^{-120}\) for the density constant. The exact printed interval and count are finite facts; no computational enumeration is used to establish the irrationality or all-exponent theorem.

The proof of infinite eventual-period classification uses descending \(2\)-adic valuation-order blocks. Counting uses disjoint residue classes and a summable tail. Irrationality uses aperiodicity of the characteristic sequence, not a decimal approximation. No formal proof assistant or independent external certification has been used.
