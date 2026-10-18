---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-14.md",
      "INDEPENDENT_AUDIT_2026-10-14.json"
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

For integral homogeneous binary F,G with nonzero homogeneous resultant R, modulo every p not dividing R there is no common nonzero affine zero: otherwise it would be a common projective root. Thus simultaneous p divisibility for a primitive integer coordinate pair occurs only at primes dividing R. Homogeneity also forces all value pairs from nonprimitive coordinates to share their coordinate prime. CRT gives beta=prod_{p|R}(1-N_p/p^2), with B(Y)=beta Y^2+O_{F,G}(Y+1) for local exclusions. Mobius inversion restricted to d coprime to rad(R) yields main constant beta prod_{p not |R}(1-p^-2) and O_{F,G}(X log X) via harmonic errors. Checked F=X^2-Y^2,G=X^2-4Y^2 at p3 N3=5, and F=X^2+Y^2,G=X^2-Y^2 at p2 N2=2; an independent exact pointwise grid count at N=11,29,37 matched the local/primitive condition for both. The finite checks corroborate but do not prove the universal resultant argument.

## originality

PASS

Bodin--Debes provides density for general coprime polynomial values; the new theorem adds an O(X log X) error and explicit finite correction for binary homogeneous forms without positivity. The 2026 Toth abstract describes a quantitative Ekedahl--Poonen formula subject to general properties; same-model notes attribute a positivity condition, but primary full text was inaccessible this turn and that precise difference remains a disclosed risk. Search found no independent exact table, alias or stronger matching quantitative implication.

## value

PASS

The resultant prime support reduces an infinite local density to finitely many residue counts while homogeneity makes effective O(X log X) summation possible even for indefinite forms. This naturally motivated class and unconditional explicit correction are useful for lattice-point counts and practical gcd-value densities, beyond merely reproducing a known leading constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
