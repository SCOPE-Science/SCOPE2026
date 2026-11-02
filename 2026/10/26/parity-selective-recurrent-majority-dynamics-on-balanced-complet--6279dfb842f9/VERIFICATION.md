---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Reconstructed the parallel open-neighborhood rule: each of the s vertices in part i sees T−t_i ones and either becomes uniform or retains its word on equality with h=(r−1)s/2. A periodic mixed part must tie at each update, so all mixed parts have a common occupancy t; equal numbers α=β of full/empty switching parts and total-ones balance give (k−1)(2t−s)=0. Thus the coefficient [z^0](C_s+z+z^(−1))^r counts balanced uniform/half-filled parts, with precisely r*binom(r−1,(r−1)/2)*(D_s−C_s) extra one-mixed cases for odd r. The sole fixed states are two unanimous plus C_s^r all-half-filled configurations. A separate tied/not-tied transient argument gives F^5=F^3; part counts (0,3,3,3,4) for r=s=5 attain entry time 3. Stirling/local Laplace on the central coefficient establishes the parity asymptotics. Independent vertex-bit iteration checked Q,P and F^5=F^3 for (r,s)=(2,1),(2,2),(3,2),(4,2),(3,3),(5,2),(4,3), matching respective (Q,P)=(2,4),(6,8),(10,22),(18,72),(2,38),(34,254),(2,8). The finite checks corroborate, not prove, the all-parameter result.

## originality

PASS

Best-of-knowledge PASS for the exact all-r labelled periodic-state census, parity-sensitive asymptotics and sharp uniform entry bound on equal-size complete multipartite graphs. Classical finite threshold period-two theory is a premise, not the enumeration; prior exact tripartite special case is acknowledged. Indexed parity automata and static C-colourings measure non-equivalent objects.

## value

PASS

An exact structural classification of all recurrent labelled configurations and uniform transient depth in a natural highly symmetric majority dynamical system; the odd/even part-size and number-of-parts transitions are not a routine restatement of period-two convergence. The result describes a reusable testbed for synchronous consensus and recurrent-state counting without asserting unrelated graph families.

The dated certificate retains the supplied scientific assessment, sources and limitations.
