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

The package contains `beat_certificate.json` and a standard-library verifier, `verify.py`.

Run:

`python3 verify.py`

The verifier reconstructs the source and target weak orders, enumerates all \(4^6=4096\) set maps, and checks which are order-preserving. It verifies that there are exactly \(44\) such maps. It then replays every certified deletion against the complete surviving pointwise poset and checks the defining unique-minimal-upper or unique-maximal-lower condition for a Stong beat point.

After all \(40\) deletions, the verifier checks that the survivors are exactly the four constant maps, that their induced order is precisely \(X_1\), and that no survivor is a beat point. The expected final output is:

`VERIFY_OK maps=44 deletions=40 up=20 down=20 core=4`

The computation is exhaustive for this finite pair. It does not verify or claim a parameterized theorem for other finite sphere models.
