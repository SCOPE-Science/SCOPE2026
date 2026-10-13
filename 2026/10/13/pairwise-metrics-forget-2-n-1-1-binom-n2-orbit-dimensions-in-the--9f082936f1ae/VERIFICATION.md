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

The checker uses exact integer/rational arithmetic and no external libraries.

For each \\(1\\le n\\le8\\), `verify.py` constructs one representative of every nontrivial unordered cut, builds the pair-by-cut incidence matrix, and computes its exact rational rank. It checks the formulas \\(m_n=2^{n-1}-1\\), \\(\\operatorname{rank}M_n=\\binom n2\\), and \\(\\dim\\ker M_n=m_n-\\binom n2\\). For every pair and every \\(3\\le n\\le8\\), it separately reconstructs twice the corresponding edge basis vector from three cut columns.

For \\(n=4\\), it checks the kernel vector with \\(+1\\) on the four singleton cuts and \\(-1\\) on the three \\(2+2\\) cuts. Two strictly positive weight vectors differing by this kernel vector are then converted into complete cut semidiversities: all six pair values agree, while the four-point diversity value changes by exactly one.

Current output:

`VERIFY_OK 118 exact assertions`

The finite computation is a consistency check. The all-arity statement follows from the displayed cut-column identity and rank-nullity argument in `RESULT.md`.
