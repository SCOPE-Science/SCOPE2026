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

# Reproduction and scope

The result has a full mathematical proof in `RESULT.md`. Use `python artifacts/check.py`; this requires Python >=3.9 and SymPy. The checker independently simulates every initial configuration on the \(2\)-row ladders from \(n=2\) to \(n=9\), for 349,520 configurations in total. It cross-checks the eventual cascade with the three obstruction types and with a separate dynamic transfer count. It then computes the rational symbolic matrix inverse and checks equality with the claimed bivariate generating function as an exact identity. It verifies the minimal seed formulas through \(n=25\) and derives the pole coefficient algebraically.

The full program returned `VERIFY_OK` in the packaged environment. Finite cases support but cannot replace proofs for all \(n\); the symbolic check and proof are the evidence for the global identity, while coefficientwise Laurent extraction and a dominant-pole argument establish the infinite families and asymptotics. Independent audit has not been performed.
