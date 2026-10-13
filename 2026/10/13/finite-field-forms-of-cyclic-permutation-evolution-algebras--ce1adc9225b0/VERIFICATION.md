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

The proof was checked from the defining multiplication rather than inferred from finite examples. The critical steps are: arbitrary isomorphisms are forced to be monomial; the monomial permutation must be a directed-cycle rotation; the diagonal recurrence closes exactly when one explicit ratio is a \((2^m-1)\)-st power; cyclic rotation squares the invariant modulo those powers; and Burnside's lemma evaluates the resulting finite cyclic action.

`verify.py` provides an independent finite check. It enumerates every element of \(\operatorname{GL}_m(\mathbb F_q)\) for \((q,m)=(3,2),(5,2),(4,2),(3,3)\), tests the full algebra homomorphism identities for every pair of nonzero weight tuples, and compares the resulting isomorphism relation with the theorem. The \(\mathbb F_4\) case uses an explicit quadratic-field implementation. It also checks exact automorphism orders and compares direct doubling-orbit counts with the Burnside formula for seventeen field orders and \(2\le m\le8\).

A successful replay prints `VERIFY_OK`, the four exhaustive case summaries, and `BURNSIDE_GRID_OK`. These computations are finite consistency tests, not a proof for arbitrary \(q\) or \(m\).
