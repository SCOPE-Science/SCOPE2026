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

The proof is symbolic and self-contained. The accompanying `verify_separated_triples.py` performs the following finite checks without serving as an infinite proof:

- verifies the scalar inequality `2*C(m,2) <= lambda*(m-1)` for all tested `1 <= lambda <= 50`;
- constructs projective points and hyperplanes of `PG(3,2)` and `PG(3,3)` from normalized nonzero vectors;
- verifies the symmetric design parameters, all point-pair and block-pair intersection counts, and containment of every point triple in a hyperplane;
- verifies that the union of the blocks through every point-pair attains the claimed boundary in those examples.

Replay command: `python3 verify_separated_triples.py`. Expected final line: `VERIFY_OK`.

Limits: the finite projective-space checks do not establish the theorem for all parameters or the sharpness family for all prime powers; those statements are proved algebraically in `RESULT.md`. Literature searches cannot prove novelty, so an older equivalent formulation remains a residual risk.
