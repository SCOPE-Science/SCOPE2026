---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For a seed between successive monitors, each of its two simple edge-disjoint routes to its bounding monitors must be blocked for non-detection, giving exactly (1-p^j)(1-p^(ell+1-j)); a seed at a monitor always detects. Summing over all n seeds derives P(X>=1). The discrete second difference of H_p is (ell+2)p^(ell+1)(1-p)^2>0, forcing strict gap balancing maximizers and gap concentration minimizers except stated degeneracies. For a fixed monitor, distinct two routes to another vertex of distances d,n-d connect if at least one is open, so reachability p^d+p^(n-d)-p^n; translation and linearity give placement-independent mean. When k=2, P(X=2)=EX-P(X>=1), proving opposite objectives. Independently enumerated every edge mask/seed and monitor combination in 447 exact rational cases (n=3..7, p=1/4,1/2,3/4, k<=3), checking both detection and mean. Boundary p=0,1 excluded from strictness; trivial gap ties correctly scoped.

## originality

PASS

Qualified PASS for exact all-k cycle gap placement classification and the opposed detection-vs-corroboration extremizers under this specific uniform-seed iid bond model. The close full Leskovec et al. 2007 report gives general outbreak sensor objectives, submodularity and approximate sensor placement, but no exact cycle gap/equality theorem; its model allows general cascades and it gives generic approximation rather than this closed solution. Miller 2008 addresses outbreak probabilities as transmissibility varies, and Christakis–Fowler 2010 empirical sentinels and early detection, different endpoints. Existing two-sentinel path results have different graph and seed domain. General submodularity does not entail the strict balancing/equality cases or the two-alarm polarity. Equivalent network reliability/coverage results could remain outside the searches.

## value

PASS

Sensor selection on a cyclic contact network is a natural exact benchmark for stochastic network surveillance; placement trade-offs matter. The theorem is not merely an objective evaluation: it gives every optimizer and strict characterization at all k,n,p, while proving a nontrivial opposite criterion for two corroborating alarms, a mathematically useful distinction between coverage and redundancy. It is explicitly not a clinical deployment result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
