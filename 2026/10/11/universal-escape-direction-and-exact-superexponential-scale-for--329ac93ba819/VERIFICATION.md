---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For even d and a>0, y_{n+1}=y_n−2a(x_n+y_n)^d makes y_n monotone. If bounded below then ∑(x_n+y_n)^d<∞ so sum→0; x_{n+1}→lim y and x_n→−lim y, forcing both limits zero. Otherwise y_n→−∞, and x_{n+1}≤y_n makes x_n→−∞. Negative a follows exact reflection. For escaping orbits set r_n=−(x_n+y_n), z_n=x_n−y_n=a r_{n−1}^d≥0; then r_{n+1}=r_n+z_n+3a r_n^d, with 0≤z_n≤r_n/3. Hence r_{n+1}=3a r_n^d(1+O(r_n^{1−d})) and normalized coordinates tend to (1/3,2/3). The logarithmic recurrence for w_n=log r_n+log(3a)/(d−1) has summable d^{-n} increments, giving H>0 and the exact prefactor (3|a|)^{-1/(d−1)} after a vanishing tail. All starting real points and even d≥2 are covered analytically. Recomputed signed recurrence identities for d=2,4 and a=±1,±2, eight cases; these finite tests do not establish global dynamics.

## originality

PASS

Best-of-knowledge PASS: Fontich–Garijo–Jarque 2024 introduce exactly this polynomial secant model, describe the compact basin and its boundary for even degree, and prove coordinate monotonicity. They do not in their materially read main theorem/Section 4 establish the all-escaping-orbit asymptotic direction, positive escape height, or exact universal multiplicative scale. Their 2405.08812 work concerns odd degree and chaotic boundary. Polynomial complex escape Green functions are conceptually broader but the exact real-global dichotomy and prefactor do not automatically follow.

## value

PASS

A complete global dichotomy and exact superexponential escape scale for every initial real state is the missing complementary side of a published compact attracting-basin classification. The universal ray and multiplicative constant give meaningful asymptotics of the precise natural polynomial model, not a fitted numerical law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
