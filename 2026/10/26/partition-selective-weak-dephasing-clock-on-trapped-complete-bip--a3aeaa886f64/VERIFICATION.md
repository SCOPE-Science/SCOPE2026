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

# Verification scope

The proof in `RESULT.md` reconstructs the reduction to dark density operators, establishes strict dissipativity of the complementary and perturbed generators, and evaluates the singular inverse using the two exact projected-dephasing eigenrelations. These are all-length algebraic arguments, not fits to data.

Run `python verify_bipartite.py` using `requirements.txt`. The verification program uses fixed numerical parameters and a seeded complex superposition. One finite execution returned at least 648 exact rational projector assertions, 80 projected/spectral checks, and 160 small-noise integrated-time comparisons. At noise scale \(\varepsilon=0.001\), the maximum absolute difference between the finite-scale \(\varepsilon T_\varepsilon\) and the limiting coefficient was 0.042418482. The checks are finite diagnostics only; they do not independently certify the limit or literature priority.

The dephasing convention is explicitly site-Lindblad, with rates on nontrap vertices \(\varepsilon\alpha\) and \(\varepsilon\beta\). A negative real part for every strictly positive-noise Liouvillian eigenvalue follows analytically; numerical eigenvalue checks are supplemental.
