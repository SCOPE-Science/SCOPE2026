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

The standard-library Python program `verify.py` implements the exact reduced six-class update and an independent direct labelled-graph simulator. Execution returned `VERIFY_OK`; output is recorded in `verify_output.txt`.

The finite exhaustive check visits all \(3^6=729\) saturated initial class-weight profiles, including empty classes, and verifies equality of each occupied initial class at times five and eight. It separately verifies that a reduced configuration satisfies \(F^3(x)=x\) exactly when it is all-rest or meets the published phase-count inequalities. This is exhaustive **because** the proof in `RESULT.md` establishes that all nonempty initial colour classes are dynamically uniform and every threshold-two test is preserved by truncation of class multiplicities at two.

Independent direct simulations iterated 29,169 labelled initial states on eleven different graph sizes. The exact multinomial census and two small-core formulas were also checked, as was an explicit configuration requiring five iterations to reach all rest. These computations corroborate rather than replace the exact quotient proof. The implementation requires Python 3 and no third-party packages.

The work has not been independently audited or independently validated. In particular, this record is not a formal proof assistant certificate and makes no claim of uniqueness in the entire mathematical literature.
