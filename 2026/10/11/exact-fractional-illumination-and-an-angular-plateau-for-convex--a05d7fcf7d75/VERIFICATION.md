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

The proof uses an open-arc formula at each polygon vertex, counting no more than \(\lfloor(m-1)/2\rfloor\) overlaps for equiangular normal fans and no more than \(q\) under the stated strict odd-sided perturbations. It explicitly constructs weighted cyclic block-midpoints that satisfy every vertex condition. Incidence at the relative interior of each edge follows from its incident vertex conditions. Consequently neither a continuum of boundary checks nor infinitely many direction checks is delegated to computation.

Execute `python3 verify_fractional_polygon.py` with Python 3. The checker uses exact rational numbers measuring angles in full turns. It evaluates every angular chamber determined by the finite arc endpoints, plus the endpoints themselves, for the constructed instances, and checks all assigned block cover incidences. The actual replay output is:

`VERIFY_OK exact_fractional_polygon assertions=738`

The deterministic verification covers all equiangular vertex-normal systems with \(3\le m\le27\), and three exact rational perturbation patterns for each odd \(m\) in this range. This cannot certify the theorem for all \(m\) or optimize the tolerance; those statements rely only on the proof. Independent audit has not been performed.
