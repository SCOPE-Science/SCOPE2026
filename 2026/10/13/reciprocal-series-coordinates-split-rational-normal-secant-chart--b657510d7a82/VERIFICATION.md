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

# Verification notes

The formal proof checks the matrix and determinantal ideals in `RESULT.md`, not just numerical ranks. Independent of the symbolic proof, `checker.py` performs deterministic integer specializations and reconstructs the inverse series. Running `python3 checker.py` in the directory containing the embedded files reproduces `checker_output.txt`, with 612 passed instances over \(4\le d\le14\) and \(2\le r\le\lfloor d/2\rfloor\). All arithmetic, including rank elimination, is exact. Passing finite specializations is not a proof of the general determinantal identity; the bivariate generating-series computation provides that proof. The input identification between secant ideals and catalecticant minors is standard published algebraic geometry, not inferred from the checker. The local-ring statement applies along \(C_d\), not to arbitrary deeper strata. No independent audit has been performed.
