---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For odd prime p and nonzero weights, the formal real quadratic extension Q=1/2Σ[(u_j−u_{j+a})²+(u_j−u_{j+b})²−(u_j−u_{j+a+b})²] diagonalizes by additive characters. With normalized a=1 and c=−b/a, signs of nonzero Fourier eigenvalues are sign cos(π(k−[ck]_p)/p); p odd excludes equality/extra nullspace. If c∈{1,2,2^{-1}}, every sign positive. Otherwise c≤(p−1)/2 after k=1 restriction and k=floor((p−1)/c) yields a strict negative mode; positive trace gives an opposite sign. Checked exact residue inequalities across 45 odd primes <200, 556,656 prime-ratio mode instances, including even negative multiplicity. Proof, not finite check, establishes all p. This does not assert realized Hilbert-scheme multiplicities.

## originality

PASS

Consequence of originating Euler form and general signed graph Laplacian results not shown to subsume exact odd-prime three-ratio classification. Specific highly plausible originating paper inaccessible in full, so best-of-knowledge priority risk is elevated. Best-of-knowledge; checked source and access limitations recorded in residual_risks.

## value

PASS

Exact inertia of the Euler correction is a natural structural invariant for the equivariant quotient dimension formula; the three precise symmetry types, one-dimensional nullspace and signs of all other modes are a complete family classification. The result deliberately separates formal quadratic energy from geometric existence, avoiding unsupported significance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
