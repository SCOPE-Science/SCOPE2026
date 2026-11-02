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

# Verification record

Run `python3 verify.py` with Python 3 standard library. The checker enumerates every specified finite obstruction and exact modular inverse assertion; its expected output begins `VERIFY_OK` and reports `obstructions=81675` and `odd_inverse_pairs=13412`. The same script checks that the union of residue classes one and three modulo four has minimum approximation error exactly \(1/q\) over the sampled reduced fractions.

The proof of the infinite statement is entirely arithmetic. It requires Dirichlet's pigeonhole approximation lemma, the parity of reduced modular inverses, and explicit fractions with denominators \(mt\pm1\). The finite checks cannot establish the universal quantifiers alone. The claimed publication priority is subject to the stated unindexed-literature risk; no independent scientific audit is claimed.
