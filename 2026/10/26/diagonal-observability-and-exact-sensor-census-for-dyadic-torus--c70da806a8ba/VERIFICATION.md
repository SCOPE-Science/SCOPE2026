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
# Reproducibility and limits

Run `python verify.py` with a standard Python 3 interpreter. The checker directly constructs the binary observation matrix of the stated cellular automaton without using the symbolic proof, applies exact GF(2) Gaussian elimination, and compares full rank with the residue test. It exhausts every sensor set on \(2	imes2\), \(4	imes2\), and \(4	imes4\) periodic grids (respectively 16, 256, and 65536 sets) and also checks the exact counting formula by sensor budget. An additional 640 seeded random placements are checked on \(8	imes2\), \(8	imes4\), \(8	imes8\), and \(16	imes2\) grids. The checker also verifies that all observation rows become zero after the claimed extinction time.

These computational checks establish correctness only for the tested finite cases. The all-size iff criterion, counting formula and limiting random-placement law are established by the analytical arguments in `RESULT.md`. No independent scientific audit or external validation has been performed.
