# Self-review

## Correctness

PASS. For \(p=2q+1\ge7\) with odd prime \(q\), all nonresidues except \(-1\) are precisely the generators. The quadratic-character filter and standard total quadratic sum give the exact identities. For \(ac\ne0\), Hasse's bound on \(y^2=xQ(x)\) and its rational 2-torsion sharpen the elliptic trace bound to \(2\lfloor\sqrt p\rfloor\); the \(ac=0\) case is evaluated directly. Sign counts and thresholds follow by exact algebra. The standalone program independently tests \(84672\) normalized polynomial triples; finite tests are not the universal proof.

## Originality

PASS, with residual risk. Sun's 2014 public paper explicitly presents the two conjectures and a linear-shift theorem. Booker–Cohen–Sutherland–Trudgian (2018) already imply two-sign existence for quadratics over safe primes \(p\ge47\); that **covered component is not claimed new**. Their theorem is existential and does not give the exact signed count or discrepancy bound, while Sun's theorems address particular linear shifts. The specialized exact count, attained uniform envelope, and sharp small-safe-prime boundary were not found in the closely compared texts. A mathematically equivalent formula in other literature remains possible.

## Mathematical value

PASS. The exact count and sharp discrepancy bound solve the safe-prime case of a published quadratic-character conjecture, strengthen its logarithmic-size bound to a square-root envelope, and clarify a natural existential exceptional boundary. These facts bear directly on distribution among primitive roots, beyond a routine numerical table; the use of Hasse's theorem is acknowledged as classical.

## Limits and closest literature

Primary source: Sun, arXiv:1405.0290, §4 Conjectures 4.8–4.9. Strongest overlapping work: Booker et al., arXiv:1803.01435, Theorem 1. General safe-prime infinitude, arbitrary prime moduli, and independence validation are not claimed.

Self-review: passed. Independent audit: not yet performed.
