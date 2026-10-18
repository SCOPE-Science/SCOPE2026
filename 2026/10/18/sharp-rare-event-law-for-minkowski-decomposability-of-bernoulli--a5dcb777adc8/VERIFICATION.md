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

The self-contained `verify.py` uses exact rational Bernoulli probabilities and exact rational affine ranks for all \(2^{2^n}\) retained subsets in each tested dimension \(n=3,4\). It enumerates full-dimensional Cartesian product splits and singleton coordinate-prism events independently. It also checks the key rate-gap inequalities at five rational values of \(p\). The script was executed from this package's source path and reported `ALL TESTS PASSED`.

The exhaustive checks corroborate small dimensions only. The infinite-dimensional conclusion is proved in `RESULT.md` by the deterministic Boolean-product theorem, independent Bernoulli block probabilities, Bonferroni, rate separation, and a cube-hyperplane count. The script does not certify bibliographic novelty, independent review, or asymptotics by finite enumeration. Run `python verify.py` with Python 3 to reproduce the checks.
