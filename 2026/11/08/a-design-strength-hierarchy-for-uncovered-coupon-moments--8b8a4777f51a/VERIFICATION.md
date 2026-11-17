---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For every fixed r-set S the probability it stays unseen after t independent k-subset draws is a_S^t, so E(U_t)_r=(v)_r E_{S uniform r-set} a_S^t. Every deterministic k-subset avoids exactly binom(v-k,r) r-sets, hence E_S a_S=binom(v-r,k)/binom(v,k). For integer t>=2 strict convexity proves uniform sampler minimizes every rank r factorial moment. Equality requires every a_S constant. When r<=v-k, double counting complements C=V minus B yields Pr(J subset C)=binom(v-k,j)/binom(v,j) for all j<=r; inclusion-exclusion makes Pr(J subset B)=binom(k,j)/binom(v,j), exactly weighted r-design. Converse also follows by inclusion-exclusion. If maximal strength s<min(k,v-k), first strict difference at rank s+1 for all t>=2. Finite projective planes of any existing order q are 2-designs: all triple avoidance probabilities take a_1=((q-1)^2-1)/v and a_0=(q-1)^2/v with collinear fraction f=(q-1)/(v-2), so strict Jensen gives first discrepant third moment for all t>=2 and t=2 gap q³(q²-1)/(v(v-2)); q=2,3,5 exact rational gap verified fresh. The result concerns factorial moments, not stochastic domination or cover times.

## originality

PASS

Full 2026 Barak-Pelleg–Berend 'Fano Geometry and Slow Coupon Collecting' and 2025 Grunbaum–Yaakobi coverage-model sources address expected completion times/coverage, not an all-law fixed-time factorial-moment Jensen inequality with equality exactly equivalent to weighted block-design strength. Search of published Resultary finds distinct Fano completion tails, stochastic thresholds, and optimization, no implication for every factorial moment/equality. General Jensen and balanced-incidence double counting are classical techniques, not claimed new individually; their combined moment-detection/first-discrepancy theorem and all-projective-plane third-moment gap survive best-of-knowledge originality. Risk that equivalent statement exists as design folklore.

## value

PASS

Precisely identifies which fixed-time unseen-count factorial moments detect the design strength of an arbitrary weighted fixed-size sampling scheme, including sharp first discrepancy at strength+1 and a nonzero uniform projective-plane signature in all existing orders. This is a natural invariant of coupon-coverage laws and finite designs, useful without implying a cover-time stochastic order; more than a single unmotivated finite Jensen calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
