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

Read original RESULT.md blob 6930dad8ae8ef2628e0914bb7ede9576eedeb765 and verify.py. Rotation increments F_{k+1}−F_k=n x_k−b and direct position sum give mean ab/2. The covariance calculation gives V=b²(n²−1)/12 −sum_{i<j ones} (j−i)(n−j+i). Gap-domain strict concavity of pair penalty makes its minimizers gap-simplex vertices, exactly one block of ones, giving upper expression. For the lower side, F_k modulo n advances by a, so each block of N=n/d successive values consists of distinct residues and has variance at least d²(N²−1)/12; total-variance equality forces each d-spaced consecutive range repeated d times. Rotation increments convert this range condition into all cyclic substring-one counts within floor/ceil b*ell/n, equivalently circular balance; the mechanical Christoffel construction attains it. Independent fresh enumeration checked every nonconstant binary word of n=2..10 and both equality criteria without relying on saved VERIFY_OK. This is an all-n proof; code bounds are only tests.

## originality

PASS

Best-of-knowledge PASS: Poovanandran–Simpson–Teh prove the first moment; Vesti/Jenkinson majorization concerns numeric rotation orbits; De Luca–Fici characterize balanced word structure. The exact scattered-pair variance identity and both equality sharpness results were not in those inspected statements. A general majorization theorem may have a latent transfer to this specific variance, and Jenkinson full text was not read.

## value

PASS

The established circular Parikh mean loses all order information. A sharp second moment quantifies exactly how much circular order can change the observable, detects the canonical homogeneous and clustered necklaces, and exposes a gcd-sensitive finite-length lower obstruction. It is a natural informative invariant, not a mere relabeling of numerical rotation weights.

The dated certificate retains the supplied scientific assessment, sources and limitations.
