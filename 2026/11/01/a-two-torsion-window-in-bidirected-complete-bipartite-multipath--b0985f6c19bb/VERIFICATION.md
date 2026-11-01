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

# Exact verification

Run `python3 CHECK.py --verify MORSE_CERTIFICATE.json` with Python 3.10 or newer and no nonstandard packages. The file `MORSE_CERTIFICATE.json` was produced by the same checker in certificate-creation mode and contains every critical simplex mask and full sparse signed integral Morse differential column.

The executable independently enumerates every multipath face in two ways; enforces the four-arrow maximum; verifies the complete augmented face-vector formulas; constructs a deterministic staged Morse matching; and explicitly topologically sorts the reversed-matched-arrow Hasse digraph to prove acyclicity. It recursively reconstructs every signed critical-cell boundary. Its exact Bareiss determinant routine checks the recorded integer minor witnesses; no floating point or numerical rank threshold is used. A separate direct simplicial chain computation over the two-element field verifies every reduced Betti vector.

For the small parameters the Smith factors follow from the full-rank determinant-two minors, modulo-two matrix ranks, and a unit entry. At the larger parameters the exhibited maximal minors are integral units, proving that each Morse boundary is split-surjective. In all cases the homotopy-type inference additionally uses the standard discrete-Morse cancellation theorem and the Hurewicz classification of maps from a two-sphere to a wedge of two-spheres, rather than treating homology alone as a homotopy certificate.

A checker run on the displayed certificate must print `BIDIRECTED_K2N_INTEGRAL_MOORE_WINDOW_VERIFIED`. Its actual saved output is in `VERIFICATION_OUTPUT.txt`. Only the six finite values are verified; no unlimited parameter range, external validation or independent audit is claimed.
