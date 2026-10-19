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

# Reproducibility record

The executable `verify_escape_variance.py` (dependencies: Python 3, SymPy, mpmath) was run against its own actual package content. It reconstructed both backward moments, checked all recurrence and wall boundary identities symbolically, and verified the closed mean, variance, quartic derivative, and necessary coefficient identities. A separately implemented two-state matrix exponential was differentiated at zero Laplace parameter for six positive-parameter examples. Ten other parameter samples checked the number of positive quartic roots as implementation sanity checks.

Observed terminal result: `PASS 42 exact symbolic, independent Laplace, and parameter-sample checks` followed by numerical mean threshold `0.5485837703548635` and variance threshold `0.5772173450159419`.

The proof of all-parameter uniqueness uses exact coefficient signs and Descartes' rule, not those samples. The existence of moments uses finite travel times, positive wall detachment, and a geometric success argument; the boundary point \(a=g=0\) is excluded. No independent audit, external certification, or simulation-based infinite proof is claimed.
