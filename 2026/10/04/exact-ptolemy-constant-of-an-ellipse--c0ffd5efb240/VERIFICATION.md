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

The analytic proof is the verification basis. The side-direction derivative is
\[
f(m)=\frac{ab}{a^2\sin^2m+b^2\cos^2m},
\]
and each opposite-angle sum integrates \(f\) over total parameter length \(\pi\). The length-\(\pi\) threshold set where \(\sin^2m\ge\cos^2m\) minimizes the integral and gives \(4\arctan(b/a)\). Combining this with the published angular Ptolemy inequality yields the global bound, and the axis endpoints attain it.

The bundled `verify.py` was designed to check the exact endpoint identities and to stress-test random ordered quadruples at several aspect ratios. Such tests are finite and are not evidence for the universal quantifier; they only guard against algebraic or normalization mistakes in the written formulas.

Unproved limits: no uniqueness classification of maximizing quadruples is asserted, and no extension beyond planar Euclidean ellipses is claimed.
