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

PASS: In PG(d-1,q), q any prime power >=2, d>=2, singletons are closed and every pair is a pseudo-intent because its line has q+1 points. A larger pseudo-intent would contain the closure of every pair and hence be a projective flat, contradiction. For synchronous one-pass closure, each independent A and full-support point p in its span has no proper-subset rule capable of adding p in that pass; therefore the premise A and root p are compulsory. Conversely minimal spanning support of any target point is independent, making those rules sufficient. Count independent r-subsets I_r=prod_j(N-N_j)/r!, and full-support roots (q-1)^(r-1), deriving both exact grouped/unit formulas. Induction on rounds with a balanced partition of support establishes R_t(S)=union of spans over supports of size <=2^t. A rank-r independent frame and its all-nonzero coordinate sum attain ceil(log2 r); general rank-r inputs achieve closure by then. Independently enumerated all 128 subsets PG(2,2) and 8192 subsets PG(2,3), checking pair pseudo-intents, direct rule counts (21/49 and 78/312, unit 1092), closure and rounds. The independent finite tests cover q=2,3,d=3; all prime powers and dimensions rest on proof.

## originality

PASS

PASS best of knowledge for the combined exact all-rank projective enumeration D_group,D_unit and round-by-round support/depth tradeoff. Wild’s general canonical-direct stem/root construction and Kashiwabara-Nakamura rooted circuits explain the compulsory-rule mechanism, and Bérczi-Boros-Makino study matroid Horn representation minimization; these prior general frameworks are credited. Their inspected material does not give the displayed field-dependent closed counts plus exact logarithmic pair-rule convergence profile for every PG(d-1,q). This remains an especially important general-theory overlap risk, not presented as a new abstract direct-basis theorem.

## value

PASS

PASS with narrow scope: exact direct-basis sizes for finite projective geometries, optimal one-pass consequence counts and the cost of reducing propagation rounds are natural motivated closure-system invariants. The contrast from O(q^(2d)) canonical pair rules to q^(d^2-O(d log d)) direct rules makes a concrete nontrivial size/parallel-depth tradeoff. Generic rooted-circuit definitions alone do not supply these field- and dimension-dependent enumerators.

The dated certificate retains the supplied scientific assessment, sources and limitations.
