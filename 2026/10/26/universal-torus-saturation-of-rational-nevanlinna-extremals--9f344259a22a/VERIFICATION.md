---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For a nonconstant real rational Herglotz–Nevanlinna φ=B/A of projective degree m, its m simple real projective poles are exactly A=0. The original two-variable h=-1/(φ(z)+w-1/w) has coprime bihomogeneous pair P=-A W0W1, Q=A(W1²-W0²)+B W0W1 of bidegree (m,2). If P=Q=0, A≠0 is impossible; over each zero A(Z)=0, coprimality forces W0W1=0, giving exactly two real-projective base points. Local coordinate x=A(Z), w=W1/W0 near w=0 gives Q=-x+b(0)w+O(xw,w²), w(x)=x/b(0)+O(x²), P|_Q≈-x²/b(0), intersection multiplicity 2; near w=∞ similarly. Bézout total is 4m. The quadratic Sylvester resultant in W with a degree-2 ε perturbation equals A²(ε²-Bε-A²) and at ε=0 equals -A^4, independently checked by symbolic resultant calculation. Domain Cayley and nonsingular range normalization preserve the complete scheme; inner representation gives the scattering-stable denominator of bidegree (m,2). Extremality of the source h family relies explicitly on Fagrell–Luger Theorem 3.1 rather than being newly proved. All m follow analytically; sampled resultant tests are corroborative.

## originality

PASS

Knese 2017/2019 defines torus saturation and conjectures its necessity for rational extreme points; his saturation plus irreducibility theorem is a SUFFICIENT extremality criterion, not a proof every rational extreme point is saturated. Fagrell–Luger 2026 proves the entire rational Herglotz family is extreme and §4.1 shows saturation for its explicit φ=z-1/z example, with §4.2 analyzing reducibility; those inspected primary sections do not state the all-degree torus divisor classification. The audited full projective base-locus and resultant for all rational φ is a motivated family-wide extension including reducible cases. Classical elimination could make the algebra more elementary than its contextual significance; historical implicit equivalence remains possible. Related Resultary research treats second-coordinate marginals, not torus base schemes.

## value

PASS

Knese saturation is a natural projective intersection invariant for scattering-stable rational inner denominators. Showing an entire independently motivated extremal family saturates, including its reducible cases, and computing every local intersection and the resultant from its pole divisor is a structurally informative, unbounded-degree classification, beyond a single known example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
