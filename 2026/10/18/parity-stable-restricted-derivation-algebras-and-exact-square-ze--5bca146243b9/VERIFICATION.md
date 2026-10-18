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
# Verification evidence and limits

The file `verify.py` enumerates the coefficient vectors of all derivations on the even and odd truncated polynomial modules over \(\mathbb F_2\) and \(\mathbb F_4\), computing operators on full monomial bases. The tests directly check the square-zero matrix product, each Gaussian-elimination rank, and the exact matrix intertwiner entry by entry. They cover all \(1\le s\le4\) over \(\mathbb F_2\) and all \(1\le s\le3\) over \(\mathbb F_4\), including the extension-field multiplication law \(w^2+w+1=0\) in the latter case.

Expected square-zero rank distributions are: \(1+T\) at \((q,s)=(2,1)\), \(1+3T+2T^2\) at \((2,2)\), \(1+3T+4T^2+4T^3\) at \((2,3)\), \(1+3T+12T^2+8T^3+8T^4\) at \((2,4)\); \(1+3T\), \(1+15T+12T^2\), and \(1+15T+48T^2+48T^3\) at \((4,1)\), \((4,2)\), and \((4,3)\) respectively.

All checked cases passed when the program was executed directly on its source text. Successful execution prints `VERIFY_OK_EVEN_ODD_DERIVATIONS`. The complete proof for arbitrary characteristic-two fields and unbounded \(s\) is the valuation and intertwiner argument in `RESULT.md`; exhaustive tests are finite corroboration, not independent or infinite verification.
