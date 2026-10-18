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

# Exact checks and boundaries

The theorem was checked against complete finite enumerations, using the standalone `verify_random_evolution.py` supplied in this same package. The script implements extension-field arithmetic from explicit irreducible moduli; its invertibility test, direct solution enumeration and histogram computation are independent of the symbolic counting argument in the proof.

The ten verified pairs were \((q,n)=(2,2),(2,3),(2,4),(3,2),(3,3),(4,2),(5,2),(7,2),(8,2),(9,2)\), covering both field characteristics and three proper field extensions. For each pair the script checked the arithmetic mean \(\mathbb E X=1\) and exact second factorial moment against the claimed rational expression. In each characteristic-two case it additionally checked the entire finite histogram against the Gaussian-binomial inversion formula.

The checker returned `VERIFY_OK: 10 complete matrix and idempotent enumerations`. It uses only Python's standard library. Execute `python verify_random_evolution.py` in a directory containing the extracted source file.

The proof of the general theorem is symbolic and self-contained; finite computations do not demonstrate correctness for all prime powers or dimensions. Independent mathematical assessment has not been performed. Bibliographic novelty remains subject to unindexed works and potential stronger general finite-field counting results.
