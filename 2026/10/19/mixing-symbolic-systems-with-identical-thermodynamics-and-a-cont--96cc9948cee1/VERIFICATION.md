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

The analytical argument in `RESULT.md` proves all statements for every real \(\beta\in(0,1)\). The finite checker `verify.py` uses integer-power inequalities for \(\beta=1/2\) and \(\beta=2/3\); it passed 1208 assertions on a local Python 3 interpreter. It exhaustively enumerates admissible marker words of lengths 1 through 12, checks their binomial upper counts, tests finite zero-extension examples, finite-gap concatenations, and the failure of selected finite periodic-marker repetitions. The finite checks are not a certificate of the all-parameter claims, mixing, approximate product property, or nonconjugacy. No independent audit has been performed.
