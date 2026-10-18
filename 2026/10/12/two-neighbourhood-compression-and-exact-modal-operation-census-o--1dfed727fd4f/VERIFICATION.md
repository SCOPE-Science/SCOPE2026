---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The precise clauses evaluate every upset U_t through b_i=max_{S in N(i)}minS and d_i=min_{S in N(i)}maxS, taking empty-family E=(-1,n), empty-neighbourhood F=(n,-1), ordinary pair (b,d) in [0,n−1]^2 otherwise. Global modal outputs depend only on suffix minima B_i,D_i, and two singleton neighbourhoods realize any b>d, one interval realizes b<=d; E and F need zero/one. n>=2 top world b=n−1>d=0 witnesses two required. Continuality restricts E worlds to one prefix. Count monotone effective suffix signatures according to D=-1 prefix length t: t=0 ordinary paired weak chains, t=m all-F boundary, 0<t<m contributes Vandermonde sum, yielding the stated formula. Independent semantic enumeration for n=1..4 returns 3,22,224,2634 exactly. For arbitrary n truth equivalence follows induction on formula complexity and the derived local upset operator identities, not from sampled checks.

## originality

PASS

de Groot 2025 defines exactly these constructive-neighbourhood clauses and completeness; Dalmonte/de Groot later study proof theory, but no inspected passage gives the exact fixed-chain quotient, two-neighbourhood normal forms or the binomial census. Other published finite-chain KI-frame endpoint normal forms enumerate different relational semantics, so their numerical tables do not imply the present neighbourhood-family quotient.

## value

PASS

Semantic compression sharpness and exact paired-modal operation counts solve natural finite-model normalization/enumeration problems for the original constructive semantics. The fixed-base claim is precise and mathematical, not a rebranding of the general completeness theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
