---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Walsh E_j decompose into 1 radial vector w_j and unaffected dark projector F_j. Rank-one secular polynomial at lambda_j=d-2j equals -tau*m_j/N times nonzero product; bright Jacobi spectrum is simple and disjoint for tau!=0. PSD Schur squares yield f^T(F_j∘F_j)f=||F_j diag(f)F_j||_F^2; induction on Fourier even weight forces all even coefficients equal, so dark kernel=odd-Walsh⊕span(h), rank=N/2-1. Odd powers H^(2r+1) have diagonals zero for shell k>r and tau(r!)^2 at k=r. Bipartite symmetry cancels dark diagonal contributions; these odd moments span radial bright intensities of dimension d+1. Their overlap with the dark range has dimension floor(d/2), giving rank N/2+ceil(d/2) and kernel O∩R_perp. Separately tensorizing the unmarked probability matrix gives rank N/2 for tau=0. Independent eigensolver checks for d=1..4 and tau=-2,0,1.3 give the predicted ranks; these are not a proof for all d.

## originality

PASS

The exact perturbation-independent marked-cube rank jump and Fourier/radial kernel classification specialize general average-mixing commutant machinery, but are not claimed in the inspected underlying continuous-time spectral theory. Discrete-time marked-vertex mixing and continuous-time search success results involve different Hilbert evolutions or outputs; exact spectral projectors and all-start time-average rank are key distinctions.

## value

PASS

A single marked site is a canonical symmetry-breaking perturbation in hypercube continuous-time quantum walks. The complete all-dimension rank and dark-subspace classification quantifies which radial Walsh sectors become visible, independent of defect strength and sign. This is a natural invariant rather than a tiny numerical curiosity or a generic rank bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
