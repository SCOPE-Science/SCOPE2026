---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

BLOKS Eq. (7) is the stated H, and (12)–(13) give the inverse of the stated P. Writing C=δE+ρ1_n1_mᵀ gives CᵀC=δ²I+(2δρ+nρ²)J and hence h₀,h₁. Blockwise zero sums, zero-global-sum block constants, and the global constant vector give the three simultaneous SPD eigenpairs and listed multiplicities. To check strict ordering independently, write F(x)=1+(δ+ρx)/(δ+λx). The inequality h₁/h₀>t₁/t₀ is exactly mF(n)>sF(s). For ρ≥λ, F is nondecreasing and m≥2s; for ρ<λ, F(n)>1 and F(s)<2. Also t₁>t₀. The s=1 within-block space is absent; when m=n=s, P=H. Comparing the real all-ones direction with the zero-sum vector having equal-modulus root-of-unity phases by block gives identical Q quadratic forms for any SPD block-diagonal Q and a quotient ratio h₁/h₀. CG takes the degree of the least residual polynomial annihilating the spectral components from a zero start, and full column rank of C makes generic responses possible. At n=8,m=4,s=2,ρ=3/5,λ=1/10 direct substitution gives 1/48,1/4,11/16 with ratio 33; b=(1,2,3,4) has each required component. In the repair the normalized top eigenvalue is 1+(mρ/δ)F(n); its derivative has the sign of ρ−λ and the middle ratio t₁/t₀ is independent of n. Packaged code was read, not executed.

## originality

PASS

Pass the exact normalized spectral profile and ordering for the actual BLOKS sketch with distinct equicorrelated nonlandmarks of arbitrary count, including the exact dependence on n. The abstract optimal block-scaling lower bound and the first appearance of a third eigenvalue are not accepted as independent discoveries. The full-center and replicated-center constructions already exhibit the homogeneous three-level mechanism and unchanged conditioning; the repair gives them explicit credit. For the same center Gram and ridge, adding distinct training points changes the normalized profile in general, whereas replication never changes it; the mathematical comparison removes the possible equivalence via scalar replication.

## value

PASS

The exact spectral calculation for a standard, normalized, realizable kernel and actual distinct-point Nyström sampling analyzes a case not modeled by copying landmarks. It shows why added off-center training points can alter the largest generalized ratio while the failure to condition better and the extra Krylov step survive uniformly. This is a useful obstruction to interpreting a sketched block inverse as automatically improving the distinct-point normal system, beyond an abstract block scaling lower bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
