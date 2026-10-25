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

# Finite reproducibility and proof boundary

Run `python3 verify.py` with Python 3 (standard library only). The checker enumerates all \(2^k\) residue classes at every \(1\le k\le17\), compares iterated least arrival times with the valuation formulas, computes the complete parity-specific depth histograms independently and checks them against the explicit symbolic census. Expected successful output:

`VERIFY_OK: full direct time and histogram matches for k=1..17; 262142 residues, two parity basins`

A finite test cannot establish the general theorem; the proof in `RESULT.md` derives every infinite-family assertion by exact valuation growth and residue-class counting. In particular, the checker is not an independent mathematical audit. No external certificate, proof-assistant verification or independent validation is claimed.
