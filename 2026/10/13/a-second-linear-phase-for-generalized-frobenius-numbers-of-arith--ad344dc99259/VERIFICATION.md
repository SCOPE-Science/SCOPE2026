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

The structural proof in `RESULT.md` is self-contained: it reduces all representations to integer lattice points, establishes the count at the last exceptional integer, verifies the next full residue window and propagates those bounds by the least generator. This is the basis for the unrestricted correctness judgment.

`verify.py` is an executable independent finite check using only the Python standard library. Its exact integer arithmetic has no numerical tolerances. Execute with `python verify.py`. The checked cases include odd \(a=3,5,\ldots,83\), all \(1\le d\le(a-1)/2\) coprime to \(a\), and all \(p\) in the theorem's claimed interval. For smaller parameters a second dynamic-programming denumerant is compared to the residue-lattice evaluation. `verification_output.txt` preserves the observed output.

Finite testing does not prove an infinite theorem and does not establish publication novelty. The restrictions on \(a,d,p\) are essential to the claimed formula; no independent audit has been performed.
