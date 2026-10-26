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

# Verification of the generalized-dihedral medial quotient

The proof is self-contained for every abelian group \(A\). It establishes the conjugation table, derives all forced reflection identifications modulo \(4A\) from one medial-identity substitution, and shows that the proposed quotient is medial because its right translations commute. This bounds the smallest medial congruence from both sides, so no extrapolation from finite examples is required.

The attached script `check_medial.py` recomputes each finite generalized-dihedral group from semidirect-product multiplication, obtains the conjugation table by actual group multiplication/inversion, generates all medial-identity pairs, and saturates the congruence under the quandle operation and its right division. It compares the generated congruence classes with the claimed singleton rotation fibers and \(A/4A\) reflection fibers. It checks cyclic groups \(C_n\) for \(1\le n\le13\), plus eleven noncyclic products (24 complete computations). Actual run status: `VERIFY_OK: 24 complete quotient computations`.

Checks are exhaustive only for the displayed finite examples. They do not establish distinctness or minimality for arbitrary groups: those are proved in `RESULT.md`. No independent audit has been performed, and no external formal certification is claimed. Potential literature equivalence remains a priority risk.
