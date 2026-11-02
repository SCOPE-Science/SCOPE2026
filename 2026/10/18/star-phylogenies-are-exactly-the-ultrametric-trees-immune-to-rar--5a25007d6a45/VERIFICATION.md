---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For finite strictly-positive-edge rooted ultrametric trees, N labeled individuals of strictly positive species abundances, uniform size-m sampling without replacement and legal a_i>=a_j+2 transfers, each edge/clade with mass u contributes l*f_m(u), f_m(u)=1-C(N-u,m)/C(N,m). On horizontal cuts, sum of these indicators integrates to expected rooted Faith PD. Increment f_m(u+1)-f_m(u)=C(N-u-1,m-1)/C(N,m) is nonincreasing, proving the star-like case (cuts one block or all singletons). For two individuals E=H+[sum_{r<s}a_r a_s d_rs]/[N(N-1)] and its transfer difference has numerator (a_i-a_j-1)d_ij+sum_{k not i,j}a_k(d_jk-d_ik). A nonstar ultrametric has an outgroup i and closer pair j,k, so a_i=3,a_j=1,a_k=M and all others 1 makes the numerator strictly negative for sufficiently large integer M; at m=N-1, the formerly unique j tip stops being omissible, increasing expectation by its positive terminal pendant length divided by N. For N<=5, the only three-species transfer is (3,1,1)->(2,2,1), and every possible clade partition has nonnegative gain; two-species cases are star-like and >=4 species cannot admit a two-unit donor/recipient gap. Thus six is sharp. For 3 tips with a=(3,1,2)->(2,2,2) and cherry length ratio eps, the m=1..6 differences are [0,(2eps-1)/15,(5eps-2)/20,(4eps-1)/15,eps/6,0]; independent labeled-subset enumeration verified eps=1/7,1/3,9/10, including [0,-1/45,-1/60,1/45,1/18,0] at eps=1/3, and independently enumerated all 186 small-census partition comparisons. Recomputed Git tree and inspected the actual checker source; the infinite theorem is analytic, not inferred from finite checks.

## originality

PASS

Best-of-knowledge PASS for the joint quantified characterization. Nipperess & Matsen (2013) already derive exact hypergeometric edge expectations and their star specialization; Nipperess (2016) already identifies the two-draw phylogenetic-evenness/Rao pairwise-distance connection; Chao et al. (2015) supply further fixed-profile accumulation/estimation. These are credited foundations, not claimed as new. Comparing the actual quantified propositions and deductions in their accessible technical text did not show a star iff all-population abundance-transfer theorem, every-nonstar negative-at-two/positive-at-N-1 witness, or the exact N=6 sharp transfer boundary. Cadotte et al. (2010) bears directly on clade abundance imbalance but could be read only in abstract, and its full technical content is not excluded. The finding is qualified by that and by potentially indexed older equivalent formulations, not a novelty certificate.

## value

PASS

This addresses the interpretation of greater abundance evenness in phylogenetic rarefaction: species-richness expectation is transfer-monotone, but the amount of sampled evolutionary history depends on relatedness. The precise natural-object boundary is all-equal-tip-distance stars vs every nonstar ultrametric. The two opposing sampling-depth effects under the SAME balancing transfer and the exact N=6/three-species minimal obstruction are reusable structural facts, not a trivial reparametrization, arbitrary numerical slice, or known-table recomputation. The proof provides an explanatory clade aggregation mechanism and minimal witness. It does not assert ecology causation, unknown trees, or all sampling designs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
