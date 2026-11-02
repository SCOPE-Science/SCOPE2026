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

# Verification summary

Run `python3 verify.py` from this package using the supplied file, without third-party packages. The embedded `verification_output.txt` is actual standard output from that code. The program enumerates every cyclic length-four factor of the literal 106-digit witness and checks its reverse-free uniqueness; it separately exhausts the complete 256-four-tuple domain for the displayed five-case inequality and reversal-pair weights, confirms the upper-bound arithmetic, and checks balanced triple incidences of the witness.

The logical claim for *all* cyclic sequences rests on the mathematical proof of the degree-parity obstruction, five-case inequality, and potential cancellation. Local exhaustive checks over 256 possible four-tuples are exhaustive for that local lemma. The explicit witness check is exhaustive for that one word, not a census of all candidate words or possible optimal words. Replaying the code does not constitute an independent mathematical audit or an external certification.
