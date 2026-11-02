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

Construct computable disjoint directed p_e-cycles indexed by (e,t) with a unique unary H mark when M_e first halts at step t. The marked p_e-cycle A_e maps into B iff M_e halts, since directed cycle homomorphism requires prime p_d|p_e and the mark requires a witnessed halt. Thus finite CSP(B) is c.e.-complete. For total computable input G, W_G={n:G|n→B} is uniformly c.e. and downward closed; hence FirstBad_B(G) equals MinMissing(W_G). Conversely from a c.e. index W_e, place gadgets A_{q(e,i)} in computably bounded consecutive intervals, where q(e,i) halts iff i enters W_e. The first failure belongs to the least missing-index interval (proper prefixes of the marked directed cycle embed in some arbitrarily long marked target cycle), and computed cumulative boundaries recover i. All prefixes map iff W_e=N, giving promised Π0_2 completeness, not a Weihrauch-degree assertion. Essential infinite argument is uniform effective reduction, not a finite experiment.

## originality

PASS

Distinct from the published finite-template first-prefix theorem, which uses decidable homomorphism tests and yields the first-zero LPO degree. Here the fixed computable infinite template has a c.e.-complete finite CSP, yielding Π0_2-complete total-computable input index set and exact least-missing-index reductions. This is an explicit universality construction, not a claim that halting encodings or arithmetical hierarchy methods themselves are novel.

## value

PASS

A mathematically motivated sharp boundary for first finite obstructions: with finite fixed templates each finite CSP test is decidable and yields a first-zero computation degree, whereas one countable computable template with just one binary and one unary relation reaches exact Π0_2 completeness. The precise least-missing-number output reduction, not bare undecidability, makes the example useful to researchers on effective infinite-template CSPs; the intentionally artificial encoding is acknowledged.

The dated certificate retains the supplied scientific assessment, sources and limitations.
