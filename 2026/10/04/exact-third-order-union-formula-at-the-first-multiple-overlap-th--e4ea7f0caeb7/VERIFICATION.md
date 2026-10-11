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

For any \(k\) simplex vertices, the sum vector has squared norm \(k(n-k+1)/n\) and inner product \((n-k+1)/n\) with each selected vertex. Cauchy--Schwarz therefore gives the exact onset \(\cos\theta\le\sqrt{(n-k+1)/(kn)}\), with equality at the normalized sum. Thus triple overlaps begin at \(\theta_{3,n}\) and positive-measure quadruple overlaps do not begin until \(\theta_{4,n}\), so inclusion--exclusion terminates exactly after the triple term on the claimed interval. Projecting uniform spherical measure to the three-vertex span gives the stated density; inversion of the regular-simplex Gram matrix gives the quadratic form and Jacobian. Scaling about the triple-contact point reduces the onset integral to a three-simplex beta integral and gives power \((n+1)/2\) with the displayed gamma coefficient. The assigned verifier checks the Gram inverse, determinants and beta identity exactly; a separate numerical integral near onset was consistent with the coefficient.

## originality

PASS

Arman, Kaire and Prymak give exact one-cap and two-cap formulas and then use second-order Bonferroni for simplex-centred caps. Full inspection shows their Lemma 2 states pairwise exactness up to the dimension-independent angle \(\arccos(1/3)\); for dimensions at least four the regular-simplex Gram calculation yields a smaller true triple-overlap onset. The audited theorem therefore not only supplies the missing three-cap integral and onset asymptotic but also corrects the first-overlap regime before extending the exact union formula to the quadruple threshold. Resultary search returned the assigned record as the exact same-object hit and no stronger prior third-order formula.

## value

PASS

The theorem repairs the first multiple-overlap geometry in the motivating spherical-cap argument and supplies the exact next inclusion--exclusion term through the quadruple threshold, together with the sharp birth rate of the missing mass. This is a natural structural correction and extension of a published cap-union calculation, with direct relevance to the source's probabilistic illumination estimates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
