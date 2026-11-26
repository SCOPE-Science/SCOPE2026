---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Detailed balance gives W=diag(a/d,1,M,1,b/d) and successive conductances (a,1,1,b). A weighted-mean-zero function supported on the two ends has Rayleigh quotient d and is not an eigenvector (the adjacent bulk equations would not hold); connectedness then gives 0<λ_gap<d. Eliminating the ends for λ<d leaves the symmetric tridiagonal with diagonal (1−λ−γa,2−Mλ,1−λ−γb), γ=λ/(d−λ), and off-diagonal −1. Its determinant is the claimed F; F(0)=0 and F_λ(0)=−(M+2+B/d). Its first positive root is simple by the irreducible symmetric path and the nonsingular Schur factors; hence F_λ there is positive. At balance the antisymmetric eigenfunction at ℓ has central coordinate zero; at M_c the same eigenvalue persists with central coordinate 1−ℓ−γa and outer bulk coordinates ±1. Here ℓ is the unique root on (0,d), since any root there must also satisfy λ<1 and (1−λ)(d−λ) decreases on (0,min(1,d)) while Bλ/2 increases. To identify the gap independently, write W^(-1/2)KW^(-1/2)=AᵀA with A=C^(1/2) D W^(-1/2) for the oriented path differences D and diagonal edge conductances C. The constructed eigenfunction strictly decreases from left to right (at criticality its central coordinate has modulus at most 1−ℓ). Thus C^(1/2)Df is strictly positive and is an eigenvector of AAᵀ, whose negative off-diagonals and irreducibility identify it with the lowest eigenvalue by Perron–Frobenius on a shifted negative matrix. This is the first positive eigenvalue of AᵀA. Implicit differentiation gives dλ/dP=−(2−Mλ)γ²/F_λ for P=ab. For M≠M_c the factor 2−Mλ cannot vanish: F=0 would then force 2(1−λ)=γB and λ=ℓ, implying M=M_c. Continuity fixes its sign from balance, while P strictly decreases with |a−b|. All strict inequalities and the exact plateau follow. The open domain excludes zero adsorption; below M_c the statement is a unique balanced minimum, not an attained fastest split at a prohibited endpoint. Independent replay `python3 /workspace/independent_reproduction.py 3` constructs the generator in the original coordinates. At B=3,d=2 it verifies the eigenvector at M=4,λ=1/2 symbolically for the entire split and checks orientations numerically for M=1 and 16.

## originality

PASS

The supported distinct claim is the fixed-total, positive endpoint-split first-gap reversal and entire critical iso-gap surface in this specific five-state reversible chain. Neither established adsorption modeling nor general Jacobi spectral tools are claimed new. The historically closest wall-diffusion article was accessible and its relevant analytical passages were compared; no earlier directly covering claim was identified in the bounded comparisons.

## value

PASS

The allocation problem fixes a natural physical budget and changes only one central storage parameter; it distinguishes a unique balanced fastest split from a unique balanced slowest split. At the critical capacity, different equilibrium surface weights cannot be distinguished by the first relaxation rate because the whole allocation curve is exactly flat. This is a useful identifiability and control benchmark for a motivated reversible compartment model, independent of whether the same effect persists in continua.

The dated certificate retains the supplied scientific assessment, sources and limitations.
