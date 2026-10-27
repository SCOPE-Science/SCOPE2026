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

# Reproducible mathematical verification

Execute `python3 verify_negative_cycles.py` beside `negative_cycles_witnesses.json` with Python 3.10 or newer; no third-party libraries are needed. Both included files are standalone and have no external scientific dependencies beyond the cited, proved descent inequality. The executable checks all inputs in each \([1,B_p]\) for closure into the sharper \([1,H_p]\) and equality of two digit algorithms, independently constructs cycles in every vertex of the closed functional graphs, checks each explicitly listed cycle member and successor, and examines every intervening integer required for the twenty nearest-happy minimality/maximality assertions.

All ten base cases returned `VERIFIED`. The proof of universal eventual trapping uses the descent theorem of Grundman–Harris and the elementary five-digit lower bound supplied in `RESULT.md`; the finite program alone cannot establish global eventual descent without this mathematical input. No outside independent audit is represented by these checks.
