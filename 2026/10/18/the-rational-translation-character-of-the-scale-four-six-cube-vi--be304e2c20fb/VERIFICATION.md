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

# Reproducibility and verification

The file `CHECK.py` is self-contained and uses Python 3 standard libraries. Run `python3 CHECK.py` from the directory containing that file. Success is indicated by `Q6_RIPS_SCALE4_TRANSLATION_CHECKS_OK` after printed exact intermediate results.

The code constructs the sixty-four Hamming vertices, all degree-seven forbidden-pair neighbors, every eligible two-point orbit for a representative translation at each weight, both a memoized recurrence and an independent parity enumeration on each resulting quotient, and a direct sixty-four-element rational Fourier inversion. It verifies the character table \((253,9,9,53,53,1,1)\), multiplicity table \((36,1,0,6,6,0,1)\), and dimension \(253\). A separate independent C++ parity enumeration agreed on all six positive-weight quotient cases, and a separate C++ maximum-degree signed-independence computation returned \(253\) for the full graph.

The passage from the reduced Lefschetz virtual character to the total rational homology character uses the published homology concentration \(\widetilde H_7\cong\mathbb Q^{239}\) and \(\widetilde H_{15}\cong\mathbb Q^{14}\), with all other reduced rational groups zero, reported by Galetto, Montaño and Wellner (2026), Appendix C.3. The very large underlying homology boundary computation has **not** been independently rerun here; the unconditional part of this result is the exact reduced Lefschetz character. No separate determination of the two homology-degree characters, integral torsion, or the full cube symmetry character is claimed.
