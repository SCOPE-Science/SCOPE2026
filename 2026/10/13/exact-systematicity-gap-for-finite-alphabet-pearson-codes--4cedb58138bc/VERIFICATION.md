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

Execute `python3 verify.py` using Python's standard library.

The verifier enumerates every primitive length-three Pearson representative for \(2\le q\le13\), and checks the exact formula \(|P_{q,3}|=3F(q-1)+3\) against an independent gcd count of ordered coprime pairs. A second equivalence method normalizes each tuple by its minimum and maximum with exact rational arithmetic, rather than gcd. For \(2\le q\le7\), it independently exhausts every ternary-length word in the ambient alphabet to check that all positive-affine classes are represented.

For \(2\le q\le5\) and \(2\le k\le4\), it constructs the length-\(k+1\) Cartesian code carrying \(q^k\) messages and verifies that both normalization methods find exactly \(q^k\) distinct classes. It independently verifies the two possible positive-affine orientation classes for a codeword with a constant information prefix and one check symbol.

Expected terminal line:

`VERIFY_OK exact_r_sys_q_ge_3=2 exact_r_free_q_ge_3_k_ge_2=1 exact_r_free_q_ge_3_k_1=2 exact_r_binary=1`

The program is finite evidence only. Universal correctness is supplied by the complete counting and orientation proof in `RESULT.md`.
