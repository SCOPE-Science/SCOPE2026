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

The separate numerical implementation in `verify.py` recomputes the complex Zak expression by two geometric tails and compares it to the claimed extremal formulas. It covers 240 distinct triples with `m` in {2,3,4,6,10,25}, 4800 randomly selected Zak fibers, an independent bounded one-dimensional minimizer for each triple, the equality of spatial endpoint multipliers, and the predicted extremal frequency values.

Observed output: `VERIFY_OK 4800 complex-Zak direct comparisons across 240 parameter triples`.

The proof is analytic; finite comparisons do not establish the universal theorem. These floating-point checks are tolerance-based (absolute-relative tolerance on the order of 1e-8), and extreme underflow/overflow regimes are not exhaustively tested. Python 3 with NumPy and SciPy is required to execute the verifier. The lower bound is strictly positive by linear independence of two positive geometric vectors; this is proved without numerical assumptions.
