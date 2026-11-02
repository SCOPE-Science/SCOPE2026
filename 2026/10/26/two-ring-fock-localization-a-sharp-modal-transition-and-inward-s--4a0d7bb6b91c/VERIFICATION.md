---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Radial Toeplitz diagonalization yields exact gamma-density integrals. The adjacent difference is a signed four-exponential polynomial with no more than three zeros; outside the two annuli the difference has fixed sign. Stirling/Edgeworth expansion uniformly with derivatives at index n=T+s sqrt(T) gives symmetric Gaussian mixture G_delta and first odd correction J_delta. The derivative roots of G_delta are one for 0<delta<1, three for delta>1 with a unique positive r satisfying r=delta tanh(delta r). Zero counting upgrades local root persistence to global modal-count classification. Evaluating J_delta(±r) yields positive inward-vs-outward height gap C_delta/T+O(T^-3/2); optimizing the primary peak gives stated norm. Independent gamma-integral sampling at T=5000, delta=.6 and 1.5 confirms one and two maxima and inward dominance; finite sampling does not establish large-T quantifiers.

## originality

PASS

Daubechies/Knutsen provide radial eigenvalue gamma integrals and one-ring localization, Dewage–Ólafsson establish general quasi-radial spectral algebra, and the symmetric Gaussian-mixture phase transition is classical. The specifically signed first correction to two competing integer eigenvalue peaks and its global modal census do not follow from these statements without further analysis. Unindexed gamma-mixture asymptotics may contain an equivalent result; Knutsen full source inaccessible in this run.

## value

PASS

Competing thin Fock localization rings form a natural multi-region spectral problem. The theorem distinguishes the emergence of an extra local maximum from global selection, and computes a positive order-T^-1 asymmetry invisible at Gaussian leading order; useful for localization-operator norm estimates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
