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

The cited scale r=2 means radius-1 closed intrinsic graph balls, whose Čech faces are subsets of closed neighborhoods of T_n; identifying T_n vertices with K_n edges gives precisely Cov(n,2). A complete ordered-coordinate matching on every augmented face has 5,142/34,308/202,141/1,099,624/5,673,836 faces and 2,561/17,129/101,018/549,714/2,836,750 matched pairs. The source verify.py was reproduced byte-for-byte with Git blob SHA e92aedbeb5d8324a6934996cba98d10fbe5f6391 and independently executed on all five n; each full V-path DAG topological sort passed and all exact integral critical 4-to-3 incidences vanished (15,35,70,126,210 columns). After excluding the augmented empty face, unpair its matched vertex to obtain one critical 0-cell; acyclicity is preserved. The resulting CW complex has a wedge of C(n-1,4) 3-spheres as 3-skeleton and C(n,4) 4-cells with degree-zero maps in pi3 ≅ H3 (Hurewicz), hence each attaches trivially. The suspension theorem then gives the bipartite Kneser types. An independently implemented complete mod-two boundary-rank computation for n=6 and 7 returns H3/H4=(5,15) and (15,35) and no other reduced homology; this is corroboration, not substitute for integral homotopy proof. n>=11 is not asserted.

## originality

PASS

The underlying complex is EXACTLY Jonsson’s earlier covering-number-two graph complex Cov(n,2); its full integral homology ranks for all n are not new. Biswas (2026) identifies a same-complex Čech model and conjectures a general 3/4-sphere wedge formula. The five finite n=6..10 WEDGE HOMOTOPY claims survive the inspected implication comparisons: rank/concentration of integral homology plus 2-connectivity alone do not supply an explicit dimension-4 CW reduction or nullhomotopic attaching maps; the assigned acyclic integral Morse reduction provides these for each finite n. Source accessibility limits prevent a categorical novelty guarantee, especially for Biswas and Jonsson. Original manuscript should additionally cite these earlier same-object results before publication.

## value

PASS

Bipartite Kneser graphs H(n,2) and bounded-cover graph complexes are canonical combinatorial-topological objects; the homotopy question is explicitly motivated by Biswas’s 2026 proposed 3/4-wedge conjecture. Jonsson already gives integral Betti numbers in ALL n, so recomputing only those would have little value. The new content here is five exact WEDGE HOMOTOPY types with independently reproducible integer Morse attachments for n=6..10, reaching a 45-vertex Čech complex with 5,673,836 faces (and 90-vertex bipartite independence complex). Five successive cases form a justified finite cutoff of a natural outstanding homotopy question, even without an all-n proof. No general-family novelty, canonical equivariant decomposition, or new homology ranks is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
