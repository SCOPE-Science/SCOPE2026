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

# Reproducibility

Run `python3 verify.py` with a standard Python 3 installation. The program uses only Python standard-library modules. Expected deterministic output is embedded in `VERIFIER_OUTPUT.txt`; the numerical lines may differ in the final displayed decimal places across math libraries.

The program exhaustively tests the threshold graph's perfect-matching criterion for every length-\(n-1\) creation word with even \(n\le10\), independently computes exact rational Pólya probabilities for five symmetric initial Beta shapes, verifies the reflection combinatorial identity through even \(n=248\), and checks representative large-\(n\) crossovers by a log-beta-binomial implementation. All 8620 finite assertions passed in the tested environment. Counts and sample values are recorded in `VERIFIER_OUTPUT.txt`.

The theorem is not a consequence of finite tests. Its analytic proof is in `RESULT.md`, particularly the joint conditional characteristic-function argument, exact variance and uniform integrability. The computation does not exhaust all dimensions, all real urn parameters or arbitrary parameter sequences. Independent mathematical audit has not been performed.
