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

# Exact finite verification

Run `python3 verify.py` and compare its output to `expected_output.txt`; `VERIFY_OK` is required. The script uses only Python's standard library. It reconstructs the full first-jet isomorphism, enumerates the 2187 incident maps and their 18 projective orbits, and computes geometric smoothness for representatives by fully reducing partial-derivative ideals in three affine charts using Buchberger over \(\mathbf F_2\). The table `orbit_table.tsv` fixes all 18 coefficient masks and all outcomes. In every case the criterion inferred from tangent multiplicity and concurrency is checked against the ideal computation.

Run `python3 crosscheck_sympy.py` using SymPy; expect `INDEPENDENT_GROEBNER_CROSSCHECK_18_ORBITS_OK`. This recomputes the affine gradient ideal tests independently from the coefficient masks and confirms each of the 18 truth values.

Mathematical scope: the three-chart unit-ideal criterion is over the algebraic closure, by the Nullstellensatz. No inference from a fixed finite extension is used. The scripts provide exact reproducible calculations, not independent review; one source-data overlap risk remains because all smooth binary genus-six quintic equations occur in an earlier census.
