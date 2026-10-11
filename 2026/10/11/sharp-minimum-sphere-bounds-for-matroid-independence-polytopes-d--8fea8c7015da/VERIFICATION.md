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
The proof in `RESULT.md` establishes the theorem for all finite loopless matroids with at least two elements.

Reproducibility: run `python verify.py` with Python 3, NumPy, and SciPy installed. The checker reconstructs representative uniform, partition/direct-sum, and graphic matroids from exact rank functions; enumerates all their independent indicator vertices and all subset-rank inequalities; and obtains a numerical Euclidean projection via a strongly convex quadratic program. It compares the resulting radius with the exact Boolean projection identity and uniform sharp envelope, tests both rank-inequality equality conditions, and checks the quantitative gap. A second optimizer solves the enclosing-ball epigraph directly for selected small cases, without using the projection formula. A five-element direct-sum example is verified by exact fractions.

Critical all-parameter steps checked in the proof: Boolean norm identity \(\|v\|^2=\langle\mathbf1,v\rangle\); projection variational inequality; the unique minimizer via an explicit squared-displacement lower bound; the rank inequality description of matroid independence polytopes; rank-based feasibility of \(t\mathbf1\); Edmonds' partition criterion; strict rank-defect lower bound through Euclidean projection and Cauchy--Schwarz; contact-exposed-face characterization; coordinate down-closedness.

The finite replay is corroborative only. It does not exhaust all matroids or establish worldwide novelty. Independent audit remains unperformed.
