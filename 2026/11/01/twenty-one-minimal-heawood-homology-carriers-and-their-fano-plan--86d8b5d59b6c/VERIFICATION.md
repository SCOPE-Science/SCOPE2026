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

## Exact finite verification
Run `python3 verify.py` and `python3 crosscheck.py` using only the Python standard library. Both were executed on the embedded files; recorded transcripts are `verification_output.txt` and `crosscheck_output.txt`, ending in `VERIFY_OK` and `CROSSCHECK_OK`. The first program directly generates all graph incidence edges, all independent simplices, explicit third/fourth boundary matrices, local kernel bases and global boundary quotients. It enumerates all 16,384 induced vertex subsets, checks that every local third Betti number equals the image rank, verifies the full 15-row rank histogram, all 21 minimum supports as `C8 disjoint K2`, all 21 class residues and all 1,330 three-class combinations, of which precisely 28 vanish by Fano-line-complement incidence.

The second checker independently builds local/global boundary systems and computes injection ranks by stacked-matrix rank identities rather than enumerating local kernel representatives. It agrees on the 16,384-subset profile and 21 minimum supports. Both use exact XOR arithmetic in finite-dimensional binary vector spaces, not floating-point approximations. The verified claim is confined to the specified finite graph and mod-two third homology. These checks do not constitute independent scholarly review.
