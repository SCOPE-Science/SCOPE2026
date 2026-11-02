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

The exact finite theorem dFl(P31) ≃ wedge^960 S4 has been reconstructed for the ordinary unordered complex of transitive vertex subsets of the Paley tournament on Z/31, with residues explicitly verified. Independent fresh Python enumeration reproduced all 27,931 faces, dimension face vector (31,465,3255,9765,10695,3255,465), and all 126,015 nonempty Hasse covers. An independently coded repeated-toggle matching in the recorded 31-pivot order has 13,396 disjoint pairs and exactly one critical 0-cell, 89 critical 3-cells and 1,049 critical 4-cells. Independently built reversed-matched Hasse graph topologically sorted all 27,931 nodes, proving acyclicity. Independent signed boundary reduction gives D of shape 89x1049, 16,282 nonzero entries and |entry|<=8; exact ranks are 89 modulo 2,3,5,7,101,601. The 89 pivot columns selected modulo 2 have an exact Bareiss-equivalent determinant -601, while full rank modulo 601 means the greatest common divisor of maximal minors is coprime to 601, therefore equals 1. All nonzero integral Smith factors are 1, with free kernel rank 960. The CW model has cells only in dimensions 0,3,4; the 3-skeleton is wedge^89 S3, where Hurewicz identifies pi3 with H3, and integral Smith changes of basis give a wedge^960 S4 homotopy cofiber. Finite exhaustive verification is sufficient for this fixed 31-vertex object, not a universal family. Independent code was kept separate from repository verify.py.

## originality

PASS

Best-of-knowledge original exact integral homotopy computation for the canonical Paley tournament P31. Govc Proposition 3.4 covers doubly regular tournaments only through 27, McKay lists order 31 incompletely without topology, and inspected Paley-19, cyclic and lexicographic findings do not imply the 31-vertex wedge. No exhaustive-priority guarantee; inaccessible original Deniz 2015 full text is a specific bibliographic risk rather than automatic scientific rejection.

## value

PASS

The Paley tournament P31 is a canonical quadratic-residue doubly regular tournament of the first permissible size beyond the completed 27-vertex DRT homotopy census. Unlike an arbitrary small-instance slice, this is a natural test object at the first uncovered order, where prior smaller doubly regular examples exhibit both torsion and mixed-dimensional Moore-space phenomena. The exact integral wedge multiplicity and full primitive Morse-boundary certificate provide a sharp benchmark and a reusable reference for tournament-topology comparisons. It is an exact finite invariant with motivation independent of an all-order theorem. It neither classifies every 31-vertex DRT nor implies all Paley orders are wedges.

The dated certificate retains the supplied scientific assessment, sources and limitations.
