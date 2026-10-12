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
# Reproducibility and mathematical limits

Run `python3 verify.py` with Python 3.10 or newer. No third-party libraries are needed. The script checks the explicitly constructed support sets at every length \(2\le n\le64\) by constructing full binary words and deleting each coordinate. It enumerates the exact maximum compatible sets at \(2\le n\le9\), and checks all relevant checksum-class sizes at \(4\le n\le64\).

The actual output from the supplied program was:

`VERIFY_OK construction n=2..64; exhaustive maxima n=2..9; modified VT classes n=4..64`

The infinite-length theorem is not inferred from these finite computations. Its certificate is the explicit weight-one descendant bound and periodic construction verified analytically in `RESULT.md`. The exact range and the distinction between experimental and theoretical verification are deliberate.
