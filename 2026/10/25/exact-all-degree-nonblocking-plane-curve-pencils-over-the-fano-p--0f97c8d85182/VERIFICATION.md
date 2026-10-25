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

The exact all-degree proof reduces to a seven-coordinate evaluation problem and does not use interpolation extrapolated from a finite sample. A degree-three indicator of each rational point is a product of three rational line equations avoiding that point; higher-degree indicators are obtained by multiplication with a suitable linear form.

Reproduce the finite incidence and geometric checks with `python scripts/orbit_census.py` and `python scripts/independent_checker.py`; compare their standard output with the two expected text files in `data/`. The first uses homogeneous characteristic-two Macaulay matrix rank and all invertible \(3\times3\) binary matrices. The second constructs all rational point-line incidences directly and checks every relevant cubic on all three affine charts using SymPy Gröbner bases.

The complete `data/orbits.json` has 112 representative triples. Both programs reproduce 18,368 fully nonblocking cubic pencils and the smooth-member distribution \((4816,9408,3360,784)\). This is a self-review reproducibility check, not independent audit. It makes no claim about the geometry of members beyond the separately checked cubic smoothness statements.
