---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

On an n>=4 tree, the sum of effective resistances is (1/n)sum_e b_e/g_e with b_e=k_e(n-k_e). Cauchy-Schwarz yields unique positive optimal g_e=B/S sqrt(b_e/c_e). The pseudoinverse voltage for a chord e_u-e_v is a sum of centered nested cut indicators divided by path conductances; their pairwise inner products min(s_i,s_j)(n-max(s_i,s_j))/n give exactly the displayed Theta_uv mixed-root expression. Trace-inverse on positive connected Laplacians is strictly convex along any nonzero simple-edge conductance perturbation. KKT at the tree-only candidate yields the simultaneous necessary-and-sufficient inequalities p_uv>=Theta_uv with equality included; subthreshold chord admits a budget-preserving improving perturbation. Independently simplified P4 unit-edge threshold 11/3+4/sqrt(3). Script exact-rational calculation inspected; its finite tests not substituted for all-tree argument.

## originality

PASS

Primary evidence and published-record searches support best-of-knowledge originality of the precisely isolated mathematical contribution, not unconditional priority. Evaluated tree-path covariance distinguishes the claimed theorem from generic sensitivity-language aliases, though it is derived from these prior methods. Claim credits generic methods and restricts novelty to a motivated closed-form cut coefficient plus simultaneous all-chord if-and-only-if region. Substantive originality concern: whether this is a routine implicit corollary of published KKT plus classical cut potentials.

## value

PASS

A natural network design question is when a priced spanning tree remains optimal despite optional chords. The theorem gives a complete closed-form all-chord no-entry phase region from tree split sizes and costs, independent of budget, for all trees and heterogeneous prices; it avoids resolving the full convex allocation whenever candidate prices vary. The nested-cut mixed terms make long-path interactions explicit. This remains worthwhile even though the generic KKT method is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
