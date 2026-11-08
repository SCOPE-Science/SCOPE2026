---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For degree<=d, each radius-t intensity U_t has Laurent Fourier modes -d..d. A 2d-point angular DFT recovers every c_m(t), |m|<d, without alias; the sole mode d combines A=a_d conj(a_0) and conj(A). The aligned and delta-rotated rings yield Re A and Re(exp(id delta)A), a 2x2 matrix with determinant -sin(d delta). If nonzero, both entire circle intensity trigonometric polynomials are known. The rational quotient of two polynomials with equal moduli on circles of distinct radii is invariant under a nonunit dilation and hence unimodular constant, including vanishing-coefficient cases. If sin(d delta)=0, 1+i z^d and 1-i z^d collide. Eigenvalues 1+/-|cos(d delta)| of B^T B give the exact best half-step Nyquist coefficient conditioning; this is not global polynomial inverse stability. All quantifiers and the d=1 boundary are valid.

## originality

PASS

Full nested-circle uniqueness (Chalendar--Partington), unbalanced 2d+1/2d-1 finite sampling (Pohl--Li--Boche), and intersecting-circle 4d constructions (Bodmann--Hammen) do not logically imply the balanced 2d+2d iff rotation diagram. Literature-based originality is qualified by possible more general finite-frame constructions with the same geometry.

## value

PASS

At critical equal measurement budgets each individual cyclic ring aliases exactly one harmonic. The exact angular resonance obstruction and unique best half-step supply natural sampling geometry and a useful spectral conditioning invariant independent of full nonlinear stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
