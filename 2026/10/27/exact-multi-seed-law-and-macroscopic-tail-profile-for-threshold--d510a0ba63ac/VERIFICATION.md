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

For each chosen terminal active set of size k containing s seeds, m=k-s candidate nonseeds must have sorted thresholds t_(j)<=s+j-1. Circular parking functions count exactly s*k^(m-1) admissible ordered vectors for m>0, with empty case one. All other N-k nonseeds must have threshold>k, yielding P(K=k)=C(N-s,k-s)*s*k^(k-s-1)/N^(k-s)*(1-k/N)^(N-k), including k=s and k=N yielding s/N. For fixed s and k>=epsilon*N, the exact ratio to the one-seed PMF tends uniformly to s. The one-seed distribution equals binomial mass B(N,k)/k and uniform Stirling yields N^(-3/2)/(sqrt(2*pi)*x^(3/2)*sqrt(1-x)); a binomial endpoint bound controls x->1, and integrating gives s*sqrt(2/pi)*sqrt((1-epsilon)/epsilon). Dividing gives conditional density sqrt(epsilon)/(2 sqrt(1-epsilon))*x^(-3/2)*(1-x)^(-1/2), no atom at 1. Independent exact rational normalization for N<=22 and exhaustive threshold vectors N<=7 confirm finite cases only.

## originality

PASS

Fontanari 2026 exact law is stated for one initial instigator; generalized parking functions are standard but enable the explicit multi-seed all-k PMF. Full accessible 2015 Karampourniotis et al. text studies heterogeneous thresholds, network topology and expected cascade sizes, not the asserted finite complete-graph discrete-uniform terminal mass. CRITICAL direct risk: Ishikawa–Fontanari arXiv:2608.20555 (20 Aug 2026) studies the same Granovetter model with initial seed fraction and Beta thresholds, claims exact finite-N combinatorial formulations. The beta(1,1) and seed fraction s/N can specialize the model, but the full text could not be read: arXiv PDF/HTML and OA failed, authorized Oxford returned vpn_disconnected. Its abstract does not display this closed parking-function PMF or the fixed-s macroscopic sqrt-N tail profile. PASS is qualified best-of-knowledge only, not proof of noncoverage; this source is high-priority before publication.

## value

PASS

A complete terminal-size distribution for every seed count and finite population size is a natural cascade-risk observable. The exact full-mobilization probability s/N, rare macroscopic-tail constant and conditional profile improve on the one-instigator law and on expectations, and mathematically explain multi-seed sensitivity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
