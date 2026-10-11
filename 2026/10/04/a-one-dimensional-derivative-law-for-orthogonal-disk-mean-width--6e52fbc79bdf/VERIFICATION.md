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

The support functions give the directional-width maximum exactly. For a uniform direction, \(t=|b|\) is uniform on \([0,1]\); conditional angular symmetry converts the switching equation into \(\cos(2\phi)=r_\delta(t)\), with switching exactly for \(t<(1+\delta)^{-1}\). Differentiating the expectation gives the displayed first derivative. At the moving endpoint \(r_\delta=1\), boundary terms cancel; direct algebra yields the stated derivative and factorization for \(1-r_\delta^2\), giving the second derivative. Its numerator is positive on the integration region, the endpoint singularity is integrable, and dominated convergence gives the asymptotic slope \(\mathbb E|b|=1/2\).

## originality

PASS

The closest prior works treat fixed members or different invariants. Bäsel’s full paper proves the mean width of the fixed oloid member and explicitly describes Finch as treating three fixed orthogonal-disk configurations. The full Nash–Pir–Sottile–Ying paper studies algebraic boundaries, face lattices, and spectrahedra; a full-text search found no mean-width result. Resultary searches for the moving-separation profile, derivative formulas, and strict convexity returned no earlier equivalent.

## value

PASS

Mean width is a standard intrinsic volume and this one-parameter family contains classical orthogonal-disk bodies studied only at special configurations. The exact sensitivity law and global convexity are structural information across the family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
