---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The vertex-idempotent quotient is commutative, and for each loopless arrow e, [idempotent at source,e]=e, giving [A,A]=J. Fix the two diagonal field entries per vertex. The arrow equation is an independent two-variable linear functional: unequal endpoint labels give q solutions for every target; equal labels give q^2 for zero and none otherwise. Factoring q per arrow and expanding the product of equality factors gives q^(2κ(S)) admissible labelings for each spanning subset, including isolated vertices. The nonnegative color sum is positive exactly for q^2-colorable target support. For r commutators, concatenating the diagonal labels gives q^(2r) colors and the concatenated arrow functional is onto exactly when some coordinate pair separates the endpoints. A full-support target forces a proper coloring of the whole underlying graph; such a coloring suffices for every target. With no arrows, χ=1, width is zero and the zero fiber has q^(2|V|) pairs. Parallel/opposite arrows still have separate radical variables. Fresh multiplication-table replays over GF(2) and GF(4) checked all fibers for 1,024, 4,096 and 65,536 ordered pairs, respectively for a parallel pair with an isolate, a directed triangle and an antiparallel pair. The bundled checker uses the arrow formula rather than multiplying basis tables independently, and its complete-graph examples evaluate the width theorem rather than exhaustively sum commutators. The general proof, not these tests, covers every prime power and width.

## originality

PASS

Credit the classical Potts/Fortuin–Kasteleyn identity, prior two-vertex all-target fibers, and the known commuting-pair specialization in the simple-graph regime. The supported distinct contribution is the arbitrary multivertex all-target fiber and the ordinary chromatic classification and width for unrestricted additive commutators. Two later catalogue findings materially overlap (one states the same three laws and adds target lengths); neither establishes antecedent coverage on the available chronology. The original does not claim the zero-fiber count as new.

## value

PASS

The result computes a natural word-map fiber for every target, distinguishes image membership from a much narrower fixed-adjoint question, and gives an exact and unbounded additive commutator width on a basic algebra family. The structural graph-coloring interpretation of representability and the target-dependent fiber formula are useful even though the partition-function identity is classical and the computation is not polynomial-time.

The dated certificate retains the supplied scientific assessment, sources and limitations.
