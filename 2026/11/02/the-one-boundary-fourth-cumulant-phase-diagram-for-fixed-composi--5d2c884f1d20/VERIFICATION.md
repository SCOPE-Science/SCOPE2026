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

# Reproducibility

Execute `python3 verify_run_cumulant.py --symbolic` under Python 3.10 or newer with SymPy installed. The ordinary checks use only Python standard-library rational and integer operations; run `python3 verify_run_cumulant.py` if SymPy is unavailable.

The checker independently enumerates binary arrangements and run counts, compares with the binomial-composition exact distribution, and evaluates the fourth cumulant from rational raw moments. It checks every pair of positive class counts for lengths from \(2\) through \(100\), all sign rows through length \(1000\), and both transformed-cubic endpoint coefficients through length \(499\). The symbolic phase constructs the cluster formula for factorial moments through order four and verifies the generic cumulant identity and four transformed coefficients by polynomial cancellation.

The infinite sign classification is proved mathematically using Descartes' sign rule, endpoint factorizations and a finite check for lengths \(4\)–\(9\). Exhaustive word enumeration is not presented as proof for unbounded lengths. Uninspected classical primary texts limit certainty about absolute novelty. Independent validation has not occurred.
