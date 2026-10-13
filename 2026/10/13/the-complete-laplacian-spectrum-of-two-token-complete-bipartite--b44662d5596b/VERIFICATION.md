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

# Reproducibility and limits

The `verify.py` program directly generates the token graph using two-element subsets and all allowed base-graph edge replacements. It computes characteristic polynomials with exact integer arithmetic via SymPy and compares them, coefficient for coefficient, against the factored formula. All 36 ordered pairs \(2\le m,n\le7\) passed. Independently, five Laplacian principal cofactors were calculated exactly and compared against the explicit eigenvalue-product spanning-tree formula; all passed. Raw output is in `verification_output.txt`.

Reproduction: Python 3.10+, install `requirements.txt`, then run `python verify.py` with the files in one directory. There are no data downloads, random seeds, or hidden package paths. The finite computations check small and asymmetric cases but cannot prove a statement for all \(m,n\); the uniform block-diagonalization proof in `RESULT.md` is the universal argument. No independent external audit or certification was performed.
