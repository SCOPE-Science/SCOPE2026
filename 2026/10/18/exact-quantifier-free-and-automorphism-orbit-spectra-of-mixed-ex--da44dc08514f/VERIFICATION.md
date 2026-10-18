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

# Reproduction and limits

Run `python3 verify_mixed.py` with standard-library Python 3. The program independently enumerates all ordered tuples, all coefficient equations defining their quantifier-free types, and the full automorphism group actions. The tested parameter pairs are \((2,1),(2,2),(2,3),(3,1),(3,2)\), where the pair means \((p,k)\). The program compares its enumerated kernel-class and orbit-class counts with the two independently coded closed formulas. The observed final result was `VERIFY_OK independent_tuples=1340 cases=5 full_kernel_equations=PASS full_automorphism_orbits=PASS`.

All-arities and all-primes validity is established by the kernel/epimorphism and upper-triangular-action proof in the mathematical result, not by this finite checker. No formal proof assistant, third-party evaluation, or independent external audit has been performed.
