---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For each graph automorphism of K_{2,n}, a fixed acyclic graph vector field is a g-equivariant directed rooted forest; signed simplicial Lefschetz trace equals (-1)^{n+1} times alternating count by selected edge orbits (including the empty forest). For g=(1,sigma), every nonfixed right orbit contributes 1-1-1=-1; fixed part is determinant det(I-L(K_{2,f}))=(-1)^{f-1}(f^2-1), with f=0 treated separately, producing sgn(sigma)(f^2-1). For g=(swap,sigma), classify right fixed orbits, 2-cycles, longer even cycles and odd cycles to obtain (-1)^{n+1}sgn(sigma)(1-f+2t). For permutation augmentation U_n, χSym²U=(f²-f+2t)/2 and χ(wedge²U+2U)=(f²+f-2t-2)/2; sum/difference reproduce both group characters, with parity-dependent swap of S2 eigenspaces. The claim is an unconditional virtual Euler character; actual homology module only conditional on separately proven nonequivariant degree-n concentration. Independently enumerated all invariant acyclic parent assignments for selected n=3,4,5 permutations, with and without swapping the two distinguished vertices: all 18 samples matched both character formulas exactly. Finite cases corroborate but do not replace the all-n orbit-case count.

## originality

PASS

The prior n=4 fully equivariant case is expressly covered, but the uniform all-n fixed-point/two-cycle trace and rational module decomposition are not implied by it or by a nonequivariant homotopy type.

## value

PASS

A closed uniform rational group-character formula and central eigenspace modules for a canonical graph family are a meaningful equivariant refinement of already known wedge/homology ranks. The formula distinguishes representations with identical Betti numbers and provides all group-element traces rather than a single finite instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
