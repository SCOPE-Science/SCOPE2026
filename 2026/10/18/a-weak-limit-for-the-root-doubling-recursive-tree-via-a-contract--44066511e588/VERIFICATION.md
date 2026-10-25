---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

The exact root-only tree transition is b→b+1 with probability b/(b+1), b→2b+2 with probability 1/(b+1), implying E B_n=2n, EB_n²=5n²−n and tight X_n=B_n/n on [1,infinity]. The normalizing clock delta_n=log((n+1)/n) makes ordinary move exactly flow phi_delta(x)=1+(x−1)e^(−delta) and a root move exactly 2phi_delta. For the proposed PDMP with deterministic drift 1−x and doubling jumps rate1/x, the survival probability from x for time delta_n is x/(e^delta+x−1), so the first-jump event is exactly the discrete root probability; within-interval movement differs O(delta_n) on jump intervals, multiple jumps O(delta_n²), yielding finite log-time coupling on compacts since sum delta_n²=O(1/n). The PDMP Foster drift A x=2−x and common one-jump minorization on bounded [1,R] give a unique attracting invariant π; conditioning backwards from N at floor(N e^(−T)) with tightness proves full X_N weak convergence. At jump epochs reciprocal post-jump variable Zprime= (1−U+UZ)/2 contracts pathwise by at most 1/2; stationary occupation of drift cycles with finite expected time T yields explicit law; prior moment convergence transfers all polynomial moments without asserting moment determinacy. Independently computed exact finite law moments n<=10 and reciprocal update identities.

## originality

PASS

Björnberg–Mailler original root-doubling model proves exact limiting moments and tightness and expressly says their method does not establish weak convergence (Proposition 1.1, Remark 1.2). The present full-sequence weak limit plus explicit unique PDMP invariant and contractive post-jump reciprocal representation closes that precise gap; published general state-dependent PDMP ergodic tools may supply standard ingredients, but do not alone connect this discrete model to the invariant law.

## value

PASS

Closes a mathematical open convergence question explicitly left by the model creators: full weak convergence despite non-Carleman moments, with a unique invariant PDMP and explicit contractive reciprocal perpetuity occupation formula. This is substantive probabilistic structure, independent of the already known moments; no new moment formula is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
