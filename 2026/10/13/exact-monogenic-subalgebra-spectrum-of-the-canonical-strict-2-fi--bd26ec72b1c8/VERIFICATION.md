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

The verification has a finite exact part and an infinite structural part.

For the exact part, `verify_monogenic_x2.py` implements the five-point levels of \(X_2\), the order from Definition 4.1, and the Esakia operation \(A\to B=(\downarrow(A\setminus B))^c\). For finite nonempty \(A\setminus B\), only finitely many top levels can remain outside its downset, so the implementation is exact rather than a truncation. It enumerates all \(31\) nonempty rank-0 upsets and all \(35\) rank-1 upsets and computes their generated closures. The distributions are
\[
\text{rank 0}:\quad 1\text{ of size }3,26\text{ of size }5,4\text{ of size }9,
\]
\[
\text{rank 1}:\quad 31\text{ of size }3,4\text{ of size }5.
\]
It also verifies that the four 9-element generators are exactly \(L_2^0\setminus\{x_0^j\}\) for \(1\le j\le4\), and for each one checks all three binary operations on its nine explicitly generated terms. The script returns `VERIFY_OK 1300 exact assertions`.

For the infinite part, no enumeration is used. If an upset contains a point at level \(r\ge2\), the defining order places that point below every maximal point in \(L_2^0\), so the upset contains all of \(L_2^0\). Every point of \(X_2\) lies below a maximal point; hence the upset has full downset and is dense. Any nonzero proper dense element generates exactly \(\{0,a,1\}\). This proves the size-3 conclusion uniformly at every deeper level.

The verifier is a consistency and exhaustiveness check for the bounded low-rank cases; the uniform mathematical argument is what covers infinitely many deeper generators.
