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

The analytic proof establishes universal claims, whereas the accompanying finite checker provides reproducible regression evidence. With Python 3, execute `python verify.py` from the extracted finding directory; no nonstandard packages are needed.

The checker asserts the two relevant squared center-to-gap-midpoint distances equal 9/16, both squared center-to-occupied-vertex distances equal 7/16, the squared center-to-origin distance equals 3/16, and the contact chord squared length equals 9/4. It checks the exact identity \(D(a,1-a)=9/4+3(a-1/2)^2\) on 101 rational values and the correct unique half-contact equality among 861 threshold-eligible rational (a,b) samples. It also checks that the opposite-edge vertical squared separation 3 strictly exceeds the disk-diameter squared bound 9/4.

No finite sample proves a statement for all real contact parameters. That step is the monotonicity-plus-square identity in RESULT.md; the perfect-matching and edge-covering deductions finish the proof. Publication priority has not been independently certified.
