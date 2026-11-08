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

The prescribed f(t) is the absorbing first-hitting density for dX=v dt+sqrt(2D)dB, with c=L²/(4D)>0 and b=v²/(4D)≥0. For Q_tau(t)=∫_{max(0,t−tau)}^t f(u)du, Q_prime(t)>0 for t<tau, and for t=tau+s, Q_prime=f(s+tau)−f(s). The log ratio G(s)=c tau/[s(s+tau)]−(3/2)log(1+tau/s)−b tau has G_prime=tau[(3/2)s(s+tau)−c(2s+tau)]/[s²(s+tau)²]. Its quadratic numerator has one positive root and G runs from +infinity to −b tau (or 0 from below if b=0), so a unique descending zero yields the unique strict post-shutoff global maximum. Density unimodality makes delta<m<delta+tau and gives 0<d t_star/d tau<1 and d delta/d b<0 by implicit differentiation. Dimensionless substitution yields w=aT+(3/2)log(1+Tw)+w/(1+Tw) with w=c/delta, T=tau/c, a=bc. Root-order estimates supply all three T→infinity regimes, including varying aT/log T→theta. Independently reconstructed the G derivative symbolically and solved representative regimes: (T,a)=(100,0) gives delta≈0.0958106364483 for c=1, and (100,1) gives delta≈0.00877020045074; both match exact density-equality and slope signs. Source verifier is finite evidence only, not the infinite proof.

## originality

PASS

Novelty is assessed for the joint global one-maximum finite-pulse absorbed first-passage-flux theorem, strict pulse-duration/drift sensitivities and explicit driftless-to-drifting long-release crossover, not for the inverse-Gaussian first-passage law, impulse mode, moving-window convolution or step/fixed-pulse transport formulas, which are established. The closest primary 1999 Yu–Warrick–Conklin paper was newly inspected in full: it handles finite-pulse/step-input breakthrough curves via temporal moments rather than the maximum or logarithmic drift crossover. Relevant first-arrival and tracer-interpretation primary papers likewise do not assert the combined theorem in the material read. A stronger older translated-kernel theorem or inaccessible Kreft–Zuber paper may still imply some or all statements. Best-of-knowledge PASS with historical priority uncertainty, not a novelty certificate.

## value

PASS

Finite continuous-rate contaminant or tracer release at an absorbing downstream receiver is a mathematically natural transport observable. Its time of maximum loading after shutoff, strict reaction to source duration and drift, and the singular b=0 versus fixed b>0 delay scales with a quantitative crossover are substantive model-sensitive information not given by the classical impulse mode or by temporal moments. In particular, the driftless delay decays as inverse log T while fixed positive drift yields inverse T, so the limit is genuinely nonuniform as drift approaches zero. The result is an exact self-contained family theorem with clear physical and mathematical motivation, not simply a numerical fit, arbitrary parameter slice or new label on a textbook identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
