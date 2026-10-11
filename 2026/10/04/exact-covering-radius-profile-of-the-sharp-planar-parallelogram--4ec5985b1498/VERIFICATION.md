---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Centering the two source parallelograms in the common basis \(u=(1,1)\), \(v=(-1/2,1/2)\) gives the rectangle half-widths \(a_\lambda=(2-\lambda)/4\) and \(b_\lambda=(1+\lambda)/2\). The transformed lattice has rows of phases \(\mathbb Z\) and \(\mathbb Z+1/2\) alternating with unit vertical spacing. A scaled rectangle covers either with one active row, requiring vertical half-width at least \(1/2\) and horizontal half-width at least \(1/2\), or with two opposite-phase rows, requiring vertical half-width at least \(1\) and horizontal half-width at least \(1/4\). These conditions are both necessary and sufficient, giving the minimum of the two stated maxima. Substitution yields exactly \(2/(2-\lambda)\) and \(2/(1+\lambda)\), switching at \(\lambda=1/2\).

## originality

PASS

The source preprint gives exactly this pair as its planar sharpness example and proves the sharp global inequality, but it states only the endpoint covering facts and equality for the balanced sum. Its theorem applied to the scaled interpolation gives only the uniform lower bound \(\mu(Q_\lambda)^{-1}\ge3/4\). The all-\(\lambda\) piecewise profile and uniqueness of the balanced equality parameter require the additional staggered-lattice covering calculation. Resultary's exact hit is the assigned profile, with no prior equivalent result among the leading matches.

## value

PASS

The pair is the canonical sharpness example for a new planar covering-radius inequality. Determining its entire interpolation profile explains the sharp constant dynamically and proves the balanced parameter is the unique equality point within the family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
