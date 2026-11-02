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

The accompanying `checker.py` uses Python standard-library bit masks to enumerate **every** binary relation on labelled carriers of cardinality \(1,2,3,4\), tests the original three frame axioms, and calculates the modal bundle \(\Diamond\Box X\land\neg\Box X\) directly for every subset \(X\). Its comparison does not assume the claimed terminal-cluster simplification. It reconstructs all nonterminal rows by intersection and singleton-complement formulas and independently groups all frames by their full powerset operator.

Observed pairs (admissible frames, distinct complex operators) are \((1,1)\), \((4,3)\), \((26,22)\), and \((255,229)\); each observed fiber has the predicted Bell cardinality. A separate exact integer recurrence checks \(Q_0,\ldots,Q_7=1,1,3,22,229,3361,71444,2233351\) from the established labelled-preorder values of OEIS A000798.

Run `python3 checker.py` after extracting it verbatim from this package. The expected terminal line is `ALL_CHECKS_OK`.

The proof in `RESULT.md` establishes the claim for all finite labelled cardinalities. Exhaustive computations cover only up to four worlds, and table-driven coefficients beyond four depend on classical preorder enumerations. The result does not establish historical priority, independent validation, correctness for infinite nonterminal cones, or equivalence of pointed models under a fixed valuation.
