---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The disjoint coding and strictly decreasing pressure give the unique s in (1/q,1); finite subsystems give the matching Hausdorff lower bound, and the probability is non-atomic as cylinder masses decay uniformly. Conditional on first symbol, the cell mass is exactly c^s[sum_(j>n) j^(−qs)+n^(−qs)Q_lambda(a)], including both endpoints. Reconstructing the tail expansion by Euler–Maclaurin and inserting x=H n^(1−q)+(a−1/2)n^(−q)/Z+O(n^(−q−1)) gives the same leading coefficient and linear correction c^s(a−1/2) in Kx^d. The −1/2 terms cancel and leave c^s(Q_lambda(a)−a); errors are uniform in a, and evaluation at a=lambda makes the order sharp. For t>0 use the same iid letters to count j>n, with at most m w_n probability of any mismatch. Here n is of order m^(1/(qs−1)) at fixed t, so m w_n and the Poisson mean error are O(m^(−1/(qs−1))); Le Cam gives O(m^(−1)). This establishes precisely the stated upper rate, not optimality of the Poisson rate. At t=0 no coded point equals zero almost surely; the survival limit follows from zero visits. Replay: RESULT.md, Eqs. (1)–(3) and proof §4, with the above reconstruction. Frozen verify_endpoint.py was read, not executed, and its two reported local examples do not directly test the TV estimate.

## originality

PASS

The reflected branch family, pressure root and general rare-event theory are not new. The inspected sources do not give the fixed-parameter uniform singular endpoint correction or this rate and constant for the specified invariant coding law.

## value

PASS

The accumulation point has a meaningful local dimension different from the survivor dimension. The sharp order and uniform branch-plus-gap profile expose the full singular CDF behind a leading power law; the independent-letter bound turns the local estimate into an explicit, usable error for orbit counts. This goes beyond re-evaluating the known pressure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
