---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

In r=sqrt(x²+y²), cylindrical field is rdot=-(mu r/21)P(r,z), zdot=-z-r²/10, thetadot=1+e(z+r²/10), P=21r^4-125r²+400z²+100. P nonnegative for r²>=5 gives a forward radial bound; explicit variation of constants bounds z, hence global flow. The exact reciprocal-radius multiplier B=1/r has divergence [((15625mu-1764)/1764)-4mu(r²-125/84)²]/r, strictly negative a.e. on r>0 for mu<=1764/15625, excluding every periodic orbit and closed saddle separatrix via Green/Bendixson-Dulac. Reduced equilibria (r,z)=(1,-1/10) saddle, (2,-2/5) sink and (0,0) origin sink; bounded planar Poincare–Bendixson with unique saddle excludes other omega limit configurations. Hyperbolic convergence makes phase drift integrable; exact d/dt(theta+e z)=1 gives asymptotic phase. By Poincare recurrence every invariant Borel probability is carried on origin and two circles, and the saddle circle has a zero-volume stable manifold, giving exactly two physical ergodic measures. For general r^alpha multiplier, alpha<-1 gives divergence positive as |z|->infinity and for alpha>=-1 the minimized bracket is strictly decreasing in alpha, proving optimality at alpha=-1. Independent exact symbolic divergence, quadratic completion and Jacobian reconstructed; all orbits theorem uses actual topological proof, not finite simulation.

## originality

PASS

The exact underlying polynomial flow, two circles, their local stability and an unweighted-Dulac no-cycle bound mu<=588/6575 belong to Castañeda–Rebollo-Perdomo 2026; at mu=1/1000 their qualitative basin separator is also prior. The surviving new content is strengthened uniform parameter interval to 1764/15625 (factor 789/625), sharpness among radial powers, exhaustive all-forward-orbits convergence and all invariant/physical measures. General Bendixson–Dulac and Poincare–Bendixson principles are textbook tools; specific sign certificate and threshold are not in inspected older paper. No published Resultary entry for same field/threshold. Potential unseen same-family improvement remains.

## value

PASS

The enlarged certified global parameter regime and complete invariant probability simplex meaningfully resolve qualitative three-dimensional dynamics of a published counterexample family; inverse-radius optimization has explicit structural motivation, rather than an unmotivated tiny numerical improvement. Does not claim actual no-cycle threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
