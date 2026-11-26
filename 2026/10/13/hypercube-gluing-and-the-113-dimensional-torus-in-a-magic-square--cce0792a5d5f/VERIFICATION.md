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

At M=0 the square-linear relations give exactly the two base quadrics and the four quadratic pair relations. The base coordinates have no common zero. The pair equations are monic in local projective trivializations, so the cover has rank 16 over the smooth base. Away from the four branch divisors it is split and reduced, and finite local freeness excludes any nilpotents supported at branch points. The two quadratic gradients have rank two (the only possible rank-drop patterns would force two zero coordinates; none is compatible with the equations). Smooth complete-intersection adjunction gives genus one. Independently, in the chart F=1 put u=H+D, so H−D=u⁻¹ and (2iuG₀)²=u⁴+6u²+1. The four roots ±i(√2±1) have cross ratio 1/2 in a suitable ordering, giving j=1728. Each of F,H,D,G₀ has four distinct simple zeros on the quartic and their zero sets are disjoint. At any such point the other three monic equations split analytically into distinct choices, with the remaining local equation a²+h²=0 and h a base parameter. This is an ordinary node joining precisely the two sheets differing in that bit. Thus each of 32 cube adjacencies carries four nodes, and connectedness gives b₁=128−16+1=113. Normalization gives the Picard extension, with characters H₁ of the multigraph. The action on vertices is regular, and each of four node orbits in direction j induces the sign action of the branch-swapping stabilizer. The boundary image is the augmentation submodule, giving 4|S|−1 for nonempty S and no invariants. An independent exact oriented-edge permutation computation gave H₁ traces 113 at the identity, −31 at each generator and 1 otherwise, and Fourier multiplicities 0,3,7,11,15 by weight. The uploaded finite-field program was inspected, not run; its field computation alone cannot prove the complex local geometry.

## originality

PASS

The distinct supported content is the ordinary-node gluing for this divisor and its equivariant torus characters, not the known sixteen elliptic components, their isomorphism class or the general Picard normalization sequence. The strongest inspected intersection calculation works after separating the branches on the resolution and does not present their gluing graph.

## value

PASS

The center-zero section is a natural split hyperplane divisor of the magic-square surface. Giving its gluing directly rather than just intersections after resolution identifies the cycles lost under normalization. The equivariant calculation then determines exactly which characters occur in the torus of gluing parameters, including absence of sign-invariant torus directions. This is a concrete symmetry invariant for work with this generalized Jacobian, not just a new scalar node count or an unmotivated slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
