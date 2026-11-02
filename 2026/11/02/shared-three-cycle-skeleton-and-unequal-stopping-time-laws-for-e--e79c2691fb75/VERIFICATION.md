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

# Reproduction and limits

Run `python3 verify.py` in this directory. The script needs only the standard Python library. The expected final line is `TRIANGLE_BOUQUET_EXCITATION_VERIFY_OK`.

The central proof certificate visits every nonempty subset of nine ordered petal types for each of three central colors: 1533 cases per update rule. For each it explicitly updates the center and the microscopic ordered states of all represented types, verifies a three-step equality at the stated sharp global cutoff, and tabulates the first time equality holds. The table is converted to the all-size count by exact integer inclusion–exclusion on supports. The code also verifies equal primitive-three periodic states and one-step actions of the two rules, and the initial catalytic-triangle characterization.

The second checker separately constructs the actual labelled graph and directly updates all initial colorings for one through five triangles, checking 199287 inputs per rule. These finite direct checks are corroboration, not substitutes for the exact support reduction that covers arbitrary sizes.

The proof does not concern larger color alphabets, thresholds or non-triangular petals. Literary comparison is not proof of universal uniqueness; historical unindexed equivalents remain a possible originality risk. Independent scientific validation has not been performed.
