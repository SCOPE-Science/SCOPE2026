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

The proof's unrestricted component is an exact binary-orthogonality argument, not an experimental conjecture. In the encoding, each multiset of multiplicity at most two corresponds to two nested binary level indicators. Orthogonality gives at most twice the ground-set order; the nesting condition excludes full rank and excludes codimension one when the ground-set order is even. The last exclusion uses the exact identity for an orthogonal projection onto a one-dimensional complement.

The standalone `verify.py` is pure Python 3. It checks all members and pairs in the displayed four- and six-coordinate certificates, pads the four-coordinate certificate to obtain the five-coordinate lower witness, and exhaustively enumerates every maximal clique of the compatibility graph for orders one through five. Its recursive pivoted Bron--Kerbosch search uses bitset candidate and excluded-vertex sets; termination occurs when both sets are empty. The complete run produces the lines in `verify_output.txt` and ends in `VERIFY_OK`.

No claim of exhaustive enumeration at order six or higher is made. For order six, the exact maximum follows from a ten-member explicit witness and the unrestricted even-order upper bound. An independent mathematical audit has not been performed. The existence and coverage of earlier equivalent results remain subject to bibliographic verification.
