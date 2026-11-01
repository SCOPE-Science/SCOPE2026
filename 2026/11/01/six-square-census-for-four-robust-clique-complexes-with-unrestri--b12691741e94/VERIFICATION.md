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

Run `python verify.py` with Python 3 and NetworkX 3.x installed, in the same directory as the embedded `census.csv`. The script independently reconstructs all square-sequence isomorphism classes through level six, checks the level and vertex distributions, validates every generated graph6 code, regenerates every allowed face from independent four-subsets, constructs every toggle pair, checks every Hasse incidence, topologically sorts the entire reversed-matching directed graph, counts residual dimensions, and compares every CSV byte.

Replayed successful result: `ALL_VERIFY_OK classes=1628 table_bytes=60908 positive_beta=1590 contractible=38`. The level totals of nonempty simplices are `15,94,1032,10617,136973,1968168` and matched pairs total 1,047,450; Hasse incidences total 9,103,719.

The mathematical conclusion uses finite exhaustive induction on graph construction length and Forman's discrete-Morse theorem, not statistical inference. The verification proves nothing about graph sequences of length seven or greater, and no independent external audit has been performed.
