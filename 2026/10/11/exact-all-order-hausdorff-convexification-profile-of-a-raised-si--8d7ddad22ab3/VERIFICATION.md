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

The proof uses barycentric coordinates of a unit-circumradius regular simplex and two exact separation arguments. Its critical steps are (i) the full set of accessible vertical heights under repeated averages, (ii) the lower horizontal bound \(n a/(n-1)\) for a barycentric-coordinate discrepancy \(a\), and (iii) the witness with exactly \(k-n+1\) feasible raised-vertex copies at order \(k\ge n\).

Execute `python3 check_profile.py`. This checks the arithmetic identities in the proof over 4,350 finite parameter pairs and separately performs 13 exact exhaustive lifted-multiplicity searches with exact convex quadratic projection. It does not attempt to certify infinitely many dimensions or averaging orders by enumeration; those quantifiers are addressed by the symbolic proof. Independent assessment has not been conducted.
