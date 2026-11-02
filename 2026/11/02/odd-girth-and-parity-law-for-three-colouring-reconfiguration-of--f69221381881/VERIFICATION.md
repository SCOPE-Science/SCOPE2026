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

The theorem is proved for every admissible \(n\ge3\) by the signed-height lift and monotone valley-raising argument in `RESULT.md`; finite programs only corroborate it. The two standalone verification programs rebuild their graphs using distinct encodings. Run `python3 verify_direct.py` and compile `verify_sign_lift.cpp` with `g++ -std=c++17 -O2 verify_sign_lift.cpp -o verify_sign_lift`, then run `./verify_sign_lift`. The first checks labelled colourings through \(n=11\). The second constructs sign lifts and checks every mixed-sign profile through \(n=16\), including simple projected closed walks of length \(3n\). Statements about arbitrarily large \(n\) rest on the written proof. Originality remains subject to independent comparison with specialized literature.
