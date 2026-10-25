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
# Verification and reproducibility

Execute `python3 verify_rook_rect.py` from this directory; it needs Python 3 and no third-party dependencies. Expected output is `verification_output.txt` and ends with `VERIFY_OK_RECTANGULAR_ROOK_H1_AND_MINIMAL_SUPPORTS`. The code reconstructs open common-neighbor triangles independently, checks the one-cochain on every triple, enumerates all four-element relations and their correct orientation signs in the four-by-four base case, certifies the unique connected signed-relation graph and one sign-inconsistent cycle, checks general count formulae on five rectangles, and verifies exact support sharpness exhaustively on two small rectangles.

The proof for all \(m,n\ge4\) is **not** an extrapolation from those cases. It uses four-by-four containment of every missing triple, overlaps between consecutive selected subgrids, and a star-forest characterization of missing-triangle-free vertex sets. The verifier does not establish statements about \(\pi_1\), higher homology, hidden equivalent published results, or independent validation.
