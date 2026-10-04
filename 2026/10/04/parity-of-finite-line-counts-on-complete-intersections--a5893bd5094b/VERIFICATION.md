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

The proof was reconstructed from the line specialization of the Debarre--Manivel coefficient formula and checked symbolically modulo two. No finite computation is used to justify the infinite quantifier.

The bundled script `artifacts/verify_ci_line_parity.py` was executed from the packaged artifact path. It prints:

`VERIFY_OK cases 209 odd_cases 55`

The script also reproduces the five standard complete-intersection Calabi--Yau threefold line counts \(2875,1280,1053,720,512\). The exhaustive range is only a regression test: \(3\le n\le12\), nondecreasing multidegrees \(d_i\ge2\), and \(\sum_i(d_i+1)=2n-2\).

The main limitation is literature-comparison risk, not proof risk: a later source may record the same parity corollary under a different formulation. The closest inspected real-line theorem has a strict inequality that excludes the present zero-dimensional boundary.
