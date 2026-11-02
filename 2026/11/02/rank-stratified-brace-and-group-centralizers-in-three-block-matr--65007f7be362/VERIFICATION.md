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

The exact claims rest on the proof in `RESULT.md`: nilpotent block multiplication, rank-nullity for two centralizers, finite-field Gaussian-binomial counts, factorization counts, and constructive rank subadditivity bounds.

Run `python3 verify.py` with Python 3.8+ and no third-party libraries. The verifier independently enumerates all adjacent block matrices and calculates products and ranks directly over the prime fields with \(q\in\{2,3,5\}\). Tested positive parameter triples are \((1,1,1),(2,1,2),(1,2,1),(2,1,3),(3,1,3)\) in the configurations listed in the research result. Its direct loop checks the centralizer sizes of every tested input, all output commutator and product fibers, and the relevant zero-probability counts against the symbolic formulas.

Observed output ends in `VERIFY_OK`. In the \((3,1,3;2)\) case, exactly 50 distinct central matrices arise from a single brace product and exactly 344 from one group commutator. The set of products of two group commutators has all 512 possible central values, whereas matrices of rank 3 do not occur as single commutators.

The checker runs over prime fields rather than all extension fields. It confirms only bounded examples and is not a proof of the theorem for every field/dimension. No independent mathematical audit has been performed.
