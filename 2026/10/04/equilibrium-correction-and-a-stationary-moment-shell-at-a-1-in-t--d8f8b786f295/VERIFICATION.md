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

At equilibrium, \(z=xy\) and \(y+z=x\), so \(y(1+x)=x\); hence \(x=-1\) is impossible before division. For \(x\ne-1\), substitution yields the source cubic, and at \(a=1\) it factors as \((x+1)(x^2-x-b)\). The polynomial observable \(F=x^2-2x-2y+2z\) has exact Lie derivative \(-2(x^2-x-b)\), verified coefficientwise in the package, so invariance gives the shell law. The variance identity follows from the two roots; endpoint variance zero forces constant \(x\), and invariance then forces an equilibrium whenever the root is admissible. For a non-equilibrium ergodic measure the quadratic must occur with both signs, giving positive mass inside and outside its root interval; the periodic crossing follows by continuity.

## originality

PASS

The primary paper's full arXiv text prints the same system, gives the equilibrium cubic \(a x^3-(b+1)x-b=0\), and discusses three-versus-one fixed-point regions. It does not handle the singular invalid denominator at \(a=1\) or state the stationary shell. Resultary searches found no earlier same-flow correction or invariant-measure theorem.

## value

PASS

The result both corrects the published equilibrium geometry on a mathematically distinguished slice and derives an exact stationary shell that constrains every compact recurrent state there. This is a motivated source correction plus a natural invariant-measure law, not a numerical recheck.

The dated certificate retains the supplied scientific assessment, sources and limitations.
