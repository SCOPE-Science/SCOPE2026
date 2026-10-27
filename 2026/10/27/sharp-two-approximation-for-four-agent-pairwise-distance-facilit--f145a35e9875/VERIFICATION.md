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

# Mathematical verification

`verify.py` uses only the Python 3 standard library and computes the expected cost twice: once by directly enumerating the six weighted facility pairs, and once using the displayed closed formula. It also checks the optimal cost by enumerating all candidate report-pair facilities, verifies reflection symmetry, and confirms strict \(2\)-approximation on all \(20^3\) positive integer gap triples. The program additionally checks five exact closed-form sharpness examples. Command: `python verify.py`. Observed output: `PASS: 32015 exact-rational assertions`.

The universal result is established by the algebraic case analysis in RESULT.md. Finite verification neither proves the continuum statement nor establishes literature originality. All limits are analytical. The statement assumes four distinct agents and positive gaps; zero gaps and larger electorates were not assessed. No independent validation was carried out.
