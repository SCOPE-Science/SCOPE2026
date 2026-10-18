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

Compile `verify.cpp` using `g++ -std=c++17 -O2 verify.cpp -o verify` and execute `./verify`. The standalone enumeration visits all rooted candidates, not a sample; the required incidence mask is exact. For \(k=5\), it confirms that every candidate of length \(5\) through \(23\) fails and exactly eight at length \(24\) succeed, with eight necklaces and four bracelets. The output includes the eight canonical strings, each containing \(00000\) exactly once, and counts of odd-weight five-windows plus duplicated even-weight five-windows. Its smaller-window checks produce \(4,7,16\) for orders \(2,3,4\).

No external solver, network call, or unpublished dependency is needed to reproduce the computation. The computation certifies the finite claims it enumerates, not a general formula for arbitrary window length. Independent review has not been performed.
