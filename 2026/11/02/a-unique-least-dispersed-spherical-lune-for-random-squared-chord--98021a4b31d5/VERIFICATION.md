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

On S² with area-normalized longitude lune 0<alpha<=pi, integration using uniform longitude and polar density sin(theta)/2 gives centroid m=(pi sin(alpha/2)/(2alpha),0,0) and second-moment matrix diag((1+sin(alpha)/alpha)/3,(1-sin(alpha)/alpha)/3,1/3). Independence gives E||X-Y||²=2-2||m||² and Var||X-Y||²=4(tr(M²)-||m||⁴), proving both stated formulas. For t=alpha/2, q=(sin t/t)², exact derivative factorization dV(2t)/dt=q qprime[8H(t)/9-pi^4/32] holds, H=(t cot t)²+t³/(tan t-t) strictly decreases from 4 to 0 by explicit derivative inequalities; unique crossing produces a strict nondegenerate global minimum. Endpoints give Var(pi)=13/12 and limit Var(0+)=20/9-pi^4/64; the latter is lower than hemisphere, so maximum is unique there. Independent scipy root gives alpha=1.1164752259454593, variance=0.6753158386946392, matching the result; finite checks only corroborate the all-angle proof.

## originality

PASS

Qualified PASS. Classical spherical random-distance and chord results overlap at moment methodology, but the closest inspected paper requires pointed spherical cone bodies and treats geodesic/cap distributions. A pole-to-pole lune is not a pointed cone, and its squared ambient chord-variance shape optimum does not follow from that source. Generic integral-geometric tensor moment formulas are prior background.

## value

PASS

The parameter alpha ranges over the standard geometric family of spherical lunes, and squared Euclidean chord dispersion is a natural two-point shape statistic. Unique interior minimization despite strictly increasing mean gives a nontrivial global shape effect with exact endpoint rigidity and curvature. The precise optimal shape could be needed for stochastic geometry benchmarks; not an arbitrarily chosen finite subcase.

The dated certificate retains the supplied scientific assessment, sources and limitations.
