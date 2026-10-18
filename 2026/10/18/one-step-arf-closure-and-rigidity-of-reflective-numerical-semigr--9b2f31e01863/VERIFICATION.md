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
# Reproduction and mathematical scope

Run `python3 verify_arf.py` with standard Python 3. The verifier generates the reflective semigroup for each admissible genus \(1\leq g\leq90\) and multiplicity \(2\leq a\leq g+1\) with \(a\nmid g\), using the generators of Shor's classification. It then checks the exact gap formula, computes all Arf consequences through the conductor using a separate saturation routine, compares the result with the claimed closure, and counts the added elements. For \(g\leq35\) it also evaluates the full ordered-triple operator directly rather than relying on the equivalent two-variable criterion.

Recorded actual output of the packaged verifier:

```
PASS cases=3760, strict_closures=3626, added_gaps=9545, original_gap_checks=229753, direct_triple_cases=534, max_genus=90
```

Finite checks detect numerical mistakes in the formulas and constructions but do not establish the theorem for unbounded parameters. The proof in RESULT.md derives the general closure from the published reflective gap characterization. No independent audit or external theorem-prover certification has been performed.
