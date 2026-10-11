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

Starting from the exact boundary scattering equations, the common denominator has leading term \(2ik e^{-i\theta}(\varepsilon\xi-2\sin\theta)\) when \(\delta=\xi/k\). Dividing the exact amplitude numerators by this term gives \((\varepsilon-e^{i\theta})/[i(\varepsilon\xi-2\sin\theta)]\); the two vertical amplitudes have the same limit and the horizontal transmitted amplitude tends to one. Direct integration of the edge plane waves then gives the stated mass ratio. In the intermediate regime \(k|\delta|\to\infty\), the \(k^2\sin\delta\) term dominates and restores suppression. The resonance exclusion \(\varepsilon\xi\ne2\sin\theta\) is exactly where the leading denominator is nonzero.

## originality

PASS

The initiating primary theorem deliberately assumes a fixed exclusion width \(|\delta|>K>0\) and proves only \(O(k^{-1})\) edge suppression there. The audited result resolves the singular shrinking window where that theorem no longer applies and identifies the exact \(1/k\) transition profile. Resultary returned no implication-equivalent published finding.

## value

PASS

The result identifies the sharp boundary-layer scale at which the source's high-energy edge suppression breaks down and gives the explicit surviving Bloch profile. That transition separates two qualitatively different transport regimes and explains the narrow exceptional windows left unresolved by the fixed-width theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
