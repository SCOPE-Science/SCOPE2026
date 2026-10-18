---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Twelve displayed primitive line vectors were read from frozen RESULT.md and compared with the gradients of F=X^4+Y^4+Z^4+3sum X²Y². An independently written SymPy Gaussian-integer determinant enumeration covered all 220 triples, finding no zero and norm histogram {4:8,20:48,36:24,40:24,64:12,80:48,100:48,200:8}; all odd prime factors are 3 or 5. Thus no triple concurrency or pair collapse for any odd p≥7, giving 66 double points. Independent F9 arithmetic normalized all twelve reductions at p3 and enumerated geometric pairwise intersections: 36 points, specifically 30 double and six quadruple, six F3-rational. At p5, two i embeddings independently yield four distinct lines, each with three original labels; the four linear forms multiply exactly to F modulo5 and have six distinct rational doubles. For p≥7 split i∈Fp yields 66 Fp points; nonsplit i gives six conjugate-pair intersections rational, and no others because triple points are excluded. The all-prime assertion is certified by exact integer determinant norms, not by sampled primes.

## originality

PASS

Dimca–Ilardi–Pokora–Sticlaru (arXiv:2301.01117) give the exact complex twelve hyperflex tangent lines and state 66 ordinary double points; this original input is not claimed as new. Pacini–Testa (arXiv:1301.1865) study the same Edge quartic/projective-dual hyperinflection set and its reconstruction/stabilizer; their exceptional p13 is a symmetry phenomenon, not a new line-incidence degeneration. The independently computed p3/p5 fibers, determinant-based all-good-prime bound and Fp rational-point counts do not follow from the characteristic-zero statement. Edge 1945 original accessible only in extract; full lawful Oxford request produced vpn_disconnected, so historic overlap is a named risk.

## value

PASS

The complete exceptional-prime incidence classification of a canonical twelve-line tangent configuration is a natural arithmetic specialization problem: it identifies exactly where the intersection lattice jumps and separately resolves rational vs geometric points. The obstruction-norm proof uniformly excludes all other odd primes; the exceptional p3 and p5 geometries have sharply different structure and provide useful test cases for reductions of complex arrangements.

The dated certificate retains the supplied scientific assessment, sources and limitations.
