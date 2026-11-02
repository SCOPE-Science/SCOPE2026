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

Run `python3 verify.py` from the extracted directory using Python 3 and the standard library. It constructs a Boolean affine \(\operatorname{SQS}(8)\), an explicit \(\operatorname{SQS}(10)\), and a Boolean affine \(\operatorname{SQS}(16)\). Each block is a four-element subset of the points. The program checks unique completion of every triple, distinctness of the four completion points of a nonblock four-set, and then computes exact equality-plus-quaternary-relation atomic extension signatures recursively through rank five. The expected terminal line is `VERIFY_OK`, and `verification_output.txt` contains the actual recorded run.

The computation proves the finite signatures of these three structures only. The separate mathematical proof in RESULT.md gives the uniform extension argument for every admissible finite order \(v\ge8\) and uses Hanani existence to attain the sharp representative size ten. No mechanically checked proof of the general theorem and no external independent validation are claimed.
