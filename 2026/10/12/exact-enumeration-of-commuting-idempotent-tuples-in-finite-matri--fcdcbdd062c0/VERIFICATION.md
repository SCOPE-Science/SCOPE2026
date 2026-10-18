---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Commuting idempotents over every F_q diagonalize simultaneously because t(t-1) is separable even in characteristic 2. Their canonical joint eigenspaces V_epsilon form an ordered 2^m-part direct sum of F_q^n; the converse constructs all tuples uniquely. GL_n transitivity with stabilizer prod GL_{d_epsilon} proves the exact count including zero dimensional parts and n=0. For fixed n and q growing, the exponent of each orbit is n^2-sum d_epsilon^2, maximal for balanced ordered profiles. A two-part denominator has leading multiplicity 1 or 2; a four-part numerator has binomial(4,n mod4), giving exactly three stated probability cases, including coefficient 6 for n=2 mod4. Separately computed count from compositions for n<=3, q=2,3 (e.g. 40 at n=2,q=2, 76 at n=2,q=3). No assertion in simultaneous-conjugacy or growing-n limit.

## originality

PASS

PASS (best of knowledge): Simultaneous diagonalization and enumeration of direct-sum decompositions are classical, and Feit–Fine/Fulman–Guralnick count all commuting matrices, while Ferraz et al count single-idempotent generators. Neither inspected source states exact all-m joint idempotent counts or the fixed-n mod-4 leading commuting-probability law for uniform random idempotents. The all-m enumeration is an immediate but nontrivial natural specialization requiring the simultaneous idempotent locus; treat the elementary derivation as prior mathematical technique, not newly discovered. The possibility of an earlier implicit treatment via semisimple representations remains a specific risk.

## value

PASS

PASS: The probability that two uniformly sampled finite-field idempotents commute is a natural matrix-statistical invariant, distinct from unrestricted commuting pairs. The exact simultaneous-tuple count works at arbitrary tuple arity and supplies an unusual residue-class n mod4 leading coefficient/rate in large q; while rooted in textbook diagonalization, the exact natural optimizer/census is independently reusable. Scope is fixed n, not q fixed and n growing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
