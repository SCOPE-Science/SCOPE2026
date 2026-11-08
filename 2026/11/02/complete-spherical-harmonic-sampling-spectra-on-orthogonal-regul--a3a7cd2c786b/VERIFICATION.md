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

Under probability surface measure on S³ the reproducing kernel is (ℓ+1)U_ℓ(x·y), with diagonal (ℓ+1)². The two regular orthogonal circles produce equal n×n circulant Gram blocks plus constant cross-blocks (ℓ+1)U_ℓ(0). The exponential Fourier expansion U_ℓ(cosθ)=Σ_{j=0}^ℓ exp(i(ℓ−2j)θ) gives each nonzero frequency eigenvalue n(ℓ+1)c_a twice, while the two constant modes have eigenvalues n(ℓ+1)(c_0±s_ℓ). Exactly min(m,ℓ+1) occupied parity-residues and c_0(2k)=1+2⌊k/m⌋ imply ranks 2min(m,ℓ+1) for odd ℓ, 2min(m,ℓ+1)−1 for even ℓ<2m, and 2m for even ℓ≥2m. The constant-mode null eigenvector proves signed circle-sum quadrature for even ℓ<2m; direct multiplicities at ℓ=2m−2,2m−1,2m give tight and √2-conditioning transitions, and asymptotic residue counts imply condition number→1. Checked m=2, ℓ=0 and independent phases in the argument. Independently built raw addition-kernel matrices and compared all eigenvalues for 248 (m,ℓ) cases m=2..9, ℓ=0..30; these finite eigenspectra corroborate but do not prove all m,ℓ.

## originality

PASS

Best-of-knowledge PASS for complete, phase-invariant exact-degree point-evaluation Gram spectrum, all ranks and the signed quadrature defect for two orthogonal regular circles. Kramer and Dowker study invariant harmonic bases for quaternionic/binary-dihedral quotient spaces, not the all-sample singular spectra in the inspected parts. A still-unidentified equivalent representation-theoretic Fourier-sampling theorem remains a priority risk.

## value

PASS

The natural sampling configurations include binary-dihedral finite subgroup orbits of S³. Their all-order/all-degree spectral ranks and singular values determine reachable sample interpolation and stability, including nonmonotonic degree rank and exact quadrature relations; this is a meaningful complete classification of a natural sampling invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
