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

Each edge has 2n−4 other incident edges, so two colours force exactly n−2 of each. Writing the indicator x_ij and row/column sums r_i,c_j gives r_i+c_j−2x_ij=n−2. The row and column equations are (n−3)r_i+T−c_i=(n−1)(n−2) and its transpose. Their difference gives r_i=c_i for n≥3; comparing different i then gives constant r_i unless n=4. The balance equation forces all indicators equal in that case, which violates exact half-balance. At n=4 the witness has row/column degrees 3 at the distinguished index and 1 otherwise, which satisfies all equations. The n=3 and n=5 matrices respectively have adjacent-colour maxima (1,1,1) and (3,3,3); the n=4 witness has maxima (2,2), all checked independently by pairwise edge incidence with /tmp/opencode/frozen_audit_small.py. The cyclic one-factors split evenly into three colours for n≥6: 2 ceil((n−1)/3)≤n−2 follows at n=6,7,8 and propagates by steps of three. An edge's own colour has two fewer incidences counted, so all colours meet the bound. A single colour fails at every n≥3. The frozen verifier was inspected but not executed. The infinite argument does not rely on finite tests.

## originality

PASS

The exact n=3 value is already the cycle result; the three-colour upper bound for n≥6 is already covered by the minimum-degree theorem. The distinct supported content is the all-order two-colour obstruction except at n=4, its explicit odd-degree exception, and closure of the n=5 exact case. Nearby exact index tables concern different families or definitions. The initiating preprint's v1 even-vertex-degree assertion is false under its own definition and does not supply a valid obstruction. This is a bounded comparison, not a historical uniqueness claim.

## value

PASS

The crown is a canonical regular bipartite family obtained by one-factor deletion. The exact index separates a genuine exceptional degree-three case from the rest of the family and answers the two-colour question left open by the general upper bounds. The exception also supplies a concrete counterexample to the initiating v1 preprint's even-vertex-degree sentence. This is useful structural information rather than another proof of the known large-order upper bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
