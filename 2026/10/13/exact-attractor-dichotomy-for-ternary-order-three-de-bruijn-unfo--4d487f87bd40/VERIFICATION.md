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

# Reproduction and scope

The complete finite computation is in `verify.cpp`. Compile with `g++ -O3 -std=c++17 -Wall -Wextra -pedantic verify.cpp -o verify`, then run `./verify`. It prints exact totals and `VERIFY_OK`, and fails with nonzero status if any expected count or rank bound disagrees.

The generator walks each directed edge representing a ternary triple exactly once, fixes the unique `000` edge first, requires return to vertex `00`, and thereby enumerates cyclic words once each. For every word and cut, it tests the unique possible nine-position set; failed cuts trigger an exhaustive search through all 275 ten-position sets that hit every three-factor window. Bitsets test all three one-letter and nine two-letter factors. A combinatorial lemma in `RESULT.md` shows these tests also guarantee coverage of every longer factor. Thus the finite search is exhaustive for the stated domain rather than extrapolation from samples.

An explicit cycle with no nine-optimal cut is `000100212012101112221102022`. For cut zero, the positions `0,3,5,8,11,14,17,20,23,26` form a ten-position full attractor; all its nonempty factor lengths were separately checked directly. The standalone code includes its own expected-result assertions but does not depend on output files or private data. This is reproducible finite evidence, not an independent audit and not a theorem for larger parameter values.
