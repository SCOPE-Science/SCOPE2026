---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Expand each intensity into Fourier k-harmonics 0,±1; their orthogonality for N>=3 yields ||Jh||_dat²=4Σ(αu_j+βu_{j+1})²+2tΣ(u_j+u_{j+1})²+2tΣ(v_j-v_{j+1})². Fourier diagonalization gives amplitude eigenvalues 4−4t+12t cos(2πk/N) and phase eigenvalues 4t(1−cos(2πk/N)). The only obligatory null is global imaginary constant; the amplitude minimum and phase nonzero minimum give the two affine terms. Their unique intersection occurs at t_N*=1/(1+3c_N+2sin²(π/N)) ∈ (0,1/4], with equality 1/4 only N=3. Numerical independent real Jacobians N=3,4,5,6,9,12 matched all eigenvalues including multiplicities to machine precision; general proof is analytic.

## originality

PASS

Known STFT/Gabor stability results concern graph connectivity, general stability, window ambiguity, and recovery, not the exact complete real differential spectrum at the flat signal under the stated data norm nor the maximin optimization over unequal two-tap amplitudes. The phase/parity obstruction and sharp all-N optimal weights are independently specified and not implied by uniqueness or general bounds.

## value

PASS

The exact worst-direction local sensitivity and optimizer matter directly for a natural normalized two-tap spectrogram sensing design. The balanced window has an additional amplitude null in every even cyclic dimension, whereas a provably unequal design restores transversality and supplies the exact conditioning scale 2π²/N². This is not a trivial endpoint renaming or known numerical table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
