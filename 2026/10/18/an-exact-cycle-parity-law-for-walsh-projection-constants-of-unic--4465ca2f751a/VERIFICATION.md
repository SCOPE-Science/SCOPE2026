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

The analytic proof defines the exact graph class and the canonical real absolute projection constant. Its critical independently reconstructed steps are: (i) Haar-averaging of projections on the finite sign group; (ii) coordinate Hahn–Banach extensions to arbitrary superspaces; (iii) exact classification of edge-sign fibres by the unique graph cycle relation; (iv) the explicit two-sign absolute-value identity, including both even and odd ambient edge counts; (v) conditional elementary-symmetric polynomials on the central or near-central sign slice; and (vi) fixed-degree central-binomial asymptotics.

Running the included `verify.py` with standard Python 3 and no external dependencies yields:

```
UNICYCLE_WALSH_PROJECTION_EXACT_OK 292
SIX_EDGE_CYCLE_LENGTHS ['7/4', '15/8', '9/4']
```

The 292 exact-rational checks comprise parity-constrained sign enumerations at \(3\le m\le13\), direct vertex-spin checks for several finite unicyclic graph shapes, and the predicted sign law. They are finite corroboration, **not** the proof of the theorem for all graphs.

The canonical general projection-kernel representation is previously known (Defant and collaborators, arXiv:2302.00233v1). The present all-graph theorem's additional content is the exact unicyclic parity evaluation. No independent scientific validation has been performed. Additional literature under parity-conditioned Ising moment or Krawtchouk nomenclature could affect novelty assessment.
