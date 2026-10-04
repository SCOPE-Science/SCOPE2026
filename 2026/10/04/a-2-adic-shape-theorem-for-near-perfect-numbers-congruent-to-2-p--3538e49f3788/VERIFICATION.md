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

The symbolic proof uses only exact identities:

- \(\sigma(2m)=3\sigma(m)\) for odd \(m\);
- \(\sigma(m)\) is odd exactly when \(m\) is a square;
- if \(m\) is odd and an even divisor \(d\mid2m\), then \(v_2(d)=1\);
- multiplicativity of \(\sigma\);
- for odd \(p\) and odd \(a\),
\[
v_2(\sigma(p^a))=v_2(p+1)+v_2(a+1)-1.
\]

The included `artifacts/verify.py` performs an independent exact-integer scan through \(2{,}000{,}000\). It computes divisor sums by a sieve, recognizes near-perfect integers from the definition, factors only the odd parts of target-residue candidates, and checks every conclusion of the theorem. The expected terminal line is:

`VERIFY_OK bound=2000000 nearperfect=50 target=3 target_values=18,234,650`

This finite replay is a consistency test only. It does not establish the infinite theorem and no unproved computational exhaustion is used in the proof.
