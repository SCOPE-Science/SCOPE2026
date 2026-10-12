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
# Reproduction and limits

Run \(\texttt{python3 artifacts/verify_target.py}\) from the extracted directory. The executed local run returned \(\texttt{VERIFY_OK}\), after exact enumeration of parity classes for branch counts \(r=2,4,\ldots,16\), polynomial expansion, torsion degree placement and the oriented-manifold degree pairing.

The proof is not a computational extrapolation. Its universal part is the orbifold extension and five-term sequence, followed by the integral Wang sequence, Künneth theorem, universal coefficient theorem and the integral codimension-three blow-up formula. The code tests arithmetic implications of those lemmas, not their geometric hypotheses. The limit of the reported calculation is finite branch counts, and no external independent review has been performed.
