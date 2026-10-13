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

The proof is analytic. The bundled `verify.py` independently checks the following supplementary identities and finite stress tests:

- the equivalence \(b^2\le4ac\iff x^2+2b\le1\) under \(a+b+c=1\) and \(x=a-c\);
- the derivative identity producing \(3y^3+(6b-1)y-2x\);
- exact sign/discriminant conditions on representative rational nonclassical states;
- reconstruction of \(\sigma_y\) as the equal mixture of coherent states at azimuths \(0,2\pi/3,4\pi/3\);
- agreement of the analytic root with a dense direct scan over the entire diagonal classical region for several nonclassical test states;
- the stationary-point simplification of the two formulas for \(Q^2\).

Running `python3 verify.py` prints `VERIFY_OK`.

The dense scans are sanity checks only. They are not used to infer the continuum minimum, uniqueness, or originality. The theorem's limits are the diagonal spin-1 state class, Hilbert--Schmidt distance, and the spin-coherent convex hull.
