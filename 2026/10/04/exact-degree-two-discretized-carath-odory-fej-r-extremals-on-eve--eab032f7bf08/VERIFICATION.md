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
The universal proof uses exact algebra and order properties of the cosine grid.

For \(m=2\) and \(m=3\), explicit choices of the second-harmonic coefficient make the sampled inequalities feasible for arbitrarily large first coefficient, proving the infinite values.

For every \(m\ge4\) with \(8\nmid m\), the two cosine samples adjacent to \(-1/\sqrt2\) are \(u_m<v_m\) in numerical order as stated in the result. The candidate factors with those two roots and is nonnegative at every sampled cosine. Positive weights \(1-2v_m^2\) and \(2u_m^2-1\) eliminate the free coefficient from the two active constraints and give exactly the same upper bound. Equality forces both active constraints to vanish, proving uniqueness of the free coefficient.

When \(8\mid m\), the grid contains \(-1/\sqrt2\), where the second-harmonic term is zero, forcing the sharp value \(\sqrt2\).

`artifacts/verify.py` checks these identities and inequalities for \(4\le m\le5000\). This finite replay is corroborative and does not replace the all-modulus proof.
