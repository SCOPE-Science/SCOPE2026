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

The theorem is proved symbolically in `RESULT.md`; the finite checker is supplementary. The exact source program is `checker.py`, with Python 3 and no third-party packages. Running `python3 checker.py` from this package constructs prescribed cycle determinants, transforms witnesses from Fourier to the original quandle basis, and computes commutators directly using \(e_a e_b=e_{2b-a}\).

Verified cases: cyclic groups with orders \(1,3,5,7,9,11,13,15,21,25\) over splitting prime fields, and direct products \(C_3\times C_5\), \(C_5^2\), \(C_3\times C_9\), \(C_3^2\times C_5\), \(C_7^2\). Exact testing includes each cyclic prescribed-minor list over \(\mathbb F_2\) and \(\mathbb F_3\) for cycle lengths 3–6. The checker terminates with `VERIFY_OK`.

The finite tests do not establish the theorem for arbitrary group order or arbitrary fields; that conclusion rests on the Fourier product identity, the no-two-cycles observation, and the inductive determinant lemma. Nonsplitting and modular characteristic cases are not covered. Independent auditing has not been performed.
