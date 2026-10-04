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
The universal proof uses only the Frobenius fixed-point-free action and elementary arithmetic.

Critical checks:
- \(V\cong C_p^r\) has
  \[
  \psi(V)=1+(p^r-1)p=p^{r+1}-p+1;
  \]
- for every nontrivial complement element \(c^j\), the operator \(c^j-1\) is invertible and
  \[
  (1+c^j+\cdots+c^{(q-1)j})(c^j-1)=0,
  \]
  hence the geometric-sum operator is zero;
- every element outside \(V\) therefore has order \(q\);
- the complement acts in orbits of size \(q\) on \(V\setminus\{0\}\), so \(q\mid p^r-1\);
- if \(D=p^{r+1}-p+1\), then \(\gcd(D,pq)=1\);
- consequently
  \[
  \gcd(\psi(V),\psi(G))=\gcd(D,q-1)<D.
  \]

The packaged checker `artifacts/verify.py` constructs several explicit fixed-point-free linear actions, enumerates every group element, computes element orders by repeated multiplication, and verifies both the closed \(\psi\)-formula and the exact gcd formula. It includes scalar actions and the nonscalar actions giving the \((2,2,3)\) and \((2,3,7)\) examples.

The replay returns `VERIFY_OK`.

Finite enumeration is not used as the proof of the universal theorem.
