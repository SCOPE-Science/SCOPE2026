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

The proof in `RESULT.md` is symbolic and applies to every binary doubly-even code in the stated admissible range. The key exact steps are:

1. A minimum-support two-dimensional subcode has three nonzero binary projective column classes with multiplicities \(a,b,c\).
2. Doubly-evenness gives \(a+c\equiv b+c\equiv a+b\equiv0\pmod4\), hence \(a,b,c\) are even.
3. Every projective class can therefore be split exactly in half.
4. Under a hypothetical \(d_2\ge2R_2+2\), the generalized covering approximation and its complement have support below \(d_2\), so both have rank one.
5. The induced rank-one idempotent has distinct image and kernel projective points and can erase at most half of the minimum-support columns, contradicting the definition of \(R_2\).

Run `python3 verify.py` for finite consistency checks. It exhausts all two-dimensional binary subspaces for lengths \(4\) through \(7\), filters the doubly-even codes, computes \(R_2\) directly from the defining minimax problem, and verifies both claimed inequalities. It also checks the projective-multiplicity parity implication for every \(0\le a,b,c\le20\).

Expected output includes:

`n=6 subspaces2=651 doubly_even=15 pairs=[(6, 4)]`

`n=7 subspaces2=2667 doubly_even=105 pairs=[(6, 5)]`

and ends with `VERIFY_OK`.

The finite census does not certify arbitrary lengths; that role is supplied by the symbolic proof.
