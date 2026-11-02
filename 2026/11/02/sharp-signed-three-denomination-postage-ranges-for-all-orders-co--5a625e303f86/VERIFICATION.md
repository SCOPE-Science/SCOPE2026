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

The proof is self-contained in `RESULT.md`; the code is a finite regression test, not an infinite proof. Run `python verify.py` in a standard Python 3 installation. The verifier exhaustively constructs the full three-element \(h\)-fold sumset for each even \(b\) from \(2\) to \(100\), and independently checks the endpoint formulas and residue-class coverage. It tests \(T=9b^2-3\) and the omission of \(T+1\) from the exhibited basis. Passing these tests is not an independent scientific audit and cannot resolve priority uncertainty.
