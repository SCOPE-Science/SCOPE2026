---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

All-projection 3-fold invariance removes all ambient harmonics except degrees 0,1,3 by SO(3)-invariant projection and nonzero allowed-parity circle Fourier coefficient (verified against source Lemmas 4.8 and 4.12). Direct independent SymPy calculation from RESULT.md checked seven harmonic Laplacians zero, orthonormal frame entries, exact 7×7 matrix determinant 625/6912 and inverse infinity norm 164/5. Rank<=6 for any three views produces nontrivial cubic perturbations with identical three translated shadows; I+ε(∇²H+HI)>0 provides actual strictly convex counterexamples. Nonzero real analytic minor yields genericity. 14 bound on sum of spherical harmonic suprema gives stated Lipschitz 2296/5. Finite matrix arithmetic is not a proof of universal harmonic reduction, which is supplied by the cited lemma.

## originality

PASS

Full 14-page structural primary source establishes the symmetry/harmonic foundation but not the proposed finite calibrated reconstruction or explicit four-view optimality. Related axial cubic brightness and general spherical sampling records do not dominate this precise map. Best-of-knowledge with finite-band tomography coverage risk.

## value

PASS

Optimal information-theoretic number of translated calibrated planar shadows, an exact rational inverse and stability for a natural seven-parameter family are independent, reusable geometric tomography facts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
