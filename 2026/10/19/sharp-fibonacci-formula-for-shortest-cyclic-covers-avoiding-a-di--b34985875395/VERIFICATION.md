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

# Verification of the cyclic-cover theorem

Run `python3 verify.py` with the Python standard library. The program independently enumerates all required forbidden-`110` length-\(k\) binary words for \(3\le k\le16\), computes degree imbalances in the exact mandatory de Bruijn multigraph, explicitly builds balancing walks, obtains an Euler circuit with Hierholzer's algorithm, and verifies that the resulting circular word contains every required factor at the claimed length.

Expected output: `VERIFY_OK cyclic_hosts_k=3..16 exact_coverage_and_length`.

For \(k=3,\ldots,10\), the ordered pairs (required factors, shortest cyclic length) are (7,8), (12,16), (20,29), (33,53), (54,94), (88,166), (143,290), (232,504). All larger cases use the same exact construction and asserted formula. The proof in `RESULT.md` is needed for every \(k\ge3\), for lower bound optimality, and for all parameter quantifiers. No independent external audit or formal proof verification is claimed.
