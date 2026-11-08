---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For n=4k+3, a=n^2,b=(n+1)^2,c=(n+2)^2, reduction identities create complete Apéry reps q b+r c with top q=0..L and lower r=1..k, q=0..L-1, L=4(n-1), giving exactly a distinct residues. Under t=q-Lr, x(t)=alpha*t mod a and alpha*(2n-1)=4a-1, exact gap heights h=q+9r+floor(alpha*t/a) identify only 2n-2 top-row cells each contributing 7(k+1) isolated gaps and k(2n-3) lower cells each contributing 2n+2. Their sum is n^3+1. Independently computed shortest-path Apéry representatives and neighbor gap counts for n=3,7,11,15,19,23,27, all matching the cubic.

## originality

PASS

The isolated gap count is a numerical-semigroup invariant distinct from genus, conductor, Frobenius number and pseudo-Frobenius set. In principle existing Hilbert series can encode gaps, but no inspected result directly yields this isolated-gap cube.

## value

PASS

The exact isolated-gap cubic is an unknown-in-inspected-sources natural numerical-semigroup invariant of three consecutive squares, measuring simultaneous representability of adjacent integers. It gives a sharp all-k law and decomposition rather than repeating a known Frobenius/genus computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
