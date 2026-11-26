---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Reconstructed the 24 necessary constraints for right evaluation through degree five, including 2b_2=2b_3=0. The independently authored replay reviews/evidence/review1_certificate.py (Python 3 with SymPy) returned det=4096 and Smith diagonal consisting of twelve 1s and twelve 2s. Unimodular column transformations are invertible modulo four and preserve entrywise evenness, so the kernel modulo four of the necessary constraints has only even coordinates. For F=2G, the reduction of G may have arbitrary matrix coefficients, but test inputs and right multipliers reduce to lower triangular matrices. In each coefficient row (u,v), triangular evaluation imposes point vanishing of both scalar polynomials at 0 and 1 plus vanishing of the divided-difference sums for v. Multiplication by a lower triangular constant maps (u,v) to (alpha u+gamma v, delta v), preserving all these conditions (also when the diagonal entries of the test input coincide). Central powers preserve nullity by multiplying the evaluation on the right by the same input power. This handles every polynomial multiplier. The independent replay checked the displayed sextic at all 128 inputs and returned the nonzero value 2E21 for the right multiple at the displayed r. The lower bound is exhaustive by the constraint argument, not a search over a sample of polynomials. The supplied checker and its recorded output were inspected, not executed.

## originality

PASS

Credit the exact first instability degree, via a new coefficient-parity obstruction through degree five and stability for entrywise-even null polynomials in all degrees, not the same-ring construction or the sextic upper bound already given by Wu. No inspected source covers this lower-bound assertion.

## value

PASS

The ring is motivated by a known small counterexample distinguishing one-sided from two-sided behavior. Determining the earliest degree of that failure answers a natural exact sharpness question; the parity obstruction additionally explains why no smaller witness can work. This value does not depend on treating the sextic as new or extrapolating the cutoff to other rings.

The dated certificate retains the supplied scientific assessment, sources and limitations.
