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

# Verification and limitations

Run the standalone checker using `python3 verify.py 1000000` with standard Python 3. Its multiplicative prime-power formula is cross-checked directly via the square-gcd interpretation through \(n=300\). For each integer \(2\le n\le10^6\), it tests whether \(\beta(n)\mid n-1\), excludes primes from the composite-candidate list, and asserts that the only composite hit is \(4\). It also tests the claimed support exclusion for each composite hit.

The actual run returned `CHECK_OK limit=1000000 composite_hits=[4] odd_support_le3=0 even_support_le4_excluding4=0`. This computation is finite and provides no proof outside the tested range. The universal proof in `RESULT.md` is entirely algebraic, using strict rational inequalities and congruence arguments. No external audit or independent mathematical certification has occurred.
