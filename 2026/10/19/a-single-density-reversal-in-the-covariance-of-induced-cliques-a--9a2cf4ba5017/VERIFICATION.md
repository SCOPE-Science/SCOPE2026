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

Independently checked the ordered-pair calculation. Given a clique on T with |S∩T|=s, the sole missing edge of the near-clique on S must be one of a−b_s unshared edges, where a=binom(r,2) and b_s=binom(s,2). This also makes the joint indicator zero at s=r; s≤1 cancels by edge independence. Dividing the covariance by binom(n,r)(1−p)p^(2a−1) gives a decreasing sum of positive multiples of p^(−b_s) minus a constant, with the s=r−1 term strictly positive in its coefficient for every n≥r+1. Its limits at zero and one have opposite signs. At p0=(a−1)/a, Bernoulli's inequality makes every overlap contribution nonpositive and the identical-set contribution strictly negative. Only the last two overlaps occur at n=r+1, yielding p^binom(r−1,2)=2/(r+1). For r=3 the only off-diagonal term has A_2=3(n−3), giving 2(n−3)/(3n−8); at n=r the counts cannot co-occur. For large n with r fixed, A_3/A_2=(r−2)^2/[3(n−2r+3)] and the other ratios are O_r(n^−2). The s=2 term after dividing out A_2 has slope −(a−1)p0^(a−2) at its zero; the s=3 term there is −(3a−1)p0^(a−3)/a². These give the stated signed correction with an O_r(n^−2) remainder by Taylor expansion on a fixed neighborhood. Inspected the frozen verifier; its exact graph census at selected small n and numerical root checks are corroboration, not the proof. No frozen code was executed.

## originality

PASS

Pass applies to the general r≥3 theorem with its finite-size endpoint and fixed-r correction, not to the overlap technique or the exact r=3 case, which was stated in an earlier record. A later more general pattern theorem subsumes the threshold and correction when n≥2r−2, without establishing earlier coverage or the full small-n range.

## value

PASS

The covariance between a complete motif and its nearest induced defect is relevant when interpreting co-fluctuation of motif counts. The theorem distinguishes exclusion on the same set from positive correlation through shared present edges and proves exactly one reversal for every nontrivial graph order, including orders where small-overlap asymptotics are inapplicable. The finite endpoint and displacement of the threshold quantify this competition beyond the standard overlap bookkeeping.

The dated certificate retains the supplied scientific assessment, sources and limitations.
