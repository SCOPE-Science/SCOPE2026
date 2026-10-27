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

# Executed finite checks

From the folder containing this file and `verify.py`, execute `python verify.py` with standard Python 3. The test completed with:

`VERIFY_OK: 16 exact four-cell updates; 80 independent finite image-count comparisons; 20782 exact cyclic lift comparisons; entropy-asymptotic ratio at t=30 = 0.99999536`

The program checks all length-four input patterns against the bond-defect dynamics, independently determinizes the \(t\)-fold local preimage transducer for \(0\le t\le4\) and compares length counts through \(n=15\), checks all qualifying periodic-word inversions for ring sizes \(1\) through \(13\), and checks the algebraic entropy asymptotic numerically. The infinite-time forbidden-word classification, exact generating function and asymptotic constant are proved in `RESULT.md`; finite tests alone do not establish them.
