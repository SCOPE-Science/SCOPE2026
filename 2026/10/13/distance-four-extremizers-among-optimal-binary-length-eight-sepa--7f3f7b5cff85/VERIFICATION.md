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

# Verification

The standalone program `artifacts/verify.cpp` reconstructs the binary separation predicate and Hamming distance from bit operations. It performs a complete recursive enumeration of every ten-word separating system of minimum distance at least four that contains the zero word. The recursion reaches a terminal count only after nine nonzero words have been selected and rejects a branch only when an exact pairwise distance, exact three-word separation condition, or cardinality bound fails. It returns exactly \(46{,}200\) systems containing zero.

Translation invariance then gives the global labeled count through \(10N=256\cdot46{,}200\). The same program directly validates the three representatives and enumerates stabilizers under all coordinate permutations together with admissible translations. It obtains stabilizer orders \(48\), \(32\), and \(16\), hence orbit sizes \(215{,}040\), \(322{,}560\), and \(645{,}120\). Distance-profile multisets distinguish the representatives, and the orbit sizes sum to the exhaustive census.

The prior cardinality maximum \(10\) is not re-claimed. Its proof was checked in the cited exact record: an eleven-word hypothetical system cannot have minimum distance one or at least five, and all normalized closest-pair cases at distances two, three, and four are exhausted by the published exact verifier.

Limits: the package proves only the stated distance-four equality classification at length eight. It does not classify maximum systems of smaller minimum distance or generalize the census to higher dimensions.
