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

For any reflexive/transitive IS4 relation on C_n, forth-up and back-up are respectively monotonic row and column maxima, and transitivity forces h(h(i))=h(i), b(b(j))=b(j); both are extensive closure maps. Conversely for any closure pair the possible relation U: j<=h(i), i<=b(j) is reflexive/transitive via idempotence and contains forced generators i→h(i), b(j)→j. Their transitive closure L has exact maxima, so all transitive intermediates L⊆R⊆U are valid frames. On a chain an upward U edge is within an h-fibre and downward within a b-fibre; failure of factorization occurs iff one of the two adjacent-bit forbidden patterns. The surviving four-symbol words count 4*3^(n-2) (n≥2), with Q1=1. Independently enumerated all paired closure maps through n=5, verified L,U and uniqueness iff, counts 1,4,12,36,108; no extrapolation from n<=5.

## originality

PASS

The full nearest Resultary maxima normal form classifies monotone row/column maxima for arbitrary relations, with independent optional edges; the IS4 preorder adds idempotent closure maps and a transitive lower closure that constrains previously optional edges. Balbiani et al. define general IS4 modal axioms, not sharp chain uniqueness. The unavailable full Girlando manuscript is a real residual coverage risk rather than an automatic failure.

## value

PASS

The row and column extremal maps are canonical observables of any finite-chain IS4 preorder. The theorem determines which pairs occur, canonical extremal realizations, when the observables reconstruct the full relation, and a sharp exponential census—useful structural information not provided by existence or finite-model decidability alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
