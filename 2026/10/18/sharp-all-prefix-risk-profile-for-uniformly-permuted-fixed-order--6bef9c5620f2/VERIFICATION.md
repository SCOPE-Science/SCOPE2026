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

Grand-center the fixed vectors and write the prefix sum as the sum of q full block totals plus the fixed r-position total of the next block J. E[S]=mean(C); conditioning on J=j gives expected full-block contribution −qB_j/(K−1), proving the mixed term, with the squared bias retained. In scalar coordinates split the input into its common within-block position profile and its zero-sum block contrasts. Their orthogonal risk forms have top quotients D/K and λmax(M)/K, respectively, where M acts on the all-ones and centered r-position indicator directions by [[A,H],[H,D]]. The contrast form is PSD and its top eigenvalue is at least D; a pair of opposite block contrasts realizes it. The RR squared-norm coefficient for the unnormalized prefix is m(n−m)/(n(n−1)). For the strict gap there is a separate trace proof: T−(A+D)=D/(K−1)>0 when 0<r<b, and a PSD two-dimensional form has largest eigenvalue at most its trace. This covers q=0 and q=K−1, including K=2. At r=0 only block-constant contrast directions attain the nonzero bound; the within/between decomposition gives the claimed strict improvement rule. Scalar arguments extend coordinatewise, with positive RR risk exactly for nonconstant data. Independent finite replay: python3 -B /workspace/branches/reproduce_frozen_checks.py 2 checked the entire exact centered permutation-mask second moment at 72 prefixes (2≤K,b≤4), including the bias term. The frozen recorded finite checks were inspected, not re-executed.

## originality

PASS

Pass is for the explicit, attained incomplete-prefix comparison and its strict gap, in the frozen matched-individual-budget fixed-order design. Complete-cluster design effects, the RR comparator, and the complete-block variance formula are established ingredients, not distinct contributions. Search and claim comparison are bounded. The v1 Mishchenko finite-population lemma is in Section 6 (Eq. (17)), rather than the frozen reference's Section 7: the locator does not affect the result.

## value

PASS

Matched individual-gradient evaluation budgets make incomplete blocks unavoidable in a prefix comparison. The result gives an exactly attained uniform benchmark at each such budget, accounts for the otherwise missed order bias, and isolates where the coarser complete-block inflation factor cannot be sharp. This is a useful finite-population design invariant without implying any optimization-iterate or runtime improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
