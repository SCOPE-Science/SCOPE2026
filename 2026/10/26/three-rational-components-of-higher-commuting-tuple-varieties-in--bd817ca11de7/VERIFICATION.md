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

# Reproducible checks

Run `python3 verify.py` with Python 3 and no third-party dependencies. The verifier independently computes strict triangular matrix products and commutators, checks their three-coordinate description for 2,000 pseudorandom pairs across four fields, and exhaustively enumerates selected commuting tuples using row-coordinate equations. It also enumerates every matrix over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\) and counts commuting pairs through the rank of its adjoint map, a separate finite computation.

The observed direct row counts were \(64\) and \(1024\) at lengths one and two over \(\mathbb F_2\), \(12160\) at length three over \(\mathbb F_2\), \(729\) and \(41553\) at lengths one and two over \(\mathbb F_3\), and \(15625\) at length one over \(\mathbb F_5\). Independent adjoint-rank counting returned \(1024\), \(41553\), \(557056\), and \(4140625\) commuting pairs for field orders \(2,3,4,5\). All matched the theorem formula.

These checks do not enumerate all triples over every field, test irreducibility algorithmically, or establish the infinite-family theorem. Irreducibility, rationality, dimension formulas, and arbitrary-characteristic coverage follow from the geometric argument in `RESULT.md`. No independent audit has been conducted.
