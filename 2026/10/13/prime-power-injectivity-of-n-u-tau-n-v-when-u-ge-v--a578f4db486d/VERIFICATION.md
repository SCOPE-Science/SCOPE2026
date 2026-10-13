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
The proof was reconstructed directly from the prime-power identity
\[
F_{u,v}(p^a)=p^{au}(a+1)^v.
\]
For distinct primes, exact prime-adic divisibility gives \(p^a\mid b+1\) and \(q^b\mid a+1\) when \(u\ge v\). The comparison \(p^a q^b\le(a+1)(b+1)\le p^a q^b\) forces the impossible equality case with both prime bases equal to \(2\). For a common prime base, strict monotonicity in the exponent completes the argument.

The bundled regression program checks \(10500\) prime-power values across \(21\) parameter pairs with \(1\le v\le u\le6\), plus \(100\) instances of the key elementary inequality and ten exact checks on the noninjective ray \(v=3u\):
`VERIFY_OK parameter_pairs=21 prime_power_values=10500 stored_values=10500 inequality_checks=100 boundary_collision=21952`

Finite computation is not used to establish the universal quantifiers. The result does not classify the region \(u<v\); it only gives the explicit noninjective ray \(v=3u\) there.
