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

For self-adjoint H the span of its hub-zero eigenvectors and its orthogonal complement reduce H and the loss projector. Taking the imaginary part of each eigenvector equation gives Im λ≤0 and equality only in the hub-zero sector. After restriction to the complement all generalized eigenmodes decay, so the limiting norm squared really is the initial orthogonal dark-projection weight for any γ>0. Deletion of the hub leaves path sine modes; for the Laplacian the principal blocks retain nonhub degree 2, so L=2I−A+2P_v implies the same dark vectors. The two endpoints of a mode cancel exactly for even indices. A coincidence at k/m=ℓ/n means (k,ℓ)=r(m/d,n/d), 1≤r<d. At mixed parity the even mode already exhausts the kernel; at even/even both are already counted. Only odd/odd adds a direction, with normalized coefficients proportional to (√m,−√n), giving precisely 2/(m+n) in the first-loop projection. This produces the floor and parity factor, and the r=1 term checks the stated strictness, including d=1, equal loops, and sites divisible by d. Tracing the projection gives the uniform-vertex mixture. The two triangles give 1/2+1/4. Independently computed modular hub-observability ranks for eight pairs (both H, two primes, e.g. 12,20 gives 16 dark directions, 6,10 gives 7, 4,6 gives 3); finite rank checks corroborate, not prove, the all-size result. The frozen script was inspected, not executed.

## originality

PASS

Pass for the two-cycle parity-filtered resonance and exact local projection law. The hub-zero projection argument, Dirichlet sine basis and gcd matching are closely related to prior results and are not separately credited. The closest actual spider theorem uses one coupled endpoint per arm and never has a zero single-arm endpoint amplitude; the cycle attaches both endpoints and changes the rank by parity.

## value

PASS

A two-loop hub is a natural minimal graph for quantifying how attaching a second loop can increase trapping-resistant survival. The exact parity/gcd and site-divisibility conditions specify when that effect exists, and the local projector gives its magnitude; the total dark dimension alone is insufficient to answer this transport question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
