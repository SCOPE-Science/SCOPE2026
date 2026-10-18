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

# Verification notes

The proof is symbolic over \(\mathbb C\) for all nonsingular binary and ternary cubic inputs. Its decisive steps are the relative-scale cube equation giving a birational map \(Y\dashrightarrow\mathbb P^1\times\mathbb P^2\), the local tangent weights \((1,1)\) and \((1,1,1)\) modulo \(3\), quasi-étale canonical pullback, and the fixed-locus Lefschetz trace \(1\) on \(H^3(X,\mathbb Q)\).

Run `python CHECK.py`. The code checks the Fermat specialization's character decomposition, Jacobian-ring invariant degree-one monomials, topological trace and invariant dimension, canonical determinant indices, and anticanonical volume. It does **not** certify the full argument, independently audit the finding, or replace the smoothness/analytic proofs.

No statement about a resolution, integral cohomology, or external validation is made.
