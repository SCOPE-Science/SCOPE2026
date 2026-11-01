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

PASS: Reconstructed the classification of nonletter Lyndon factors by exactly one, two or three 1s in w=0^a1 0^b1 0^c1 0^d. One-1 factors are 0^i1 (i>0); two-1 factors obey strict first run longer than middle; three-1 factors have initial run longer than both later runs, or the precisely resolved tie i=b>c. No duplicate two-one factors arise from the two adjacent pairs. The m=0 word 111 is handled separately. Summing positive parts and the indicator gives equation (1); rational gap summation gives the stated generating function. Case splits on the largest run prove the unique maximum 3m+2 and gap 3 at m>=4; Dirichlet lattice-simplex convergence and six explicit order-cone integrals give first and second limiting moments 19/24 and 37/45, hence 563/2880 variance, with O(1) and O(m) remainders from piecewise-linear Riemann sums. A wholly separate brute rotation checker tested 330 words m<=7 and independent aggregation through m=12, plus maxima m=4..12. These bounded tests corroborate, not prove, the universal statement.

## originality

PASS

PASS qualified: Saari studies Lyndon source words and Fibonacci/Sturmian factors, whereas the claim counts factors in arbitrary non-Lyndon binary sources conditioned on three ones. Glen–Simpson–Smyth 2017 gives unconditional source-word expectation and unconstrained maxima, which cannot determine a conditional fixed-weight individual gap law, exact conditional aggregate, unique conditional extremizer, or its limit moments. No matching theorem was located through actual mathematical-index and bibliographic searches. The known general framework is credited, not claimed; unseen exact fixed-weight formulas remain a genuine priority risk.

## value

PASS

PASS: Distinct Lyndon factors are a standard factor-complexity invariant. Conditioning on exactly three markers gives a natural sparse-composition regime distinct from unrestricted random words. The full formula, rational census, sharp isolated extremum and nondegenerate variance law are structurally useful rather than an arbitrary finite computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
