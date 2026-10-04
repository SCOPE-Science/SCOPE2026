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

The universal statement is proved symbolically in `RESULT.md`. The critical steps are: reduction of simultaneous \(x\)- and \(x+1\)-stripping to the \(z=y+1\) valuation on \(\mathbb F_2[y]\); the factorization \(B_n=1+z^t y^qQ\); the exact one-factor recurrence through the first \(t-1\) steps; the final higher-valuation step leaving \(B_{n+t}\); and the next-multiple argument showing that block indices reach the next power of two without overshoot.

`verify.py` independently replays the polynomial dynamics with exact bit-polynomial arithmetic for every starting index in the conjectured family through \(R=8\). It checks all block endpoints, all intermediate one-factor valuations, and all resulting sequence lengths. The expected terminal line is:

`VERIFY_OK r=1..8 starts=255 odd_steps=10795 block_identity=exact length_formula=exact`

The finite range is not an exhaustive proof for arbitrary \(R\); its purpose is to detect algebraic or normalization errors in the symbolic proof. No floating-point arithmetic, random search, or external certificate is used.
