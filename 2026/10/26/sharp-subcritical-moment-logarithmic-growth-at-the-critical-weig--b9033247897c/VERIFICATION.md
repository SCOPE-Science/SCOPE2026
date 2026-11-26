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

With u_i=|x_i|^p/i, the admissible set is exactly the probability simplex and F_k=Σ_{i>k}i u_i/(i−k). Set r=q/p. The uniform column bound for the first m=floor(δN) rows is mH_m, by monotonicity in i past m; Jensen then bounds the contribution to the normalized r-moment by (m/N)(H_m/log N)^r, tending to δ. On m≤k<N independently apply Hölder to (NF_k/(k log N))^r(k/N)^r. The two resulting factors are (Σ F_k/(k log N))^r and ((1/N)Σ(k/N)^{r/(1−r)})^{1−r}. The reciprocal decomposition i/[k(i−k)]=1/k+1/(i−k), with the first sum O_δ(1) and second ≤H_N per column, bounds the limsup of the first by one; the second is bounded in the limit by (1−r)^{1−r}. This verifies the sharp upper estimate without any restriction on support. For u_i=f(i/N)/Σf(j/N), f(s)=s^{r/(1−r)}/(1−r), the denominator is asymptotic to N. In bulk, writing i=k+j gives a bounded unweighted summand and a weighted harmonic sum with leading term (k/N)f(k/N)log N; split at j=ηN, use uniform continuity inside the split and bounded harmonic mass outside, then send η to zero. The integral of (sf(s))^r is (1−r)^{1−r}. The root converts the log exponent to 1/p and yields the claimed coefficient. For point-mass u at i≤N, the normalized sum is bounded by i^r/N times Σ_{j≤i}j^{−r}; i>N is no larger than i=N by monotonicity. No triangle inequality for q is used. The optional frozen finite witness diagnostic was inspected, not run.

## originality

PASS

Prior work gives boundedness failure, exact coordinate reduction at p, and adjacent finite-budget/weak-endpoint results. On this exact critical shift the p-moment is H_N before taking the root, whereas passing to q<p by Jensen gives only the leading coefficient one, not the strictly smaller sharp constant or a diffuse asymptotically maximizing profile. The strongest inspected lower-moment record uses the strict weight inequality α<1/p and a finite bound, not the critical harmonic divergence.

## value

PASS

The critical power weight is singled out by the loss of absolute Cesàro boundedness, and the exact lower-moment coefficient answers a natural refinement left open by the endpoint envelope. The argument identifies a structural change from a single-coordinate extremizer at p to diffuse lower-moment near-extremizers; neither nonboundedness alone nor the logarithmic order from interpolation gives that information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
