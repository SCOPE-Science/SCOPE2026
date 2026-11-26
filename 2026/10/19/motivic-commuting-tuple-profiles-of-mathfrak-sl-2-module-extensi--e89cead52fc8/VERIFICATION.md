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

The bracket map from the second exterior power of sl2 to sl2 is an isomorphism in the allowed characteristics, so the projected tuple equations are precisely the rank-at-most-one minors in coordinates. The zero tuple has radical fiber A^(ds); the nonzero rank-one locus is the punctured rank-s tautological bundle on P². The split nilpotent conic has class L+1 and its complement class L². A nonzero nilpotent gives one Jordan string per summand, even for degree zero; a nonnilpotent has distinct eigenvalues over a separable splitting field and gives a zero weight exactly in even degree. No nonzero weight or string coefficient vanishes under p>m and p>2. These rank checks hold geometrically, so on either reduced stratum the linear radical equations have a locally free kernel. Choosing a nonzero pivot x_h leaves v_h free and one action-kernel variable per other entry, giving rank d+(s−1)r. This proves the stated motivic class without assuming the full equation scheme is reduced. It includes t=0 and gives L^(d+3) at s=1. The point-counting realization applies over every extension of a permitted finite field. For the collision, the radicals are characteristic, and the least dimension of a simple submodule of the radical under the quotient action is 2 in the first case and 3 in the second. This is invariant even under twisting by an automorphism of the quotient. The positive-degree simple summands give neither fixed vectors nor trivial quotients, so centerlessness and perfection follow. The identical triples (7,1,2) give the same counts over all extensions, hence equal zeta functions. Independently substituting q=5, s=2 gives the reported 1,215,625 and 6,619,140,625. Read VERIFICATION.md and verify.py, not executed; direct collision nullity checks are at q=5, whereas q=7,11 at lines 115–118 compare only the formulas. This support-description overstatement does not enter the proof.

## originality

PASS

The supported increment is the reduced motivic profile for every arity and the perfect centerless nonreconstruction pair. Standard matrix centralizers, symmetric-power weights and generic stabilizer methods are not novelty claims. No statement-level equivalent or stronger covering theorem was found in the inspected sources.

## value

PASS

The formula identifies precisely which elementary representation data are sufficient for the entire profile. The explicit pair answers a natural reconstruction question even for perfect centerless algebras and a motivic invariant stronger than single-field pair counts. The nonreconstruction claim is about equality of classes, not isomorphism of tuple varieties.

The dated certificate retains the supplied scientific assessment, sources and limitations.
