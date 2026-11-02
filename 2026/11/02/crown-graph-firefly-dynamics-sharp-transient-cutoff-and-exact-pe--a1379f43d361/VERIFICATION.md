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

# Verification of the mathematical result

`verify_support.py` is an exact, standalone Python 3 standard-library certificate for the nine-type, three-level quotient. It enumerates all 19,683 capped vectors, follows each deterministic orbit until first repetition, computes the full labelled period from the permutation of occupied types on each recurrent quotient orbit, asserts 33 recurrent quotient cycles and the period classes, determines the feasible sharp transient times, and checks the complete basin polynomial coefficients. This supports the claims at all graph sizes because the nine-type quotient is exact independently of pair multiplicities.

`verify_egf.py` checks the identity for the nineteen-term period-four generating polynomial and both recurrent-state polynomials as exact equalities in the integer polynomial ring in two indeterminates, with no coefficient truncation and no numerical approximations.

`verify_vertices.cpp` implements the update rule directly on individual labelled vertices and independently enumerates all 5,380,830 configurations for the six sizes from two through seven matched pairs. It verifies basin sizes, recurrent-state counts and maximal entry times. C++17 compilation uses `g++ -O2 -std=c++17 -Wall -Wextra verify_vertices.cpp -o verify_vertices`, followed by `./verify_vertices`.

`verify_support_output.txt`, `verify_egf_output.txt`, and `verify_vertices_output.txt` contain the actual output from the included source programs. A successful output alone does not replace the definitions and reasoning in the proof; source code and its exact finite enumeration are also available. These checks establish finite-state claims within the stated model, not independent authorship or a general theorem for unrelated update maps.
