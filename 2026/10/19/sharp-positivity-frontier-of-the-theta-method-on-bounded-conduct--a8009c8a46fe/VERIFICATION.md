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

The analytical proof covers every integer \(n\ge3\), all conductances bounded by \(w\), and all \(\theta\in[0,1]\). A graph's matrix \(I+tL\) is a positive-definite Stieltjes matrix, so its inverse is entrywise nonnegative. The graph-edge cap implies the Loewner comparison with the complete-graph Laplacian. Equality of the \(i\)-th inverse diagonal reduces to vanishing slack on **all** edges incident to vertex \(i\). The full continuum in \(h\) follows from a positive spectral mixture, not finite experimentation.

`verify.py` requires Python 3 and SymPy. It enumerates all labeled simple connected graphs on 3 and 4 vertices, checks the exact rational positivity boundary and the saturated-hub equality test for several theta values, then checks representative capped saturated graphs up to size 5. The script is supplementary and not a proof of all-order completeness. No independent external audit has been performed.
