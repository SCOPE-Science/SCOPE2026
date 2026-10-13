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
# Verification

Run `python3 verify.py` beside `verify.cpp` and `certificate.json`.

The C++ checker performs an exact depth-first enumeration normalized to initial pair \(01\). On appending a letter, it tests every new suffix of length \(L\) for every period \(p\) satisfying \(4L\ge7p\). This is exactly the condition for creating a factor of exponent at least \(\frac{7}{4}\).

At length \(67\) it checks all \(414112\) normalized survivors and finds exactly one with \(d_3\ge3\). At length \(68\) it checks all \(486776\) normalized survivors, verifies that every one contains all eight reduced pairs, and obtains the histogram \(397780,83006,5990\) for \(d_3=0,1,2\), respectively.

The checker also performs a direct all-factor period scan on the length-\(67\) representative, recomputes \(D_3=\{\mathtt{010},\mathtt{101},\mathtt{303}\}\), verifies that the word is a palindrome, constructs all eight alphabet permutations commuting with inversion, and checks that the orbit has size eight.

The finite length-\(68\) census combines with the proof that, once every reduced pair occurs, further extensions can only remove minimal absent triples. Thus the verification supports the all-longer-length upper bound, not merely the finite census. Independent audit has not been performed.
