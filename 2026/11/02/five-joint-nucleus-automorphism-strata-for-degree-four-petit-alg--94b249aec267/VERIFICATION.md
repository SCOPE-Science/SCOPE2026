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

# Verification and limits

The accompanying `verify.py` uses only Python's standard library. Run `python3 verify.py` from its directory. Expected last line is `VERIFY_OK`.

The first algorithm enumerates every nonempty coefficient support in a primitive-fourth-root Kummer basis, discarding only \(\{0\}\). It determines \(r(I)\) and \(e(I)\) by their gcd characterizations, counts projective parameters, and divides by full Frobenius orbit length.

The second algorithm does **not** reuse the support rules: it enumerates Frobenius orbits of exponents in the cyclic quotient \(K^\times/F^\times\) and computes the genuine coefficient field-degree by checking \((q^r-1)k\equiv0\pmod{q^n-1}\) for each candidate divisor \(r\) of \(n\). It also measures projective orbit sizes directly.

The two algorithms agree at \((q,n)=(5,4),(9,4),(13,4),(17,4),(7,6)\). The first four reproduce the five symbolic polynomial multiplicities. For \(q=5\), the five counts are \(36,2,2,2,1\), totaling \(43\). The auxiliary degree-six case is a consistency check on the support mechanism, not a degree-six theorem claimed here.

The complete mathematical proof depends on the stated literature-based isomorphism, automorphism and right-nucleus results plus a finite symbolic support partition, not on enumerating arbitrarily large fields. The program's finite verifications do not prove the infinite family. Absolute historical priority and any independent audit are not asserted.
