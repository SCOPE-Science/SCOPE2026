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

Flow conservation makes the three off-diagonal high-minus-low differences equal to a common nonzero integer t. After orientation and ordering the low entries, the six off-diagonal positions have only five possible low/high interleavings; inserting the three loops gives exactly 420 length-relevant shape classes, with 72 labeled rankings per shape. For fixed t, adjacent strict inequalities are lower-bound difference constraints in six base variables; longest-path closure gives the componentwise least nonnegative feasible solution and hence the minimum positive linear length objective. An independent exact-integer replay over all 420 shapes and t=1,...,28 reproduced maximum 86 and a unique worst shape. Since total length is at least 3t, t>=29 cannot improve a <=86 witness. For the unique worst shape, three distinct loops between b+t and c+t force c-b>=4 and c<b+t forces t>=5, giving the sharp minimum values 0,5,6,10,11,12,13,14,15 with sum 86. The displayed balanced matrix attains them and its strongly connected balanced directed support has an Euler circuit, producing a circular realizing string of length 86.

## originality

PASS

The founding ternary window-two DNA-profile work defines the shortest-realizing-length problem and gives the 30240 feasible-ranking base repository plus coarse representative-size bounds; later work improves constructions and studies enumeration/structure. None of the inspected material supplies the exact worst shortest length 86, the unique length-relevant extremal shape, or the exact 72-ranking multiplicity. The submitted result adds a finite but exhaustive 420-shape optimization with an independent analytic lower proof for the unique extremal shape.

## value

PASS

Shortest realization is an explicitly motivated storage-cost invariant in the base ternary window-two rank-modulation model. The exact worst case and maximizer multiplicity close the complete finite base instance and provide a reusable quotient-shape method rather than an arbitrary census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
