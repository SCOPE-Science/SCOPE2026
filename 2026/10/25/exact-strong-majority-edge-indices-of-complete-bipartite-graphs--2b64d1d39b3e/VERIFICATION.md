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

# Verification

The self-contained `verify.py` checks the explicit three- and four-colour matrices against all neighbours, including 101 periodic parameter pairs and 99 two-row instances. It prints `VERIFY_OK`. The `exception_checker.cpp` source uses only C++17 and the standard library. Compile with `g++ -std=c++17 -O2 exception_checker.cpp -o exception_checker`, and run `./exception_checker`.

The exhaustive checker reports for \(K_{3,4}\): four canonical first rows and 931 attempted partial row extensions, without any valid complete three-colouring. For \(K_{4,5}\): five canonical first rows and 59228 attempted extensions, also without a completed colouring. The first-row normalisation uses global colour and column permutations; sorting the remaining row patterns uses row permutations; a violated partial degree-colour count cannot decrease on extending the partial array.

Infinite results are proved analytically in RESULT.md. The two exclusions are finite exhaustive arguments whose transparency depends on the included source, not external data. This does not constitute independent audit. The full text of the later August 2026 study was unavailable during originality checking; its reported \(\delta\ge5\) result is credited, while more specific overlap cannot be ruled out.
