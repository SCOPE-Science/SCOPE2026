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

For the stated nonsticky natural-scale extension the resolvent density u relative to speed measure solves u''-r|x|^alpha u=-r delta_b. Continuity of u and u' at zero follows from the absence of an atom or source there; at b only u' jumps by -r. The small-argument Bessel expansion gives q(0)=1 and q'(0)=-h; s' q-s q'=2h, producing the stated normalization and jump. Integrating the equation with u' vanishing at infinity gives total mass one, and the exponential-age resolvent is the unique stationary law (two starting laws can be coupled at their first common reset). For x>0, E=q'^2-r x^alpha q^2 has E'=-r alpha x^(alpha-1)q^2<0 and E tends to zero, so (log q)''=-E/q^2<0. The log of x^alpha q is strictly concave and its density branch vanishes at both endpoints, hence there is one critical point and strict increase/decrease on either side. Since x^alpha s is strictly increasing for 0<x<b, this proves both mode locations, including equality b=m where the right derivative is zero at b but the branch strictly decreases beyond b. q strictly decreases, s increases, and both start at one, proving the strict pointwise positive-side dominance. Integrating q'' gives negative mass q(b)/2; independently, the reset-age process must hit zero before being negative, after which symmetry and the memoryless age give the factor 1/2 (no zero atom). The bounded independent Bessel/quadrature comparison at alpha=r=1 gave m=0.88405046, normalized mass and the matching negative masses 0.34493523 and 0.06938266 for b=m/2 and b=2m, respectively. Numerical checks are corroborative; the uploaded checker was inspected but not run. Modes refer to the prescribed continuous Lebesgue density.

## originality

PASS

Pass for the off-centre matched law and all-parameter mode classification of the specified natural-scale Itô reset model. The centered law, Bessel hitting transform and general reset resolvent are covered and properly distinguished. The opposite-side mass is an elementary consequence of the known hitting transform, symmetry and exponential age, useful as a check/corollary but not a separate originality basis.

## value

PASS

The singular mobility centre and independent reset location produce two observable modes, including one that switches exactly from diffusivity-selected to reset-site-pinned. This is a sharp global prediction, not a replot of a centered law or an arbitrary parameter slice. The exact density and opposite-side mass are useful tests for models with a different interface or noise convention.

The dated certificate retains the supplied scientific assessment, sources and limitations.
