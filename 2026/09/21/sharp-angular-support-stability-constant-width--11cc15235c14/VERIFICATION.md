---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-01.md",
      "INDEPENDENT_AUDIT_2026-10-01.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

After Steiner centering, constant width leaves exactly odd Fourier modes n>=3 and the area deficit is (pi/2) times the weighted coefficient energy. Weighted Cauchy--Schwarz for the two-point evaluation functional gives the claimed series; the odd-mode series evaluates to M(d)=(1-cos d)/2+(pi/2-d)sin d, with d=pi recovering the 2pi Hausdorff coefficient. For odd q-fold symmetry only frequencies q(2k+1) survive, and the reciprocal-weight sum is pi/(4q) tan(pi/(2q)), yielding 2q cot(pi/(2q)). The finite Fourier truncations in the package can be scaled so h+h remains positive and their ratios converge to the displayed constants, so finite computation is only corroborative, not the infinite proof.

## originality

PASS

An earlier 2026-09-20 record already proves the antipodal/Steiner-disk inequality D>=2pi d_H^2, so that subclaim is prior-covered. The surviving final claim is strictly stronger: it gives the sharp two-direction kernel for every angular separation and the exact odd q-fold symmetry hierarchy. Neither the earlier record nor the inspected external sources imply those d-dependent or symmetry-resolved constants.

## value

PASS

The all-angle kernel is a structural sharpening of a canonical stability inequality, resolving how support differences scale with angular separation, and the symmetry constants quantify a natural improvement under cyclic symmetry. These are meaningful geometric refinements rather than a bare restatement of the prior 2pi endpoint.

The dated certificate retains the supplied scientific assessment, sources and limitations.
