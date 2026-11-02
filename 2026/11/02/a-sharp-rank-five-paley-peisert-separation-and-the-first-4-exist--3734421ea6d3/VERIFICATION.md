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

# Verification record

The encoded field model uses base-\(p\) polynomial coefficients and the monic irreducible moduli listed in `RESULT.md`. Every chosen multiplicative generator is checked primitive; the Python implementation also checks irreducibility by trial division, while the C++ verifier uses independent quartic-character arithmetic and checks the field Frobenius identity and generator order.

The Python verification script, which uses only the standard library, checks four explicit obstructions for orders \(9,49,81,121\) and exact symmetry-reduced four-extension minima at orders \(121,361\). It computes both order-\(121\) three-extension minima. The C++17 program independently enumerates all \(280840\) four-subsets containing zero for both order-\(121\) graphs and all \(257044\) Peisert order-\(361\) four-tuple orbit representatives. It computes all sixteen adjacency masks for each tuple, checks degree and common-neighbor parameters, and independently verifies the 3-e.c. order-121 comparison.

Observed completed runs are recorded in `python_output.txt` and `independent_output.txt`. Both reproduce the positive Peisert order-\(361\) minimum \(10\) and the order-\(121\) Paley minimum \(2\). The C++ order-\(121\) Peisert enumeration identifies \(400\) failing four-sets containing zero and confirms the exact missing-all-neighbors tuple \((0,1,16,17)\). The mathematical orbit-normalization argument in `RESULT.md` is necessary: finite testing without that coverage argument would not prove a universal statement over all four-subsets.

**Limits:** These exhaustive computations address only the named finite field orders. They do not establish 4-e.c. for every larger Peisert graph. Independent mathematical audit has not been performed. Historical-priority assessment remains qualified because the full 2004 pseudorandomness article was not accessible.
