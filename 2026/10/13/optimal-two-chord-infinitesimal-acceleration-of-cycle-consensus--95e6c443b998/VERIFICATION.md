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

The isolated Fiedler eigenvalue mu=4 sin^2(pi/n) is doubly degenerate. Projection of edge incidence vectors onto its normalized sine/cosine eigenspace has squared norm (8/n)sin^2(pi d/n) and mutual absolute cosine determined by endpoint sums. Degenerate perturbation yields the smaller eigenvalue of H=xpp^T+(1-x)qq^T. The two-vector maximization is ab(1-c^2)/(a+b+2 sqrt(ab)c), with optimal x=(b+sqrt(ab)c)/(a+b+2 sqrt(ab)c). Parity of chord lengths and integer endpoint sums proves each global upper bound and attains it. The 2 mod 4 nonorthogonal upper bound is strictly smaller than the long-short orthogonal gain; for odd n maximal chords realize the closest discrete right angle. The isolated eigenspace and bounded updates give a uniform-in-choice O_n(eps^2) remainder. A rank-one single chord leaves one Fiedler eigenvector unchanged, so no gain. Independent numeric enumeration checked all unordered eligible chord pairs for n=4..17 against formulas, including S_6=4/7; infinite proof is the exact Fourier/parity argument.

## originality

PASS

The exact two-chord global optimizer and unique length/split parity pattern are not stated by the inspected generic algebraic-connectivity network-design papers or the recent single-chord cycle article. Theorem is not a rephrasing of the known one-edge multiplicity obstruction; it solves the minimum two-edge design. Best-of-knowledge priority only.

## value

PASS

Finding a cheapest pair of additional consensus links that first lifts a repeated Fiedler eigenvalue is a natural graph-design problem. The all-size closed form, parity-sensitive optimizer, and counterintuitive n=2 mod 4 shorter-chord superiority are exact, potentially reusable benchmarks, beyond a routine perturbation example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
