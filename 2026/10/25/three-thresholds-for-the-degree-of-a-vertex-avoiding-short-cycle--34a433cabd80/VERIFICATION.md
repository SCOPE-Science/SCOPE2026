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

Execute `python verify.py` from a directory containing the attached standalone verifier. Python 3 with standard library suffices. The program enumerates each of the \(2^{\binom n2}\) labeled graphs for \(2\le n\le6\), identifies directly whether the distinguished vertex belongs to a triangle or a simple four-cycle, compares each exact coefficient of the joint degree-and-edge-count polynomial with the independent neighbor-count expression, and checks rational probabilities at \(p\in\{1/3,2/5,1/2\}\). It also checks the exact adjacent-weight identity for every feasible pair of positive degrees. Expected output: `PASS 285 exact assertions, exhaustive graph enumeration through six vertices`.

These checks are finite and do not certify any asymptotic statement. The asymptotic work is justified by the uniform adjacent-ratio bounds, Chernoff estimates, discrete Laplace principle, and critical Stirling expansion detailed in RESULT.md. Independently inspect the proof before relying on it for publication or further mathematical work.
