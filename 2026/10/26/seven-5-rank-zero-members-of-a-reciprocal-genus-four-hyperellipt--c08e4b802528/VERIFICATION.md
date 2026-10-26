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

# Verification notes

Run `python verify.py` in the directory containing `requirements.txt`, after installing the specified version range of SymPy. The exact-arithmetic verifier regenerates the \(4\)-by-\(4\) Cartier coefficient matrix, checks the resultant factorization, checks the irreducibility of the degree-six polynomial by Rabin's finite-field criterion, checks the parameter substitution and a lexicographic elimination identity, checks the smoothness criterion against polynomial gcd for all \(25\) base-field pairs, and verifies the base-field unique smooth rank-zero pair. It also checks that the block Cartier matrix at that pair is square-zero, and independently counts the six \(\mathbf F_5\)-points of the associated genus-four curve.

The observed execution completed with `VERIFY_OK`, with output `F5_rational_p_rank_zero_parameters [(3, 2)]`, `nontrivial_field_of_definition_degree 6`, and `C_3_2_F5_points 6`. This constitutes computational corroboration of the algebraic eliminations, not independent external validation. The infinite-field and all-extension assertions derive from the displayed polynomial identities and irreducibility, not from finite enumeration.

The statement does not determine Newton polygons or isomorphism classes. Historical literature searches may miss unindexed prior computations. Independent audit has not been performed.
