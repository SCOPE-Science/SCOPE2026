---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

Reconstructed without relying solely on the inaccessible original paper: for each complex multi-index alpha with |alpha|=m, Fourier integration on coordinatewise circles inside the ell_p unit ball gives |a_alpha| ≤ (m^m/alpha^alpha)^(1/p)||P||_p, with p=infinity interpreted via unit polydisc. Weighted AM-GM/Hölder maximizes |u^alpha| over ||u||_t≤1 at (alpha^alpha/m^m)^(1/t), including t=infinity. Thus each coefficient term is ≤(m^m/alpha^alpha)^(1/p-1/t)||P||_p||u||_t^m. If t≤p the exponent is nonpositive and the pure monomial z1^m gives sharp C=1. If p<t, only alpha with support at most k=min(s,m) matter; splitting a part ≥2 strictly reduces alpha^alpha until exactly k parts, while strict convexity of x log x shows minimizers have balanced parts q,q+1 for m=kq+r. A monomial with precisely those exponents and diagonal u_j=(alpha_j/m)^(1/t), or 1 at infinity, attains both optimizations, including all m,s,n,1<=p,t<=infinity. Strict support growth through k=m follows from a strict split. No enumeration purports to prove arbitrary m.

## originality

PASS

Best-knowledge PASS for this specific finite *weight-vector* support-budget profile, with material direct-source risk. The focal paper publicly studies sparse coefficient bounds and weighted Hardy--Littlewood functionals; the frozen research package identifies an unrestricted maximum as Proposition 4.4. Primary full text could not be read this execution, so coverage of its detailed propositions is not ruled out. The directly read 2026 Springer paper treats bounded variables in each nonzero monomial and an ell_q coefficient-sum Bohnenblust--Hille norm, not an s-supported diagonal weight in a coefficient *maximum*. The exact balanced-composition staircase is not implied by the unrestricted constant without the new constrained integer optimization.

## value

PASS

Diagonal-weight sparsity is a natural variable in weighted polynomial estimates; the formula gives a complete exact finite support threshold k=min(s,m), strict increase for s<=m, the balanced exponent geometry and both published unrestricted and pure-coordinate endpoints. This supports choosing sharp constants in sparse inputs rather than an arbitrary small-computation exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
