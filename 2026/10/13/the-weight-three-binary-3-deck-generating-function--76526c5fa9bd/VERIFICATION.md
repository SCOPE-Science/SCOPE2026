---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The three counts for 011,101,110 impose respectively 3 delta a+delta b=0, delta b+delta c=0, delta c+3 delta d=0, so the only possible gap displacement is t(1,-3,3,-1) for integral t. Let p=(a,a+b,a+b+c) count zero prefixes before each 1; these change by t(1,-2,1). In sum_i binom(p_i,2), the linear part of the change is t(p_1-2p_2+p_3)=t(c-b) and the quadratic part is 3t^2. The shifts sum to zero. For fixed zero total m=n-3 the suffixes are m-p_i, and sum_i binom(m-p_i,2) differs from the prefix count by an affine function of sum_i p_i; hence the 100 change equals the 001 change. The three exactly-one-one counts sum to 3 binom(m,2), so the 010 change is minus twice that change. The all-zero and all-one counts are fixed. For a distinct partner, t=(b-c)/3 is thus forced; the partner is allowed only if all gaps stay nonnegative. Orient by increasing a and write d=t+e, giving the stated unique parameterization with no missing or multiply counted class. Its length is a+e+2c+4t+3, yielding the correction series with first possible term z^7, while all words contribute z^3/(1-z)^4. For n<3 both counts vanish. Independent replay: python3 /workspace/checks/5.py constructs decks by incremental subsequence counts (without gap formulas), classifies 58,905 words for n=0..35, and checks every resulting pair and the coefficients computed by successive geometric-series multiplication. The census corroborates but does not prove the all-length argument.

## originality

PASS

The exact rational generating function and one-dimensional kernel were already stated, as conjecture and proved partial step respectively. The distinct claim assessed here is the all-length proof and exact pair classification for the fixed-weight slice. Indexed records later in October/November contain the same result, including the identical parametrization up to renamed variables, so the catalogue now has duplicate mathematical coverage. Those entries do not establish coverage before the October 13 frozen record. In the substantially earlier primary text, the general generating function is expressly conjectured and only 20 coefficients are checked. No earlier exact theorem was established in the comparisons performed; this is not a historical-first claim.

## value

PASS

The weight-three slice is singled out in the published enumerative problem, not chosen post hoc. The nontrivial collision classification resolves a named exact generating-function conjecture, explains both the delay to length seven and the rational correction factors, and yields the exact equivalence classes rather than just an improved finite coefficient list or asymptotic bound. No unrestricted binary 3-deck enumeration is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
