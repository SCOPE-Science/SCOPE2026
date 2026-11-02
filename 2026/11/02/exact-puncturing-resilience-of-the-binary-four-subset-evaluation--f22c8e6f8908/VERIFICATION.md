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
# Verification and limits

Run `python3 verify.py` from the same directory. Successful execution prints `VERIFY_OK` after checks of all admissible type compositions at the four finite bases, every target three-type XOR at the size-seven base, direct Krawtchouk counts for every independent ordered binary message pair at lengths six through nine, and the rank and obstruction counts for the explicit equality witnesses. The script relies only on exact integer arithmetic from the Python standard library.

The proof in RESULT.md includes two separate inductions: a lower bound on three-subset XOR counts and a length-growth bound for the four-subset support obstruction. Those symbolic steps, together with exhaustive finite base cases, establish the theorem for every integer length in scope. A finite run alone is not an infinite proof.

Originality was compared with the complete fixed-weight construction and with published characterizations of minimal codes; possible unindexed priority is not excluded. This is an internal mathematical review only; independent audit and validation have not been performed.
