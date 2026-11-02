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

The proof is analytic. `verify.py` supplies an independent finite exact-rational check using matrix inversion, not a spectral quotient implementation. It constructs every requested weighted adjacency matrix, its stationary distribution from weighted degrees, then the fundamental inverse \((I-P+\mathbf1\pi^{\mathsf T})^{-1}\). It checks the trace formula against the claimed rational \(\Delta_{a,b}(t)\) for 240 triples \((a,b,t)\). Exact checks also verify the family-wide lower bound on the sampled grid and the sign threshold on balanced graphs. Additional rational checks verify stationary derivative signs about the unique root without using numerical floating-point guesses.

Run `python verify.py` using Python 3. Successful execution prints `PASS` with the assertion count. This finite computation is not an exhaustive verification for unbounded graph sizes or real conductance; the published proof handles those quantifiers. No independent audit has been conducted.
