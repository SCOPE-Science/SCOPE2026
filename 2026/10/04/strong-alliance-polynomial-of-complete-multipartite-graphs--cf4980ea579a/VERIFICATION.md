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
The proof was reconstructed from the literal strong defensive alliance inequality. For \(G=K_{n_1,\ldots,n_r}\), a vertex in \(V_i\) has exactly \(s-s_i\) neighbors inside \(S\) and \((N-n_i)-(s-s_i)\) outside \(S\), which gives the exact part-capacity criterion. The half-order bound, upper-ideal property, tight-part deletion test, parity minimum, coefficient formula, and normalized level-density inequality were then checked as separate logical steps.

The standalone `verify.py` was run from the packaged source and exhaustively checked every ordered positive part profile of total order at most \(9\). It tested every nonempty vertex subset against literal adjacency, compared that result with the structural criterion, checked connectivity of every accepted set, checked every one-vertex upper extension, checked inclusion-minimality against the two-tight-part rule, reconstructed every coefficient independently by dynamic binomial convolution, checked the parity minimum, checked the normalized density inequality, and compared every bipartite profile with the published two-tail formula.

Exact replay output:

`VERIFY_OK profiles=502 subset_checks=173238 criterion_checks=173238 coefficient_checks=4554 upset_checks=179490 minimal_checks=62544 density_checks=3550 bipartite_checks=36 max_order=9`

The computation is finite and does not certify the infinite theorem. Its role is to stress-test boundaries, parity cases, singleton parts, and the consistency of the derived formulas. The proof supplies the infinite argument.
