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

The accompanying `verify.py` uses only the Python standard library. Run `python verify.py` from the directory containing that file. It creates surjective assignment models as bitmasks, computes closure of any selected atoms directly as the intersection of all consistent models, and separately constructs the three proposed implication-premise families. It tests their exact sizes against the associated-Stirling recurrence, evaluates one simultaneous round against the model-based closure, and removes each rule in turn to verify that this displayed rule family is irredundant for simultaneous evaluation.

Exhaustive parameter pairs are \((3,3)\), \((4,3)\), \((5,3)\), and \((4,4)\), involving respectively 512, 4096, 32768, and 65536 subsets. Deterministic additional test sets of 15,255, 15,858, and 15,695 distinct inputs are generated for \((6,3)\), \((5,4)\), and \((5,5)\), respectively. In total the code evaluates **149,720** inputs. For the three-colour exhaustive cases, it additionally checks the explicit lattice cardinality by counting model-closed inputs.

The expected final status is `VERIFY_OK candidate_subsets 149720 exact_surjection_closure=PASS necessary_premises=PASS sharp_one_round_basis=PASS associated_stirling_count=PASS tricolor_lattice_count=PASS`.

No finite computation establishes the theorem for all parameters. The general proof is in `RESULT.md` and does not assume a checker exhausts unbounded parameter space. Mathematical correctness and originality have not received any independent external audit.
