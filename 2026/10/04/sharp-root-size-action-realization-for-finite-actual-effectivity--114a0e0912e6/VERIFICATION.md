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

The theorem was checked at two levels.

First, the proof was reconstructed symbolically. For \(Q=\mathbb Z/q\mathbb Z\), fixing any coordinate of \(H(x_1,\ldots,x_k)=(x_1-x_k,\ldots,x_{k-1}-x_k)\) leaves a bijection from the remaining \(k-1\) coordinates to \(Q^{k-1}\). Composing with any surjection \(Q^{k-1}\twoheadrightarrow R\) therefore makes every one-coordinate slice onto \(R\). This is exactly the property needed to recover every prescribed outcome inside each fixed action's neighborhood.

Second, `verify.py` performs deterministic finite replay. It exhaustively checks the slice bijection for several small \(k\) and \(q\), generates many finite deterministic concurrent games, extracts their actual-effectivity neighborhood frames, reconstructs games using the theorem, and checks exact equality of all neighborhood families. It also verifies the arithmetic strict inequality \((q-1)^{k-1}<r\le q^{k-1}\) used by the worst-case lower bound. The replay result is `VERIFY_OK`.

The finite replay is supplementary evidence only; the theorem is an exact finite proof and does not rely on experimental extrapolation.
