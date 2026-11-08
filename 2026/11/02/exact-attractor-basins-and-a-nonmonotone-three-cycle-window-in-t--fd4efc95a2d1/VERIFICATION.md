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

Cohorts of equal initial color never split; replacing each size by min(size,2) faithfully preserves the threshold at every time. Each shore has 26 nonempty capped profiles and the exhaustive finite quotient has 676 pairs, with exact period/preperiod histogram (145,15,6,171,36,225,6,72) ordered (0,1),(0,3),(0,4),(1,1),(1,4),(2,1),(2,4),(3,1). The actual code constructs a full four-variable integer monomial census and verifies exact polynomial identities for B3 and B4; substitution of e^z-1-z for capped-2 cohorts and z for singletons is an all-a,b exponential generating-function proof, not interpolation from samples. Independently reconstructed 676 signatures and four-variable coefficient identities, and checked all-size moment/existence boundaries. All 676 signatures are covered; initial cohorts cannot split. The theorem does not classify individual fixed-point attraction basins.

## originality

PASS

Classical threshold-contact cyclic automata and general-graph threshold-one CCA are antecedents. Their update/graph hypotheses are inequivalent to simultaneous threshold-two three-color contact on finite bicliques; the infinite regular-tree threshold-two theory likewise cannot determine finite-biclique period counts. Resultary parity-automata four-cycle census concerns a binary parity update, not the three-color contact threshold. No statement checked implies the exact B3/B4 polynomials or the missing three-cycle window; historical 1991 model paper is a residual source risk.

## value

PASS

The exact finite quotient yields all-size attraction probabilities, all possible periods and sharp transient time, and reveals a nonmonotone existence window in a concrete natural contact process. A complete basin census is useful beyond a tiny numerical example because it is valid for all a,b.

The dated certificate retains the supplied scientific assessment, sources and limitations.
