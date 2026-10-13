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

The analytical proof uses only a four-state bijection under a fixed orthogonal matrix and the independent centered-summand fourth-moment identity. These steps apply to arbitrary finite \(m\ge2\) and \(\zeta\ge1\). For \(b\ge3\), strict positivity of \((b-1)(b-2)/(b^3\zeta^3)\) excludes the matched Gram distribution. Finite tests do not establish those quantifiers independently.

`python3 verify.py` uses only Python's standard library. It exactly enumerates complete two- and three-column Gram laws for six \((\zeta,m)\) pairs, checks the Hadamard four-state mapping, verifies \(108\) rational fourth-moment identities, and independently enumerates collision signs for six block widths. It returned `VERIFY_OK exact_full_gram_cases=6 exact_moment_cases=108 support_checks=6` before packaging and is replayed from the decoded packaged path in delivery verification.

Limits: the checks operate in exact integer and rational arithmetic, not floating point, GPU execution or dynamically chosen inputs. The independent audit status above reflects an external activity that has not been performed.
