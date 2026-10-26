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

The exact finite verifier is the accompanying `verify.cpp`. Execute `c++ -std=c++17 -O2 verify.cpp -o verify && ./verify` in the directory containing that file. A successful run ends with `VERIFY_OK`. It checks all reduced-row-echelon subspaces at dimensions needed for the first ten maxima, the stated exact passing counts through length nine, all upper-bound exclusions, and the length-ten generator's complete one-deletion incidence histogram \((220,232,60)\).

The finite enumeration is exhaustive because each binary linear subspace has a unique reduced-row-echelon basis and every free entry of every pivot pattern is visited. Distinct deletion outputs of a single codeword count once. The complete computation proves the stated short-length scope only; it is not a formal proof of an infinite-length conjecture.
