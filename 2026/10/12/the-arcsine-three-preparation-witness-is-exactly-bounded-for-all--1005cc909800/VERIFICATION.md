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

The universal statement is proved analytically in `RESULT.md`; no finite experiment is used to infer a universal quantifier.

The bundled `verify_j3.py` performs three reproducibility checks:

1. It verifies on a deterministic grid that every sampled contraction parameter pair satisfying \(\lvert a\rvert+t\le1\) obeys the squared gradient inequality used to establish the one-Lipschitz property.
2. It checks the scalar boundary inequality
   \[
   \arcsin(a+tc)+\arcsin(a-tc)\le\frac{\pi}{2}+\arcsin(a-t)
   \]
   throughout a deterministic grid of admissible \((a,t,c)\).
3. It evaluates the explicit equality pattern \((2^{-1/2},2^{-1/2},2^{-1/2},-2^{-1/2},-1)\) and confirms \(J_3=3\pi/2\) to floating-point tolerance.

The checker prints `VERIFY_OK` when all checks succeed. These computations are diagnostics for transcription and boundary errors; the proof in `RESULT.md` supplies the exact all-parameter argument.

Scientific limits: the result is only for the specific three-preparation, two-binary-measurement witness \(J_3\). It does not classify the whole qubit correlation set or establish higher-dimensional analogues. Literature comparison cannot exclude an obscure, poorly indexed equivalent proof.
