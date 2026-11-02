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

# Verification of resistance-mode theorem

The analytical proof in `RESULT.md` establishes the full infinite-lattice claim. Its needed separate ingredients are: exact Fourier band \([0,8]\); unitarily staggered resolvent; strictly decreasing positive finite-dimensional Birman--Schwinger matrix; the divergent logarithmic common Green kernel; the dominated-convergence difference equal to half the resistor effective resistance; rank-one Schur-complement compression; inertia congruence; and strict exclusion of zero-threshold eigenvalues from \((8,\infty)\).

The exact corner geometry uses \(R(1,0)=1/2\) and \(R(1,1)=2/\pi\) from the established square-resistor lattice. The compressed resistance form has eigenvalues \(1/\pi\) and \((\pi-1)/(3\pi)\), with corresponding strict pinning thresholds \(\pi\) and \(3\pi/(\pi-1)\).

Run `python check_square_pinning.py` with NumPy and SciPy. The script performs 23 checks: eight periodic-Fourier two-point-resistance comparisons, twelve compressed-matrix mode-count comparisons, and three independent finite-torus sparse-eigenspectrum comparisons. For a \(70\times70\) torus, equal three-corner pinning at strengths \(2,3.5,6\) produces respectively one, two, three eigenvalues above the unperturbed upper band edge eight. Because the torus is finite and has discrete band-edge levels, none of these tests certifies the infinite-square-lattice theorem or exact threshold equality; those are handled by the proof.

Scientific boundaries: only scalar unit-mass nearest-neighbour square lattice and finite strictly positive local foundation springs are covered. No edge-resonance classification is claimed. Source priority is literature-search based and not independently certified. The independent audit remains not performed.
