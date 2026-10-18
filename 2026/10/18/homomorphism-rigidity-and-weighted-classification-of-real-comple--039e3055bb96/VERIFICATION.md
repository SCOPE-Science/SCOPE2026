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

# Verification of weighted complete-multipartite evolution-algebra rigidity

The universal proof is in `RESULT.md`: target square-class independence, blockwise orthogonality, connectivity propagation, equal-dimension saturation, preservation of source square classes, and forced scale factors. This is a mathematical argument for all positive real weights and equal finite dimensions, not an extrapolation from tests.

Run `python3 checker.py` with Python 3 (standard library only). The program constructs full structure constants and verifies \(f(e_i e_j)=f(e_i)f(e_j)\) for every ordered basis pair, in four exact rational examples, including non-permutation orthogonal blocks, part reorderings and bipartite and balanced tripartite random-walk rescaling. It also rechecks determinants of \(J-I\) for part numbers from two through eight by rational elimination. Recorded output: `CHECKER_OK: four exact multiplication certificates and square-class independence r=2,...,8`.

Exact arithmetic avoids floating-point ambiguity. The finite checks do not independently certify the full proof, all parameter choices, or the novelty assessment. Independent audit: not performed.
