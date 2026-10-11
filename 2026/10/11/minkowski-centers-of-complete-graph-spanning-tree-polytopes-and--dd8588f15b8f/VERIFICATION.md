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
# Finite computational verification

Run `python3 verify.py` using Python's standard library; no nonstandard dependencies and no external network or data sources are required. The script encodes rational coordinates as integers or exact `fractions.Fraction` and uses Prüfer sequences for the complete tree census of each \(K_n\) for \(3\le n\le7\). It checks that the reflected point of every enumerated spanning tree at the proposed optimal factor lies in the full, nonredundant subset-inequality description of the spanning-tree polytope. Two sample centers are used for every \(n\ge4\), including a signed four-cycle perturbation that changes edge weights while preserving degree equations; \(n=3\) has one center.

Expected output includes `checked 36491 reflected spanning trees, 4151797 subset constraints`, the six-vertex exact violation with induced sum \(21/10>2\), the seven-vertex disconnected regular weighting passing all reflected inequalities, the arithmetic cut-threshold checks for \(7\le n\le199\), the unsigned incidence row-rank checks for \(3\le n\le10\), and final `VERIFICATION_OK`. These are **finite tests**: proof of the theorem for every \(n\ge3\) comes from the reflection-containment biconditional and the exact cut-polynomial argument in `RESULT.md`, not finite enumeration.

Scientific literature checks compared complete primary HTML texts arXiv:2010.10227v2 and arXiv:1903.07292v4. Priority is not independently certified. No external independent audit has been performed.
