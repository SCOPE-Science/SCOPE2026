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

# Verification record

`python3 verify.py` uses exact integer arithmetic and a Bareiss determinant computation. Its three classes of checks are: (i) \(625\) integral parameter quadruples, each satisfying all \(64\) defining multiplicative relations, both matrix determinant formulas, and the claimed right-annihilator restriction; (ii) \(32\) affine basis permutations, realizing eight distinct quotient affine transformations; and (iii) \(17\) sampled elements of an unbounded shear family and \(81\) exact compositions. The finite output is recorded in `verification_output.txt`.

The symbolic argument for all integer parameters is contained in the proof. The tests do not purport to enumerate all automorphisms, prove the absence of covered literature, or substitute for independent review.
