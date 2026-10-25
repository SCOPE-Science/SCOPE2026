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

# Verification notes
The claim is proved analytically in `RESULT.md`, through Gaussian projection, three-edge cumulant census, specialized trivariate absolute Gaussian moments, and an explicit rational strict sign bound. The standalone diagnostic `width_moment_checker.py` enumerates and checks 141 connected unlabeled graphs with three to six vertices by directly recomputing Gaussian covariance and joint absolute moments, rather than using the derived graph motif counts in its right-hand expression. It separately compares the triangular prism and \(K_{3,3}\), checks the coefficient \(\delta<0\), and provides one independently seeded Gaussian Monte Carlo sanity check. An example successful run printed: `VERIFY_OK connected_graphs= 141 delta= -0.076857861575 prism_minus_K33_exact= -0.922294338898 simulation= -1.0267011`.

Finite tests cannot certify all-dimensional identities. The nonstandard Gaussian absolute-moment identity is sourced to Nabeya (1952). The radial/angular normalization is sourced to Kabluchko–Litvak–Zaporozhets (2015). The candidate's originality status is based on recorded actual comparisons of those ingredients, Padrol–Pilaud–Poullot (2021), and related geometry/graph-width results; equivalent unindexed Gaussian-statistics formulations cannot be ruled out. No independent audit has been conducted.
