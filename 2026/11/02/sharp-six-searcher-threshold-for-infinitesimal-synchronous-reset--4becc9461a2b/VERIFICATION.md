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

For independent fair nearest-neighbor lattice walkers started at 2 and stopped when any reaches 0, reflection gives Pr(tau_1>2m)=Pr(tau_1>2m+1)=a_m=(2m+1)/(m+1)*C(2m,m)/4^m. Thus mu_N=2 sum_m a_m^N, h_N=sum_m(4m+1)a_m^N and mu finite iff N>2, h finite iff N>4. Geometric reset after failed steps gives exact mean (1-q)(1-f_N(q))/(q f_N(q)), f_N=E(1-q)^tau, yielding right derivative mu²-mu-h for N>=5 and -infinity N3,4. Source check_restart.py provides outward integer fixed-point sums through m=9999 with analytical Wallis/integral remainder bounds, giving h+mu-mu² positive N5,6 (D6 in (0.082,0.084)), negative N7,8 and h9<2; monotonicity hN<=h9 and muN>=2 completes N>=9. Fresh independent long-series numerical sums corroborated approximate D5=3.8973,D6=0.08287,D7=-0.67706,D8=-0.90187, but unrestricted sign rests on the rigorous tail certificate, not truncation. N1,2 unreset infinite while any positive q has finite mean.

## originality

PASS

Biroli–Majumdar–Schehr derive a closely related Brownian continuous-space multiwalker restart threshold near 6.3556, yielding a similar 6-versus-7 integer division but not the fixed-site lattice renewal law. Das–Giuggioli study discrete-space reset first passage, principally single-walker. The exact lattice distance-two rigorous cutoff and narrow 6-walker margin were not located in primary material read; possibility of a general theorem already implying it remains.

## value

PASS

Distinguishing the exact effect of weak synchronized restart for parallel search on a discrete lattice is a natural lattice-scale phenomenon: a sharp six-to-seven transition proved for every N, not a sample or time-limited simulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
