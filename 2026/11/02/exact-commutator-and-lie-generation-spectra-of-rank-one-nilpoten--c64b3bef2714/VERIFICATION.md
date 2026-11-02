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

Run `python3 check_rankone_commutators.py` with a standard Python 3 interpreter. No third-party modules, files, or network access are required. The script verifies full partner counts over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\) in dimensions two through five, with exhaustive ordered-pair comparison in six small configurations and one-fixed-factor complete partner comparison in three larger configurations. It directly implements finite-field arithmetic (including \(\mathbb F_4\)), matrix multiplication, rank, commutator, and Lie-span tests; it does not import the proof formulas from any external file.

A successful execution prints `RANKONE_NILPOTENT_COMMUTATOR_SPECTRUM_OK`. Explicitly verified per-fixed-factor rank counts include \((5,8,8)\) for \(n=3,q=2\), \((14,36,54)\) for \(n=3,q=3\), \((25,48,32)\) for \(n=4,q=2\), and \((122,432,486)\) for \(n=4,q=3\). The final example uses one fixed factor, not all ordered pairs. Finite tests cannot establish statements for unbounded dimension or untested characteristics; the mathematical proof in `RESULT.md` does.
