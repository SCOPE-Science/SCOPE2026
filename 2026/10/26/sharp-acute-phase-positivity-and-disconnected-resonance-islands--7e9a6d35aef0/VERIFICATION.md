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

# Verification

The analytic proof consists of coordinatewise Fourier factorization, the positive-cosine-component phase-strip lemma, algebraic trigonometric reformulation, sharp branch intersection, and exact endpoint Fourier-sector computation. The checker `CHECKER.py` uses direct finite-group character sums, rather than reusing the analytic factorization as its only eigenvalue input. Running `python CHECKER.py` under Python 3 standard library passed 540 comparisons over alphabet sizes 2–5 and lengths 1–3. The sample points provide no exhaustive proof over real parameters or arbitrary dimensions; analytic proof is given in `RESULT.md`.

The publicly available primary literature used for scientific background was inspected in accessible HTML, specifically the spherical Fourier/Krawtchouk analysis of arXiv:1209.4148 and Krawtchouk reproducing and Poisson kernels of arXiv:1309.1510. The closest Hamming-shell sampling research records were available as searchable summaries only, not full texts, and remain a novelty-search limitation. Independent audit and independent validation are not performed.
