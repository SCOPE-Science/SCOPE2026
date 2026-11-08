---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Independently reconstructed Cayley adjacency of Shrikhande and coordinate-sharing rook graph, verified both SRG(16,6,2,2) with different local neighborhoods C6 and 2K3. Enumerated 2^16 vertex masks for each by forbidden connected triples; 176 forbidden triples each and face vectors R (16,120,384,528,144), S (16,120,384,544,240,32), 1192 and 1336 nonempty faces. Independently constructed prescribed greedy acyclic Hasse matchings (542 and 638 pairs), with critical cells dimensions 0:1,2:1,3:106 for rook and 0:1,2:1,3:58 for Shrikhande. Calculated signed integral 3-to-2 Morse coefficients exactly: R {-1:8,0:82,1:16}, S {-1:10,0:43,1:5}; each has unit coefficient, so a 2-cell and one 3-cell cancel homotopically, leaving wedge^105 and wedge^57 3-spheres, respectively. No torsion follows from actual homotopy cancellations, not mod-two Betti inference.

## originality

PASS

Qualified PASS: earlier exact same-pair distinction at ordinary cutoff one is acknowledged, but the present cutoff-two integral homotopy computation is not a corollary of it. Checked general higher-independence and chordal theorems and distinct cut-complex duals.

## value

PASS

Natural comparison of uniquely two nonisomorphic strongly regular (16,6,2,2) graphs: even though they share all faces through dimension2, their Ind2 integral homotopy types distinguish them by 48 three-spheres. Exact finite natural invariant with structural significance in graph-topology discrimination.

The dated certificate retains the supplied scientific assessment, sources and limitations.
