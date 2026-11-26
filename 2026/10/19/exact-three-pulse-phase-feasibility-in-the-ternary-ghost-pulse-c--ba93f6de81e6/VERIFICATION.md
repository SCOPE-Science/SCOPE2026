---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Any admissible signing can be replaced by one with exactly one same-sign pair: splitting a monochromatic support only drops constraints. For u<v that pair contributes only u,v,2u−v,2v−u; the last two must be supported or outside the finite interval. This gives each of the three stated pair tests with the correct strict left and weak right endpoint inequalities. If an adjacent pair works by an outward reflection, the extreme pair also works. Otherwise the third position must complete an arithmetic progression. For the left exception the necessary and sufficient conditions are a<d and a+4d<n; the reflected exception instead has a≥2d and is disjoint. The outer count sums c−a−1 over c≥max(2a+1,ceil((n+a)/2)); the AP count sums min(d,n−4d). Splitting the AP count at 5d≤n gives the floor formula. For the residue table, split at 3a+2<n and separate parities in the ceiling branch. For each n modulo 6 the parity-specific cutoffs are affine in the quotient and the summands quadratic, so the result has degree at most three in each residue; the independently checked table contains at least four exact values in each residue. The limit is independently obtained by integrating y−x for 0≤x≤1/2 and max(2x,(1+x)/2)≤y≤1, splitting at x=1/3: the integral is 11/108, and the AP terms have order n² only. Thus the limit after division by binomial(n,3) is 11/18.

## originality

PASS

The supported distinct result is the finite, unbounded-interaction, existential-sign weight-three classification and enumerator, not the definition of the constraint, a general TGP count, or a claim of universal priority.

## value

PASS

Weight three is the first pulse-count layer not made automatically admissible by using different signs for at most two pulses. This makes the slice natural: the exact boundary classification separates the bulk count from the two reflected exceptional classes and quantifies the first phase-feasibility loss by a nontrivial limiting fraction. It is more than a numerical slice of the published total table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
