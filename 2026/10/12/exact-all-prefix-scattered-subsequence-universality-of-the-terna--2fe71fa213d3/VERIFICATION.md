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

Execute `python3 verify.py` using Python 3.9+. The checker reconstructs the four possible aligned 16-letter blocks from the binary digit recurrences, tests all eight possible input masks for a five-arch full-block count, and exhausts the six permissible Thue–Morse triple contexts against all sixteen partial positions. It then independently generates a 24576-letter morphic prefix and checks the difference coding, verifies each prefix formula directly, enumerates ternary subsequences for prefixes of length at most 22, and checks that the discrepancy attains both extremal values.

Expected terminal line:

`VERIFY_OK templates=4 masks=8 triples=6 prefix_count=24576 brute_prefixes=0..22 discrepancy_min=-10 discrepancy_max=6`

The finite-state block and context tables are enough for the symbolic infinite proof. Testing finitely many prefixes alone would not establish an infinite statement. There has been no independent audit.
