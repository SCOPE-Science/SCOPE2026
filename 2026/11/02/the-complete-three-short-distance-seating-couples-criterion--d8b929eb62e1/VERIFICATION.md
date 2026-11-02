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

The standalone `verify.py` depends only on Python 3's standard library. Run it from the same folder as this document using `python3 verify.py`.

It checks that the constructed matching uses every vertex exactly once and has the specified circular-length profile for all feasible triples with \(3\le n\le80\) (\(46{,}748\) cases). A separate recursive enumeration of allowed matchings on the circle exhaustively determines attainable profiles for \(3\le n\le18\) and compares their full set, including all excluded profiles, to the claimed criterion (\(702\) realized profiles). Each of the six finite block patterns is checked separately by ordinary absolute differences. Observed final message: `VERIFY_OK`.

No calculation proves the unrestricted theorem by itself; the case distinction, parity argument, residue-class obstruction, and block construction in `RESULT.md` are the infinite proof. The enumeration does not claim exhaustive testing for larger sizes or any independent external mathematical review.
