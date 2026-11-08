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

At the exact pinned result, +1 cross-role and -n same-role additive valuations make any individually rational coalition a role-transversal clique: a duplicate-role member has utility at most (s-2)-n<0. A strictly positive Nash product has only pairs/triples/quartets with factors 1,8,81. Gale-Ryser for four row degrees (a,b,c,d) and p,t,q columns reduces feasibility to 2p+3t+4q=n, q<=d, t+2q<=k=n-2a. The dominant class condition a>n-a forces a singleton/zero product, while a<=n-a admits a no-quartet baseline. An increase in quartet count q<min(d,floor(k/2)) is strictly profitable: for t>=2 replace two triples by a quartet and pair (81>64); for t<=1 use two pairs to make a quartet when C-a>=1 and p>=2 (the boundary p=t=1 yields the stated contradiction). Thus q*=min(d,floor(k/2)); at fixed q* maximize t subject to the parity t≡n mod 2 and t<=min(k-2q*, floor((n-4q*)/3)). The coefficient of e2^p e3^t e4^q times the role factorials divided by coalition-slot factorials counts labeled maximizers without overcounting. This covers n>=2 and d=0 boundary; no zero-product maximizer count is claimed. Pinned RESULT.md and exact verify.py were read. Separately enumerated all feasible size spectra on 178 sorted test profiles through n<=17; all maxima and unique p,t,q matched. The finite checks corroborate, not prove, the general Gale-Ryser/exchange argument.

## originality

PASS

The new four-nonempty-role classification is not just the known clique characterization or the single 81-versus-64 quartet example: it gives the globally forced counts for every role-size profile and exact labeled maximizer coefficients. Pagano–Schlenga 2026 establishes Nash welfare for enemy-averse hedonic games and discusses the local tradeoff; Bullinger–Chatziafratis–Shahkar study utilitarian welfare. An older all-class multipartite classification could cover the result under different language, but no concrete implication was found in inspected primary material or the published Resultary matches.

## value

PASS

The exact Pareto-type choice between pair/triple/quartet coalition sizes in four-role enemy-averse games is a natural constrained Nash-welfare optimization, not a tiny arbitrary instance. For all sizes it gives a sharp feasibility threshold, unique optimum size spectrum and a count of all labeled maximizing partitions. The four-role interaction q<=d and t+2q<=n-2a is new structural content beyond a routine substitution into three-role results; a researcher could use the formula and coefficient count for benchmarks and mechanisms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
