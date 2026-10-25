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

# Verification
The self-contained `verify_shortcut.py` enumerates every directed arc subset by direct source/target-degree and cycle tests. For all 35 pairs \(4\le n\le10\), \(2\le k<n\), it compares the resulting face sets to the proof's independently generated forbidden-pattern criterion, computes the complete reduced mod-two Betti vectors, and checks counts of nonempty simplices.

For every case with \(k\ge3\), the program also generates the claimed descending-cardinality free-face pairs, checks each pair is currently incident to a unique maximal coface and therefore constitutes a legal elementary collapse, then verifies that the remaining faces are exactly the unchorded directed cycle's boundary. The actual program run examined 17,349 nonempty simplices and 1,291 elementary collapse pairs. The recorded output is included as `verification_output.txt`, ending in `VERIFY_OK`; reproduce with `python3 verify_shortcut.py`.

The mathematical result for arbitrary parameters is established by the explicit link, relative collapse and nullhomotopic cone-attachment proof in `RESULT.md`, not by finite enumeration. The program does not verify novelty, independent certification or all infinite parameter values.
