---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

On X={+/-v_e: e two-subset of {1..8}} in the 7-dimensional coordinate-sum-zero space, direct inner products yield +/-1/3 off-diagonal. The K8 edge-incidence Seidel matrix S=2BB^T-3I-J has eigenvalues 9 (multiplicity 7), -3 (multiplicity 21). Antipodal parity and normalized Gegenbauer kernels give the exact four block eigenvalue expressions 2(1+27c_k),2(1-c_k) for even k, and 2(1+9c_k),2(1-3c_k) for odd k, where c_k=P_k(1/3). Rational recurrence values yield ranks 1,7,27,21,27 for k=0..4; for 5..9 |c_k|<1/27; beta-moment estimate |c_k|<=965/59049<1/27 for k>=10 proves every k>=5 has rank28. The first consecutive complete two-degree interpolation is 5+6 rank56; 4+5 rank55. Independent rational 28x28 Gram rank computations through k9 agreed; the beta-moment inequality, not the finite data, proves all k.

## originality

PASS

The Gegenbauer addition kernel and Seidel/association scheme framework are standard; the all-degree rank-sequence specialization, low-degree exceptional fourth-degree defect, and first full consecutive harmonic sampling pair 5,6 are not stated or dominated by inspected harmonic-index design results. This remains best-of-knowledge, with 56-point tight-design association-scheme character tables a material equivalence risk.

## value

PASS

The 56-point Gosset code is a canonical exceptional finite spherical configuration; determining every exact harmonic evaluation rank and the minimal two-consecutive-degree interpolation threshold gives a natural complete sampling-spectrum invariant. The all-k threshold and fourth-degree missing direction provide genuinely useful design/interpolation information beyond a finite rank sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
