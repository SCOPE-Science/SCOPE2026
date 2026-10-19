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

# Verification details

The `checker.py` file is standalone and uses Python's standard library (`fractions`, `itertools`). From the project directory, run `python checker.py`. It exhaustively checks each binary sign word of lengths one through eight, for parameter pairs \((\lambda,\mu)=(2,1/2),(3,1),(5,2)\). For each sequence it multiplies exact rational matrices and verifies the claimed product formula and squared norm identity for \(t\in\{1,2,3\}\) and \(c=1/2\). It also verifies first-cylinder separation for three rational contraction ratios. Expected line: `EXACT_PRODUCTS_AND_SEPARATION_OK 4590`.

The direct product induction, recurrence of terminal sign blocks, geometric-series coupling, strong-separation cylinder measure, and bi-Lipschitz normalizer arguments in `RESULT.md` provide the actual infinite proof. The computational tests are finite checks, not evidence that enumeration covers all signs or parameters. The 2026-10-08 motivating preprint concerns fixed nonequatorial directions; this result concerns explicitly changing directions.
