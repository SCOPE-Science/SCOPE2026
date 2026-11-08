---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For independent rounds of uniform fixed-cardinality d_n=floor(cn) subsets with 0<c<1, set q=1−c,a=−log q, t_n=floor(log n/a), phase α_n. For any fixed R marked coupons, a prescribed inclusion/exclusion pattern in one round has exact hypergeometric factor (d_n)_s(n−d_n)_u/(n)_R = c_n^s q_n^u(1+O_R(1/n)); over O(log n) rounds this approximates independent geometric first arrivals with relative O_R(log n/n). Thus finite vectors of late first-discovery counts N_{n,k}, along α_n→α, converge jointly by all factorial moments to independent Poisson(c q^{k−1−α}) variables. Exact factorial moments of unseen U_{n,t_n+k} imply Poisson(q^{k−α}) and two-sided tightness of final offset T_n−t_n. A terminal batch at t_n+k has exactly r first discoveries there and none later, giving joint mass exp(−q^{k−1−α})(c q^{k−1−α})^r/r!, summed over k to H_{c,r}(α_n)+o(1). Its periodic profile has Fourier coefficients c^r Γ(r−2πim/a)/(a r!), nonzero for m≠0 since Gamma has no zeros; all phases realized by integer n, so no ordinary limit. Logarithmic weighted phase equidistribution yields mean mass c^r/(a r) and complete logarithmic-series law since Σ_{r>=1}c^r/r=a. Independent exact-rational direct finite subset-state Markov enumeration agreed with independent inclusion-exclusion terminal-multiplicity formula for n=3..6 multiple d and t; finite tests do not prove limiting independence.

## originality

PASS

Best-of-knowledge originality PASS based on direct comparison of exact statements, hypotheses and implications. Prior model ingredients and general lemmas are credited; no inspected full-text theorem establishes the precise additional classification. The named inaccessible and abstract-only comparisons remain risks, not proof of priority. A limit law for unseen count U_t at a single t gives P(T_n<=t), but not the full joint law of number newly seen in the last round: consecutive unseen counts and their dependence must be analyzed. The joint factorial-moment argument and subsequent Fourier/logarithmic averaging are additional steps beyond the inspected scalar limit statements.

## value

PASS

For fixed positive fraction group sampling, finishing a coupon collection can discover several missing types at once. The full last-round multiplicity distribution, nonvanishing lattice oscillations, multitime first-arrival Poisson structure and logarithmically averaged logarithmic-series law are natural explicit observables beyond expected completion time. The singleton finish probability c/−log(1−c) has a precise operational interpretation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
