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

The analytic proof in `RESULT.md` is the basis of the theorem. The packaged script `artifacts/verify.py` is a finite regression check of two independent ingredients: the reduction from an arbitrary abelian kernel to the order of a character, and the residue-class closed forms.

It enumerates all characters of \(\mathbb Z_m\times\mathbb Z_n\) for \(1\le m,n\le16\) whose order is at least \(3\). For each character it computes the full product-group average of \(|\operatorname{Re}\lambda|\), compares twice that average with the claimed \(C_L\), and verifies the unique contractive order through \(L=400\).

Actual replay line:

`VERIFY_OK abelian_character_cases=17920 max_formula_err=6.883e-15 contractive_orders=[4]`

These finite checks do not prove the universal statement. The proof uses the induced-character formula, exact Fourier inversion, equal fibers of a finite character map, finite cosine-sum identities, and the monotonicity argument stated in `RESULT.md`.
