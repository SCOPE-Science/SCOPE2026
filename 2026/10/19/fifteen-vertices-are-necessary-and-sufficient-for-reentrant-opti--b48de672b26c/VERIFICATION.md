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

Reproduce with Python 3.10 or later by installing the packages listed in `requirements.txt` and running `python verify_reentry.py`. The program uses exact integer counts and rational polynomial arithmetic for decisive comparisons; no Monte Carlo sampling or floating-point root-grid conclusions are used. Reproduced tree-shape totals for orders \(2\) to \(14\) are \((1,1,2,3,6,11,23,47,106,235,551,1301,3159)\). The only shapes requiring full root isolation after fixed-sign dominance elimination occur at orders \(13\) and \(14\), in counts \(6\) and \(17\). The \(23\) shapes have \(60\) isolated candidate-comparison root cells; winner regions over their complementary exact-rational open intervals are contiguous.

The \(15\)-vertex witness has a difference quotient with ascending coefficients `[1,-3,1,1,1]`, corresponding to \(q(p)=1-3p+p^2+p^3+p^4\). The complete integer coefficient tests assert that origin \(1\) strictly dominates the other \(13\) origins for every \(p\in(0,1)\). The checker confirms two distinct roots of \(q\) in that interval via rational Sturm isolation. The proof gives an independent analytical root-count argument from strict convexity, endpoint positivity, and a negative midpoint. It verifies exact global winner identities at representative rational points.

The program does not prove the correctness of its external nonisomorphic-tree enumeration library, does not analyze general graphs or larger trees, and does not constitute independent verification. Literature inspection is reported separately; a 2026 related article was unavailable in full.
