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

# Verification record

For the claim of exactly fourteen components of the closure of \(\sigma_{-3}(\mathbb N)\), the accompanying `verify_components.py` is executable by `python3 verify_components.py` and requires no external packages. It constructs all twenty-four rational candidate intervals, bounds \(T\) using exactly one hundred terms and integral-test tails, proves the needed four prime-exponent cutoff inequalities with rational arithmetic, proves the five exceptional prime-tail comparisons, groups all candidate intervals using interval bounds, checks the fourteen exact endpoint pairs and density weights, and asserts their total density equals one.

The successful terminal indicator is `CERTIFICATE_OK ordinary_sigma_minus_three components=14 candidates=24 tail_threshold=11 rational_density_total=1`.

The unbounded parts of the proof are mathematical: Nagura's prime-interval theorem, Sanna's greedy tail interval lemma, and Chinese-remainder limiting densities. They are not certified by a finite program or a truncated numerical search. The matched finite rows are complete for the stated symbolic reduction, not a bound on direct enumeration of integers. The exact component classification and density computations have undergone self-review; independent audit has not been performed.
