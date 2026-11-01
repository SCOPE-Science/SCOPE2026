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
# Verification of the matching-defect cyclic dynamics census

The proof is analytic and covers all integers \(n\ge5\), \(1\le k\le\lfloor n/2\rfloor\), \(n-k\ge4\). The separate computations below test the exact six-class count and the full-state identity without extrapolating from finite graph sizes.

Compile and execute the C++17 implementation:

```sh
g++ -O2 -std=c++17 verify_matching_exhaustive.cpp -o verify_matching_exhaustive
./verify_matching_exhaustive
```

The implementation directly inspects neighbors for every vertex at each update, testing the entire labelled state space for every admissible \((n,k)\) up to \(n=11\), alongside the complete-graph control \(k=0\). Its expected successful terminal line is recorded in `verification_matching_exhaustive.txt` as `EXHAUSTIVE_CENSUS_OK cases=36 states=1560978`.

Run the independently formulated Python verifier:

```sh
python3 verify_matching_structure.py
```

The Python program classifies initial configurations by their unique blocked missing edge and, separately, performs direct successor-contact updates. It confirms that predicted structural classes equal actual first-periodic-entry classes and reproduces all six formulas through \(n=10\). The reproduced terminal line in `verification_matching_structure.txt` is `STRUCTURAL_CLASSIFICATION_OK cases=30 states=498096`.

The boundary \(n-k=3\) is outside the new quantitative theorem because exact tripartite results already exist; graphs with only two multipartite shores can support other periods. No infinite-range certificate is inferred from the finite replay. The family-level result depends on the proof's uniqueness of the initial blocker and the explicitly checked disappearance of the second blocker at update two. Independent external validation has not been performed.
