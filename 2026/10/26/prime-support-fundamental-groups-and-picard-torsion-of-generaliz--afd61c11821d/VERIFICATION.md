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

# Verification of the arithmetic component

The theoretical proof requires (i) the published fixed-point criterion, (ii) simple connectedness of the complete intersection, (iii) Armstrong's fundamental-group theorem, and (iv) the character-descent lemma for line bundles, and (v) the known quasi-étale class-group exact sequence. The supplied `verify.py` tests **only** the subsequent finite cyclic-group arithmetic, including all intermediate subgroups, for many values of \(k\). A finite check is not an infinite proof, and none of the geometric theorems is reduced to computation.

Run `python3 verify.py` using Python 3 with the standard library. The expected success message is `VERIFY_OK cyclic_fixed_subgroups_k=2..240 prime_power_dichotomy=true all_intermediate_quotients=true`.

The infinite arithmetic proof is explicit: the fixed-point exponents are exactly the nonunits modulo \(k\); their generated subgroup has index equal to the gcd of all proper divisors greater than one, namely \(p\) if \(k\) is a power of \(p\), and \(1\) otherwise. The empty set for prime \(k\) gives index \(k\). For \(s\mid k\) with \(1<s<k\), the subgroup generator itself has fixed points.
