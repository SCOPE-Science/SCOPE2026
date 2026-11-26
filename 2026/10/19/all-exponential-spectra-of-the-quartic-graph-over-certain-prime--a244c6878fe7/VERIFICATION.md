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

The high-digit sum modulo p^2 retains precisely the stationary roots of a+4br^3 modulo p. For unit b there is exactly one, hence no cancellation; for b divisible by p and unit a there are none. When a=pA and b=pB, the prime cyclotomic count criterion reduces the question to whether Ar+Br^4 permutes the field. The stated power-sum computation works, including h=0 (p=5). There is also a direct check: if AB is nonzero, the unique nonzero root of r^3=-A/B collides with r=0 under Ar+Br^4, and if A=0 and B is nonzero then r and -r collide. Hence the exact zero criterion holds. It forces a fixed second residue and an exactly fixed second coordinate in each first-residue block. Full size saturates every block and exhausts first coordinates; the reverse differences satisfy the criterion. The unique parameters give p^(p+1) sets, with p^3 affine graphs since the slope must be divisible by p and the field function must be affine. Finite recorded checks were not rerun and do not establish the infinite statement.

## originality

PASS

Credit the entire frequency-set family and both counts as already known for the prime-square parabola. The distinct content supported here is the quartic-specific Fourier-zero identity, namely that despite different spatial graphs the quartic has that very same collection of spectra for p congruent to 2 mod 3. Once the identity is proved, the classification and census transfer directly from the parabola; they are not a separate new classification method. Inspected exact and general results do not themselves imply the quartic identity.

## value

PASS

The first nonlinear even monomial beyond the parabola is a natural test of whether increasing degree changes orthogonality. Proving identical zeros on all frequencies for the specified prime progression explains why a different spatial graph has exactly the same full family of bases, including nonlinear bases, rather than merely exhibiting one basis or reproducing a count in small examples. The value is the structural coincidence, not the length of the power-sum proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
