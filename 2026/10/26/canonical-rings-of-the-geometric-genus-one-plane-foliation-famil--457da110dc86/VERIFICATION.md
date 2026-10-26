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

The standalone `verify_plurigenera.py` uses only the Python standard library and exact integer arithmetic. Execute:

```sh
python3 verify_plurigenera.py
```

Actual checked ranges: integer \(2\le n\le10\), integer \(0\le m\le55\). For each of the 504 pairs it enumerates the triples defining \(H^0(mK_{\mathcal F_n})\), decomposes every admissible monomial into the proposed generators, and compares the dimension with the generating function. It also checks the \(n=2\) weighted-partition formula, and equality of the catalecticant binomials at all checked indices. Successful output starts with `VERIFY_OK`.

The general proof does not rely on the finite cutoff. It consists of the exact local divisorial valuations at the final infinitely-near centers, equivalence of divisorial conditions to monomial inequalities, a unique semigroup factorization modulo the catalecticant swaps, and an exact summation of the lattice-point series. The source's independent volume formula checks the leading asymptotic term. There has been no independent audit.
