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
# Verification

The mathematical check is exact. `verify.py` implements the published EAIE formula and cumulative grade transformation with `fractions.Fraction`. It verifies the minimal counterexample and compares formal coefficient dictionaries for several multigrade vectors against
\[
\frac1{|F|}\sum_{j\in F}\sum_{q=1}^{d_j-1}\zeta_{j,q}.
\]
It also checks that all such defect coefficients vanish when every factor has one positive grade.

The general proof in `RESULT.md` is symbolic and does not depend on the finite test cases. The executable checks protect the transcription, sign, indexing, and minimal witness. No floating-point calculation, exhaustive-search claim, or external certificate is used.

Scope limit: the verifier checks the EAIE/COTR identity only. It does not validate unrelated axioms, reduced-game arguments, dynamic convergence, or any proposed repair.
