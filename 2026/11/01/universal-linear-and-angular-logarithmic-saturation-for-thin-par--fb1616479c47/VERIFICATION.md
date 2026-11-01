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

## Analytic checks

The identity for the triangular difference density \((1-|z|)_+\), the exact kernel primitive, its second-derivative estimate, the two triangular moments, the four boundary-edge cases, and the remainder orders are displayed in `RESULT.md`. Both mean distances have the required common limiting value \(1/3\); the linear correction comes from the fraction of boundary arclength on the short edges. The second-order shear term cancels for the boundary mean but survives in the interior mean. No step depends on an empirical extrapolation.

## Computational checks

Run `python check.py` after installing the local dependency from `requirements.txt`. The script independently checks three kernel primitives, four angles at four small lengths each, four reflection symmetries, the exact square interior-distance mean, and direct area/arclength random-pair sampling (180000 pairs in each measure). The observed remainder is consistent with \(O_{\vartheta}(\ell^3\log(1/\ell))\). These are finite checks, not an exhaustive certificate or an independent review.

## Limits

The proof assumes fixed \(0<\vartheta<\pi\). No uniform angle limit, general-convex-body stability estimate, publication-priority certification, or separate external mathematical audit has been established.
