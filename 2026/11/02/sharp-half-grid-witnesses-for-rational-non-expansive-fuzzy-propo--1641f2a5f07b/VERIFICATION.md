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

The allowed negation and clipped shifts preserve a finite max-of-mins representation by constant pieces and clipped signed unary literals with intercepts in d^-1 Z. For each clause and hidden variable the maximum of min positive and negative clipped slopes is at an endpoint or their crossing (b-a)/2, in G_(2d), independently of all retained valuations. Finite max commutes with sup; inf follows by negation. The unique crossing for f_d(x)=min(x,S_(k/d)(1-x)), k=0,1,2 according to parity, has reduced denominator exactly 2d. All quantifiers are finite-variable and the result is purely propositional, not modal. Independent exact rational evaluation of 1,440 random signed-literal clauses d=1..8 matched half-grid maxima; this checks examples, not all terms.

## originality

PASS

Best-of-knowledge PASS narrowly for fixed half-grid optimization precision and its sharpness for every d; Gebhart–Schröder–Wild already establish much stronger modal uniform interpolation existence, so that existence is not new. Their interpolation construction involves halves, but the current claim bounds all hidden-variable witnesses on one fixed 2d-grid despite arbitrarily deep terms. Their related Appendix A half-sum lemma creates a real implicit-coverage risk; full paper was inaccessible in this execution and Oxford access was blocked, so this is expressly qualified.

## value

PASS

The precision of hidden-variable witnesses is a natural computational invariant: a fixed denominator 2d independent of hidden count and nesting depth turns a continuum supremum into one finite rational grid without approximation. The example proves the factor is globally necessary. This is a motivated exact refinement of interpolation existence, even though formula size may grow exponentially.

The dated certificate retains the supplied scientific assessment, sources and limitations.
