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
Run `python3 verify.py` with a standard Python 3 installation. The program enumerates every overpartition through size \(11\), independently computes unrestricted overpartition numbers by a logarithmic-derivative recurrence through size \(900\), and checks the exact joint-tail and equality counting generating functions. It prints three exact-coefficient coincidence proportions and three finite saddle comparisons and terminates in `VERIFY_OK` when all assertions pass.

The calculation neither exhausts the infinite set of partitions nor independently proves a limit. Analytic proof details (the multiplicative restricted generating functions, constrained coefficient saddle transfer, and tail summation) are supplied in RESULT.md. Mathematical correctness and originality were reviewed within the self-review; independent audit is unperformed.
