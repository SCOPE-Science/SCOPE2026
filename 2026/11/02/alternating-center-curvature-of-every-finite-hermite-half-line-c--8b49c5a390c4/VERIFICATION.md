---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Let A_q(t) be the Gram compression of 1_[t,∞) to h_0,…,h_(q-1), V_q(t)=tr A_q(I-A_q). Normalized physicist Hermites satisfy h_j″=(t²-2j-1)h_j. Boundary Wronskians and parity give the Hermite overlap integral and first two threshold derivatives. The finite central-binomial identity S_mR_m=H_m (where H_m=sum_{j<m}[C(2j,j)/4^j]^2) follows from generating-function recurrence, then adding an odd/even Hermite level yields curvature increments (4/pi)H_m and -(2/pi)(c_m²+2H_m). From V_1″(0)=-2/pi, induction gives (-1)^q(2/pi)H_ceil(q/2). Reflection A_q(-t)=I-D A_q(t)D gives evenness and stationary center; H_m>0 forces strict local maximum for odd q, strict local minimum for even q; c_j²~1/(pi j) yields magnitude (2/pi²)log q+O(1). Independently verified Wronskian double-sum rational coefficients against closed form q=1..40; checks are finite corroboration of proof.

## originality

PASS

Qualified PASS for uniform all-finite-q closed-form moving-threshold second derivative, parity-alternating strict local extremum, and logarithmic magnitude. Forrester–Witte treat exact index variance at t=0 but not its moving-t curvature in the inspected sections. Polyanalytic Fock literature identifies the Hermite matrix but does not in inspected material produce this curvature identity. Genuine priority risk of older finite-GUE moving-threshold variance derivative identities expressed via Hermite kernels or Fredholm determinant calculus.

## value

PASS

The half-line concentration trace defect is the determinantal-particle-number variance and a canonical spectral-concentration observable. Its local curvature controls symmetry-threshold stability and has a nontrivial strict parity switch at every order plus increasing logarithmic strength; a complete all-q identity is naturally motivated beyond known centered value and isolated low orders.

The dated certificate retains the supplied scientific assessment, sources and limitations.
