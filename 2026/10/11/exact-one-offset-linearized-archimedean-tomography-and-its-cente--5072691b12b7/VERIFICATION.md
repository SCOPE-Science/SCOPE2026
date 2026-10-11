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

The exact radial-graph area element is
\[
r_\varepsilon^2\sqrt{1+r_\varepsilon^{-2}|\nabla r_\varepsilon|^2}\,d\omega.
\]
Differentiation at the sphere gives \(2\varphi\,d\omega\). The two moving boundary circles are regular because both offset levels lie strictly between \(-1\) and \(1\). Their signed first variations give the delta distributions stated in the proof.

For a normalized Legendre polynomial \(P_\ell\), the zonal harmonic multiplier is
\[
2\pi\left(2\int_s^{s+h}P_\ell(t)dt+sP_\ell(s)-(s+h)P_\ell(s+h)\right)
=2\pi J_\ell(s,h).
\]
The infinite-degree proof uses the nonzero leading coefficient \(h(1-\ell)c_\ell\) for each \(\ell\ge2\), not finite checking. This proves that the exceptional-offset set is countable. Harmonic orthogonality then proves the exact kernel; parity proves centered odd-degree invisibility.

The bundled `verify.py` independently tests the exact polynomial identities through degree 12 and tests the first-variation normalization through degree 4 by differentiating numerically the **actual area integral** of a perturbed radial graph, with the slab intersections recomputed at each perturbation. Expected output begins `VERIFY_OK`. These finite tests are diagnostic only and do not certify a uniform stability estimate or a nonlinear inverse theorem.
