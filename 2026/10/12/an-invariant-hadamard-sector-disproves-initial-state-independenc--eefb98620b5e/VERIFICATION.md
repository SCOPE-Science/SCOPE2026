---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

At λ=1/√2, γ=0 and zero phases, the inspected reversal coin has two invariant 2D sectors and its (x+,y−) restriction is H=(1/√2)[[1,1],[1,−1]]. This allows only x+ or y− steps; setting Z=X+Y gives X=(t+Z)/2 pathwise. The Fourier Hadamard dispersion sin ω=sin(k)/√2 yields velocity v=cos(k)/sqrt(1+cos²k). Spectral projectors give E[Z]/t→±I, E[Z²]/t²→I with I=∫v²dk/(2π)=1−1/√2. Hence E[X²]/t²→(1+3I)/4 or (1−I)/4, unequal by I>0. Weak convergence implies these moments because |Z/t|≤1. Direct independent rational-integer coin check verified NᵀN=2I, det(N)=4, and Hadamard-sector invariance; finite t=64 walk iterates corroborate distinct trends but are not the infinite-time proof. Boundary γ=0 is explicitly within the primary admissible parameter region.

## originality

PASS

The original nonreversal paper numerically conjectures independent even-total-degree leading moments, but its proof is only for the different nonrepeating walk. The boundary coin gives an explicit valid counterexample with an exact degree-two asymptotic, not merely a finite-time fluctuation; Konno/Grimmett-Janson-Scudo supply classical 1D Hadamard weak limits, which alone do not state this particular 2D nonreversal objection.

## value

PASS

A concrete analytically proved counterexample corrects an explicit universal conjecture about this walk; the invariant-sector explanation identifies an overlooked admissible boundary and explains why generic random sampling can miss it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
