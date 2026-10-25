---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

The launch law is q into shell 1 on halving and p2^(-(j+1)) into shell j on doubling, with return immediately at j=0. Conditional hitting probabilities solve ph_(j-1)+qh_(j+1)=h_j, h_0=0,h_m=1, giving (r^j-1)/(r^m-1) for r=p/q !=1 and j/m at p=1/2. The launch average qh_1+p Σ_{j=1}^{m-1}2^(-j-1)h_j+p2^(-m) yields the claimed rational quotient. Direct limits at r=1,2 and q=0 give H_m(1/2)=(1-2^(-m-1))/m, H_m(2/3)=(m+1)/(3(2^m-1)), H_m(1)=2^(-m). Separate expansions give mH_m→2a/(e^(2a)-1) when m(2p-1)→a and (3·2^m/m)H_m→(1-e^(-t))/t when m log(p/(2q))→t; removable zero arguments are treated continuously. An independently implemented rational hitting-system check passed 84 exact (p,m) combinations. Those checks corroborate but cannot prove the asymptotic statements. Time-to-return and stationary-law claims are excluded.

## originality

PASS

No matching maximum-shell-depth distribution or both parameter–depth crossover laws was found among the inspected mathematical sources. General gambler's-ruin probabilities and the Markov map representation are prior knowledge; the remaining claim combines a specific geometric launch law with an exact extreme-value law. The closest 2026 article concerns first-return durations, but its inaccessible full text is a concrete priority risk, not a basis for asserting full-paper noncoverage.

## value

PASS

The maximum approach depth toward the neutral fixed point during a completed excursion is a motivated stochastic-dynamical invariant. Its complete discrete distribution distinguishes the recurrence transition at p=1/2 from geometric-reinjection resonance at p=2/3 and supplies two nontrivial critical windows; it is not a single arbitrary finite parameter computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
