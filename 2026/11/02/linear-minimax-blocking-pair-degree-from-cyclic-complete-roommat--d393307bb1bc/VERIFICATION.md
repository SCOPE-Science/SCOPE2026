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

The two included standalone sources require Python 3 standard library and a C++17 compiler. Run `python3 verify.py` to construct every cyclic instance for \(2\le n\le10\), enumerate **all partial matchings**, compute blocking degrees directly, compare the exact minima to \(\lfloor(n-1)/2floor\), and verify the circular-triple lemma for each distinct triple. The run reported matching counts \(2,4,10,26,76,232,764,2620,9496\) for these respective orders; every assertion passed.

Compile `census.cpp` as `c++ -O2 -std=c++17 census.cpp -o census` and run `./census`. The program enumerates every symmetric acceptable graph, each agent's strict ordering of their neighbors, and every partial matching for \(1\le n\le5\), using integer ranks and exact logical comparisons. It reported total profile counts \(1,2,18,2634,15199074\) and counts requiring maximum degree at least two \(0,0,0,0,7752\). The code verifies no profile among these has optimum greater than two.

These finite checks support the exact five-agent global threshold and stress-test the explicit family, but only the written argument proves the all-order formula and asymptotic conclusion. Independent human or external scientific validation has not been performed.
