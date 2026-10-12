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
Reproduce finite regression checks by running `python3 artifacts/check.py` from the package root using Python 3, with no third-party dependencies. The checker verifies the two rational quadratic constructions over \(3\le d\le300\) and the totient minimization predicted by the number-field threshold over \(3\le d\le2000\). The source of correctness for arbitrary \(d\) is the symbolic argument in `RESULT.md`, not these finite checks.

Independent symbolic Gröbner-basis spot checks using SymPy separately confirmed both opposite lex initial ideals for sample \(3\le d\le15\) in which the rational constructions exist; SymPy is **not** a package dependency and those samples are not a proof.

The polynomial obstruction is checked in characteristic zero only. There is no claim of automatic extension to characteristic \(p\) where inseparability can invalidate the double-root argument.
