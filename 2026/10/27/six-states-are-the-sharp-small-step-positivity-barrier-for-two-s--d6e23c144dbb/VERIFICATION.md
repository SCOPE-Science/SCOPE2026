---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The completed linear two-stage Radau IIA stability map r(z)=(6+2z)/(6-4z+z²) has Taylor coefficients a_1..a_5=1,1/2,1/6,1/36,-1/108. For any row Markov generator with n≤5, the first nonzero (i,j) power is exactly a positive path-sum at the shortest directed distance d≤n−1≤4; unreachable entries are identically zero, and diagonal entries tend to one. Thus every fixed such generator has a (not uniform in Q) positive small-step interval. The irreducible directed six-cycle first reaches displacement five at order h⁵, giving -h⁵/108+O(h⁶); longer directed cycles share this local sign failure. A direct rational-inverse computation for P⁶=I verifies the common positive denominator, four strictly positive offdiagonal numerators, the positive diagonal via Bernstein and shifted certificates, and N_5=h⁵(h⁵+15h⁴+60h³+90h²+36h−12). The latter polynomial has strictly positive derivative on h≥0 and a unique positive root τ≈0.208608859735, so six-cycle entrywise positivity holds exactly for h=0 or h≥τ; the h=1/10 negative witness is -743849/19268401151106. Exact rational checks independently reconstructed every 2..6-cycle class; irreducible cycle diagonalization yields eventual positivity for n≥6. These calculations prove only the explicit finite rational identities, not the general generator theorem, which follows from the shortest-path argument.

## originality

PASS

Best-of-knowledge original contribution as delimited by the final assigned theorem, not novelty of its foundational method. Direct original statements and implications were compared against the checked primary results and the published-finding search. Highly relevant inaccessible works remain named as residual priority risks; no failed search or abstract alone proves whole-document noncoverage.

## value

PASS

The smallest Markov state space permitting loss of end-step positivity at arbitrarily small positive steps is a natural dimension threshold for high-order time integration; an exact six-cycle return interval is a meaningful quantitative complement to generic SSP obstructions. The result is not merely a negative example: it supplies an all-generator five-state guarantee and a sharp classification for the six-state witness, clarifying what step-size reduction can and cannot fix.

The dated certificate retains the supplied scientific assessment, sources and limitations.
