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
# Reproduction and exact-scope checks

Run `python3 verify.py` with SymPy installed in a directory containing `verify.py`, `entropy_spectrum.csv`, and `rule_catalog.csv`. The verifier was executed on the enclosed three-file bundle and returned:

`VERIFY_OK: 256 exhaustive exact image automata, 19 distinct isolated Perron roots, 2304 independent finite-block comparisons, common irreducible class factors, all saved CSV bytes reproduced`

The source constructs four-state de Bruijn transitions for each of the 256 rules, enumerates all reachable nonempty subsets, computes exact integer characteristic polynomials, and uses exact Sturm real-root counts on disjoint rational intervals. It verifies a shared irreducible Perron polynomial across each class and matches every catalog row against a fresh exact reconstruction. Its separately implemented direct input-block enumeration tests all 256 rules for word lengths from 0 through 8.

The infinite word-growth conclusion uses the proved path-count identity and the Perron–Frobenius argument. The finite enumeration is an exhaustive certificate for the finite 256-rule classification, but the direct finite-length consistency tests by themselves would not establish the asymptotic entropies. No independent external validation has been performed.
