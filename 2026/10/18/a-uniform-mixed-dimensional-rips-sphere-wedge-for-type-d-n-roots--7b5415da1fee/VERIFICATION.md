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

The command `python3 verify_dn_root.py` was executed against the accompanying standalone source. It enumerated all maximal and nonmaximal cliques at the exact dot-product threshold, determined all simplicial boundary ranks over the field of two elements, and checked the number and dimensions of every face not belonging to a signed-coordinate star for \(n=4,5,6,7\).

Exact observed outcomes: \(n=4\): face vector \((24,96,96)\), reduced \(\beta_2=23\); \(n=5\): \((40,240,400,160)\), reduced \(\beta_2=49\) and \(\beta_3=10\); \(n=6\): \((60,480,1120,960,384)\), reduced \(\beta_2=111\) and \(\beta_4=12\); \(n=7\): face vector \(84,840,2520,3360,2688,896\), \(\beta_2=209\) and \(\beta_5=14\). All other positive-dimensional Betti numbers were zero. Output marker: `VERIFY_OK`.

These are exhaustive finite computations over \(\mathbb F_2\), not integral Smith-normal-form certificates or a proof for arbitrary \(n\). The integral infinite-family theorem relies on the structural star-and-triangle homotopy proof in `RESULT.md`. In particular, each signed-coordinate star is a genuine sphere, and every remaining attaching loop reduces to a crosspolytope triangle after null-homotoping its arcs within simply connected stars. No independent scientific audit has been performed.
