---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For every n>=3, the code of even-index adjacent pairs (2j,2j+1) plus long-gap pairs (4j+1,4j+4) has floor(n/2)+floor((n-1)/4) distinct words. Their weight-one deletion descendants and distinct weight-two descendants cannot overlap across blocks. For the upper bound take all n-1 weight-one outputs and ceil((n-1)/2) chosen adjacent weight-two outputs covering each adjacent input; every input has >=2 distinct selected outputs. Disjoint descendants force 2|C|<=n-1+ceil((n-1)/2), whose integer floor equals floor((3n-2)/4). Independently checked construction and transversal via raw strings for n=3..55; unrestricted theorem follows from the symbolic argument.

## originality

PASS

The earlier constant-weight deletion code colorings, including optimal colorings on weight-two graphs, do not imply maximum independent set size; the submitted theorem gives the precise all-n packing number and a matching integral two-output dual construction. The general constrained fractional LP bound does not specify the exact all-n formula. No indexed exact same formula in Resultary or inspected primary results.

## value

PASS

Determines a natural error-correcting code capacity uniformly for the first nontrivial constant weight, with explicit all-length matching construction and upper cover. This is not a single arbitrary input parameter, a renaming, or merely optimal coloring; it determines the true maximum packing number for the entire binary weight-two layer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
