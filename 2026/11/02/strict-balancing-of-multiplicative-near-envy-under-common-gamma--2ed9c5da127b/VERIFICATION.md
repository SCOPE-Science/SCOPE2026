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

Sums of iid Gamma(alpha,lambda) goods give independent Gamma(theta_i,lambda) bundle values, theta_i=alpha count_i; empty bundles cannot satisfy finite R. For a fixed shape pair i,j of total t, Beta–Gamma factorization makes S=Y_i+Y_j independent U=Y_i/S~Beta(theta_i,theta_j), independent of all other bundle values. Conditioning on S and others turns all ratio constraints into a symmetric central Beta interval [L,1-L], with L>=1/(1+R), independent of within-pair imbalance. The folded density of |U-1/2| is proportional (1/4-z²)^((t-2)/2)cosh(d atanh(2z)), with d=|theta_i-theta_j|. Ratios for larger d increase strictly in z, so balancing gives strict stochastic preference for every nonempty proper central interval; open positive-probability choices of other values guarantee strictly increased overall P. Finite sequence of T-transfers gives strict Schur-concavity and unique optimal integer balanced counts. Conditioning on minimum leads to integral sum_i∫f_i(x)∏(F_j((1+eps)x)-F_j(x))dx; Gamma density dominates the scaled integrand, yielding epsilon^(n-1) Γ(T)/(n^(T-1)∏Γ(theta_i)). Fresh numerical folded-beta comparisons checked 8 imbalanced pairs across R=1.2,1.5,2,5; analyticity and integrability, not finite checks, prove all-alpha/R.

## originality

PASS

Stochastic fair-division mechanism theorems use different strategies, agents or bounded valuations, and Dirichlet-extrema/range papers may encode the event but the accessible descriptions do not establish strict shape-majorization. A plausible Corrado 2011 original paper remains unread despite OA attempts and a protected Oxford request reporting disconnected VPN; this is a specifically stated best-of-knowledge risk, not automatic scientific failure.

## value

PASS

For fixed pre-realization allocations this gives the exact optimal size multiset at every nontrivial tolerance independent of Gamma scale and shape, plus a sharp near-equality asymptotic and multinomial occupancy link. It resolves a motivated nontrivial fair-division probability question, not a mere Gamma CDF restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
