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
# Verification and limits

Execute `python verify_vamos.py` with standard-library Python 3. The checker verifies the five Vámos circuit-hyperplanes, enumerates the 65 bases, tests each coordinate and circuit facet by exact rational affine rank, and compares an independent quotient-lattice canonical Cartier-equation calculation to the claimed dichotomy for each basis. It also computes all six orbits under the specified generators and tests six rank-three-to-five sparse-paving parameter cases. Successful execution ends with `VERIFY_OK`.

Proof dependence: the all-ranks theorem requires the connected-flat facet argument and integral divisor sequences in `RESULT.md`; finite computations alone are not a proof of arbitrary rank. The calculations do not determine singular scheme structure or every non-fixed local germ. There has been no independent audit or independent validation.
