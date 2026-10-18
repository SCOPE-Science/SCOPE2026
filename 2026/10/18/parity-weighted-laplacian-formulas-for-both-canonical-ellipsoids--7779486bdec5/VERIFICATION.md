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

# Reproducibility and scientific limits

Run `python3 verify.py` with a standard Python 3 interpreter; no dependencies outside the Python standard library are required. It uses exact rational matrix arithmetic rather than floating point. The expected summary is:

`VERIFY_OK cases 61 facet_contacts 26006 vertex_contacts 998`

The script constructs connected cacti from one or more cycles of lengths \(3\) through \(8\) and attached bridges, including trees and mixed-parity multicycle examples. It explicitly enumerates all product polar vertices for each instance, reconstructs graph potentials, checks that the active edge vectors span the full \(d\)-dimensional incidence space, evaluates \(y^{\mathsf T}\Sigma_Jy=1\) for every polar corner, and evaluates \(b_e^{\mathsf T}(\Sigma_L|_H)^{-1}b_e=1\) for both signs of each graph edge. Equality checks use `fractions.Fraction` and exact Gaussian elimination.

These tests establish finite-instance consistency only. General correctness rests on the linear-isomorphism, polar-vertex, uniqueness/symmetry, determinant-optimization, and determinant-ratio arguments in `RESULT.md`. The implementation does not enumerate arbitrary cactus graphs, certify literature priority, or constitute an independent audit.
