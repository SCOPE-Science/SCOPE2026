---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Diagonalizing the cycle normalized Laplacian gives distinct low-pass lambda_k=1-cos(2*pi*k/N); each pair of conjugate Fourier eigenspaces has two-site 2x2 Gram eigenvalues (2/N)(1±|cos(2*pi*k*s/N)|), the constant block gives 2/N. This proves exactly the demixed frame constants (not those of raw trajectories). The map u=(2/g)s modulo M is surjective with fibers g; the K+1 cyclic residues 0,u,...,Ku have a gap <=q=floor(M/(K+1)), yielding min_{k<=K}||ku/M||<=q/M; u=q attains equality for all k. Divisibility forces equal gaps and generator u=aq (gcd(a,K+1)=1), giving g*phi(K+1) winning separations. Distinct eigenvalues make K+1 temporal Vandermonde powers invertible and 2K observations from K times insufficient in dimension 2K+1. Independently exhaustively tested ALL s for 1,558 (N,K) instances with 5<=N<=80, including all divisible equality counts; finite testing complements the all-integer pigeonhole proof.

## originality

PASS

The exact problem is spectral-projector-demixed sensor geometry, not the raw graph frame operator. Bulai et al. arXiv:2609.25472 (Sept 21, 2026) gives general graph Paley–Wiener dynamical sampling and path-graph numerical frame design in its accessible abstract; the full 31-page manuscript could not be retrieved and Oxford access returned VPN disconnected. Yang–Yang–Huang (2021) materially read graph signal sampling/node selection including undirected ring numerical experiments; no exact all-parameter two-site demixed cyclic maximin and totient equality theorem was identified in the inspected material. Aldroubi et al. (arXiv:2411.12670) treat noisy dynamical graph reconstruction. Resultary similarity searches locate other finite Fourier and path problems but not a stronger statement implying these exact cycle demixed constants. Classical Fourier diagonalization/pigeonhole principles are credited, leaving bounded unindexed/cycle manuscript coverage risk.

## value

PASS

The low-pass graph Fourier band and two-site placement are natural sensing design choices; exact worst-eigenspace recovery and the finite-grid arithmetic loss quantify conditional stability for all cycle lengths and cutoffs, including an equality classification. The theorem expressly does not optimize the raw time-trajectory norm, which also suffers Vandermonde conditioning; within its defined demixed norm it is a complete meaningful natural finite spectral design invariant, not a cherry-picked tiny grid.

The dated certificate retains the supplied scientific assessment, sources and limitations.
