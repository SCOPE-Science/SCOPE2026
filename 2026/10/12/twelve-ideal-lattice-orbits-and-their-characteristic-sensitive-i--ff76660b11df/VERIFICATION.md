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

The included `verify.py` is standalone Python 3 code with no third-party dependencies. Running `python3 verify.py` directly checks finite fields \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5,\mathbb F_7,\mathbb F_8,\mathbb F_9\), including nonprime fields. In each field it generates projective points in the three-dimensional quadratic socle and planes via the contragredient action, verifies three quadratic-form point classes and three plane classes, calculates the point-plane incidence multiset, and checks twelve orbit sizes sum to \(3q^2+4q+7\).

An independent \(\mathbb F_2\) full-subspace enumeration obtains exactly 374 vector subspaces of the radical, 26 proper ideals, 384 automorphisms and 11 proper-ideal orbits; adding the whole algebra yields 27 ideals in 12 orbits. The saved output ends with the direct enumeration after the marker `VERIFY_OK`. The program makes no claim to exhaust every finite field, much less to prove the theorem from finite samples; that role belongs to the symbolic proof in `RESULT.md`.

The only supplied computational files are `verify.py` and `verification_output.txt`. The mathematical proof is reproducible without software. Independent audit has not been performed.
