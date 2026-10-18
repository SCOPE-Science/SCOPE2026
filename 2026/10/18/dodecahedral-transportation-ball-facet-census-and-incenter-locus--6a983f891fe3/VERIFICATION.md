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
# Verification of the dodecahedral transportation ball

The calculation uses precisely the edge list \(u_iu_{i+1},u_iv_i,v_iv_{i+2}\), with all indices modulo ten and \(0\le i<10\).

Run the exact exhaustive checker with `g++ -std=c++17 -O3 verify.cpp -o verify && ./verify`. It constructs the graph and enumerates every normalized integral 1-Lipschitz function (14,607,387 candidates), checks all tight-edge subgraph connectivity tests, verifies 3,678,208 extreme potentials and the six edge-incidence counts, and proves the maximal squared centered-normal numerator is 580, realized at exactly the 20 normalized distance profiles. The source code contains assertions for the stated numerical values and prints `ALL EXACT CHECKS PASSED` on success.

Run `python3 verify_rank.py` for a separate standard-library check of distance layers \((1,3,6,6,3,1)\), graph antipodal identities, and the displayed integer 10-by-10 minor determinant of \(-2\). It prints `ALL EXACT RANK CHECKS PASSED` on success. Both programs were executed successfully against their embedded source versions.

Proof/certificate coverage: Every polar extreme potential is integral because the tight-edge graph contains a spanning tree of unit edges. The C++ recursion visits all integers permitted by prior assigned neighbors in a connected vertex order, hence does not discard valid candidates. Connected tight edges are equivalent to maximal rank of tight constraints. The exact Euclidean inradius follows from maximizing centered normal length; the 20 strict maximizers and their rank determine the affine hull of all centers. The computations do **not** furnish any classification for metrics other than the specified graph, or a symbolic closed form for the census.
