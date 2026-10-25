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

# Reproduction and verification

Run `python3 verify.py` from the directory containing this file, using only Python 3 standard-library modules. The output saved as `verification_output.txt` was produced by actually executing that script.

The script checks the complete 16-vertex distance-four graph and all 16×16 common-neighbor pairs; reconstructs all 392 nonempty independent faces and the face vector; constructs 191 Morse pairs and all 1200 face covers; verifies all 392 faces are visited by a topological sort of the Morse-oriented diagram; and independently checks mod-two boundary ranks 15, 65, 95 and 16. The combinatorial Morse certificate proves the previously known homotopy type needed for the character calculation.

For each of 1920 automorphisms, the verifier computes the signed simplicial fixed-face sum and separately computes the orbit-conflict independent-polynomial evaluation, then asserts equality with the closed representation character. It also checks the seven conjugacy classes of the coordinate-permutation subgroup and all pure translations. Successful reproduction ends with `VERIFY_OK`.

These checks cover the entire explicitly defined finite structure; they do not establish any uniform theorem for larger folded cubes, prove the absence of an unindexed earlier calculation or substitute for independent external scientific review.
