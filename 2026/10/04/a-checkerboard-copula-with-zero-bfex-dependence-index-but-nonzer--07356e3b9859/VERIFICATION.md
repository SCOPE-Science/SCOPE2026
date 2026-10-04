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

The finding is verified by exact algebra and the accompanying `verify_checkerboard.py`.

For the displayed checkerboard matrix, the script checks:

- every cell probability is positive;
- every row and column sum is exactly \(1/3\), hence the margins are uniform;
- at least one cell probability differs from \(1/9\), hence the checkerboard law is not independent;
- \(\int_0^1\int_0^1 C(u,v)^2\,du\,dv=1/9\), so BFEx is \(1/36\), exactly the independence benchmark;
- \(\int_0^1\int_0^1 C(u,v)\,du\,dv=1153/4356\), so \(\rho_S=64/363\);
- along the one-parameter checkerboard direction, \(\int C_t^2=1/9+(4/81)t+(121/81)t^2\), making the cancellation at \(t=-4/121\) exact.

All computations use Python's rational `Fraction` arithmetic. The proof does not rely on floating-point output or simulation.

Scientific limit: this verifies one explicit absolutely continuous counterexample and the associated one-parameter identity. It does not enumerate the entire zero set of the BFEx index.
