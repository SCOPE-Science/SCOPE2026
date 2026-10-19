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

The analytic Fourier-fiber proof covers every integer \(n\ge2\) and every unordered three-element support in the specified group. The complex nullity follows from explicit \(2\times2\) matrix blocks and congruence counting. The independent finite checker `check_q.py` computes group products, convolution matrices, and modular ranks directly. Its completed run passed 1,081 modular comparisons and checked the complete predicted arithmetic census for every \(2\le n\le24\), printing `PASS 1081` and `CENSUS_PASS`.

Finite-rank checks are over \(\mathbb F_{1000000007}\) and are not a substitute for the characteristic-zero proof. All-support enumeration to \(n=24\) tests the arithmetic formula but does not establish the infinite statement. Source inspections support a best-knowledge originality assessment; no independent audit or exhaustive publication-priority certification was performed.
