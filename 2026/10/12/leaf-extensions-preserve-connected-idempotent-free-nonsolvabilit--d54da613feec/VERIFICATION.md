---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

In any new idempotent x+sum_j b_j f_j, the square has no f_j component, forcing all b_j=0; it then reduces to a base idempotent, necessarily zero. Every old basis square is nonzero by nondegeneracy and each new square e_1 is nonzero, so annihilator remains zero. Attaching leaves to vertex e_1 preserves underlying graph connectivity; standard connected graph criterion yields indecomposability for nondegenerate evolution algebras. Old E is a subalgebra, so its nonterminating derived series embeds termwise in the extension. For Hu–Wen seed set u=e_1+e_3, v=e_2+e_3 and directly compute u²=0, uv=u, v²=-u+2v, hence S²=S and perpetual nonsolvability. Independently enumerated all idempotents over F_3/F_5 at n=3,4 and found only zero, with expected square-space dimensions; these checks are not the general field proof.

## originality

PASS

The previously published three-dimensional counterexample and easy dimension extensions with zero summands are credited. The leaf-extension preservation under simultaneous nondegeneracy, connectedness, idempotent-freeness and nonsolvability is a distinct structural family and gives indecomposable examples, not merely larger vector-space dimensions.

## value

PASS

The known idempotent-free nonsolvable three-dimensional phenomenon could be dismissed as an isolated or decomposable artifact in larger dimensions. The uniform leaf lemma preserves four natural structural conditions and yields explicit indecomposable witnesses for all dimensions n>=3, which is a mathematically motivated strengthening even though its proof is short.

The dated certificate retains the supplied scientific assessment, sources and limitations.
