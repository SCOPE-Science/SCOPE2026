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

# Verification of the ladder perfect-matching shattering theorem

The package contains `verify.py`, `certificate.json` and `verification_output.txt`. With Python 3.9 or later and no external dependencies, invoke `python3 verify.py` in the directory containing these files. It constructs every perfect matching of each two-row ladder from one through five columns by two independently organized methods: recursive interval tilings and recursive exact graph matchings. It calculates VC dimension through exhaustive trace tests and Littlestone dimension through the exact recursion on restricted concept subsets.

For the five-column ladder, `certificate.json` lists the eight perfect matchings, a complete depth-three query tree, the eight leaf witnesses and every edge's incidence frequency. The verifier checks each of the 24 edge-answer constraints along those root-to-leaf paths, uniqueness of all eight witnesses, the static two-coordinate certificate, and uniqueness of the four-of-eight balanced query. The saved transcript ends with `ALL_MATCHING_SHATTERING_CHECKS_PASS`.

The verifier also constructs connected bridge-chain graphs for one, two and three blocks, checks that the bridge edges appear in no perfect matching, verifies product counts and connected graph degree/bipartiteness. The unrestricted positive-integer statement is proven separately by a parity argument on bridge cuts and independent block choices, not by finite extrapolation. Planarity is supplied by the explicit geometric row-chain construction. The code does not test historical publication priority, prove a formula for larger ladders, or perform independent external validation.
