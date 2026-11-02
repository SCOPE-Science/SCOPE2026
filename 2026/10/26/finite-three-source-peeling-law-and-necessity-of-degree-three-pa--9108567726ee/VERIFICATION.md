---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For exactly three binary information symbols with iid support draws (singletons each rate a=p1/3, pairs each b=p2/3, triple c=p3) and peeling-only recovery, independently enumerated all 128 present-support subsets and its iterative peeling closure for target A. The resulting survival event has 28 failure sets and expands exactly as 2u^3v^3w-u^3v^2w-2u^3v^2+u^3-2u^2v^3w+2u^2v^2+uv^2w, u=e^(-at),v=e^(-bt),w=e^(-ct). Unit-rate Poissonization and integration produce all seven rational terms of E; zero p1 gives infinite time because no peeling begins. For p3=0, exact rational reduction yields E2(x)=(5x^4-20x^3+25x^2-4x+12)/(x(x-3)(x-2)(x+2)). Independent rational arithmetic checked Q(x)=22079x^4-116237x^3+361684x^2-375052x+120000 and its strict convex lower certificate on x in [0,1], hence E2(x)>27921/10000. Exactly 24 copies of each singleton, nine of each pair and one triple give 100 columns and E=13700419/4906902<27921/10000. This proves degree-three necessity for any global finite-length symmetric optimum if one exists, without asserting that the witness is globally optimal.

## originality

PASS

Distinguishes precise finite-three-symbol iterative peeling access expectation/support necessity from prior finite-k unrestricted linear decoding and asymptotic symmetric fountain-code equivalence. Best-of-knowledge original conditional on the unchecked older LT small-case thesis; it could contain a comparable optimal degree-three distribution.

## value

PASS

Although the numerical improvement is small, support-necessity is a mathematically meaningful structural boundary for a canonical finite-dimensional LT/peeling model: no weight-one/two-only fully symmetric matrix of any length attains the three-weight finite witness. The exact seven-term expected hitting-time law is independently useful for finite-symbol comparisons. No practical throughput or optimal length-100 design claim is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
