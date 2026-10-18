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

Compile `rewiring_verifier.cpp` with a C++17 compiler, for example:

```sh
g++ -O3 -std=c++17 rewiring_verifier.cpp -o verify
./verify
```

The program enumerates every connected bipartite incidence matrix with positive guild sizes and combined order at most nine, every connected-output checkerboard switch, and integer pair-union difference coefficients. For every difference polynomial, it calculates coefficients of \((1+x)^nP(x/(1+x))\) exactly and checks they have a common sign. Its independent recurrence for connected labeled bipartite graphs reproduces the number enumerated in every cell.

The largest cells \((m,n)=(4,5)\) and \((5,4)\) contain exactly \(636331\) connected labeled incidence matrices each and \(5246640\) valid directed switches each. The witness check independently enumerates every pollinator-failure subset at \(q=1/4\) and \(3/4\); the variance differences are \(-9/256\) and \(9/256\), consistent with the polynomial formula. The executable ends with `ALL_EXACT_CHECKS_PASSED`.

This is a complete finite lower-bound certificate; it is not proof of any classification beyond nine total species. The ten-species witness is an exact algebraic construction and requires no enumeration of larger networks. The science and bibliographic comparisons have not undergone independent audit.
