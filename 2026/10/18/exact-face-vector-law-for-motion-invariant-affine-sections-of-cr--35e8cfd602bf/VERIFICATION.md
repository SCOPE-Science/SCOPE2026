---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For generic s>0 write a_i=|u_i| and k=#(a_i<s). Every (j+1)-simplex face of the cross-polytope cuts the plane in a j-face iff its signed vertex heights straddle s. For an m=j+2 coordinate set with q coordinates below s, count 2^m-2^q-1_{q=0}, producing exactly the displayed F_{d,j}(k). The vertex formula 2[binom(d,2)-binom(k,2)] proves d-1 distinct vectors (k=0,1 coincide). Offset intervals have widths a_(k+1)-a_(k), and Gaussian radial independence gives the ratio of half-normal expected order-statistic gaps. For high d, tilting by Gaussian max M_d changes the law by vanishing total variation, as M_d/E M_d ->1 in L1; conditional uniform offset uM_d leaves ell=d-k=d^{1-u²+o_P(1)}, and first-order faces f_j ~ [2^(j+1)/(j+1)!] ell d^(j+1). Simultaneous fixed-rank exponent follows. Actual independent exact signed-face enumeration checked 166 (d,k,j) cases for 3<=d<=8; finite checks do not prove the limit.

## originality

PASS

Best-of-knowledge: targeted published finding search and primary-source theorem comparison did not identify a prior result implying the entire final claim; known components are explicitly credited, not counted as novel. A complete all-dimensional invariant-affine-section face-vector distribution and common high-dimensional exponent, rather than only expected face count or section volume. Unindexed-equivalent risk retained.

## value

PASS

Motion-invariant affine sections differ essentially from central section laws: their actual random offset governs how many cross-polytope vertices lie above the plane. Explicit positive probabilities for all d-1 attainable face-vectors and a shared random exponent across all fixed ranks provide a natural complete classification and nontrivial geometric-probability limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
