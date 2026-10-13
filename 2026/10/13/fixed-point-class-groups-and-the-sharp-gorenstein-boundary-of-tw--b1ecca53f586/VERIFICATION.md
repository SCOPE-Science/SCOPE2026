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
Run `python verify.py` in Python 3 with SymPy installed. It checks every allowed fixed-point chart for \(3\le a,b\le6\), giving 292 tests of generator spans, proposed facet validity, supporting-facet rank, coordinate-lattice saturation, class ranks and canonical Cartier conditions. `verification_output.txt` records the complete stdout from the same packaged script.

The infinite-family proof is the explicit cone equality and toric divisor calculation in `RESULT.md`. Finite checks neither establish exhaustiveness for untested parameters nor replace that proof. No independent external mathematical validation has been performed.
