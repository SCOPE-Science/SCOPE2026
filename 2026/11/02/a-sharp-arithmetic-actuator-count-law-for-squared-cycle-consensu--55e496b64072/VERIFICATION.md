---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For n>=5, adjacency Fourier eigenvalues of fixed unit-weight C_n^2 are a_k=4*cos(2pi*k/n)^2+2*cos(2pi*k/n)-2. Different cosine values collide only when their sum is -1/2. Averaging zeta^k+zeta^-k+zeta^l+zeta^-l=-1 over cyclotomic Galois automorphisms gives mu(r)/phi(r)+mu(s)/phi(s)=-1/2; elementary order classification restricts actual extra collisions to (2,6), (3,4), and distinct cosine values from order5. They yield eigenspaces of dimensions 3 for 6|n, 4 for 12|n, and 4 for 5|n respectively; other nonconstant conjugate pairs have dimension at most two. PBH requires at least maximum multiplicity control channels, and the first d consecutive vertices give nonzero Fourier Vandermonde determinant on each d-dimensional eigenspace, so exactly q(n)=4 if 5|n or12|n; else 3 if 6|n; else 2. Independent direct numerical eigenspectrum tests over all 5<=n<=180 agreed. The finite test is diagnostic; analytic cyclotomic and Vandermonde arguments prove all n. No claim concerns arbitrary edge weights, input effort, or structural controllability.

## originality

PASS

Qualified best-of-knowledge PASS for the exact arithmetic n-divisibility classification and explicit consecutive optimal leader placement, not for general PBH max-multiplicity principle nor the known squared-cycle Fourier spectrum. Saha–Das 2025 gives same spectrum but only standard conjugate-pair presentation; general circulant network paper of Nabi-Abdolyousefi–Mesbahi 2013 remained full-text inaccessible and may include relevant special cases. No precise arithmetic q(n) law was located among inspected sources.

## value

PASS

C_n^2 is a natural four-regular consensus network. The exact minimum number of independent vertex inputs is a natural operational invariant and changes nonmonotonically with divisibility by 5,6,12; the cyclotomic origin of that sharp law and explicit consecutive minimal set provide reusable spectral/control insight. Not a generic PBH restatement because the accidental eigenvalue multiplicities require a nontrivial arithmetic classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
