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

Starting on the left of c with slope m=2+a, the next branch has slope -m and the subsequent inner-left iterations have slope m up to the first exit to z_k<=1/4. Solving that affine recurrence gives exactly the stated z_j and -m^j for 2<=j<=k. The exit condition is a^2 m^(k-1)>=1, with k=O(log(1/a)), so the tail beyond k is O(a^2). I independently obtained the needed signed normalization from the published density series: write W=sum_{j<=k}m^-j=1/(1+a)+O(a^2). Then S=W+O(a^2). The leading indicator lengths are 1/2+a/4 plus errors whose weighted sum is O(k a^2), since for j>=2 each location correction is a^2(m^(j-1)-1)/(4(1+a)); the full integral I of g is (1/2+a/4)W+O(k a^2). Consequently Z=(1-2S+2I)/(1-2S)=-3a/2+o(a). Fixed-index indicators then converge on the a scale to the two opposite half-lines of total weights 1/2 each. At the left edge the fixed j>=2 threshold is (m^(j-1)-1)/(4(1+a)), hence the indicators select the limiting tail with u<q_j, while the j=1 term remains. At the right edge only j=1 switches. The shared inverse-slope tail bound controls the exchange of limit and series even for parameter-dependent later orbits; it bounds a*h uniformly and gives local L1 convergence. For bounded r_a/a the moving endpoints are harmless by local L1 and boundedness; for r_a/a tending to infinity a fixed a-scale window gives the lower bound and closed fixed windows in the published weak limit give the upper bound. The canonical representative and excluded jump values are necessary for the pointwise formulation. The frozen rational-checker code and notes were read, not run; the proof of the asymptotics is analytic, not an extrapolation of the sampled enclosures.

## originality

PASS

The exact map, series, pre-exit iterates, normalization estimates and atom were already available and are not credited as new. The supported distinction is resolving their cancellation and scale separation into local profiles, in particular an infinite left-edge staircase and a single right-edge step, together with the resulting all-radii law. The cited paper already integrates a shrinking interval to obtain the atom; it does not give the two edge blow-ups or the arbitrary-window statement in the sections inspected.

## value

PASS

The object is the standard expanding-map instability with a known point mass but unresolved local geometry. The coarser flat layer, narrower one-sided infinite hierarchy, and complementary single right jump explain how the atom forms. The resulting quantitative mass law for mesoscopic centered windows is usable where weak convergence is not, and the edge asymmetry gives information beyond the elementary mass and normalization checks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
