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

Use Python 3.10 or later and SymPy 1.11 or later. Execute `python verify.py` from a directory containing the accompanying verifier. It uses exact symbolic and rational arithmetic; no downloaded datasets or external files are required.

The checker reconstructs all four joint Bernoulli state updates directly from the node cache and mixing equations; derives the invariant quadratic-moment operator independently of its target form; checks the determinant/cofactor generating function; verifies the critical pole, residue and Lyapunov drift identity; and compares the transfer-matrix moments to explicit weighted paths for all lengths zero through six, with \(q\in\{0,1/4,1/3,1/2\}\). It passed 11,176 exact weighted path cases.

The unbounded-time claims are not asserted on the basis of path enumeration. The proof separately invokes exact rational identities, positivity of Lyapunov leading minors, and an uncancelled interior generating-function singularity. The unit-circle pole argument excludes competing singularities at criticality.

# Boundaries

No independent audit is recorded. No finite-precision, high-dimensional or general-graph claim is made. The documented proof, not this checker alone, supplies the infinite-time quantifiers.
