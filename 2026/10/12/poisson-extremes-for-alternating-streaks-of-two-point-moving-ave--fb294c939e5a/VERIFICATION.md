---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the stated scientific claim

The included `verify.py` is a standalone Python 3 exhaustive rational checker. Invoke `python3 verify.py` from the directory containing this file. It enumerates \(1{,}641{,}300\) permutations in two independent groups of small finite windows, checks the exact parity-chain event probabilities for \(1\le r\le7\), and confirms both finite \(H_n\) tail inequalities for \(2\le n\le8\). It also checks ten finite overlap probabilities, including the exact longer-run identity and the two-shared-coordinate upper bound. A successful replay prints `VERIFY_OK enumerated 1641300 permutations`.

The mathematical proof, not this enumeration, justifies all integers and the infinite-time results. Its nonstandard ingredients are the conditional shared-coordinate rank-density bound (density ratio at most \((m)_s\)), the exact overlap equivalence for distances below \(r\), and the dependence-neighborhood calculation. The Poisson theorem applied is Arratia--Goldstein--Gordon (1989), Theorem 1, with zero remote-dependence term. The almost-sure result additionally uses Stirling's formula, a disjoint-window lower bound, and Borel--Cantelli on dyadic sample sizes.

The package establishes no external audit, no peer-review certification, no uniqueness of a centered longest-streak limit, and no theorem for unequal smoothing weights.
