---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Conditioning on the unique u–v path length ell leaves an (ell+1)-rooted forest extension, counted with weighted Cayley identity. The third vertex w lies on the interior path with probability (ell−1)/(n−2); if off path its degree is 1+Bin(n−ell−2,1/n), if on path 2+Bin(n−ell−2,1/n)+Bern(1/(ell+1)). This yields the stated exact generating-function mixture; terminal ell=n−1 has deterministic D=2. Subtracting adjacent tail generating functions gives a quadratic with positive constant, negative leading coefficient for ell>=2. Convolution by A(z)^h, A(z)>0 coefficientwise, cannot introduce additional alternating sign changes, while first and last terms remain opposite, proving exactly one positive-to-negative tail crossing. Ell1→2 is all-positive, terminal comparison explicit, and the conditional means increase by a rational positive difference. Independently enumerated every Prüfer code at n=3..6, checked exact laws and all threshold signs, and verified coefficient and one-crossing identities for n4..50. The algebraic proof, not bounded enumeration, establishes universality.

## originality

PASS

The weighted Cayley forest formula and the conditional one-point marginal are classical, and a published endpoint-degree/marked-distance theorem establishes opposite-sign stochastic regression when the degree is at a distance endpoint. This paper studies a distinct third vertex, where means increase but tail laws exhibit exactly one sign change rather than domination. The full crossing theorem is not a corollary of the known endpoint law nor of Janson distance-profile limit theorems.

## value

PASS

Conditional third-vertex degree is natural when two other vertices are fixed as a geometric reference pair. Its stochastic behavior is qualitatively subtler than endpoint regression: strictly increasing means coexist with opposing tails and a unique sign reversal at each noninitial distance step. The uniform exact classification of all thresholds is a motivated dependence theorem, not just computing one marginal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
