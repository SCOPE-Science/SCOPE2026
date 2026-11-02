---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible checks and their limits

Run `python verify.py` with Python 3.10 or later. No network, packages, or proprietary software are needed. The supplied `verification_output.txt` records a successful execution ending in `VERIFY_OK`.

The script reconstructs the coefficient of each of the three relevant monomials from an independent ordered-monomial expansion of the fourth power of the quartic polynomial; this is separate from the hardcoded simplified Hasse expressions. It checks that the field with \(u^2=3\) has order \(25\), independently enumerates the \(25^3\) triples, isolates exactly eight Hasse-zero smooth coefficients, verifies their Frobenius action and invertible Hasse Jacobian matrices, and counts points on each of the eight projective quartics by exhaustively enumerating \(651\) projective-plane points over \(\mathbb F_{25}\).

Computational scope: the finite enumeration confirms the conclusion over \(\mathbb F_{25}\). It cannot by itself rule out zeros over larger extensions; the algebraic elimination in `RESULT.md` does that. The direct projective point counts check maximality at \(25\) elements, not zeta functions of the curves over arbitrary extensions. The displayed symbolic Jacobian formula is checked at all algebraically possible geometric zeros, since the proof shows they all lie in \(\mathbb F_{25}\). No external audit or certification is claimed.
