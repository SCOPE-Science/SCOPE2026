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
The code is self-contained C11; a standard C compiler and POSIX `sh` suffice. Execute `sh verify.sh`. `count.c` performs the complete Pfaffian-kernel test; `direct16.c` independently evaluates all geometric Jacobian minors at the \(85\) points of \(\mathbf P^3(\mathbf F_4)\) and \(4369\) points of \(\mathbf P^3(\mathbf F_{16})\). Its finite-field checks alone are not an infinite-field smoothness proof; the degree-two Pfaffian geometric lemma in RESULT.md supplies sufficiency. `orbits.c` generates the full \(\operatorname{GL}_4(\mathbf F_2)\) action from permutations and a transvection, with all eight orbit outputs. The scripts compare all \(40,320\) accepted mask pairs, not only counts. `EXPECTED.txt` records reference totals and orbits.

These are same-investigation computations, not independent human review or external formal certification. The computation and theorem are confined to \(\mathbf F_2\).
