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

# Verification notes

The proof uses the prime ideal presentation of Košir--Sethuraman, the Cohen--Macaulay theorem of Jonov, and an independent explicit Schur-complement coordinate change. The geometric proof is valid for every pair of integers \(3\le m\le n\) in characteristic zero. The included script `check_transverse_jet.py` performs 20 exact modular differential-rank checks over the field with 101 elements, for pairs \(3\le m\le n\le6\) and derivative ranks one and two. Run it with `python3 check_transverse_jet.py`; the final line must read `PASS: 20 exact finite-field rank checks at p=101; general proof is separate`.

These finite-field tests verify neither the general characteristic-zero proof nor the originality claims. The primary argument is the symbolic row-column chart computation in `RESULT.md`. The reduced global singular set is proved; the scheme-theoretic Jacobian singular subscheme at low-rank boundaries has not been determined. A relevant Smith--Weyman resolutions preprint remained uninspected in full, so its possible implications are a documented literature risk. No external independent audit or validation is asserted.
