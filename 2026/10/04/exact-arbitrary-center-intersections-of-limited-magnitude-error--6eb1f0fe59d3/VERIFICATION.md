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

The proof is symbolic and all-parameter. The executable check is an independent finite corroboration of the local factors, coefficient dynamic program, one-coordinate corollary, and known global-maximum specialization.

`verify.py` constructs \(\mathcal B(n,t,k_+,k_-)\) directly, translates it for every displacement in the finite test grid, computes literal set intersections, and compares them against the coefficient formula. It does not infer an infinite theorem from the finite grid.

The exhaustive grid uses \(1\le n\le4\), \(1\le t\le n\), \(1\le k_+\le2\), and \(0\le k_-\le k_+\), with every displacement whose coordinates lie in \([-K,K]\). A separate symbolic grid checks the support-one closed form for larger parameters.

Limits: the computation is finite and is not a proof of the all-parameter claim; correctness for arbitrary parameters rests on the coordinatewise bijection in `RESULT.md`. The verification does not test code constructions or packing-density consequences because none are claimed.
