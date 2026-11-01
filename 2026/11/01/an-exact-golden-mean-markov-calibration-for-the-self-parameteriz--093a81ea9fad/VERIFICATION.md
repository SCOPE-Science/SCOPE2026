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

# Exact-algebra and independent computational reproduction

The attached `verify_markov.py` is standalone source code requiring Python 3, SymPy and mpmath. Invoke `python verify_markov.py` from the same folder. It verifies the three-critical-iterate factorization over rational polynomials, the exact radical control and critical orbit, its strict rational root bracket, the Lucas trace recurrence through period fifteen, and every admissible cyclic inverse-branch trajectory of lengths one through eight at 65-decimal-digit precision. It also checks duplicate symbolic orbits with high precision and the exact endpoint relations. The run completed with `all exact symbolic identities and inverse-branch checks passed`.

The algebraic proof in `RESULT.md` establishes the unbounded-period and all-orbit statements. The finite numerical tests do not independently certify the infinite orbit census, exclude inaccessible literature, or imply physical/cryptographic performance. The proof's standard external ingredients are the elementary contraction theorem, primitive finite-state Markov coding, entropy of subshifts of finite type, and entropy concentration on a compact map's nonwandering set. They are used in the explicitly stated invariant core and boundary circumstances.

No independent audit is asserted.
