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

Run `python3 verify.py` with Python \(3\). The verifier uses only the standard library.

It performs these checks from definitions:

1. reconstructs all \(64\) binary source words of length \(6\);
2. verifies that first bit plus derivative is a bijection and that one repetition is exactly one zero insertion in the derivative;
3. constructs exact one- and two-repetition descendant sets and checks all \(2016\) unordered source pairs;
4. compares direct two-repetition compatibility with the zero-bin \(\ell_1\)-criterion on every pair within every fixed-first-bit, fixed-derivative-weight layer;
5. exhaustively enumerates every subset in each of the six derivative-weight layers and verifies the layer optima \((1,2,3,1,1,1)\) and equality counts \((1,3,1,10,5,1)\);
6. constructs all \(150\) maximum codes in each first-bit sector and directly rechecks correction for one and two repetitions;
7. checks that every sector maximum covers exactly \(71\) exact-two descendants, hence every global maximum covers \(142\) of \(256\) length-eight outputs.

The exact expected single-line output is stored in `EXPECTED.txt`.

The computation is exhaustive only for the stated finite domain. It proves no claim for longer source words, larger alphabets, or duplication lengths greater than \(1\).
