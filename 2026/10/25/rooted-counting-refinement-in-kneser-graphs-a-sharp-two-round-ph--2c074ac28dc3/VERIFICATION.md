---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Orbital quotient B_tu=binom(k−t,u)binom(n−2k+t,k−u) computed independently. The binomial-polynomial invariant space has k+1 distinct eigenvalues λ_j=(−1)^j binom(n−k−j,k−j); vertex transitivity gives nonzero P_j e_R, so Krylov powers A^r e_R span the orbital functions and are separated by k counting rounds. First-round classes root/zero intersection/remaining, second-round B_t0=binom(m+t,k) yields iff threshold m>=k−2. Odd quotient when m=1 yields a pathlike alternating BFS order of k+1 strata and exact k−1 rounds. Boundary k=1,2 and matching complement case verified. Independent quotient refinement checked 120 (n,k) pairs and 5 full labeled graphs; finite tests support but do not prove all n,k.

## originality

PASS

The Jordan/Kneser association-scheme spectra and odd-graph distance symmetry are old; reviewed claim is their root-refinement consequence with exact two-round density threshold and sparse depth. Inspected graph-partition and general WL studies do not directly state the one-anchor infinite-family classification; folklore priority risk noted.

## value

PASS

One anchor is minimal symmetry breaking. Establishing all k+1 orbit strata, sharp density threshold for stabilization in exactly two synchronous counting rounds, and unbounded sparse-depth k−1 gives a structural complexity phase in a natural infinite association-scheme graph family; not merely a restatement of standard eigenvalues.

The dated certificate retains the supplied scientific assessment, sources and limitations.
