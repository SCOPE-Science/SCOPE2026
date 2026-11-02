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

# Verification and boundaries

Run `python3 checker.py` using Python 3 and only the standard library. The script exhaustively tests the identity
\[\sup_x(D_w(x)-D_{w,F}(x))=\sup_{v\notin F}R(w,v)\]
on all vectors of length 1–4 over the four-element sample grid, for all finite coordinate sets. It reports 4,680 tested weight/subset configurations and `ALL_CHECKS_OK`. Additional assertions check monotone finite stages of both infinite-star examples. All embedded files can be extracted as UTF-8 and run without external packages.

The general proof does not depend on the checker: infinite nonattainment follows from explicit countable subsequences; product discontinuity follows from arbitrary finite-coordinate basic neighborhoods; and the finite-superlevel implication yields actual finite witnesses. The checker is not a certificate for uncountable sets or independent validation. The analysis uses only the product topology, not the uniform topology, and permits arbitrary [0,1]-valued propositional atoms. A formula may contain nested modalities, but the universal condition is verified via its resulting successor-value vector.
