---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For connected simple theta graphs with path lengths a<=b<=c (a>=1,b>=2), every bond is either a transversal 3-set containing one edge per path or a within-path 2-set: follows connected bipartition criterion. All bonds <=3 gives Ldim<=3. For a>=2 three distinguished path edges realize all 2^3 traces => (VC,Ldim)=(3,3); a=1 forces VC=2, and for (1,2,2) 6 hypotheses force Ldim<=2, while a=1,c>=3 embeds explicit depth-three house shattering tree => (2,3). Tree and unicyclic bond families have stated low dims. Independently enumerated all 595 connected labeled simple graphs on 2..5 vertices <=6 edges, computing bonds and exact VC/Ldim: precisely 60 labeled exceptions (5 vertices,6 edges,VC=2,Ldim=3), all house isomorphism type. The proof (rather than finite enumeration) covers arbitrary theta parameters and larger trees/unicyclic graphs.

## originality

PASS

The bond=graphic cocircuit=matroid-hyperplane duality gives several equivalent terms. Guingona et al zero-set theorem proves VC=Ldim for ALL nonzero linear-form zero sets; restricting to maximal proper zero sets (hyperplanes) is a subfamily operation and does not preserve equality, as house counterexample explicitly shows. Bond size extremal research does not determine learning dimensions. Sharp 6-edge threshold and theta classification appear uncovered in inspected primary texts.

## value

PASS

A sharp first static-adaptive shattering gap for natural graphic-matroid concept classes, together with all-theta phase classification and cactus low-cycle boundary, is a structurally motivated finite threshold and general combinatorial theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
