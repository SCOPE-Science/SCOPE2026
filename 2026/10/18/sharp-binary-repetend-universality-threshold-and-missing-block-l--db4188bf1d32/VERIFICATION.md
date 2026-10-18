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

Run the included `verify.py` with Python 3 from the extracted package directory. It uses only the standard library. The program independently forms binary periods by integer long division and compares cyclic windows at every length from one through the critical length plus one against quotient bins of the reduced residues. For \(1\le k\le9\), it checked 45,390 distinct-word memberships without mismatch, verifying both the exact missing-word formula and the maximal universal length. For \(2\le k\le100\), it additionally checked the arithmetic phase equivalence in 99 cases.

The critical deficits at \(k=1,2,3,4,5,6,7,8,9\) were \(0,0,2,0,4,0,0,544,0\), respectively. The period and residue enumeration are independent calculation routes; neither constitutes a proof of the infinite theorem, which instead follows from the valuation, bin-count, and irrational-rotation arguments in `RESULT.md`. No independent mathematical audit or external certification has been performed.
