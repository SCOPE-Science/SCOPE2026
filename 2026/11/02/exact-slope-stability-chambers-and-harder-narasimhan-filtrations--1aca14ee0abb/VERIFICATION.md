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

# Verification scope

The standalone executable `verify.py` uses only Python's standard library and exact fractions. Execute `python3 verify.py` to check all included finite cases. Its observed success line was `VERIFY_OK 84100 slope comparisons; 16 exact evaluation factorizations`.

The script tests rank and first-Chern-class additivity for the two bundle extensions; computes the exact rational three slopes in both directions for \(1\le a,b\le10\) and \(1\le\alpha,\beta\le29\); verifies strict exterior inequalities and wall equalities; and checks both tensor-product evaluation factorizations with rational Gaussian elimination at one explicit point for \(1\le a,b\le4\).

The finite checks do not establish global exactness, semistability, interior stability, infinite parameter range, or publication priority. The mathematical proof in `RESULT.md` supplies the first four via universal evaluation sequences, the cited central-polarization stability theorem, and linearity on the ample cone. Historical novelty is not externally certified.
