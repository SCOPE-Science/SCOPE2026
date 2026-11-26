---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The probability-measure addition theorem with the 1/√(2ℓ+1) sampling scale gives exactly the Legendre Gram matrix. Antipodal redundancy reduces rank to the 15 representatives. A separate exact midpoint construction checked all row valencies, obtained ranks (1,3,5,7,9,11,10,15,14,15,15,15,15,15,14) through degree 14, and checked the zero row sums at 8 and 14. Thus the degree-6 compatible nullity is five and the sole missing direction at each of 8 and 14 is constant. A separately written prime-field recurrence and elimination confirmed nonsingularity for all 185 degrees from 15 to 199. Reduction is valid in the subring where the recurrence and coordinate denominators are prime-to-p; nonsingularity after reduction implies it before reduction. For degree ≥200, DLMF 18.14.3 with α=β=0 gives the stated Bernstein bound. The valencies and the fourth-root estimates bound each off-diagonal row sum by (1046/63)/√300<1, proving positive definiteness. This covers the infinite tail, rather than extrapolating from the certificate.

## originality

PASS

The distinct indexed conditioning record covers the exact nonsingular-degree set, hence also the eventual threshold, which receive no separate originality credit. Its inspected statement and certificates do not evaluate ranks or sole null directions on the singular degrees. The verified distinct contribution is the quantitative defect classification of this same orbit, especially rank ten at six and rank fourteen with one missing direction at eight and fourteen. Related harmonic-index designs and classical symmetry constructions do not establish those evaluation ranks in the material inspected. This is a bounded scientific comparison, not a priority determination.

## value

PASS

On the canonical antipodal edge-midpoint orbit, knowing that a degree fails surjectivity does not tell a researcher how many independent measurements survive or which data constraints must be imposed. The exact difference between five missing directions at degree six and a single explicit constant obstruction at eight and fourteen is useful for one-degree interpolation and distinguishes the geometry from a generic 15-point parity sampler. This value rests on the defect information, not on rediscovering the indexed full-rank threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
