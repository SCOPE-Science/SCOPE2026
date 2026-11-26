---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Reconstructed the quantifier-rank lemma. After r moves, compare the counts of each marked-coordinate row modulo truncation at 2s^(R-r) and match the kernel of the unmarked-component tuple. On a move a large parent cell of size at least s times the new threshold has a large child; copying small children leaves enough coordinates to fill all large children, on either side. The unmarked complement has room for each new independent choice. At the last move the row data distinguish zero, one and multiple contributions: all linear term equalities and the condition for a term to equal one marked basis vector are preserved. This also covers R=0. Conditioned on any fixed mark count, the uniform subset is independent with probability tending to one by the sequential span bound, including the possibility of selecting zero. Tightness and the binomial-to-Poisson limit justify truncation and substitution of the finite references. Exact-cardinality sentences and complements realize the entire stated spectrum. The compact subsum image has no isolated points by flipping late digits and admits covers with 2^(m+1) intervals of factorially small length, proving dimension zero and empty interior. Independently checked exact binary two-round types at (k,h)=(8,2) vs (9,3), (2,2) vs (2,3), and (2,2) vs (3,2), including a saturated unequal-count pair absent from the submitted tests. Replay: python3 /tmp/opencode/frozen_independent_checks.py (first output line).

## originality

PASS

Pass for the bounded-rank collapse and effective convergence in the finite vector-space language, not for the numerical Poisson-subsums form or its immediate topology in isolation. No inspected result was found to imply the marked-vector-space equivalence; this is a best-of-knowledge comparison, not historical priority certification.

## value

PASS

The explicit finite cutoff tells which bounded reference structures suffice for every sentence despite arbitrary nested quantifiers and linear terms. This is useful structural and algorithmic information about adding a sparse predicate to an algebraic host, unavailable from the convergence of the count alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
