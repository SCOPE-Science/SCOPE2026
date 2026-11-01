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

# Verification procedure

Run `python3 verify_cut_cycles.py` with Python 3.9 or newer. No nonstandard packages, network connection, random seeds from outside the script, prior files, or external tables are needed. The program independently implements the chip-firing transition and the cut-polynomial coefficient calculation, and enumerates all chip configurations inside the rigorously established box \(0\le x_v<2d_v\).

# Checks executed

The recorded execution returned `CUT_CYCLE_ALL_CHECKS_PASSED`. It covered 72 connected graphs (all simple connected isomorphism classes through five vertices and larger structured or seeded connected examples), tested 1,821,396 vertex-level states, evaluated the complete coefficient dictionaries rather than only total counts, checked extreme energies, MAX-CUT multiplicities and palindromicity, matched the rooted-tree recurrence in 21 cases, and compared the path sequence through 15 vertices against the Pell recurrence.

Some independent sample coefficient dictionaries: for the four-vertex path, coefficients at totals 3, 4 and 5 are 1, 3 and 1; for the triangle, coefficients at totals 4 and 5 are 3 and 3. The complete machine-readable execution summary is embedded as `verification_output.txt`.

# Scope of evidence

The finite computation detects errors in the derivation on these graphs but is not a proof for arbitrarily large graph orders. The all-graph statement rests on the graph-Laplacian argument, the exact chip-interval characterization, the cut quotient and the elementary MAX-CUT boundary argument supplied in `RESULT.md`. External audit and separate independent scientific validation have not been performed.
