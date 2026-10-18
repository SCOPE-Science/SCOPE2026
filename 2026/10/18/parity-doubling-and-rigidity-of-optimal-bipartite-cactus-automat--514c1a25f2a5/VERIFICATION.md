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
Run `python3 verify.py` with a standard Python 3 installation. The program constructs complete labeled residue-cycle automata, tests their transition-compatible bipartitions and cycle/edge graph shapes, and tests exact modular acceptance for all lengths from zero through four times the construction size, for every modulus 2 through 25, every residue, and unary/binary alphabets. The expected final count is 648 parameter/alphabet configurations.

The correctness proof does not rely on these finite checks. The lower bound, prohibition on extra arcs, and rigidity are justified by the closed-walk length-divisibility argument in RESULT.md. The testing script does not enumerate arbitrary NFAs and is not offered as such a certificate.
