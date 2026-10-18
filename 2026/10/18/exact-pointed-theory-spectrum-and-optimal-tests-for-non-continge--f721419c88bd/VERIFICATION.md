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

The explicit finite program `verify.py` uses only Python 3 standard-library functionality. Run `python3 verify.py` from the directory containing that file. It enumerates the successor supports for \(n=0,1,2,3\), checks signatures induced by \(\Delta\chi_a\), confirms support equivalence and sharp information-count lower bounds, and independently evaluates nested formulas on every small pointed star to check terminal flattening and root evaluation.

Expected final line: `ROOTED_STAR_NONCONTINGENCY_ENUMERATION_OK`. The printed counts are \(1,4,48,1984\) pointed theories at \(n=0,1,2,3\), with \(5952\) root/formula truth tables independently compared at \(n=2\). The all-\(n\) theorem is supported by the structural-induction and counting proof in `RESULT.md`; the finite script is neither claimed as an infinite proof nor as independent peer review. The sources were compared for overlap, but no historical uniqueness certification is claimed.
