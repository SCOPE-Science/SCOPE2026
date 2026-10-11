---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For fixed positive alpha and sufficiently large n, every prime in the window exceeds square-root n, so Legendre's formula collapses exactly to floor(n/p). The condition floor(n/p)=j is the interval n/(j+1)<p<=n/j, leaving only finitely many cells. Summing log p on each fixed positive-scaled interval and applying the prime number theorem gives the coefficient formula. The aligned top-window harmonic simplification and parity comparison are immediate finite sums. The bundled verifier independently confirms the exact cell regrouping in 250 finite cases and the predicted top-window profile numerically.

## originality

PASS

Ma's recent theorem proves equal residue mass on fixed power bands, a scale whose total mass is of order n log n; its fixed-endpoint theorem does not imply a window with endpoints proportional to n, whose mass is only order n. Older valuation-pattern papers vary n for fixed primes and therefore have different quantifiers. No inspected or Resultary source gives the explicit piecewise-harmonic linear-window law or the parity bias. The result survives best-of-knowledge originality despite its classical proof ingredients.

## value

PASS

The result identifies the natural boundary scale at which the recent fixed-power-band equidistribution ceases to look uniform and quantifies the resulting bias exactly. The explicit 3/5 versus 2/5 split is a concrete obstruction to unjustified uniform extrapolation and the general coefficient is reusable for any fixed linear window.

The dated certificate retains the supplied scientific assessment, sources and limitations.
