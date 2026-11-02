---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

For every n>=3, each selected incidence constrains two adjacent oriented cycle edges to a common sign. Nonconstant cyclic orientations are acyclic and admit a total vertex order. Thus a marked 0,+,- word is a face precisely when adjacent nonzeros never disagree and a single-sign word has an adjacent zero pair. For a fixed simplex the augmented signed trace is -(-1)^c where c is the number of permutation cycles on selected incidences. For rotations of period d=gcd(n,a), weighted signed words give -tr[T(-1)^d]+2tr[U(-1)^d]=-1+6[3|d]-4[4|d], with d=1,2 addressed directly. Reflections swap the sign and force boundary sites/pairs zero; the j free mirrored pairs give Z_0=1,Z_1=-1,Z_{j+2}=-Z_j and the three stated parity cases. Finite-group transfer on barycentric subdivisions then yields the two quotient reduced Euler averages and mod-24 periodicity. Independent enumeration from acyclic edge orientations (not the submitted verifier) reconstructed all faces and 84 dihedral signed actions for n=3..9, agreeing exactly. The symbolic orientation/transfer proof, not finite tests, establishes all n.

## originality

PASS

The submitted all-n virtual D_n homology character of the FULL strong cycle matching complex, especially the signed reflection fixed-face trace and mod-24 cyclic/dihedral quotient Euler values, was not implied by the directly read source paper, the published pure-strong cycle rotation result, or the full-strong path reversal result. Actual Resultary and literature searches included equivalent Lefschetz/Burnside formulations; the exact indexed duplicate was excluded as independent priority. Historical priority is best-of-knowledge and cannot rule out unindexed work.

## value

PASS

The full strong cycle matching complex is a natural recently defined combinatorial-topological family with unknown individual full-complex homology beyond an enumerated finite range. The invariant is the complete virtual D_n-action and its two natural quotient reduced Euler characteristics for every n, supplying nonidentity rotation and reflection symmetry information unavailable from ordinary face counts or the known pure-subcomplex character. The 24-periodic quotient formulas constrain proposed equivariant decompositions even without a full Betti census. This is a motivated all-parameter structural result, not an arbitrary narrow numerical recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
