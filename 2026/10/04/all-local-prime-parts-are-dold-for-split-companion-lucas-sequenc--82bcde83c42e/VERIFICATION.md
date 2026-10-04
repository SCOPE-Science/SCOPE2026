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
The proof was checked symbolically in the split-root parameterization \(V_n=a^n+b^n\). For odd primes, the critical facts are that the root ratio lies in \(\mathbb F_p^\times\), its order divides \(p-1\), and the sum-version lifting identity gives the exact valuation on odd multiples of the half-order. For \(p=2\), parity gives an explicit two-level p-part sequence.

The standalone exact script `verify.py` checks all coprime ordered pairs \((a,b)\) with \(-8\le a,b\le8\), excluding zero and \(a=-b\), against every prime \(p\le29\). It verifies Dold divisibility through index \(120\) and checks the stated realizability criterion from the signs of the Möbius transforms. Its expected terminal line is:

`VERIFY_OK 1700`

The finite computation is a consistency check and not a substitute for the infinite proof.
