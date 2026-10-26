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

The included `VERIFY.py` assembles the entire weighted graph Laplacian for the two-clique complete-bipartite gateway network, evaluates the explicit optimal edge allocation, and checks the resulting second eigenvalue and total edge-conductance budget. It compares feasible unrestricted, asymmetric random conductance allocations against the claimed upper bound. SymPy separately verifies the characteristic polynomial of the invariant four-dimensional quotient, the active-region stationary derivative, and the involution identity that bounds the scalar minimization domain.

The recorded output is in `verification_output.txt`. It reports 189 exact graph-structure numerical comparisons using eigenvalues, 2,430 asymmetric trial allocations, symbolic algebraic identities, and illustrative boundary cases. The numerical tolerance is coded explicitly; finite tests cannot certify the theorem for all integers or prove novelty. The proof for the infinite family is given directly in RESULT.md. The printed output is an execution record, not an independent certificate.

The formula covers integers \(k\ge2\), \(u\ge1\) and real budgets \(B>0\), with all conductances nonnegative. It does not assert uniqueness of unrestricted asymmetric optima. Independent auditing is not performed.
