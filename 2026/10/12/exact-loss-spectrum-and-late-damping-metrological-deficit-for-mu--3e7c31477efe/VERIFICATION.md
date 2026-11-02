---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For N>=4, 2<=k<=N-1 and all p in [0,1], independently reconstructed the exact lost-excitation Kraus block rho_s(S,T)=p^(k-s)(1-p)^s/C(N,k)*C(N-|S union T|,k-s). Complementing the lost-set indices yields the Boolean inclusion Gram W_{s,N-k+s}W^T; sl2 raising/lowering harmonic rank-j chains give eigenvalues lambda_sj with d_j=C(N,j)-C(N,j-1), including null chains and endpoints. J+ moves adjacent excitation sectors with squared amplitude (s+1-j)(N-s-j); the complete support-to-kernel SLD spectral sum gives the stated transverse QFI, Jz=0, and equal transverse directions. Pure and fully-reset endpoints are respectively N+2k(N-k) and N; explicit order-epsilon expansions of lambda_00, lambda_10 and lambda_11 give -2k(N-k+2), all other terms O(epsilon^2); hence a strict below-N interval near p=1, and positivity follows a nonzero rank-one-chain edge. Independent newly written full Kraus dense-state calculation tested 45 (N,k,p) cases N=4..6, worst eigenvalue error 4.996e-16, QFI error 1.776e-14, 377 analytic endpoints, and symbolically simplified the universal slope to -2k(N-k+2). Computations only corroborate, not prove, unbounded assertion.

## originality

PASS

Best-of-knowledge PASS for all-excitation exact damping spectrum and collective-spin SLD QFI plus strict late-loss derivative, after reading six relevant primary full texts and querying three Resultary formulations and web aliases. W-state k=1, pure-Dicke QFI and noisy witness bounds, N=8 numerical balanced plots, generic Liouville-basis methods, and dark-matter field FI with damping after encoding do not mathematically entail the complete statement. Prior finite and methodological overlap is credited. Unlocated stronger representation-theoretic theorem remains a real historical-priority risk; search cannot certify novelty.

## value

PASS

Multi-excitation Dicke probes under independent local energy loss are a canonical physically motivated family; the general output spans exponentially many computational basis states and nontrivial permutation irreps. A complete rank-resolved binomial eigenvalue census and O(N^2) exact total collective-spin SLD QFI replaces exponential diagonalization for every excitation count, and a universal strictly negative first derivative near total reset proves a non-obvious interval with information below the N shot-noise reference although the undamped pure probe is above it. The exact finite-population calculation and sharp endpoint sign are independently useful, unlike a single finite plotted slice or pair-concurrence fact. It does not give measurements, heterogeneous loss, unique crossover, or general noisy channels.

The dated certificate retains the supplied scientific assessment, sources and limitations.
