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
# Verification record

The ordinary degree-five homology concentration and rank rely on the published total-cut classification together with combinatorial Alexander duality. The new reflection calculations have a complete orbit-enumeration argument in `RESULT.md`, so no inference from finite cases to infinitely many ladders is used.

Execute `python3 verify.py` with Python 3.10 or later. The included program performs two logically separate checks: exhaustive invariant-face enumeration and signed Lefschetz sums at all widths from 4 through 36; exhaustive face generation and augmented mod-two boundary-matrix reduction at widths 4 through 8. The supplied `verification_output.txt` records 99 agreement checks and five mod-two homology checks. The code is standalone and has no external dependencies.

The program does not compute integral equivariant chain equivalences, integral quotient homology, or the status of unindexed literature. The cross-checks corroborate rather than replace the infinite argument.
