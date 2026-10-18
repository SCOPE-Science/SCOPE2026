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

# Verification and reproducibility

The mathematical proof is in `RESULT.md`. Run `python3 check.py` in the same directory using Python 3 (standard library only); this performs 48 high-precision parameter-case checks, 101 rim/interior positive-semidefinite block checks per case, and nearby-factor obstruction checks. The output is expected to report `PASS` and expressly distinguish the finite test from proof.

The all-parameter correctness rests on three analytically verified bridges: (i) trace-preserving supported perturbations exclude rank above one from the extreme-point set; (ii) averaging admissible Minkowski centers over the stabilizer of the reference projector preserves feasibility and yields a two-eigenvalue center; (iii) the rank-one positive-semidefinite condition is equivalent to a reciprocal-eigenvalue scalar inequality and has a rigorously located minimizing argument. The quadratic identity and bound on the optimizing center are written out in `RESULT.md`.

No formal proof assistant, external expert, or independent audit has verified the result. A finite computation cannot establish global novelty or infinite quantifiers. The reviewed primary sources and residual scientific risks are identified in `AUDIT.json` and `REVIEW.md`.
