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

# Reproducible verification

The executable `verify_ideal_census.py` needs Python 3 and no third-party dependencies. Run `python3 verify_ideal_census.py` in the directory containing that file. The expected output is stored in `verify_output.txt`, with terminal marker `VERIFY_OK_RADICAL_SQUARE_ZERO_ALL_IDEALS 22`.

It enumerates **every** subspace of the finite-dimensional truncated path algebra for each of 22 finite-field/quiver configurations and tests, directly from the original multiplication table, whether the subspace is stable under left and right multiplication by every basis element. The independent comparison computes the dimension counts through the Gaussian-binomial formula. Tests cover loops, parallel arrows, opposite arrows, chain, fork, mixed-loop and disconnected examples over fields with two, three and four elements; the four-element field is represented as a genuine degree-two extension.

The original proof in `RESULT.md` is necessary for all quivers, all base fields and the geometric classification. The 22 finite checks are supporting evidence and cannot establish those universal statements. The statement concerns reduced geometric ideal varieties rather than an assertion that the original defining scheme is reduced. No external or independent audit is asserted.
