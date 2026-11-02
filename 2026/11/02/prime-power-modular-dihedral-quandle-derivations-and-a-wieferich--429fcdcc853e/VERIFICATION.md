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

# Reproducibility and bounds

Run `python3 verify.py` using Python 3 and the standard library; there are no external data files or dependencies. The verifier constructs the original \(n^2\)-unknown coefficient system for quandle derivations and independently reduces all \(n^3\) Leibniz equations, obtaining dimensions \(4,6,4\) for moduli \(9,27,25\), in characteristics \(3,3,5\), respectively. It separately enumerates signed doubling orbits, tests the complete basis-level Leibniz identities and the Lie bracket of selected normal forms, including tests at modulus \(49\), and verifies the Wieferich parameters at \(p=1093\). The successful terminal marker is `VERIFY_OK`. Earlier intermediate experiments additionally gave direct nullity \(4\) for modulus \(49\).

The mathematical proof itself establishes the theorem for every odd prime, every exponent at least two, and every field of that characteristic. The verifier samples finitely many cases and cannot certify non-existence of earlier equivalent work or substitute for independent mathematical review.
