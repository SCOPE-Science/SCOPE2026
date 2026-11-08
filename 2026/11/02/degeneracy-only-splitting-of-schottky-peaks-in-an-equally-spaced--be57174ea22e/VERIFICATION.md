---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For Gibbs weights 1,b,c with J in {0,1,2}, exact moment algebra yields variance P/Z^2 with P=b+4c+bc and third cumulant Q/Z^3 where Q=(c-1)(b^2-bc-b-8c). Independent symbolic reduction reproduced both identities, and for sampled M≥256 confirmed derivative signs +,-,+,- at x=L,L+1,3L/2,2L+1. The proof bounds Q/(PZ)>1/3 at the negative checkpoints uniformly for M≥256; positive checkpoints use Q≤0. Continuity and analyticity force two strict local maxima separated by a minimum. Near hot/cold scales two adjacent levels dominate, giving x=L+4/L+O(L^-2) and 2L+2/L+O(L^-2), heights L²/4 and L². The midpoint is exactly 9L²/[2(sqrt M+2)]. Domain is integer M≥256 and strictly positive temperatures; at least two maxima, not an assertion of exactly two or of phase transitions.

## originality

PASS

Qualified PASS: de Souza et al. 2015 gives general three-level canonical formula and demonstrates two-peak effects from widely separated gaps and degeneracies. The present quantitatively bounded equal-adjacent-gap family (1,M²,M³), uniform M≥256 four-sign certificate, peak-location and valley scaling is not stated in the inspected primary discussion. Formula-level dependence is acknowledged, and older multilevel Schottky works may contain an equivalent equal-gap degeneracy construction.

## value

PASS

It is physically and mathematically motivated to separate gap-induced from degeneracy-only thermal anomalies. The explicit all-M cutoff and asymptotic two-scale peak positions show a rigorous mechanism for two maxima even at equal excitation gaps; not a mere temperature rescaling or a small sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
