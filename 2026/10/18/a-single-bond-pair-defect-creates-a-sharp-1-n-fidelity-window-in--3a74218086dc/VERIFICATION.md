---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

The explicitly given n×2n incidence matrix B has full row rank. Direct multiplication gives BB^T=2LL^T+2δ²e_2e_2^T. The inverse of 2LL^T and Sherman-Morrison imply Q=1+(N-1)δ² and exact endpoint flat-band projector Gram entries η_S=1/(2Q), η_R=(1+Nδ²)/(2Q), Λ=(-1)^(N+1)δ/(2Q), also N=2. Spectral functional calculus of the 2×2 Gramian yields transition amplitude Λ/Δ [cos(ω_+t)-cos(ω_-t)] and probability ceiling [1+N²δ²/4]^-1. At δ=0, Λ=0 and transfer is identically absent. For nonzero δ outside a countable frequency-ratio exceptional set, irrational torus-phase density makes the bound the actual supremum. Exact λ± expansion at δ=c/N yields splitting gc√(c²+4)/(2√2N)+O_c(gN^-2), and the cosine factor enforces an Ω(N/g) slow-beat time. Independent direct dense projection calculations gave max Gram errors 5.6e-17 (N=2), 1.1e-16 (N=5), 1.5e-16 (N=9) at three signed defects. All claims explicitly concern the resonant projected model, not the full finite-coupling chain.

## originality

PASS

Almeida et al. already derive the two-hub effective Hamiltonian and the general transfer envelope in terms of endpoint overlaps. The reviewed contribution specializes to one microscopic defect, evaluates the exact rank-one flat-band projector and its finite-N Gramian, then deduces a specific sharp defect-versus-length law. General envelope itself is NOT claimed new.

## value

PASS

Computes an otherwise abstract two-hub coupling Gram matrix from a physically natural single antisymmetric bond-pair defect and extracts a sharp design tolerance 1/N and time cost N/g. The zero-defect discontinuity and generic attainability are concrete, independently useful features not supplied by the general reduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
