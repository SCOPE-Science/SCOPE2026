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

Let \(e_1,\ldots,e_r\) be the coordinate idempotents. For a basis tuple with \(n_j\) copies of \(e_j\), the only permutations contributing to Grinberg's cycle formula are those preserving every label class, because a cycle mixing two distinct coordinate idempotents has product zero. Hence
\[
f_m(e_{i_1},\ldots,e_{i_m})=\prod_j(c_j)_{n_j}.
\]
The signed cycle identity used here is
\[
\sum_{\sigma\in S_s}\operatorname{sgn}(\sigma)c^{\#\operatorname{cycles}(\sigma)}=(c)_s.
\]
It is an integral polynomial identity, so reduction modulo \(p\) is legitimate.

For the standard representative \(a_j\in\{0,\ldots,p-1\}\) of \(c_j\), one has \((c_j)_s\ne0\) exactly for \(s\le a_j\). Thus a nonzero basis value of \(f_m\) exists exactly when \(m\le\sum_j a_j\). Multilinearity converts this basis criterion into the claimed identity/nonidentity criterion for the entire Frobenius map. No enumeration is used to extend a finite pattern to arbitrary \(p\), \(r\), or \(m\).

A separate small regression expansion over permutations was performed for primes \(2,3,5\), ranks at most \(3\), and Frobenius orders at most \(5\); it matched the product formula. This check is supplementary only. The theorem does not verify or claim determinant-law pseudocharacter identities outside Grinberg's normalization-free definition.
