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

# Verification evidence and limits

The script `verify.py` uses exact modular arithmetic and no external packages. It constructs normalized projective representatives and the ordered opposite-sign pairings, computes matrix rank, checks every entry of \(HJH^{\mathsf T}\), enumerates the complete radius-one syndrome map, checks pairwise inverse-syndrome structure, and verifies a weight-three zero-syndrome Pauli and absence of one-coordinate stabilizers by exact rank over \(\mathbb F_p\).

Executed command: `python3 verify.py`.

Tested \((p,r)=(5,2),(5,3),(5,4),(13,2),(17,2)\). The expected final output line is `PROJECTIVE_QUANTUM_LEE_VERIFICATION_OK`; `verification-output.txt` records the original run. These checks are finite corroboration only. The proof for all primes \(p\equiv1\pmod4\) and integers \(r\ge2\) is mathematical and is provided in `RESULT.md`.

The generalized quantum stabilizer definitions and Lee sphere-packing bound were checked against Guo et al., arXiv:2610.04834v1 §§3.1–3.2; the distinct-syndrome and centralizer assertions were proved directly. Independent mathematical audit and external verification have not been performed.
