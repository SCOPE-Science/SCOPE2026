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

The source criterion was checked directly under the canonical hypotheses:
\[
p\text{ even},\qquad q\text{ odd},\qquad 0<|q|\le p/2,\qquad \gcd(p,q)=1.
\]
It states that a two-bridge link \(b(p,q)\) admits a non-trivial L-space surgery exactly when
\[
p\equiv\pm1\pmod{|q|}.
\]

For even \(p\ge4\), this is equivalent to \(q\) being a positive proper divisor of \(p-1\) or \(p+1\), with \(q=1\) shared by the two families. Schubert equivalence up to mirror sends a nontrivial divisor to its complementary divisor. A complementary pair is fixed exactly when the corresponding \(p-1\) or \(p+1\) is a square.

The bundled verifier enumerates all canonical positive denominators, applies the congruence criterion, quotients by modular inversion up to sign, and compares with the closed formula for every even \(p\le1000\). It reports:

`VERIFY_OK exact_even_p_through=1000 scaled_density=100:110/313:7.63137269,1000:1629/26156:9.01597735,5000:10107/638096:9.29843265 target_pi2=9.86960440`

The finite computation does not prove the asymptotics. Those follow from
\[
\sum_{\substack{n\le X\\n\ {\rm odd}}}\tau(n)
=
\frac14X\log X+O(X),
\]
the bound on inversion-fixed points, and
\[
\sum_{\substack{n\le X\\2\mid n}}\varphi(n)
=
\frac{X^2}{\pi^2}+O(X\log X).
\]

No independent audit has been performed.
