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

For W_n=K1 join C_n with n>=3, unit edges and independent unit Brownian follower noise, dX_F=-L_FF X_F dt+dB_F gives stationary trace covariance exactly tr(L_FF^-1)/2. The two-shorted-terminal effective-resistance formula follows from minimizing an unrestricted quadratic energy split (negative component currents are permitted); summing over all vertices equals the grounded inverse trace. For T=3I-A(C_n), solving the exact circular recurrence establishes G_d=(q^d+q^(n-d))/(sqrt5(1-q^n)), with q=(3-sqrt5)/2, and sum_v resistances to one rim vertex=(2n+1)G_0-2. Differences between rim potentials give sum_v(r(v,a)-r(v,b))^2=8((T^-2)_00-(T^-2)_0d), and -d/da log(G_0(a)-G_d(a)) at a=3 gives the claimed R_n(d). For hub+rim, differentiating the path tridiagonal determinant gives H_n. On 0<d<n/2, s_n(d) grows strictly and phi(d)+phi(n-d) falls strictly because phi(t)=t/(e^{ct}-1) is strictly convex; thus maximum separation uniquely minimizes rim pairs. Direct rational n=3..8 comparisons establish all boundary cases (n=3 all 6 pairs tie at 3/4; n=4..6 opposite rim pair; n=7 hub+rim). For every n>=8, R_n(d)-H_n > delta_n=(n+1)/(2sqrt5)-2-(phi(n)+phi(2n))/sqrt5, delta_8=33sqrt5/10-36362/4935>0, and delta_n increases because phi is decreasing. Therefore n>=7 hub/rim is uniquely optimal by type, counting n rotations; no extrapolation from finite computations. Independent Python built exact integer grounded Laplacians, inverted them over rationals and compared 96 leader-pair orbit-class costs (n3..18), including 80 rim distances, to formulas. The exact cyclic Green inverse entries were compared to the closed form for all n3..29; n3..8 rational table verified. Git tree independently recomputed from eight actual blob SHAs and matched b45e2831ab01a1a071d63896a14d0f15dc69e8b4.

## originality

PASS

Best-of-knowledge originality for the exact all-size, all-pair wheel optimizer classification with its strict hub/rim transition at n=7, not for the general H2 objective, grounding/effective-resistance identity, cycle Green resolvent, or generic network optimization framework. The three primary arXiv papers were compared in full-text at their hypotheses and specialized conclusions; Resultary published-result searches and web searches found no dominating exact wheel classification. This is not historical-priority certification.

## value

PASS

Optimal placement of two noise-free leaders minimizing H2 coherence/steady-state variance is a mathematically motivated network-control problem. The unweighted wheel is a natural symmetric rim with structurally distinct hub, where coverage (opposite rim pins) competes against centrality (hub pin). The sharp switch at n=7, all placement equality cases, exact optimal costs and strict pair-distance ranking classify an infinite family rather than arbitrary tiny instances. The result provides a sharp, reproducible benchmark for network-design and leader-selection algorithms and illustrates a topological phase change not obtained by merely naming a known generic resistance objective.

The dated certificate retains the supplied scientific assessment, sources and limitations.
