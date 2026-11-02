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

# Verification notes

The reproducibility artifact `VERIFY.py` uses Python's standard library. Execute `python VERIFY.py` after extracting the embedded file. It checks the exact companion matrix and finite-difference Hensel approximations to the critical index, then enumerates all sequence positions in every complete fundamental period for \(5\le k\le15\). The designated residue has exactly \(2^{\lfloor k/2\rfloor}\) occurrences, and all matching positions lie in the branch \(n\equiv3\pmod6\).

The unrestricted proof uses two-adic matrix logarithms and a contraction argument. The finite enumeration corroborates but does not imply this conclusion. Historical priority and independent expert verification remain open.
