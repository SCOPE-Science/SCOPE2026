---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

Run `python3 verify.py`. The script enumerates all 2158 realizable saturated seven-support signatures, verifies their exact successor-availability transitions, and checks the assertion that every support signature is monochromatic or all-advancing after at most two updates. It verifies the three-step return of all resulting support signatures. Saturation at two is sufficient because one only needs to know whether a successor color occurs in zero, one, or at least two distinct graph parts.

The script separately checks the finite factor on all support-tuples for three, four, and five parts and runs a vertex-adjacency implementation on ten graph-size vectors, covering 24246 labelled configurations. It verifies the claimed primitive-period counts, the sharp transient bound, and direct agreement with the support sum. The exact output appears in `verification_output.txt`.

The finite-graph enumerations are cross-checks; the all-size proof uses the exact 2158-class quotient. This verification is not independent external certification. The claimed theorem does not extend to arbitrary graph topologies, greater numbers of colors, or asynchronous updates.
