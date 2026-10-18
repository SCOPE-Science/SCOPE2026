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

# Reproducibility and scope

The included `verify.py` constructs actual finite-field Lie brackets for split extensions whose actions consist of distinct irreducible factors. It enumerates all subspaces of the abelian ideal using reduced row-echelon matrices and all subalgebras not contained in the ideal using the classification described in `RESULT.md`. Separately it tests every ordered pair of constructed subalgebras by comparing Lie brackets to their vector-space sum; it compares the result with the closed Gaussian-binomial formula.

The completed checks are five finite prime-field examples: a single quadratic factor over fields of size two and three, one cubic factor over size two, two distinct quadratic factors over size three, and factors of degrees two and three over size two. The two genuinely multi-factor examples have \((N,P)=(312,51264)\) and \((N,P)=(419,144477)\), respectively. Running `python verify.py` terminates with `VERIFY_OK` on success and raises an assertion on a mismatch.

The abstract statement for every permitted prime power, irreducible-factor degree tuple, and choice of distinct factors follows from the algebraic proof, not exhaustive computation. There is no external or independent scientific audit; the front-matter records that status only.
