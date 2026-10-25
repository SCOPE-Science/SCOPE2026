---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

From Agustin-Aquino Theorem 5.1 the affine sum reduces to S_(2p²)=C_(2p²)+p(p-1)C_(2p); the latter summand is integral by their Theorem 8.2. The odd-root block is integral from the monic polynomial ((X+1)^q+(X-1)^q)/2 for q=p². For primitive p² roots, v_p of alpha(z)^(2p²) is -2p/(p-1)>-2p. For primitive p roots, the p-adic Newton power-sum expansion for squares alpha(z)^2 has a unique lowest-valuation contribution from c_d^(2p+2)c_1 p², of valuation -2p; the other cases s<=2p+1 give at least -2p+1. Non-p primes are integral by cyclotomic units. A separate Newton–Girard exact rational reconstruction checked p=5,7,11, obtaining denominators 5^10, 7^14 and 11^22. Six-prime submitted checker was inspected, not relied on for the universal proof.

## originality

PASS

Agustin-Aquino first reduced affine derangement sums to cotangent blocks and already proved the 2p denominator. The inspected 2026 paper has general divisor/Bernoulli expressions but not the uniform 2p² exact reduced denominator p^(2p) in its stated theorems. A nontrivial Newton-term valuation argument is needed, beyond plugging a modulus into a symbolic expression.

## value

PASS

The affine Wang–Sun sum is a recognized arithmetic root-of-unity object. Determining the first nontrivial prime-square denominator layer uniformly over all p>=5 resolves a genuine p-adic cancellation problem beyond the known p layer; it is an exact natural invariant with transferable Newton valuation structure. No general higher power theorem is needed for value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
