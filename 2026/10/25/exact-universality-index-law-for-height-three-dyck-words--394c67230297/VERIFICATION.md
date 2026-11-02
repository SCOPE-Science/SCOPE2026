---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The binary greedy arch factorization counts the subsequence-universality index; pairing adjacent unlike symbols greedily with a used-bit flag is equivalent to each completed minimal two-symbol arch. The 12 reachable states (height h=0..3,last letter b,paired flag m), initial first opening step and acceptance at h=0 yield a rational transfer matrix G(x,u). Its determinant and bordered numerator have x-degree at most 12; clearing the proposed denominator (x-degree 8) gives a difference numerator of degree <=20. The attached exact symbolic check of every coefficient through x^20 is therefore an ALL-DEGREE identity certificate for F(z,u)=[1-4uz+(u+4u²)z²+(u-3u²)z³]/[(1-uz)((1-2uz)^2-u²z³)], not only an experimental interpolation. Independently generated height<=3 Dyck words through n=8 and matched complete arch histograms, including n=4:5u²+7u³+u⁴. At u=1, F(z,1)=(1-2z)/(1-3z+z²); its simple dominant pole and implicit differentiation of (1-2uz)^2-u²z³ give mean slope 2/sqrt(5), with variance O(n) proving convergence in probability. The seven-blob Git tree matches its assigned SHA. Fresh independent symbolic reconstruction of the 12-state polynomial-weight transfer checked all coefficients of D(z,u)F(z,u)-N(z,u) through z^10 (equivalently x^20), sufficient by the stated degree bound; the n=8 histogram was u^8+127u^7+432u^6+50u^5 (610 paths).

## originality

PASS

Best-of-knowledge PASS for the exact height-three Dyck arch-index distribution and limit law. The general arch mechanism and unrestricted binary-word distribution are explicitly prior; inspected Dyck pattern and height papers treat different classes/statistics. No stronger theorem or table established actual coverage.

## value

PASS

Height-three Dyck excursions are a natural first finite-height constrained Catalan language with nontrivial arch statistics; an exact all-length bivariate distribution and non-obvious typical index 2n/sqrt(5) are motivated combinatorial invariants beyond the existing extremal statements.

The dated certificate retains the supplied scientific assessment, sources and limitations.
