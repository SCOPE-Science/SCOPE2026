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
# Verification

Reproduce the identities with Python 3 and the installed SymPy library by running `python verify.py`. The self-contained program directly builds the transition matrix and both driving vectors, checks the independent-sampling and reshuffling Lyapunov equations symbolically, verifies both comparison factorizations for all symbolic \(p\), verifies the limiting coefficient \(1/4\), and checks selected rational signs. The proof of the sign comparison for **all** \(p\in(0,1)\) is the denominator and polynomial analysis in RESULT.md, not the finite spot checks. No independent audit has been performed.
