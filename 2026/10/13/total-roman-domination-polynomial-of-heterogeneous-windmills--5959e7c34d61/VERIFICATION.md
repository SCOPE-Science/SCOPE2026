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

The proof is symbolic and covers every \(r\ge2\) and every \(m_i\ge2\). The standalone script `verify.py` provides an independent finite regression check: it constructs each graph from the definition, enumerates every labeling in \(\{0,1,2\}^{V}\), tests the total Roman predicate directly from adjacency, and compares the full coefficient vector with the closed formula.

The checked tuples are \((2,2)\), \((2,3)\), \((3,3)\), \((2,2,2)\), \((2,2,3)\), and \((2,4)\). The replayed output is:

`VERIFY_OK cases=6 labelings=14094 valid_functions=7531 coefficient_checks=86 minimum_checks=6 total_checks=6 max_order=8`

The script also checks that the least nonzero coefficient occurs at weight \(3\), that its coefficient is \(M=\sum_i m_i\), and that evaluating the polynomial at \(1\) equals
\[
3^M+\prod_i\bigl(3^{m_i}-2^{m_i}+1\bigr)+\prod_i\bigl(3^{m_i}-2^{m_i}+1-m_i\bigr)-2.
\]

These finite checks do not replace the infinite-family proof. Their role is to detect algebraic or boundary-case errors in the derived formula.
