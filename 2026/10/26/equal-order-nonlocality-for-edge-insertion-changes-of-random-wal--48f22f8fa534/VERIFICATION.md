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

Execute `python verify.py` from the directory containing `verify.py`. The program uses only the Python standard library; it constructs both graphs, verifies their labelled radius balls, and computes exact discrete-time cover times with independent visited-mask Bellman systems solved over rational numbers. It also checks strict analytic-inequality margins at 203 radii.

Actual run output is embedded as `verification_output.txt`. It includes exact responses \(362/105\) versus \(-1727/1995\) at radius \(1\) and \(664/105\) versus \(-5429299/1588860\) at radius \(2\). Both graph pairs have equal order. The large-size all-radius proof is analytical in `RESULT.md`; the checks are only finite corroboration and are not infinite certification.

A separate historical-priority risk remains as described in `AUDIT.json`. No independent mathematical audit has been performed.
