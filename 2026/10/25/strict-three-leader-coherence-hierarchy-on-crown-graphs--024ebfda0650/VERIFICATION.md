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
# Reproducibility of the exact three-class result

Run `python verify.py` using the locally available SymPy version satisfying `requirements.txt`. The code checks symbolic identities for the three class formulas and both exact positive-gap formulas; it independently enumerates all \(inom{2n}{3}\) triples and computes the **exact rational** inverse trace of the grounded Laplacian for each \(n\in\{3,4,5,6,7,8\}\). It compares each configuration against its analytically determined class and checks the count of all-one-side minimizers. The deterministic output is embedded in `verification_output.txt`.

The \(n=3\) computation is a boundary consistency check on a graph already covered by the known cycle case; the claim is for \(n\ge4\). Exact finite experiments are not an exhaustive proof for infinitely many graph orders; the proof for arbitrary \(n\) is in RESULT.md. The external independent audit was not performed.
