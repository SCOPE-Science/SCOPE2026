# Independent mathematical audit

## correctness

PASS

For three additive agents, known horizon m>=6 and each frequency multiset {H,1^(m-1)}, with H>(m-2)(m-3), the policy maintains nonempty completion by forced fill when remaining goods equal empty bundles. Before first shared-high arrival, only at most one unsatisfied agent is occupied; the shared-high good has an empty high recipient, who is frozen. Later distinct high values are allocated to owners or forced-fill singletons. Thus any high good assigned to a nonowner is in a singleton, and otherwise own value>=1 whereas deleting a unit from any other bundle leaves at most m-3 low goods. Gives 1/(m-3)-EFX. Adaptive adversary first delivers m-2 all-low goods and makes penultimate high for early recipients P, final high for complement. An exhaustive final-two-recipient case analysis bounds every realized allocation by max((m-2)/H,1/(m-3)), with the assumed H threshold giving matching equality. Independent game recursion for m=6,H=13 yielded exact 1/3 with 1964 cached states, and source code covers more horizons; quantifier proof is analytic.

## originality

PASS

The close Neoh–Teh 2026 primary work proves no horizon-independent positive EFX factor for three agents even in exactly this one-high/rest-low frequency model (Theorem 4.2 and Appendix C); its same terminal adaptive adversary is fully credited. But its proof chooses horizon to defeat a fixed alpha and does not give the sharp fixed-horizon minimax factor or a constructive online policy at all m>=6. Earlier Neoh–Peters–Teh supplies stronger general impossibility in a broader model but not exact finite-m frontier. A similarly titled five-good special value cannot imply all m>=6.

## value

PASS

Quantifies exactly how fairness decays with known finite planning horizon under the tight one-high predictive domain, supplying an explicit sure-ex-post online policy matching an adaptive adversary at every m>=6. This is a practically and mathematically motivated sharp quantitative refinement of known qualitative impossibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
