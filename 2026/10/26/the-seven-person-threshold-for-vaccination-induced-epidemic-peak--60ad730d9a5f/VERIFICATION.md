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

# Verification of the finite network theorem

The exact proof is in RESULT.md. The universal six-person assertion is proved analytically using shortest-path layers and a counting obstruction, not by graph sampling.

The self-contained `verify.py` uses only Python's standard library. Its `seven_vertex_census` function checks all 128 subsets of the seven specified directed contacts, validates the exact count table, constructs the signed polynomial coefficients as integers and locates the unique root of the monotone fifth-degree factor. The verified coefficient list, in increasing power order, is `[0, 0, -1, 0, 0, 3, -2, 1]`; the numerical root lies between `0.7878336603052378` and `0.7878336603052379`. The same program checked 20,000 pseudorandom directed graphs of sizes two through six with seed 20261023. Those tests are not exhaustive over all directed graphs, and do not replace the analytic universal proof.

Execute `python3 verify.py`; the expected final status line is `VERIFY_OK`. Numerical bracketing is not needed to establish existence and uniqueness: those follow from the derivative sign argument. The full 2007 Floyd–Kay–Shapiro paper was not available for material comparison, and no independent external proof audit has been performed.
