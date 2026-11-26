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

The stated open-end signs give eigenvectors u_k(j)=i^j√[2/(N+1)] sin(jq_k) of A with simple eigenvalues t_2 cos(q_k). The zero endpoint sines give the stated Wu_k even at the ends. Its squared magnitude is 2F_{j,k}/(N+1), strictly positive since sin(q_k)>0 and sin(jq_k), cos(jq_k) never both vanish. At finite loss, an eigenvector with real eigenvalue would have B=0 by dissipativity; then it would be an A eigenmode annihilated by W, impossible. Thus all evolution decays and its norm-balance identity gives unit total integrated loss. For the infinite-time strong-loss calculation let η=1/Γ. The zero cluster of ηH_Γ at η=0 is the A subspace; the fast spectrum is that of -iD and lies uniformly below the real axis at fixed N. Analytic spectral projections give an O(η) fast initial component; a fixed contour below -i min(w_j)/2 around the fast cluster bounds its propagator by C exp[-min(w_j)t/(2η)], without requiring simple fast eigenvalues. Its weighted squared integral is O(η²). The slow Schur complement of H_Γ is A-iηWD^-1W+O(η²), with B amplitudes -iηD^-1Wu_k+O(η²). The slow expansion coefficients tend to the overlaps with u_k. Since r_k=<u_k,WD^-1Wu_k>>0, the diagonal time integrals have leading η^-1/(2r_k); off-diagonal integrals are bounded by the nonzero frequency gaps and vanish after multiplying by the O(η) channel prefactor. The fast–slow interference also vanishes, by Cauchy–Schwarz. This proves the finite-sum branching formula and its strict positivity and normalization. Reflection preserves F, giving w_jπ_j=w_{N+1-j}π_{N+1-j} with no symmetry hypothesis on w_j. For the sequential limit the denominator divided by H_N tends to (t_1²+t_2² sin²q)/2 uniformly away from endpoints by the bounded interior cosine sums with weights 1/j. Each F is at least min(t_1²,t_2²) sin²q and F_1 is at most (t_1²+t_2²) sin²q, so the scaled summand is uniformly bounded even near the endpoints. The sine source weight for S=N and the Riemann sum then give exactly the stated integral; H_N/log N→1, and π_N=π_1/N already holds at every fixed size in this profile.

## originality

PASS

The Hamiltonian, integrated-loss observable, linear gradient and numerical edge-burst behavior are prior. General effective decay-channel elimination and Green-function representations are prior tools. The inspected sources do not supply the evaluated fixed-size distribution in this regime, its inverse-weight reflection identity for arbitrary positive profiles, or the sequential logarithmic law and coefficient. The comparison supports the explicit chain-specific evaluation and consequences, not a new general elimination method or the discovery of the physical effect.

## value

PASS

The known numerical remote-edge concentration motivates an exact question for a canonical graded chain. The inverse-loss ratio is geometry-dependent through reflection yet exact for all positive profiles and all source sites at fixed size. For linear loss the exact endpoint ratio N coexists with vanishing absolute end escape probabilities on the two different logarithmic scales; the explicit coefficient is quantitatively useful. This goes beyond observing a peak or writing down a generic elimination equation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
