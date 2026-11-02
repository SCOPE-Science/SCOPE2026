---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

Weighted RMS-AM yields N_T(f)>=||f||_1, and pointwise ℓ2<=ℓ1 yields upper S||f||_1. On period-m invariant component, residue aggregation gives b_mr, and a Borel selector E_m of one representative per finite orbit attains Σ_r sqrt(b_mr) by one-marker disjointness. If long orbits exist in positive measure for every L, a countable-cylinder separation of successive orbit points produces positive-measure marker E whose shifts are disjoint on any fixed finite window; their coordinate contributions give lower bound Σ_{k∈F}√a_k, tending to S. Strict positivity ensures S_m<S because each congruence class has several weights and sqrt is strictly subadditive. Equality with S would force all shifted positive-measure supports pairwise disjoint, impossible in a probability space. Pairwise ℓ1−ℓ2 deficit obeys (2−√2)∫min(c_k,c_l)≤S||f||1−N_T(f) and a finite-window upper bound by Σpairs∫min + ||f||1 Σk∉F√a_k; these establish the iff near-extremizer criterion for normalized f. Independent cyclic numerical checks of a_k=(3/5)4^(-|k|) confirmed S=3sqrt(3/5), S1=1, S2=(sqrt(17)+sqrt8)/5, and S_m<S for 1<=m<=19. These are illustrative, not a substitute for orbit-marker proof.

## originality

PASS

Dantas–Kaasik–Perreau introduced this exact orbit square norm and established general ||f||1<=N_T(f)<=S||f||1; the audited claim does not claim that construction. The inspected abstracts and related finite-truncation SCOPE result do not state the optimal constant as a function of period spectrum, equality classification, or full pairwise-extremizer equivalence. Complete original Dantas preprint body was inaccessible in this execution; unverified chance of an implicit sharpness lemma remains. Qualified best-of-knowledge PASS.

## value

PASS

The sharp comparison constant is a canonical geometric Banach-space invariant for this explicitly constructed family of L1 norms. The result identifies a genuine dynamical distinction between uniformly bounded finite orbit length and aperiodic/unbounded lengths, plus complete extremizer attainment and near-extremizer rigidity. It answers a natural quantitative gap left by a nonsharp construction bound without claiming new Daugavet or convexity theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
