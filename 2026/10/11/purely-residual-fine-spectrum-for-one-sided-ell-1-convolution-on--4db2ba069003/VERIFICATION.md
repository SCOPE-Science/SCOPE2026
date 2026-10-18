---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

The representation T_a=Σ_{k≥0}a_kR^k converges in operator norm since a∈ℓ₁ and ||R||=1. Phase-align finitely many x_{N−k} to show ||T_a||≥Σ_{k≤N}|a_k| for every N, yielding exact norm ||a||₁. For non-scalar a, first nonzero offdiagonal a_m and first nonzero coordinate x_j of an eigenvector force eigenvalue a_0 and then contradiction a_m x_j=0 in coordinate j+m, so point spectrum empty. For |z|<1, summation F_z(x)=Σz^n x_n is a nonzero adjoint eigenfunctional for R; for |z|=1, twist a shift-invariant Banach limit L((z^n x_n)) to obtain a nonzero eigenfunctional. Therefore T_a−Φ_a(z) has range inside a proper closed hyperplane and is injective, hence Φ_a(closed disk) is residual. Conversely characters on convolution algebra ℓ₁(N₀) are evaluations at |z|≤1, so outside Φ_a(closed disk) the algebraic convolution inverse gives an actual bounded inverse on ℓ∞. No tail truncation or approximate eigenvectors are mistaken for the infinite theorem. The scalar kernel exception is separately correct.

## originality

PASS

Saha–Patra same-space ℓ∞ fine-spectrum result is explicitly polynomial / finite-band (Theorem 5.5), while their infinite convolution section works on a different σ∞ space. The claim covers all one-sided infinite-support ℓ₁ kernels with a precise residual-vs-point/continuous partition. A general analytic Toeplitz/Wiener algebra theorem might imply the same result under different words; no decisive covering statement was located, and this residual risk is recorded.

## value

PASS

Provides the natural infinite-support closure of recent finite-band ℓ∞ residual-spectrum classification and proves the fine-spectral partition survives arbitrary summable tails, not just the total spectrum. Boundary Banach-limit separation and the Wiener inverse make it a useful exact class statement rather than finite-band substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
