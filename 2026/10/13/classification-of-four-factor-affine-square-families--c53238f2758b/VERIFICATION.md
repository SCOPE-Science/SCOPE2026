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

# Verification

The theorem is proved symbolically in `RESULT.md`; no finite experiment is used as evidence for an infinite statement.

The critical checks are:

1. Unequal adjacent leading coefficients are impossible because the prime number theorem supplies a prime in a fixed proportional interval. In the first pair this prime occurs exactly once in the largest factorial and nowhere else. After the first factorial square is cancelled, the same argument applies to the lower pair; only a fixed number of linear block factors can interfere, while the proportional interval contains an unbounded number of primes.
2. Once both slope pairs agree, cancellation reduces the problem to a polynomial \(F(t)\) that is a square integer for every sufficiently large integer \(t\). The finite-difference lemma in `RESULT.md` proves that \(F\) must be a polynomial square: for \(k=\lfloor\deg(F)/2\rfloor+1\), the \(k\)-th forward difference of \(\sqrt{F(n)}\) is an integer tending to zero, hence eventually vanishes.
3. Each block polynomial has only simple linear roots. A polynomial square therefore forces equality of the two root sets. Any common block length at least two would make the two lower affine functions identical, contradicting distinctness, so both block lengths equal one.
4. The remaining product of two linear polynomials is a square precisely when the factors differ by a rational square. Clearing the reduced ratio \(r/s\) forces the smaller affine function to be divisible coefficientwise by \(s^2\), giving the common integer affine core \(H\).

The converse is checked by exact algebra:
\[
(r^2H)!(r^2H-1)!(s^2H)!(s^2H-1)!
=
r^2s^2H^2\bigl((r^2H-1)!(s^2H-1)!\bigr)^2.
\]

No computational cutoff, enumeration, or numerical approximation is part of the proof. The only non-elementary analytic input is the prime number theorem in fixed proportional intervals. No effective parameter threshold is claimed.
