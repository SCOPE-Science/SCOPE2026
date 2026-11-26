---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Intents are all window intersections, so complementing gives all unions of cyclic r-windows. Every included vertex can be covered by one such window iff the mixed word has all one-runs of length at least r. Marking one of j runs produces n choices for its start and j-fold overcounting; stars and bars gives the stated binomial factor. Independently, the formal series for the positive-index counts divided by n is -log((1-z)^2-z^(r+1)), by summing the marked run-pair contributions over j. This gives the trace polynomial, initial terms and recurrence, including r=1. The state graph is strongly connected with a loop and each allowed labeled cyclic word gives exactly one closed walk, so the trace has leading Perron term with coefficient 1. The root equation gives strict decrease in r and limit 1. The one-run term is n*ell; a second run is possible exactly when n >= 2(r+1). A single run of length r proves strict nesting when the defect increases to r+1. Proper intents have size at most ell, and concentric intervals supply an ell+2-element chain. In the middle regime W_0 intersect W_1 is properly below W_0 and contains W_2 intersect W_0, but adjoining W_2 to W_0 intersect W_1 forces the full join by cardinality; this violates modularity. The two boundaries are the Boolean lattice and the modular n-atom diamond, with the n=2 coincidence accounted for. A separately written checker matches the complete intent families, recurrence, formula, crossover and monotonicity for n=2..11, checks maximum chain sizes through n=8 and both modularity and distributivity through n=7, and recovers the n=8 count vector.

## originality

PASS

The supported contribution is the explicit classification of this labeled cyclic-window closure lattice, including crossover, strict inverse width recovery, height and modularity/distributivity. The general FCA representation and run-language tools are not original, and no standalone priority is inferred for the trace or run count as a word-enumeration technique. The strongest inspected nearby findings describe different structures or different invariants, not the lattice classification.

## value

PASS

The family comprises canonical translation-invariant interval incidence contexts. Counting and characterizing their closed sets answers which width can be recovered from cardinality and exactly where a second complementary run changes the low-width law. The height bound and modularity witness add order-theoretic information not recovered from cyclic word counts. The result is a full two-parameter classification, not a selected numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
