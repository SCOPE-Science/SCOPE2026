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
Run `python3 verify.py`.

The checker constructs \(\sigma(r)\) for every
\[
1\le r\le200000
\]
and verifies the exact parity equivalence
\[
\sigma(r)\ \text{odd}
\quad\Longleftrightarrow\quad
r\ \text{is a square or twice a square}.
\]

It then groups integers by their divisor sum and checks every possible partner in those equal-\(\sigma\) fibers for
\[
m^2+n^2=\sigma(m)^2.
\]
No pair occurs through the stated bound.

Finally, it checks the five MP(2,2) examples displayed in Dimitrov's Table 8 and confirms the defining identity
\[
\sigma(m)^2+\sigma(n)^2=2(m^2+n^2)
\]
for each, while confirming that none has equal divisor sums.

These calculations are regression checks only. The all-integer obstruction is proved symbolically in `RESULT.md`; the two deep nonexistence inputs are the classical Fermat infinite-descent theorems stated there.

A successful replay prints `VERIFY_OK`.
