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

# Reproducibility and boundaries

Execute `python3 verify.py` using Python 3's standard library. It prints the exact rational Gegenbauer values and each spectral branch for degrees zero through twelve, then terminates with `E7_ROOT_HARMONIC_CERTIFICATE_OK`. The verifier constructs all 126 integer root vectors, selects all 63 antipodal lines, checks the full \(8\times8\) tight-frame identity, all 3969 entries of each matrix polynomial identity, exact low-degree ranks and the complete finite positivity range needed before the analytic tail begins. It also rechecks the two rational integral moment inequalities that bound the infinite tail.

The checker is an executable, exhaustive finite calculation on a specified configuration. The analytic integral representation and monotonic bounds, explained in `RESULT.md`, are required to extrapolate from finitely many checked degrees to all degrees; the checker is not a substitute for that reasoning. The sources and remaining possible historical equivalences are listed in the scientific result and review. No independent mathematical validation has been performed.
