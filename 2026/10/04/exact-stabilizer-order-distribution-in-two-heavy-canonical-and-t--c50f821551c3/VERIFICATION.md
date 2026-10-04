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
The bundled checker exhaustively enumerates the canonical and terminal parameter regions for every \(2\le r\le200\). For each integer \(g\), it compares the number of pairs with \(\gcd(a,b)=g\) against \(3\Phi(\lfloor r/g\rfloor)\) and \(3\Phi(\lfloor(r-1)/g\rfloor)\), respectively. It also verifies that summing over \(g\) gives the total counts \(3r(r+1)/2\) and \(3r(r-1)/2\).

This computation is a finite regression test only. The all-dimensional theorem is proved in `RESULT.md`.

Expected terminal output: `VERIFY_OK`.
