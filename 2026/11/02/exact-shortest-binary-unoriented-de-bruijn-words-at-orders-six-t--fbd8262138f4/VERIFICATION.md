---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

The overlap graph has one labeled edge per reversal class, signed types at nonpalindromic endpoint incidences; any covering word induces a compatible alternating-type edge walk. The mandatory graph has odd counts 8,14,16,30 for n=6..9, and the extra alternating trails must meet the deficient types except for two free endpoints. Thus a shortest-type-path perfect-matching relaxation lower-bounds additional traversals. All 4 finite certificates give integer doubled vertex potentials satisfying each pair and terminal dual inequality with total objective precisely 2*(7,14,19,38). I independently reconstructed the signed graphs and BFS transitions, verified all pair inequalities and the explicit binary upper words contain all reversal classes. This is exhaustive finite certification of exactly four n, conditional on the mathematical trail reduction, not a speculative extrapolation.

## originality

PASS

Burris–Motta–Shipman introduced reversal-class edge graphs, alternating Euler tours, general upper bounds and small-order examples, but the inspected original paper does not give these four exact later shortest linear lengths and matching-dual certificates. Mitchell–Wild treats the opposite maximal cyclic no-repeat orientation problem. Resultary related string results did not provide a dominating exact U(6)..U(9) list. Historical small tables or implicit Chinese-postman computations remain a serious residual risk.

## value

PASS

Determining sharp next four natural minimum lengths extends prior n=4,5 illustrations with exact lower certificates in an unoriented de Bruijn covering problem. Each finite endpoint is a meaningful extremum of a canonical string-design invariant, not an arbitrary word example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
