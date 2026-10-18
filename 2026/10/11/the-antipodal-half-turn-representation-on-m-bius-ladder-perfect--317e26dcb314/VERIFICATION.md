---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

I reconstructed the graph (2n rim edges plus n spokes), τ-fixed faces of the *perfect-matching complex*, and their bijection with disjoint spoke monomers and complete rim-edge-orbit dimers on the n-column cycle. A fixed face with s spokes and t dimers has signed simplicial trace (−1)^t on chain degree s+2t−1, yielding reduced Lefschetz −Σ_(D,S)(−1)^(|D|+|S|). For each D, alternating over all n−2|D| free spoke monomers cancels except complete dimer coverings. There are exactly two for even n (including n=2 with distinguished parallel orbit dimers), none odd, giving 2(−1)^(n/2+1) and 0. Theorem21 of Agarwal–Basak supplies degree n/2−1 even and odd ranks 2 or4. An order-two operator on rational H has eigenvalues ±1; trace=2 on even rank2 forces identity and odd trace0 forces equal multiplicity. Finite n≤9 checks are only corroboration; all-n cancellation is analytic.

## originality

PASS

Opened primary arXiv:2608.30601v2 and inspected precise Theorem21 and proof on p14, plus definitions/main theorem. It classifies nonequivariant wedge-of-spheres types, not the central involution action; an abstract sphere count does not imply traces or eigenspaces. Searched half-turn, signed Lefschetz, C2 character and dihedral aliases; close honeycomb and ordinary matching-complex sources involve different objects. Thus strongest inspected same-object source is not covering.

## value

PASS

The antipodal central involution is canonical in the Möbius ladder. Its rational homological character and surprising even/odd dichotomy answer a natural symmetry refinement left undetermined by the published ranks, using a nontrivial signed fixed-face monomer–dimer cancellation that works uniformly for all n.

The dated certificate retains the supplied scientific assessment, sources and limitations.
