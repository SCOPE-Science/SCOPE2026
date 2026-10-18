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
Run `python3 verify.py` in a directory containing that standalone file. No third-party packages are required.

The verifier checks actual positional digit sums and equality of \(H_b\) on \(b=7,\ldots,30000\), compares actual squarefreeness of the two witness integers against the algebraic criterion for \(b=7,\ldots,2000\), checks the first ten permitted bases at least eleven, and counts all residues modulo prime squares for primes \(2,3,5,7,11,13,17,19,23,29,31\).

The verification run passed all checks. Finite enumeration cannot establish the infinite theorem; the general proof is the separate exact digit expansion, factor gcd analysis, CRT, and large-square tail bound. The claimed density is for the explicit witness family only. No independent mathematical audit was conducted.
