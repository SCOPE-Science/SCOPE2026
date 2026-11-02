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

# Reproducibility of the finite hypercube certificate

The attached `verify_total_hypercubes.cpp` is a self-contained C++17 program. Build using `g++ -O3 -std=c++17 -Wall -Wextra -pedantic verify_total_hypercubes.cpp -o verify_total_hypercubes` and execute `./verify_total_hypercubes`. Its enumerations are exhaustive over the explicitly bounded domains:

- All even-distance pairs in \(Q_4,Q_5,Q_6\) (\(56,240,992\) distinct constraints). Odd-distance pairs are proved automatically separated by every nonendpoint vertex.
- All five-element subsets containing zero in each cube (\(1365,31465,595665\) candidates), with zero total-resolving instances.
- The three explicit six-element witnesses, each tested against every required pair.
- All \(8008\) six-element subsets of \(Q_4\), giving exactly \(1600\) valid bases.
- The complete \(16\cdot24\) translation-permutation automorphism action on eleven representative bases, yielding disjoint orbits of sizes \(32,32,96,96,192,192,192,192,192,192,192\) whose union equals all \(1600\) bases.

Observed final output includes `ALL_CHECKS_PASSED`. This is a complete finite-domain certificate, not an infinite-dimensional proof. The program uses `assert`; do not compile with `-DNDEBUG`. No independent external verification has been performed.
