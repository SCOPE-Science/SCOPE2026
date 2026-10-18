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

# Reproducible checks
The included `verify.py` independently builds each graph's adjacency sets, enumerates all candidate subsets and tests the original majority-stability predicate before constructing a symmetry-compressed fractional-covering linear program. The HiGHS solver found optima agreeing with the exact formula for all \(230\) eligible ordered profiles with \(1\le t\le4\), \(1\le s_i\le4\), \(1+\sum_i s_i\le11\), examining \(189012\) labelled subsets in total.

Run `python verify.py` with Python 3, NumPy, and SciPy. The expected first line is `verified_profiles 230 subset_states_enumerated 189012`. Sample computed fractions include \(3/2\) for \((2,2)\), \(5/3\) for \((2,4)\), and \(2\) for \((2,3)\).

The unrestricted result is proven algebraically using the central block-capacity inequalities and the constructive weighted distributions. The finite numerical solver compares floating-point optima at tolerance \(10^{-8}\) and does not certify a theorem for untested orders. Independent audit has not been performed.
