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

The included `artifacts/verify.py` performs an independent finite replay of the combinatorial side of the claim.

It enumerates every labeled \(3\)-uniform hypergraph on \([n]\) for \(0\le n\le6\), detects a tetrahedron by checking each four-set for all four constituent triples, and verifies the exact tetrahedron-free counts

\[
1,1,1,2,15,768,477965.
\]

It also verifies the corresponding extremal edge counts

\[
0,0,0,1,3,7,14,
\]

and checks that the published rational upper bound

\[
\frac{312372062889819}{560000000000000}
\]

lies strictly between \(5/9\) and \(0.557808\). A successful replay prints `VERIFY_OK`.

This finite computation does not prove the asymptotic Nagle–Rödl theorem; that step is literature-backed and separately audited in the review.
