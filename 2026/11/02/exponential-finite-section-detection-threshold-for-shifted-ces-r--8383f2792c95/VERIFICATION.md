---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For i≤j, multiplication gives K_ij=Σ_{k≥j}a_k²−(i+1)a_i a_j. Telescoping Σ_{k≥j}g_k=a_j and 1−(i+1)a_i=αa_i give K=Σ d_k v_kv_k*+αaa*, with finite positive trace Σ(k+1)d_k and a∈ℓ². In the invertible partial-sum coordinates of the leading N-dimensional space the positive part has diagonal weights d_0,…,d_{N−2},D_{N−1}; the corresponding coefficient vector is (g_0,…,g_{N−2},a_{N−1}). This gives the exact dual norm squared and, after positive congruence, the required inertia including the simple null direction at equality. The N=1 interior sum is empty and the positive trigamma tail is still exact. Strict increase follows by splitting the merged tail: the first ratio g_{N−1}/d_{N−1}=N+α is strictly less than the d-weighted average of g_k/d_k=k+α+1 for k≥N. The harmonic part diverges; this supplies a negative direction for every −1<α<0 and rank one bounds the full negative index by one. For α≥0 the two terms are positive semidefinite. Uniformly for small ε, the scalar is log N+2−ψ(2−ε)+O(1/N); bounded sections cannot cross 1/ε, and the crossing integers squeeze log N_*−1/ε to −1−γ. The witness partial sums equal k+α+1 up to L−1 and vanish thereafter, giving B_L(1+α B_L), and the same squeeze without the tail term gives 1−γ and the ratio e². Its actual support dimension is L+1, with no change to the limiting ratio. The supplied checker was inspected, not executed: it checks selected exact-rational identities and interval signs with the infinite tail enclosed; the all-N and limiting claims rest on the proof.

## originality

PASS

The assessed distinct contribution is the exact optimal leading-section inertia criterion, the first-section prefactor e^(−1−γ), and its quantitative comparison with the onset for Ma's witness. The qualitative hyponormality boundary, the witness construction and trace class are not new, and the full real-shift index also appears explicitly in a distinct indexed record. None of those observations is treated as an independent novelty here.

## value

PASS

Leading sections are a canonical diagnostic for nonhyponormality. The result resolves exactly when this diagnostic first succeeds, including equality and a sharp exponential prefactor that is invisible to both eventual negativity and finite sampling. The e² gap quantifies the cost of restricting attention to the known test vector and isolates the role of the infinite tail.

The dated certificate retains the supplied scientific assessment, sources and limitations.
