---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For G=K_n∘K_1, signed graph-distance KR norm equals sum |leaf masses| + 1/2 sum |collapsed core masses|, by forced pendant flows and complete-core direct transport. Edge-difference heat vectors decompose into trivial and index-mean-zero two-by-two blocks, leading to exact two edge-type transport costs E_n=r_n+(3-n)q_n and P_n=(n-1)/n(2r_n+(n-2)q_n)-(n-2)/n e^-2t. For t>0 E_2>P_2; n>=3 P_n>E_n from explicit positive difference. Equality along nonzero spanning-tree flow edges determines extremal 1-Lipschitz potentials (ramp when n=2, n rays otherwise). A strictly decreasing derivative sign bracket has initial n-3, so n=3 decreases, n>=4 unique positive peak. Exact coefficient inequalities give strictly Λ<2 for every finite n,t while at t=log(n)/n, P_n→2. Time t=0 every nonconstant f extremizes. Boundary parameters and normalization stated.

## originality

PASS

Best-of-knowledge PASS for exact all-time Lipschitz heat norm and extremizers on complete-graph coronas, phase at n=4 and limiting sharp factor 2. Barik–Pati–Sarma Theorem 3.2 already supplies general corona Laplacian spectral decomposition, but not KR transport dual norm, edge-type max, extremal profiles, or amplification envelope. General heat-gradient/curvature methods describe other settings without this computed exact norm. Related Resultary complete-graph corona entry gives general-position polynomial, mathematically distinct.

## value

PASS

Graph heat flow need not contract edge-Lipschitz seminorm on these natural nonregular coronas. Exact all-time value, threshold for transient amplification at four core vertices, uniqueness of extremizing configurations and unattained sharp family norm 2 form a useful structural counterexample and envelope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
