---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Independently reconstructed the pressure-coordinate proof for the frozen closed, fixed-susceptibility SIR equations with one infectious pool. With x'=I and positive I, s_j=s_j(0) exp(-lambda_j x) and I=1-R(0)-gamma*x-s_1-s_2. Write H=sum lambda_j*s_j, K=sum lambda_j^2*s_j. Then H'=-K<0, I'=H-gamma in pressure and the time derivative of incidence IH is I times Q=H(H-gamma)-IK. I reproduced the exact finite certificate independently using alternating Taylor bounds for exp(-z/32) at orders 22 and 23 on [0,5/8], then raising the positive interval to the 32nd power; the original used reciprocal positive Taylor bounds and was read, not executed. Replay: /workspace/branches/record-4-independent.py. All twelve printed I,H,Q intervals match RESULT.md exactly, including signs +,-,+,- for Q at 0,1/50,1/20,1/5 and H(1/5)>4/5. Monotone H ensures I'>0 throughout that pressure interval and hence I>=I(0)>0; the inverse time integral of 1/I is finite there. The analytic nonzero Q has isolated zeros, so each open interval between successive checkpoints contains a sign-changing zero in the required direction, giving strict maxima, minimum, maximum. H decreases to zero; the unique pressure solving H=gamma is later and reachable with positive I, which by then has increased. Continuity of the strict endpoint signs and the H margin gives an open neighborhood in admissible parameters and initial fractions (including positive initial removed fraction). The proof shows at least two incidence maxima, not an exact count or repeated prevalence rises. The quoted 3.72496275 is the initial effective reproduction factor H(0)/gamma; the fully susceptible normalized 49:1 mixture would give 3.725. The distinction is nomenclatural here and neither number is needed for the proof.

## originality

PASS

Existing multiwave examples and the heterogeneous SIR reduction are credited. The supported distinct claim is a strict incidence double maximum in one rising-prevalence interval in the autonomous pooled two-susceptibility model, with an exact localized witness and open persistence. A later Resultary finding materially repeats the central existence theorem with different parameters and strengthens it by proving one class insufficient. This is real statement-level overlap, but the archived record of that result is later, and their shared earlier initiating paper supplies the model rather than either incidence witness. No evidence of prior public coverage of the exact claim predating the frozen record was verified; dependence and broader priority are not certified.

## value

PASS

The construction gives a useful exact counterexample to identifying the number of peaks in aggregate incidence with the number of rises in aggregate prevalence, without changing a transmission coefficient over time, using latent stages or separating infectious pools. The complete rising-prevalence interval and persistence under admissible small changes matter: the example is not just a numerical trace with one shallow wiggle that vanishes in the exact equations. This is value as a mathematical shape distinction, not as a prediction of clinically separate waves, and does not rest on the numerical depth of the trough.

The dated certificate retains the supplied scientific assessment, sources and limitations.
