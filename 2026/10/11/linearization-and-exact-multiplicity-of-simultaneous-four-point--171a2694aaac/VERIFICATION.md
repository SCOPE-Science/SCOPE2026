---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Four restricted Walsh characters are orthogonal iff their six nonzero pairwise frequencies lie in joint Fourier-zero Z. Plane cosets b+W give 2^(d-2)T. For independent B=b+{0,x,y,z}, six distinct nonzero directions of H=span(x,y,z) lie in Z, leaving t=x+y+z. For each four-point A, the binary evaluation map H->F2^2 (plane time set) or F2^3 (independent time set) has image rank <=2; its kernel cannot contain any of the six zero directions, hence is exactly {0,t}; t annihilates all time differences. Conversely t in joint annihilator I and admissible W span H of dimension 3 and yield six zeros. Counting four complements W for each (H,t), eight independent unordered quadruples of prescribed nonzero four-sum in each 8-point H coset, yields N_ind=2^(d-2)(2^h-1)T, total 2^(d+h-2)T. d=2 forces h=0. Independent direct finite binary enumeration checks the seven obstruction subfamilies counts 16,16,4,16,4,4,0; finite tests corroborate rather than prove the universal law.

## originality

PASS

No source located giving exact arbitrary-family orthogonal four-character multiplicity with joint-annihilator exponent; simultaneous Riesz-basis literature is about invertible rather than necessarily orthogonal bases, while adjacent Walsh support and 8-point tables count different objects. Older small Hadamard and universal-spectra literature remains a genuine residual priority risk.

## value

PASS

Structural existence reduction to admissible two-dimensional frequency planes, complete plane versus independent count, and minimal three-set obstruction are motivated finite-harmonic-analysis classifications for arbitrary-size families, not a toy sampled instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
