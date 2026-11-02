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

# Reproduction and verification

The bundled `checker.py` is a standalone Python 3 program using only the standard library. Run it from the extracted package directory with `python3 checker.py`. The verified output is:

```
CORE_FORESTS 153 SUBSETS 129444
SYNTAX_CASE (11, 5, 2048)
ALL_CHECKS_OK
```

For each ordered rooted core-forest through five nodes, it enumerates **all** truth/falsity bit assignments, retains precisely those satisfying positive-classicality implications, and then exhaustively checks **every** subset of signed positive premises for semantic satisfiability versus the forbidden-triple condition. The 153 forests include every parent choice for each new vertex. A separate actual unary-formula-string experiment checks two negation parities, circle nesting, and syntactically distinct circled double-negations for 2,048 premise subsets. These experiments are finite checks; the full theorem is established by the explicit constructive model in RESULT.md, independently of any search bound.

The displayed formula criterion and constructive extension are specific to the minimal evidence-logic valuation clauses and to the unary premise fragment. Earlier work supplies the implication from a single classicality triple to unsatisfiability; the reverse implication and tight global obstruction classification are the assessed contribution. The computational tests do not independently establish originality or historical priority.
