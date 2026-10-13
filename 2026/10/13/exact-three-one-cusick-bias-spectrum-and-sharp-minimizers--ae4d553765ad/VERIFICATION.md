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

# Exact check record

Run `python3 verify.py` using a standard Python 3 installation; no third-party packages are needed. The verifier calculates all sixteen canonical shifts three ways, then checks the carry and finite-deconvolution recurrences for every gap pair with \(1\le a,b\le16\). It produces the recorded values in `verification_output.txt`.

The carry-count calculation enumerates precisely all possible lower-bit patterns modulo the sufficient power of two, with a proven truncation above the high digit. The direct-residue count is independent of the state aggregation, and the finite-deconvolution method uses independent exact Fraction arithmetic. The gap-stress tests do not establish the infinite-gap theorem; the proof of gap clipping in `RESULT.md` does that. These checks do not establish originality or constitute independent scientific audit.
