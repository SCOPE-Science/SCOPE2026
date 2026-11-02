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
# Exact verifications

The included `verify_symbolic.py` (Python 3 and SymPy) recomputes \(\Delta\), the entries of the Cartier coefficient matrix, \(UZ-VW=5a\Delta\), the determinant identity, the rank-one specialization, and the semilinear stable-rank factorization. It enumerates all \(343\) coefficient triples, testing squarefreeness via a polynomial gcd; successful output `SYMBOLIC_VERIFY_OK` with \(252,30,12\) smooth strata and \(49\) singular triples.

The included `verify_counts.py` (Python 3, standard library only) separately enumerates all smooth triples using an independent polynomial gcd, constructs \(\mathbb F_7,\mathbb F_{49},\mathbb F_{343}\), counts rational points, computes the first three L-polynomial coefficients using Newton identities, and recovers \(7\)-rank modulo seven. It successfully printed `POINT_COUNTS_OK {1: 30, 0: 12, 3: 252}`. This is a finite cross-check, not a proof of the geometric statement over all algebraically closed characteristic-seven fields.

The displayed Cartier-semilinear contraction and polynomial factorization supply the infinite-family proof. The source overlap assessment has a specific unresolved risk for an inaccessible 1991 Picard Hasse–Witt paper. Independent audit and independent validation have not been performed.
