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

## Reproducibility checks

- Artifact: `artifacts/verify_k33.py` (Python standard library only).
- The subdivided graph has 15 vertices and 18 edges; the unordered three-particle cubical chain-group ranks are \((455,1404,1386,432)\).
- Exact ranks over \(\mathbb Q\): \((454,946,432)\).
- Exact ranks over \(\mathbb F_2\): \((454,945,432)\).
- The script verifies \(\partial_{k-1}\partial_k=0\) over \(\mathbb Z\) for each applicable degree.
- Computed Betti vectors: \((1,4,8,0)\) over \(\mathbb Q\) and \((1,5,9,0)\) over \(\mathbb F_2\); all Euler-characteristic checks equal \(5\).
- Replay command: `python3 artifacts/verify_k33.py`; expected terminal line: `VERIFY_OK`.

## Limits

The calculation does not compute a Smith normal form, the exponent of the 2-primary summand in integral \(H_1\), odd-primary torsion, the cohomology ring, or the homotopy type. It makes no claim for particle counts other than three. Independent validation and independent audit remain unperformed.
