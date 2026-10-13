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

The claim is proved symbolically; no finite enumeration is used as evidence for the universal statement.

The arithmetic check is:

1. Let \(d=\operatorname{ord}_N(p)\).
2. The congruence \(p^\nu\equiv-1\pmod N\) puts the nontrivial order-two element \(-1\) inside the cyclic group \(\langle p\rangle\).
3. The unique order-two element of a cyclic group of even order \(d\) is \(p^{d/2}\). Therefore
   \[
   \nu\equiv d/2\pmod d,
   \]
   and the least admissible exponent is \(d/2\).

The geometric check is read directly from the initiating source:

- Lemma 7.7 gives the quotient
  \[
  \mathcal H(2m+1,q^2)\to X_N^{2m}
  \]
  whenever \(N\mid q+1\), with \(e=(q+1)/N\) and degree \(e^{2m+1}\).
- Proposition 7.9 gives
  \[
  q^m\mathrm N^m(X_N^{2m})\subset\Lambda_Z\otimes\mathbf Z_{(p)}
  \]
  when the cover degree is prime to \(p\), and gives the same \(q^m\) annihilator for the \(p\)-primary part of \(\Lambda_Z^\vee/\Lambda_Z\).
- The proposition also gives \(\ell\)-adic unimodularity for \(\ell\ne p\) not dividing the cover degree.

At the least admissible power \(q_0=p^{d/2}\), the integer \(e_0=(q_0+1)/N\) is prime to \(p\), so all hypotheses apply. Substitution gives \(q_0^m=p^{md/2}\).

For every other admissible exponent, \(\nu=d/2+kd\) with \(k\ge0\), hence both \(q=p^\nu\) and \((q+1)/N\) are larger. This verifies that the chosen cover degree and the source-provided \(q^m\) bound are simultaneously minimal inside this construction.

Illustrative checks: \((N,p)=(3,2)\) gives \(d=2\) and bound \(2^m\); \((N,p)=(5,2)\) gives \(d=4\) and bound \(2^{2m}\). These examples are not used in the proof.

Limit: the verification proves only the smallest bound delivered by this Hermitian-cover method. It does not determine the exact exponent of the saturation quotient.
