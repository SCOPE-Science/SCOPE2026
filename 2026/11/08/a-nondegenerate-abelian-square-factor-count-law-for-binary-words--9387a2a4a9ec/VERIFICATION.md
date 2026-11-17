---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Each weight-two word is uniquely 0^a 1 0^b 1 0^c with a+b+c=n-2. Two-one Abelian squares are exactly 0^u 1 0^b 1 0^v satisfying 0≤u≤a,0≤v≤c, |u-v|≤b and parity u+b+v≡0 mod2; zero-only classes add floor(max(a,b,c)/2). Each pair defines a literal distinct factor. Strip lattice counts are uniformly half the area up to O(n), and gap triples rescale to Dirichlet(1,1,1). Independently enumerated all 560 two-one words of lengths 2–15 and their literal factor sets, exactly reproducing count formula. Independently integrated all six polynomial simplex sectors in exact SymPy rational arithmetic to get E[A]=1/24, E[A²]=5/1728; the proposed L=A/2 has mean 1/48, second moment 5/6912, variance 1/3456. Bounded convergence of moments follows from the uniform error; finite checks are corroboration only.

## originality

PASS

PASS best-of-knowledge: previous upper bounds and two-one constructions establish deterministic Θ(n²) distinct Abelian squares and a known parity-strip counting technique; neither fixes the full uniform fixed-weight-two conditional limit law or second moment. Related 2026 records for three-marker Abelian-square laws, minimal absent factors, and Lyndon factors involve different words/invariants. No exact prior variance 1/3456 surfaced from targeted original-article/Resultary searches.

## value

PASS

PASS: a natural sparse-string ensemble (all weight-two binary words equally likely) has a surprising nonconcentrated quadratic-normalized limit, unlike simply reporting a maximum or an arbitrary small count. Its exact variance is a usable quantitative answer about typical Abelian-square richness, requiring a nontrivial uniform lattice-to-area argument and six-region squared-area integration. The known deterministic strip formula is explicitly not credited as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
