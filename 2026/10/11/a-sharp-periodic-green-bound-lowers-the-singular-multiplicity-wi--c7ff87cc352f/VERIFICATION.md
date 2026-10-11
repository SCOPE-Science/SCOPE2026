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

The new step is the exact oscillation bound for the periodic solution of \(w''=f\) with zero-mean \(f\). Using the explicit periodic Green kernel, the difference between two translates has two linear branches and absolute maximum \(d(2\pi-d)/(4\pi)\), which is at most \(\pi/4\). This yields \(\operatorname{osc}w\le(\pi/4)\lVert f\rVert_1\).

`verify_green_bound.py` checks the branch identities on exact rational normalized coordinates and the algebraic endpoint identity; its recorded output is `VERIFY_OK`. The proof in `RESULT.md` is analytic and does not infer an infinite statement from the finite replay.

The focal 2026 full text was inspected at Theorem 2.1 and the lower-function construction. The 2003 original paper was inspected at Proposition 1.5 and Theorem 4.3, and the 2001 construction paper at Proposition 2.4. These sources use the larger coefficient \(\pi/3\).

Limits: sharpness is established only for the linear periodic-corrector oscillation estimate. No claim is made that \(\pi/4\) is the best possible threshold for every nonlinear multiplicity argument.
