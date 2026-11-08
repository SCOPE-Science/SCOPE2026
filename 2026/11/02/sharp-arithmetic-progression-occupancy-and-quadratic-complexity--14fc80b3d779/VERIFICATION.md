---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For every integer b>=2, n>=1, start s>=0 and step d>=1, the difference-of-powers gcd identity forces the distance between r ones to be >=G_r=(b^(r-1)-1)/(b-1). The witness s=0,d=b-1 attains the exact H_b(n) logarithmic envelope. At critical n=1+G_r equality forces adjacent normalized exponents and the unique pattern at G_1,...,G_r, with r=1,2 treated directly. For words with at least three ones, exponent gap f<=floor(log_b(n-1)), the first two one indices (i,j) and f fix the entire factor, and s>=0 implies j>b^f i. Thus the injective encoding gives the stated finite double sum and the O_b(n^2) upper bound; no matching lower bound is claimed. I independently enumerated s<85, d<43 for bases 2-5, lengths 1-16, verifying H, critical uniqueness and subquadratic sample counts. Finite grids are not exhaustive.

## originality

PASS

Best-of-knowledge PASS. The known effective-alphabet theorem gives subexponential growth for r=1 but not an explicit quadratic AP-factor bound, exact occupancy, or critical rigidity for pure-power support. The published characteristic-support prefix envelope counts ordinary positions and is not equivalent to maximization over progressions with arbitrary steps.

## value

PASS

Arithmetic-progression complexity is a standard and substantially harder invariant than contiguous subword complexity for automatic words. Exact progression occupancy, unique jump-length extremizers and an unexpectedly polynomial rather than generic subexponential language bound give genuinely useful natural combinatorics of a sparse automatic sequence. The precise limitations are explicit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
