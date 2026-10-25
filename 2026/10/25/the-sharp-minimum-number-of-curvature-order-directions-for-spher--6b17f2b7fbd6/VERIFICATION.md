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

Analytic checks:

1. The vector \(v\) is unit since \(1/3+(d-1)2/[3(d-1)]=1\), and all its coordinates are nonzero.
2. For the first-coordinate reflection, \(\langle v,S_{e_1}v\rangle=1/3\). The irrationality proof uses the root-of-unity algebraic-integer argument, not a decimal approximation.
3. The closure of the generated reflection group contains continuous rotations in \(\operatorname{span}\{v,e_1\}\). Conjugation and Lie brackets generate every elementary skew-symmetric coordinate generator, hence \(\mathfrak{so}(d)\).
4. The centroid fixes the locations of all symmetry hyperplanes; translating it to the origin makes the generated reflections linear.
5. For any at most \(d-1\) tested directions, the displayed ellipsoid is invariant under each corresponding reflection and has equal \(\sigma_m\) values at opposite chord endpoints.

No numerical experiment is used as a proof of an infinite statement. No independent audit or independent validation is claimed.
