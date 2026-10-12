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

The infinite theorem is verified by the proof in `RESULT.md`. The executable check is supplementary and does not substitute finite enumeration for an infinite argument.

`verify_old_windmills.py` constructs \(W_{r,m}\) directly, tests every subset against the literal OLD definition using nonempty pairwise-distinct open-neighborhood signatures, compares that truth value with the claimed structural characterization, reconstructs the predicted cardinality polynomial, and compares minimum sizes and minimum-set counts.

Replay:

`python verify_old_windmills.py`

Observed output from the packaged script before assembly:

`VERIFY_OK parameter_pairs=10 subset_checks=22816 minimum_checks=10 max_order=13`

The tested pairs include friendship cases and \(m\ge3\) cases. The largest tested graph has order \(13\). No finite range is presented as proof beyond that range.
