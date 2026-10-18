---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-11.md",
      "INDEPENDENT_AUDIT_2026-10-11.json"
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

Verified the exact meaning of \(\mathrm{FRAC}(K_n)\): pair inequalities and nonnegative coordinates, not the stronger clique-sum inequality. Standard half-integrality and odd-cycle tight-edge criterion, specialized to the clique, yield all vertices \(0,e_i,\frac12\mathbf1_S\) for \(|S|\ge3\). Symmetric uniqueness restricts the center to \(t\mathbf1\); squared vertex distances are \(nt^2\), \(nt^2+1-2t\), and \(nt^2+k(1/4-t)\). For \(n\le6\), the unit-vertex simplex center \(t=1/n\) contains all fractional vertices strictly; for \(n\ge7\) it excludes the full-half vertex, and equality of active distances yields \(t=(n-4)/(4(n-2))\), radius squared \(n^3/[16(n-2)^2]\). Positive barycentric coefficients \(a=n/[2(n-2)^2]\), \(b=(n^2-8n+8)/[2(n-2)^2]\) place the center in the convex hull of sphere contacts, proving global optimality and uniqueness by variance identity, not by local numerical minimization. Independently enumerated all half-support sizes and their exact distances/contact sets for \(3\le n\le12\), including the \(n=7\) gap \(1/2800\). Finite checks corroborate the all-n symbolic proof.

## originality

PASS

This particular final statement and its implications were checked against the named primary sources; the returned primary literature supports the stated best-of-knowledge comparison, while incomplete/full-text risks are expressly recorded. The Resultary semantic query returned temporarily_unavailable (search_completed=false), not a negative hit; no absence or external certification is inferred.

## value

PASS

The standard fractional edge relaxation of a clique has a surprisingly sharp metric phase transition: it matches the integral stable-set simplex sphere through dimension six but requires a fractional contact from dimension seven, with a growing explicit radius gap. The exact center, contacts, and threshold are motivated quantitative geometric facts about a canonical combinatorial relaxation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
