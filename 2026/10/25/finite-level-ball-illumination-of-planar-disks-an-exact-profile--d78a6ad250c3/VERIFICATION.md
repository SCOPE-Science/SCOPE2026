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

# Verification scope

`verify_illumination.py` is executable with the Python 3 standard library. It checks numerical area independently of the circular-segment derivation: for six choices of \((R,r,t)\), it samples both arcs of the feasible-center lens \(B_2(0,R-r)\cap B_2((t,0),R)\), intersects all sampled enclosing radius-\(R\) disks via their directional radial minima, and evaluates the resulting polar-area quadrature. Agreement with the proposed explicit excess area is checked within \(0.011\), a bound deliberately wider than the observed quadrature errors.

The script also tests strict increase along 200 subdivisions in each of four radius pairs, exactly evaluates the endpoint formula, and compares near-endpoint normalized excesses with the independently derived \(3/2\)- and \(1/2\)-power coefficients. These are deterministic numerical consistency checks; the analytic proof in `RESULT.md` establishes the continuous statement. No external or independent mathematical certification has been performed.

Run from the directory containing these files:

`python3 verify_illumination.py`
