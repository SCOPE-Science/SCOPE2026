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

# Verification of the cyclic \(b\)-symbol spectrum

Execute `python3 verify_quadratic_tail.py` with Python 3.8 or later. The script uses only the standard library, constructs all coefficient masks of Boolean polynomials of degree at most two, enumerates all their codewords by a Gray-code recurrence, and counts nonzero cyclic read windows directly. It checks every legal high-window width in dimensions \(m=3,4,5\), comparing complete coefficient maps rather than only minimum weights.

The second, independent phase enumerates every codimension-two affine subspace of \(\mathbb F_2^m\) by an independent pair of dual linear forms. It deduplicates dual bases, examines each of four cosets, and computes minimal circular containing intervals for \(3\le m\le8\); only the eight predicted span-\(2^{m-2}\) flats lie below the threshold.

Expected terminal output: `VERIFY_OK quadratic_tail_m3_to_m5 affine_flats_m3_to_m8`.

The general theorem and the sharpness of the width boundary are deduced symbolically in `RESULT.md`. The finite enumerations do not establish an infinite theorem on their own. The coordinate order, cyclic wrap, even-rank condition, exponent counts and small-dimension boundary are explicit.
