---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Reproduction of first-entry layer checks

Run `python3 support_certificate.py` (Python 3.10 or newer, without `-O`). This enumerates all 441 projected states of the two hub colors and two nonempty sets of nonhub colors. It checks the period-one and period-three classification, tests the lifting condition at all three phases of each period-three cycle, and compares all thirteen labelled layer generating functions by exact polynomial coefficient equality. It verifies the maximum entry times for singleton nonhub masks and checks the witnesses for both sharp bounds. A successful run prints `PASS: 441 support states, exact recurrent lifting, all 13 polynomial identities, and sharpness`.

The original `finite_certificate.py` is a supplementary capped-count calculation. For a separate direct finite-size check, compile the original `independent_direct.cpp` with `g++ -O3 -std=c++17 independent_direct.cpp -o check_direct` and run `./check_direct`. It updates individual labelled vertices and compares the full observed first-entry counts on twelve pairs of orders. The original recorded outputs are in `finite_output.txt` and `direct_output.txt`.
