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

# Reproducibility and limits

The embedded `verify.py` is a standalone Python 3 program using only the standard library. Invoke `python3 verify.py` from the directory containing that file. It exits unsuccessfully upon a failed assertion and prints a summary only if all checks pass.

The checker directly evaluates base-digit sums, scans greedy complete-alphabet arches, and compares to the independent closed formula for bases 2 through 30 and 91,029 prefix lengths in total. It also checks 58,000 digit-carry relations, including the precise position of the missing symbol, and for 155 short prefixes explicitly enumerates every possible candidate subsequence at the next length to compute the universality index without using the arch count. Power-length instances are checked for all tested feasible exponents.

Reproduced result:

`VERIFY_OK direct_prefixes=91029 carry_relations=58000 brute_subsequence_cases=155 bases=2..30 power_prefixes=checked`

The argument for all integers \(b\ge2\) and all prefix lengths is the symbolic induction in `RESULT.md`, including the case of composite bases and positive valuations \(\nu_b(q)\). Finite tests cannot establish an infinite classification by themselves. Literature comparisons cannot rule out undiscovered identical prior work. Independent external validation has not been performed.
