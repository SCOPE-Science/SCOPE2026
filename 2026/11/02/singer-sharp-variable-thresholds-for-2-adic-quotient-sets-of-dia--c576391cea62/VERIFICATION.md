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

A nonzero evaluation has a unique least-valuation nonzero term because the residues of all nonzero terms modulo N are distinct. Dividing out that term gives a factor in 1+pℤ_p, an N-th power by Hensel since p∤N. Hence no quotient can leave the listed power cosets. Each coset is approached by quotients of single-coordinate evaluations: the bases of the powers range over ℚ×, dense in ℚ_p×. The power subgroup contains 1+pℤ_p, so is open and closed in ℚ_p×; adjoining zero to the finite union gives a closed set in the full field, and zero is an actual value quotient. At 2 and odd degree all units are powers, giving the exact difference-cover criterion. At most r(r−1) ordered differences can be nonzero, so r≥q+1 for N=q²+q+1. Independently checked the Singer argument including characteristic three: the trace polynomial X+X^q+X^(q²) is nonzero and has degree below q³, so the trace takes a nonzero value. For any c≠0, multiplication by c is invertible, giving nondegeneracy of the trace pairing. Thus a nonidentity coset cannot stabilize the trace-zero plane (equal kernels would give proportional functionals). Its translate meets that plane in exactly one projective point, giving one ordered representation per nonzero difference. Coefficients 2^d realize the resulting q+1 distinct residues, with all variables essential. This verifies the exact closure and attained lower bound with no reliance on finite sampling.

## originality

PASS

Credit the two ingredients to prior work: the translate-intersection argument already gives the sufficiency of a valuation difference-cover when all units are powers, and the optimal cyclic difference configuration is classical Singer. The remaining contribution is the exact tame all-unit-class closure for this distinct-residue family together with the sharp dyadic minimum obtained by applying that interface. The exact same closure is verified in a distinct cubic special case; a previously recorded general local coset statement is alluded to there but not identified. The inspected published theorems do not cover that general formula or already state the optimal existential dyadic variable law.

## value

PASS

The closure determines precisely which regions are missing in a non-dense quotient set, including unit-class obstructions that a density-only test with surjective unit powers cannot see. The exact odd-degree family separates the least attainable variable count (q+1, order √N) from the older universal sufficient count (order N), and gives coefficients realizing that gap for infinitely many exponents. The useful content is the sharp boundary for integral forms and the closure description, not recomputing Singer parameters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
