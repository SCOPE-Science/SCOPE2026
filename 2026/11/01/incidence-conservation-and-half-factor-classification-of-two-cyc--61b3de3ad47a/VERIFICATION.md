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

The identities in RESULT.md are proved symbolically for all finite simple graphs satisfying equal degree parity along every edge. The exact half-factor condition is necessary and sufficient. The exhaustive computations below check finite instances but are not substitutes for that proof.

Run `python3 verify.py` to check all 1,099 labelled simple base graphs on at most five vertices, of which 154 satisfy the parity condition; this includes 4,909 state checks. Run `c++ -O2 -std=c++17 -Wall -Wextra -pedantic check.cpp -o check && ./check` to exhaust the named line-graph instances, including 2,097,152 configurations on the line graph of the complete graph with seven vertices. Both tests verify that the degree-parity hypothesis cannot simply be omitted, using a three-vertex path.

The recorded outputs in `verify_output.txt` and `check_output.txt` were produced from the embedded source files. The checks do not classify transient lengths or attraction basins of arbitrary line graphs, and do not establish absence of stronger statements in inaccessible literature.
