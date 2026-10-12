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

# Computational and proof verification

The classification theorem is proved in `RESULT.md`, Steps 1–4. Singleton valuations convert the full semantic \(\mathsf{Alex}\) implication into the monotonicity of the forward-orbit minimum. Its fibers are proved to be consecutive intervals, each carrying a directed rooted tree; this yields the exact enumeration by Cayley's formula.

From the extracted directory containing `RESULT.md`, run:

```sh
python3 artifacts/check_alex.py
```

The checker uses no third-party package and verifies the following independent conditions:

- Two versions of the enumeration, a sum over all ordered compositions and a dynamic recurrence, agree for every size from one to ten.
- Every endofunction on a chain of size one through seven is tested: its orbit-minimum criterion agrees with the explicit rooted-tree decomposition, and the number passing agrees with the enumeration.
- Every Boolean valuation is tested against the actual two modal operators for every endofunction on chains of sizes one through five. Those truth-table results agree with the orbit-minimum criterion.
- A two-world discontinuous valid map and an invalid three-world map are witnessed explicitly.

Expected final line: `VERIFY_OK`. Reproducibility is independent of external data. The test is finite evidence and **cannot** substitute for the general proof. No external or independent audit of this mathematical result has been performed.
