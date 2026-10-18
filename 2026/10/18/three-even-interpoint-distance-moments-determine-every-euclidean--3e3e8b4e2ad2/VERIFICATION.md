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
# Verification

Execute `python3 CHECKER.py` with Python 3 and no additional dependencies. The program evaluates both sides of the moment identities as rational polynomials in the three Gram entries, on a complete unisolvent integer grid of \(8\), \(27\), and \(64\) nodes for degrees \(1\), \(2\), and \(3\). Because the exact separately bounded polynomial degrees follow from the multinomial expansion, this finite check establishes those global algebraic identities, not merely numerical agreement on examples. It also checks the exact two-moment ambiguity and cubic-instability construction.

The remaining proof obligations—validity of barycentric integration for a nondegenerate triangle, uniqueness of the squared-side cubic, Rouché root-cluster counting and the sharp exponent—are treated explicitly in `RESULT.md`. The checker is not claimed to certify those arguments or priority. The 2026 motivating source was checked from its accessible public statement, not its unavailable full text; no independent audit has been performed.
