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
# Verification of the threshold theorem

The verification is a mathematical, fully symbolic reconstruction. At the boundary \(w=n-1\) the weighted metric agrees exactly with the unit path metric and its free space is isometric to \(\ell_1^{n-1}\). For \(0<w<n-1\), every cyclic edge is geodesically essential; its normalized molecule is exposed by prescribing slope \(1\) at that edge and equal normalized slope \(-l_i/\sum_{j\ne i}l_j\) elsewhere. The dual ball is precisely the weighted cube section \(\sum l_i\theta_i=0\), and its vertices are characterized by at least \(n-1\) saturated coordinates. McGregor's characterization converts the presence or absence of a nonsaturated dual vertex into the desired exact numerical-index-one criterion.

The explicit sign patterns for odd \(n\), even \(n\) with \(w>1\), and even \(n\) with \(w<1\) satisfy the hyperplane equation exactly, leave exactly one coordinate interior, and work throughout their specified ranges. At even \(n\), \(w=1\), parity forces the last coordinate to saturate. All regimes and parameter boundaries were checked symbolically. No numerical sampling, symbolic-algebra run, or checker output is represented as a proof.

Scientific limitation: no formula for the numerical index in the nonmaximal regimes, no complex analogue, and no general arbitrary-weight classification. Related published results were inspected; full historical absence cannot be certified.
