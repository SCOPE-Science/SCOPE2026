---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Using the precise Fourier isometry of Monguzzi–Peloso–Salvatori Cor 3.6 for fixed a>0, s>1/2 and m=floor(s−1/2) excluding half-integer endpoints, evaluation kernels are u_lambda(xi)=[exp(−i lambda xi)−P_m(−i lambda xi)]|xi|^(−s) in H=L²[−a,a]. At xi=0 the Taylor remainder behaves as O(|lambda xi|^(m+1)); at infinity as O(|lambda xi|^m). Therefore C_{s,m}=∫|R_m(t)|²|t|^(−2s)dt finite exactly m+1/2<s<m+3/2 and ‖u_lambda‖²~C|lambda|^(2s−1)→∞ at |lambda|→∞. Bessel bound forces sampled lambda bounded. Norm-continuity excludes infinite subsequences approaching nonzero lambda_* (including repeated nonzero points), so any infinite sampling sequence must accumulate only at zero. Expansion u_lambda=lambda^(m+1)v+O_H(lambda^(m+2)), v≠0, and Bessel inequality against v implies Σ|lambda|^(2m+2)<∞; hence Σ‖u_lambda‖²<∞ (finitely many outside small neighborhood), so the frame operator is trace-class and cannot dominate A I in infinite-dimensional H. Finite sampling is similarly impossible; lambda=0 contributes zero. The contradiction is a genuine infinite-dimensional compactness proof, not experiment. Independently checked the kernel exponent integrability and representative small/large scaling ratios via numerical quadrature (not used as a proof).

## originality

PASS

Best-of-knowledge PASS for the supercritical (s>1/2) **real point-sampling nonexistence** theorem. The very same Monguzzi–Peloso–Salvatori primary paper Section 5 proves no sampling for 0<s<1/2 via a fixed-window exponential frame condition but does not state the supercritical Taylor-subtracted-kernel result in the inspected full text. Its fractional Laplacian reconstruction using another functional is not a point-sampling counterexample. The new mechanism is Bessel norm growth plus a trace-class frame obstruction, not a reworded subcritical theorem; broad frame compactness lemmas themselves are standard and credited.

## value

PASS

Stable point-sampling is a central question for fractional Paley–Wiener spaces. The theorem closes the complementary supercritical parameter range of the cited primary problem using a sharp structural impossibility mechanism; the obstruction is global across every countable real sampling set and not a cheap failure of a particular lattice or a finite-dimensional check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
