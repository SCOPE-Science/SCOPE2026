---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Every graph edge is exactly a substituted reduction axiom, so paths compose to derivations. For the converse, predecessor sets satisfy inclusion exactly when the corresponding depths are reachable. The modal operation sending each predecessor set at depth r to that at depth r plus one, fixing top and sending every other subset to empty, is well-defined because mutual reachability is shift-invariant. Positive exponents make every generating reduction valid on every subset. Assigning the variable to the depth-zero predecessor set therefore falsifies every non-reachable implication. A fresh finite test on a two-generator family reproduced the predecessor-set inclusion equivalence.

## originality

PASS

The closest pure-necessitation sources inspected use one modal-reduction principle, while the closest arbitrary-family source works over normal modal logic K and proves a finite-model-property theorem rather than an exact consequence relation. No Resultary hit gave the arbitrary-family reachability iff. The assigned converse is a genuine separating Boolean-algebra construction tailored to the reachability preorder, not an instance of the stated prior results.

## value

PASS

The theorem turns joint reasoning with an arbitrary collection of positive modal reductions into an exact graph problem and supplies explicit independence countermodels. That is a natural structural normal form for the fragment, not a small parameter census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
