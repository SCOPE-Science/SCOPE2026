---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The factorial-moment equivalence is correct: exchangeable conditioning on K converts the first three factorial moments exactly into three-wise-independent fair bits. After writing K=r+qJ, the prescribed moments become a mean, variance n/(4q^2), and zero centered third moment. The cubic-polynomial lattice inequalities in the package give the exact low-variance obstruction for a given fractional mean; the explicit high-variance zero-skew four-point law brackets the target at n=q^2+2 and convex interpolation uses at most five J-values. Below q^2-1, nearest-integer variance already blocks one residue; at q^2-1,q^2,q^2+1 the displayed residues violate the sharper zero-third-moment minimum. The fetched exact-rational verifier independently checks constructions through q=200 and the boundary formulas, but the proof is analytic.

## originality

PASS

Best-of-knowledge originality passes. Benjamini--Gurel-Gurevich--Peled connect k-wise independence with moment problems but do not state modular Hamming-weight freedom. Di Cecco solves sharp threshold-event optimization under three moments, not support on one residue class. Orthogonal-array work minimizes sample-space rows rather than coordinate length. No checked source gives the q^2+2 threshold or the residue-vertex construction.

## value

PASS

This determines a sharp transition for how much modular information can be prescribed under exact three-wise independence, separating coordinate length from orthogonal-array sample-space size. The q^2+2 cutoff and sparse residue-vertex construction are natural moment/design-theoretic boundary data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
