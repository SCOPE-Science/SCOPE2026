---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

At I0=a,S0=1-a,R0=0, let r=(1-a)/a,u=beta*a. The I2=I1 condition is beta*S1=gamma, hence beta=u(1+r), gamma=u(1-u)r, I1=(1+u²r)/(1+r). Descending transversal derivative of beta*S1 at fixed a is (1-a)(1-2u)<0, so u>1/2; S1>0 implies u<1; all subsequent susceptible updates stay strictly positive iff at the crossing beta*I1=u(1+u²r)<1, equivalent to r<(1-u)/u³. Since max such r tends to 4 as u down to 1/2, a>1/5 is exactly necessary and sufficient. The jump S1-S2=gamma I1=u(1-u)r(1+u²r)/(1+r) increases in r, yielding J<(1-u)²/(1-u+u³)<2/5 by factor (2u-1)(u²-2u+3)>0. Boundary approach supplies unattained sharpness. At a=2/5, u=8/15, r=3/2, rational witness gives J=5992/28125. Off-crossing global peak placement follows S_t monotone and sign(I_{t+1}-I_t)=sign(beta S_t-gamma). Independent rational checks corroborate exact algebra.

## originality

PASS

Ozbay–Nielsen–Nguyen already report nonmonotone cumulative attack at peak and discrete peak-day jumps, which are not asserted new. Their investigated Euler behavior and plotted bifurcations do not present the sharp strict-positive day-two-to-one feasibility threshold a>1/5 or supremum 2/5 as mathematical theorems. Broad discrete renewal frameworks, nonstandard SIR integrators, and continuous-time overshoot instead use different update laws or peak quantities; neither statement implies the inspected sharp pair. Published Resultary hits concerned other SIR transitions. Unindexed analysis of the same numerical example remains possible.

## value

PASS

The early peak-switch is a natural singularity in peak-time epidemic metrics. The strict seed threshold and jump ceiling are nontrivial universal optimization constraints emerging from positivity and transversal dynamics, precisely sharpening a numerically known phenomenon, rather than replotting a known sawtooth.

The dated certificate retains the supplied scientific assessment, sources and limitations.
