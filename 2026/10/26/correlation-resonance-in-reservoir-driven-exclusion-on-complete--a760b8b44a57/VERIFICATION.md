---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Irreducibility: one can remove each B particle and transfer residual A particles to B for removal; from empty, form the desired B subset by successive A injections and transfers, then inject the desired A subset. Uniqueness implies within-class exchangeability. The single-site balances are n d=alpha(1-x), m d=beta y, and net edge flux is x-y since the blocking terms cancel. For the cross pair, write U=eta_i-x and V=eta_j-y. Their shared swap changes the product to (V-d)(U+d), with mean change -d^2. Other edges replace one centered factor, yielding (m-1)(u-w)+(n-1)(v-w); the bath terms contribute -(alpha+beta)w. Within a class both sites give the same drift n(w-u)-alpha u, or m(w-v)-beta v. Solving gives all three covariances and their strict signs. At fixed ratio, write D=tG and d=t/(t+C). The derivative of |w| has numerator H=(C-t)G-t(t+C)G' and positive denominator (t+C)^3 G^2. Each reciprocal contribution to H has derivative -[(2C-p)t+p^2]/(t+p)^3, or the analogous q term; hence H strictly decreases from positive at C to negative at infinity. The unique root is the maximum and exceeds C. The balanced expression gives N|w(N tau)|=tau(tau+1/2)/[2(tau+1)^2(tau+1-1/N)]. It and its tau derivative converge on compact positive intervals; the limiting derivative has numerator 1+2 tau-2 tau^2. Bracketing the unique finite-size root on either side of the positive limiting root gives both constants. For gamma<1, d~N^(gamma-1)/L and D~K N^gamma; at gamma=1 all four terms of D are order N, and above it d tends to 1 and D~(a+b)N^gamma. Replay: RESULT.md lines 78–120 and the direct generator steps above; the reported exact count-chain check is finite supporting evidence, not required for the proof. The optimum concerns covariance magnitude, not the Pearson correlation coefficient, which in the balanced case does not have this optimum.

## originality

PASS

The open-graph model and two-particle covariance methods have established precedents. In particular the all-sites baths fit an earlier general model, and the equal-rate part fits a later indexed Green-function representation. Neither inspection covers the unique magnitude maximum for every fixed positive source/sink rate ratio, its strict threshold, or its balanced scaling constants. The closest indexed optimum uses a different process, observable sign, and scan parameter.

## value

PASS

An all-rates exact stationary covariance in a basic solvable open-network geometry gives a rigorous rate selection law. The unique interior peak, explicit crossover and balanced constants quantify how the nonequilibrium covariance responds when both reservoirs speed up, in contrast with the strictly increasing net flux at fixed rate ratio. This goes beyond a sign test or a single numerical optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
