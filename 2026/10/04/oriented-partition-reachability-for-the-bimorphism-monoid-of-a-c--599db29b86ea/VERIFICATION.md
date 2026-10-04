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

The bundled `verify.py` is a standard-library exact checker. It constructs every set partition of \([n]\) through \(n=7\), weights a block of size \(m\) by the \(2^{\binom m2}\) possible labeled tournaments, and verifies
\[
A_0,\ldots,A_7=1,1,3,15,121,1665,43883,2437423.
\]

For comparable pairs it computes the Bell-product expression and, independently through \(n=6\), loops over every pair of set partitions and tests refinement directly. These two methods agree and give
\[
C_0,\ldots,C_7=1,1,5,53,1193,60329,7071533,1893360157.
\]

The script also checks the complete rank distribution in each tested arity. In particular, rank zero has one state (all coordinates in different components), while the unique-block top rank has \(2^{\binom n2}\) states (all labeled tournaments).

Observed output:

```text
A_0..A_7 = [1, 1, 3, 15, 121, 1665, 43883, 2437423]
C_0..C_7 = [1, 1, 5, 53, 1193, 60329, 7071533, 1893360157]
rank rows n=1..7 = [(1,), (1, 2), (1, 6, 8), (1, 12, 44, 64), (1, 20, 140, 480, 1024), (1, 30, 340, 2040, 8704, 32768), (1, 42, 700, 6440, 42784, 290304, 2097152)]
VERIFY_OK
```
