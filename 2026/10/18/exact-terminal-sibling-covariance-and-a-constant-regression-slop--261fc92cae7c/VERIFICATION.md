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

The analytic proof uses conditional uniform-attachment increments and induction. The accompanying `verify.py` is a standalone standard-library implementation. It computes each sample's terminal vertices and terminal-sibling pairs directly from its parent list, exhausts all \((n-1)!\) equally likely parent-choice vectors for \(2\le n\le8\), checks each indexed sibling-event probability as an exact rational number, and independently propagates the four moment recurrences to \(\(n=150\)\). The packaged replay passed 6,596 exact rational assertions.

The checks explicitly include \(\(n=2\)\) and \(\(n=3\)\), for which the unrestricted \(n/8\) formula is not asserted. Results for \(n>150\) rest on the algebraic derivation, not any extrapolation from the finite calculations. The code requires only Python 3 and its standard library; from the directory containing the file, run `python verify.py`.

The leaf convention is rooted outdegree zero, and the sibling count includes every unordered pair under a parent with multiple terminal children. The separate undirected degree-one convention is not used.
