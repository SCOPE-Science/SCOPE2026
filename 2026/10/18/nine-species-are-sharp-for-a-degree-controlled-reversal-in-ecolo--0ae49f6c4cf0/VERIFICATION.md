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

# Exact checks and scope

Compile the standalone `verify_matching_capacity.cpp` using a C++17 compiler, then run it. Its complete finite search covers all \(2^{ab}\) labeled binary incidence matrices for positive integer guild sizes \(a,b\) with \(a+b\le8\). A finite connectivity test rejects nonconnected matrices; no unexamined isomorphism-class reduction is applied. Within each joint degree signature, every pair of distinct matching-capacity coefficient vectors is checked for componentwise comparability. Identical vectors are tied.

The verifier independently recomputes all 32 possible surviving-pollinator subsets for each witness using exhaustive injective assignments, checks the exact coefficient vectors and expands the difference polynomial. The subset formula proves positivity of the Bernstein basis for all \(0<q<1\); the polynomial factorization proves the unique interior crossing exactly, without numerical root finding. All operations establishing the theorem are integer exact.

The returned finite check reports 70,492 connected labeled matrices and 21 distinct coefficient-vector pairs for the smaller orders. The verifier does not analyze larger graphs, weighted partner capacity, dependent extinctions or actual realized pollination. It is ordinary reproducibility code, not a formal proof assistant or independent external certification.
