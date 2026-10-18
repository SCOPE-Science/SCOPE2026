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

# Reproducibility and limits

Compile `verify.cpp` using a C++17 compiler with `g++ -O3 -std=c++17 -Wall -Wextra -Werror verify.cpp -o verify`, then run `./verify`. The test directly builds all two-subset Kneser distances and independently applies the four-obstruction graph-component test.

Every ground graph on \(5\), \(6\), and \(7\) labeled vertices was checked: \(1024\), \(32768\), and \(2097152\) selected-edge masks. The number of resolving cases was \(843\), \(31232\), and \(2056474\), respectively. Another \(150000\) independently seeded samples on \(8\), \(9\), and \(10\) ground vertices were checked at selected-edge probabilities of \(0.05\), \(0.15\), \(0.25\), \(0.50\), and \(0.75\). No disagreements occurred. Detailed output is recorded in `verification_output.txt`.

The C++ verifier is finite evidence for the deterministic equivalence, not an infinite proof or a numerical test of the Poisson theorem. The infinite deterministic and asymptotic claims rely on the explicit arguments in `RESULT.md`. Full-text bibliographic checking is not exhaustive, and independent scientific validation was not performed.
