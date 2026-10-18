---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The result uses scattered subsequences, not contiguous factors. For L=down(a^7) union down(ba^5ba) and K=down(aababa), principal-ideal substitution gives S=down((aababa)^7) union down(b(aababa)^5 b(aababa)); closures commute with this substitution because K is the downward closure of a single word. A separate independently implemented BFS over canonical maximal-subsequence antichains gives exactly 15, 8, 127 reachable distinct left quotients for L, K and S, respectively; 127 exceeds 15*8=120. Each maximal antichain defines a unique residual language, so reachable distinct antichains certify minimal DFA state counts, not merely NFA sizes. In addition, the ACTUAL certificate.json blob (not its VERIFY_OK log) was read and every one of 15+8+127 states and 30+16+254 letter transitions was checked independently for canonicality, correctness, reachability and uniqueness. This is a complete finite witness refuting a universal conjecture; it does not establish an asymptotic superquadratic lower bound.

## originality

PASS

Guyot, arXiv:2407.10355v1, Conjecture 2 in converted HTML (Conjecture 3.25 in PDF) states precisely the product bound for arbitrary overlapping alphabets; it is not a theorem or already refuted in the inspected original version. Its Theorem 3.2 proves the bound only for disjoint alphabets, and Theorem 3.3 when L is a product of atoms. Both hypotheses are absent here, since both inputs use the binary alphabet and L is the union of two incomparable principal ideals. Guyot already observes difficulty with overlapping alphabets, but no prior exact 15*8<127 counterexample was located in inspected material. An uninspected later author version may affect priority; this is a best-of-knowledge PASS with that explicit risk.

## value

PASS

An explicit small two-generator binary counterexample settles the truth value of the exact proposed product bound. State complexity for downward-closed languages is a natural automata invariant; the complete 150-state quotient certificate makes the falsification checkable. The seven-state violation is mathematically decisive despite small numerical excess, and it does not pretend to disprove every quadratic-factor upper bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
