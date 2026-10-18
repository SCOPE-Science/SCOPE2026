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
# Verification information

The self-contained mathematical argument is in `RESULT.md`. Run `python3 verify.py` using Python 3 with its standard library. It enumerates direct representation candidates for 615 parameter pairs with \(3\le a\le14\) and \(\max(a,8)\le T\le60\), and checks the example \((a,T,Q_T,b_T)=(3,20,1870,95)\). The expected terminal result is `VERIFY_OK cases=615 example_a3_t20_Q1870_b95`.

The finite program checks the obstruction, not the infinitely many cases or the prime number theorem in arithmetic progressions. The derivation of asymptotic optimality follows because every prime \(p\le T\), \(p\equiv-1\pmod a\), is forced into any admissible divisor cover.
