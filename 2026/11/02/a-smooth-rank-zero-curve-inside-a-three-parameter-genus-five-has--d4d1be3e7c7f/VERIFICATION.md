---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Read and independently reconstructed the coefficient-extraction Hasse–Witt matrix H and odd/even block decomposition. B rank2 always; C rank<2 would force c=0,ab=1 and singular quintic. The twisted two-step 2×2 block D has det T=a³b³+c³(a⁴−b)−1, and rank-one D on T=0 has second iterate controlled by E=b³+ac³+a^27. Frobenius stable rank doubles, proving 4/2/0. T=(a⁴−b)c³+(ab−1)³ irreducible by noncube pole along a⁴−b. On U∩{T=0}, c≠0 and partial derivatives T_b=−c³,E_a=c³ give smooth transverse codimension-two loci. Three F3 triples witness each stratum. Independent F3 full enumeration and symbolic matrix verification corroborate without replacing generic proof.

## originality

PASS

Novoselov develops Hasse–Witt methods for odd-power trinomial families x^{2g+1}+u x^{g+1}+vx; at genus5 exponents differ (11,6,1). Frei examines large a-number and Nourozi–Rahmati–Tafazolian binomial families, none of the inspected primary statements gives exact T,E stratification of this three-parameter odd family. Resultary search returned unrelated characteristic-3 algebraic examples, not an equivalent genus-five family.

## value

PASS

Determines the entire stable Frobenius rank in a natural order-four-automorphism hyperelliptic genus-five family where ordinary Cartier rank stays fixed; the rank-zero curve and rank-drop divisor are geometrically characterized, not just samples in small fields.

The dated certificate retains the supplied scientific assessment, sources and limitations.
