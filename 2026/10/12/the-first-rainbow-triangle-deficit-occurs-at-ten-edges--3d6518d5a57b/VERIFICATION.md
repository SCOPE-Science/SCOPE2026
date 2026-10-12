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

Compile and execute the included `verify.cpp` as `g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify.cpp -o verify && ./verify`. Its actual recorded stdout is in `verification.log`.

The program iterates all unlabeled *candidate ranges* by using **labeled** graph bitmasks with ten or eleven edges for each of the vertex orders three through seven. It tests exactly 709801 labeled profiles, verifying that having at least eight ordinary triangles with ten edges, or nine with eleven edges, forces a \(K_5\). It separately enumerates all 59049 three-color assignments to the complete five-vertex graph and verifies that its maximum number of rainbow triangles is seven, then checks twelve explicit construction profiles.

The independently implemented `verify_atlas.py`, using NetworkX `graph_atlas_g` on all graphs up to seven vertices, confirmed maximal triangle counts seven and eight, respectively, for the no-\(K_5\) ten- and eleven-edge cases. This external-package test is corroboration, not a substitute for the included complete labeled census or the structural reduction.

The proof that high-triangle candidates with at most eleven edges reduce to at most seven vertices is given in `RESULT.md`. The conclusion is exact only for budgets up to eleven; computation alone would not prove a bound for arbitrarily many vertices. All integer counts are exact and the file hashes in the enclosing package enable byte-exact replay. An independent audit has not been performed.
