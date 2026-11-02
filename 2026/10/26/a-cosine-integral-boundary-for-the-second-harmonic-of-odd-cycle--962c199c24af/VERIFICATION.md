---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For odd N=2m+1>=5 the shortest-path distance matrix is circulant, and the real character of frequency two has eigenvalue F_N(s)=2 sum_{r=1}^m r^s cos(4πr/N). Recomputed geometric-sum identities F_N(0)=-1, F_N(1)=-1/[4cos²(π/N)], F_N(2)=N cos(2π/N)/[2sin²(2π/N)]. Ordered cosine coefficients have exactly one sign change for N=5,7 and exactly two (+,-,+) for N>=9. The generalized Descartes bound for exponential polynomials and signs at -infinity, 0, 1, 2 prove a unique simple root sigma_N in (1,2) and no other nonnegative roots. Differentiation at s=1 gives F'_N(1)/N²→L=[γ+log(2π)-Ci(2π)]/(8π²)>0; F''_N(s)=O(N²log²N) in 1<=s<=1+c/N². Uniform Taylor bracketing implies N²(sigma_N-1)→1/(4L)=8.0976273568665367..., with the exact C5 root log2((3+sqrt5)/2). For s>sigma_N the real mean-zero cosine eigenvector has positive distance quadratic form, disproving CND, and derivative of e^{-td^s} at t=0 is negative in this sector. Recomputed multipliers at N=5,7,9,11,31,101,301,1001 and the integral constant independently; those finite examples corroborate, not replace, the infinite proof.

## originality

PASS

Best-of-knowledge comparison of actual propositions, implications and hypotheses; the credited prior fragments are not claimed as new. Full texts actually read are identified, and inaccessible same-object papers remain explicit risks; an unsuccessful search is not novelty proof. The previous C5 p-negative type identity coincides with sigma5. General determinant and vertex-transitive criteria imply the witness method but do not furnish unique sector roots or the asymptotic coefficient without additional analysis.

## value

PASS

Sharp, dimension-dependent obstruction in a canonical Fourier sector of powered odd-cycle distance matrices. The all-odd unique exponent threshold and exact Ci(2π) N^{-2} asymptotic quantify loss of negative type beyond 1, a natural metric embedding invariant. Does not claim the exact full supremal negative-type exponent; the known C5 result alone does not imply the asymptotic constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
