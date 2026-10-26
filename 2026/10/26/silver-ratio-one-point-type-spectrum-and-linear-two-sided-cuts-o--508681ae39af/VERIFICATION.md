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
# Verification notes

The source `verify.py` needs only the Python 3 standard library. Run `python3 verify.py` in the directory containing this file. Its completed output is stored as `verification_output.txt`.

The test does not assume the displayed transfer-matrix result when counting complete comparison patterns. It iterates three labels (below, above, incomparable) on every one of the `2*n` parameter points for n=5,6,7; independently checks lower-ideal, upper-filter and all lower-to-upper comparability conditions; and obtains counts 225, 469 and 1041.

For every n=5,...,14 it also counts ideals by upper-subset forcing, counts two-sided cut patterns by common upper-neighbor sets, and counts ideals by cyclic zero-triple weighted words. Each agrees with the Pell--Lucas and 12n formulas. Finite checks cannot certify an infinite formula; the proof in `RESULT.md` establishes all n>=5.

Originality assessments are self-review only; no independent validation has been performed.
