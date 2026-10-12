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

The proof has four exact steps. First, the lifting in arXiv:2610.04317v1 identifies the contraction quotient with the split-algebra quotient and preserves its submodule lattice. Second, Lemma 3.2 of that paper gives the exact quotient \\(V\oplus V\\). Third, because the split algebra is \\(\operatorname{End}_K(V)\\), the commutant on \\(V\\) is exactly \\(K\\); every simple submodule of two copies of \\(V\\) is therefore the image of \\(v\mapsto(av,bv)\\) for a unique projective point \\([a:b]\\). Fourth, the module/ideal correspondence transports the projective-line lattice to the left ideals above the contraction.

The infinitude assertion is independent of the finite verifier: if the center were finite, central finiteness would make the division ring finite, hence commutative by Wedderburn's little theorem. Therefore the chosen finite extension \\(K\\) is infinite.

`artifacts/verify.py` enumerates every vector subspace of \\(V\oplus V\\) for \\(A=M_2(\mathbb F_p)\\), with \\(p=2,3,5\\), and tests invariance under matrix-unit generators. It finds exactly \\(p+1\\) nonzero proper invariant subspaces, all of dimension two, and checks that distinct such subspaces are complementary. `artifacts/verification_output.txt` records the replay and ends in `VERIFY_OK`. These finite cases verify the structural calculation only; they are not used to infer the arbitrary-field theorem.
