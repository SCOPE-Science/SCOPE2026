---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

For every angular support direction conjugate the cyclic Hermitian part to a weighted real cycle with total phase n theta. Matching expansion gives D_k=q_n-(a^2+b^2-1)q_(n-2)+(a^2-1)(b^2-1)q_(k-2)q_(n-k-2)-2ab cos(n theta). Chebyshev recurrence implies D_(k+1)-D_k=Delta*q_(n-2k-2). A principal unit-weight path of n-k vertices bounds lambda_max(H_k) strictly above the largest zero of q_m, so q_m>0 above the edge. Root interlacing/sign of the determinant difference yields strict support-function ordering at every angle, uniform by angular compactness. Independent symbolic characteristic polynomials n=4,5,6 and numerical support eigenvalues n=6,8 corroborated; proof is all n.

## originality

PASS

The 2023 Chien--Kirkland--Li--Nakazato study gives numerical-range rearrangement tools and global maximizing patterns only for n<=6, conjecturing full-n maxima. The 2012 Chang--Wang work concerns global numerical-radius maximizers; neither inspected source establishes the all-n full-set two-defect nested chains and mixed-sign reversal. The closely titled 2015 Chien et al. determinantal original could overlap; OA/arXiv attempts failed, Oxford institutional tool reported VPN disconnected, and the risk is explicitly retained.

## value

PASS

Exact strict set inclusion, stronger than numerical-radius inequalities, classifies every separation of two defects for all dimensions and exposes a natural sign-change reversal by spectral polynomial positivity; useful robust example in numerical-range rearrangement geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
