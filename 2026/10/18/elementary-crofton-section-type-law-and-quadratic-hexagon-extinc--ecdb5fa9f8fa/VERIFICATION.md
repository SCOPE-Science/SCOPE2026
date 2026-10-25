---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For each generic direction sort the projected halfwidths xi>=eta>=zeta. Sweeping all twelve box edges gives positive-offset lengths (2zeta, 2(eta-zeta)+(xi-eta-zeta)_+, 2min(xi-eta,zeta), (eta+zeta-xi)_+) for 3,4,5,6 vertices, summing to xi+eta+zeta. Integrating with Haar dOmega dt (width-biased normals) gives p3=4T/s and p6=2Q/s, the remaining probabilities by the exact length identity. Spherical Stokes vector-area integrals give the stated arccos/arctan closed forms for T=E min(A,B,C) and Q=E(S-2max)_+. Coarea on a|U1|=b|U2| near c=0 gives Q/c^2->1/(2sqrt(a^2+b^2)) and hence the extinction constant 1/((a+b)sqrt(a^2+b^2)); the small simultaneous X,Y case contributes only O(c^3). Independently counted intersections of all 12 physical edges at 70,000 weighted normals for each of (1,1,1) and (.7,1.5,.3): max empirical discrepancy 0.0031. This is finite corroboration, not a substitute for the spherical/coarea proof.

## originality

PASS

The motion-invariant noncentral-affine-plane four-type distribution and flattening coefficient are not implied by an equal-probability central-section theorem or cube-only tabulation; the searched recent combinatorial slicing paper concerns possible face types and reconstruction, not invariant affine hit-conditioned probabilities. Best-of-knowledge original for arbitrary positive aspect ratios; Bray chapter 10 inaccessible leaves genuine historical risk.

## value

PASS

An exact all-aspect-ratio law for random intersecting affine sections of the natural three-dimensional rectangular box supplies probabilities of four combinatorial types without quadrature and a sharp, positive c^2 degeneration invariant. This is a substantial geometric-kinematics fact, not the earlier cube-only table or the known mean-four formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
