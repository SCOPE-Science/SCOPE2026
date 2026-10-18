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

The universal mathematical proof is reconstructed in `RESULT.md` in three stages: (i) integral Lefschetz for each even complex dimension \(n\ge4\); (ii) Cartan–Leray with the exact \(\mathbb Z/2\) group-cohomology table and all degree-two and degree-three differential targets; and (iii) finite étale descent and the analytic exponential sequence. The canonical two-torsion follows from the determinant sign on a holomorphic residue form. No computer experiment is relied on to establish a statement for infinitely many dimensions.

Run `python3 low_degree_check.py` with the Python standard library. It checks only the group-cohomology parity pattern and bidegree support in low total degrees. Its reported success is an auxiliary consistency check, **not** an independent verification of the geometric hypotheses, spectral-sequence convergence, or proof for all dimensions. The proof does not assume that a computational enumeration is exhaustive in any higher degree.

The key external input describing actual smooth free members is Boissière–Camere–Sarti, arXiv:2409.09160v1, Section 6.1.5. Brauer-group and cyclic group-cohomology comparisons use Frassineti–Rizzo–Tufo–Verni, arXiv:2605.05450v1, Sections 2–3. No independent audit has been performed.
