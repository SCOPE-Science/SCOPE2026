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
# Reproduction and limits

Run `python3 verify.py` with Python's standard library. The program uses an odd-part unbounded/even-part at-most-once dynamic program for the signed weighted statistic and a separately computed 4-regular partition dynamic program for the unweighted counts. An integer-square test enumerates representations by both quadratic forms using only positive coordinates with \(4\mid y\).

It verifies the claimed coefficientwise identity modulo eight at each of \(2401\) indices, checks the classical two-square normalization at those indices and the inert-prime transfer at \(1019\) eligible indices, independently enumerates actual partitions through index \(25\), checks \(2401\) unweighted product coefficients, and checks \(678\) progression indices through \(2400\). Output is stored in `verification_output.txt`.

These are actual finite checks. They are not exhaustive over all nonnegative integers and cannot establish the new infinite statements; those follow from the proof in `RESULT.md` and the cited published counting congruences. Neither an independent audit nor an external formal certification has been performed.
