---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Gaussian projection to the sum-zero hyperplane gives exact W=2 sqrt(2) M/(sqrt(n-1) R), M=max_{ij in E}|g_i-g_j|/sqrt(2), R^2=chi²_{n-1}/(n-1). Disjoint edge increments are independent; adjacent increments have |correlation|=1/2, yielding joint tail <=4 exp(-2u²/3). Bounded-degree dependency components contribute o(1) to fixed factorial moments at u=b+x/b, while singleton components converge to Poisson mean exp(-x), giving the Gumbel law; chi correction is negligible since b²=O(log n). To prove uniform angular probability, integrate the independent far-edge maximum distribution against uniform variable m*p(Y_e), dominate by a linearly large matching, and exclude nearby wins with the same m^-4/3 joint tail; each orientation gets half the winning-edge probability. For star, leaf upper/lower extrema combine with one common center Gaussian to give |Z|. Independent checks: 150 exact support identities, 11,500 path samples at n=850 with empirical CDF 0.3792 vs exp(-1)=0.3679, star sample mean 0.998 vs asymptotic 0.798 (visible finite-n centering bias). No finite result proves the asymptotic law.

## originality

PASS

Statement-level implication and object/parameter comparisons checked in cited primary literature and Resultary; novelty is best-of-knowledge, with named inaccessible full texts and generic-theorem risks. The previously known subclaims are explicitly excluded from the novelty claim.

## value

PASS

Two natural metric/geometric invariants of symmetric edge polytopes—random width and root normal-cone angle—exhibit universal asymptotic behavior even on nontransitive bounded-degree graphs. The star comparison isolates a substantive boundary where a hub changes both the leading scale and fluctuation distribution. Normal angles quantify angular visibility not captured by facet counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
