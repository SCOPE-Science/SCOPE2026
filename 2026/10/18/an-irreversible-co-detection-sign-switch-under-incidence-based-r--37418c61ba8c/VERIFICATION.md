---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Reconstructed definitions and proof for all N≥2, nonempty proper occupied sets A,B, and every fixed 1≤m≤N under uniform m-subset sampling without replacement. q_t(m)=C(N−t,m)/C(N,m) with zero beyond support; inclusion–exclusion gives C_m=q_(r+s−a)(m)−q_r(m)q_s(m). Nested sets have nonnegative C_m by I_A≤I_B. For nonnested sets, at m=N−(r+s−a)+1 joint miss is impossible while both marginal misses have positive probability, so covariance is strictly negative. On positive joint-miss support the successive-m ratio R_m=q_u/(q_r q_s) starts at R_0=1 and has multiplier minus 1 equal to [a(N−m)−rs]/[(N−r−m)(N−s−m)]; the numerator decreases in m, so a positive-sign segment can only precede a negative segment. C_1=(Na−rs)/N² gives strict two-sign iff nonnested and Na>rs. The bound Na>rs≥(a+1)² enforces N≥5; the complete N=5 arithmetic leaves precisely (2,2,1) and (3,3,2). For r=s=2,a=1 the exact polynomial x(x−1)(N−x)((N−2)x−2(N−1))/[N²(N−1)²(N−2)], x=N−m, gives positive m≤N−3, negative m=N−2, zeros at N−1,N. Independent shortest-subset exhaustive enumeration verified 3,774 rational covariance instances across 460 feasible parameter triples for N=2..10 and the full sign criterion, plus 5,040 exact special-family polynomial/sign comparisons for N=5..100. Source verification script and certificate were inspected; the unrestricted conclusion relies on analytic proof, not finite checks or certificate labels.

## originality

PASS

Best-of-knowledge PASS after fresh Resultary searches, four actual published mathematical RESULT.md comparisons, and full mathematical reading of accessible primary rarefaction/co-occurrence sources. Previously known sample-based rarefaction expectations and static incidence covariances are expressly credited. No inspected stronger theorem yields the overlap-dependent single sign-change classification, strict iff Na>rs, sharp N=5 onset, or all-N delayed-reversal construction. Unindexed older finite-population/survey literature remains an explicit residual priority risk.

## value

PASS

For fixed species-by-site incidence matrices, covariance of the two natural random pooled-detection indicators is a meaningful survey-scale dependence invariant, distinct from static site-level co-occurrence. The theorem gives an exact complete sign-order classification, a nonnested-plus-overlap iff criterion, the smallest population permitting reversal and both extremal five-site shapes, and a family with reversals arbitrarily late. These are motivated structural facts applicable whenever rarefaction changes pooled survey depth; not merely a relabeling of C_1 or a finite table. No general ecological causal interpretation or nonuniform-design extension is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
