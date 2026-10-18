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

For every prime power q≥2 and nontrivial unitary additive character ψ of Fq, the 4q−3 functions 1 and ψ(u a),ψ(u b),ψ(u c),ψ(u d) on SL2(Fq) are distinct under the uniform probability inner product. Reconstructed |SL2|=q(q²−1), one- and adjacent-two-coordinate Fourier sums −q leading to ρ=1/(q²−1), and opposite-entry blocks ρ K_−(a,d), ρ K_+(b,c). Orthogonality gives K_ε 1=1 and K_ε K_ε*=q²I−(q+1)J. On the sum-zero (q−2)-dimensional frequency space H, K_ε/q is unitary with ± coupling spectra 1+ρ±qρ=q/(q±1); each opposite pair contributes q−2 to each. The orthogonal five-dimensional mean-frequency block splits into eigenvalues q/(q+1) (twice), q/(q−1) (once), and eigenvalues μ_± of the explicit 2×2 matrix B_q. Multiplicities μ_-:1, q/(q+1):2q−2, μ_+:1, q/(q−1):2q−3 sum to 4q−3. From det B_q=q(q−1)/(q+1)²>0 and discriminant 9q²−14q+9, derived strict 0<μ_-<q/(q+1)<μ_+<q/(q−1), including q=2 when H={0}. The eigenmode construction gives sharp Riesz bounds and full equality spaces. Independently enumerated SL2(Fq) for q=2,3,5,7 and diagonalized Gram matrices, maximal error <1.8×10^-15; all-q proof rests on exact orthogonality not these four cases.

## originality

PASS

PASS best of knowledge: Li–Hu Theorem 2.4 evaluates general ambient additive Fourier transforms on SL_n via rank and Kloosterman sums; it provides ingredients for Gram entries but not this 4q−3-function family’s full diagonalization, closed eigenmultiplicities, equality spaces or sharp frame bounds. Thill–Hassibi §VII builds nonabelian representation-character group Fourier frames of SL2, not additive ambient coordinate characters restricted to determinant-one variety. Related GL_m Resultary spectra are for the different set GL_m and do not imply SL2 conditioned on det=1. No same-family stronger spectral theorem found in actual comparisons.

## value

PASS

PASS: exact finite-field Riesz spectra and optimizing modes of a natural first-coordinate Fourier restriction to the determinant-one hypersurface are useful exact invariants with simultaneous uniform positivity and asymptotic conditioning. The Kloosterman-unitarity block reduction is structural and the arbitrary-prime-power theorem is not just a small-field numerical table or renaming a general additive transform.

The dated certificate retains the supplied scientific assessment, sources and limitations.
