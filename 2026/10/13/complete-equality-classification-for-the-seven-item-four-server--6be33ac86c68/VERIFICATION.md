---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Re-derived Hall equivalence for r<=3: each server pair U contains at most two fully supported items. Summing all six pair inequalities gives 3a1+a2<=12; combined with seven items forces excess storage >=5. At equality a1=a3+2a4+2, and disjoint singleton supports force precisely profiles (3,3,1,0),(2,5,0,0). The former consists of one three-subset and star pairs to a fourth server (16 cases); the latter of two singleton items and five pairs with unique allowable multiplicities (30 cases). A NEW independent finite enumeration of all 116280 multisets found 39112 Hall-valid codes, 46 storage-12 optima, S4 orbit sizes 4,6,12,24, and 171360 fully labeled assignments. Both known optimum and equality numbers checked; finite enumeration genuinely exhausts this finite parameter only.

## originality

PASS

Best-of-knowledge: the minimum 12 follows from known general k=3 theory; the 46 equality optima, four orbit taxonomy, and fully labeled census are additional exact finite structure. The inspected Brualdi et al. theorem covers n=m+1,m+2, whereas here n=m+3. Possible inaccessible finite tabulation remains a risk.

## value

PASS

This is a complete equality classification immediately beyond the previously classified n=m+1,m+2 structural range, for a natural minimal storage batch-code parameter. Knowing all optimizers rather than only their cost is useful for design and uniqueness questions, and cannot be read off directly from the optimization formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
