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
# Verification details

The proof in `RESULT.md` is symbolic and valid for every integer \(a\ge2\) and every odd prime \(p\); the restricted complete classification applies when \(\Omega((\sigma(n)-n)/4)\le2\), after \(\nu_2(\sigma(n)-n)=2\) is proved.

Run the included `verify.py` with a standard Python 3 interpreter. Its trial-factorization routine independently computes \(D\) and \(\Omega\); its primality checks use deterministic Miller–Rabin bases for unsigned \(64\)-bit integers. The captured successful check was:

```
CHECK_OK tested_prime_pairs=3861 fixed_points=2 low_odd_support=2 family=[(3, 152, 19, 37), (11, 8394752, 4099, 2098687), (15, 2147581952, 65539, 536895487)] exceptional=284
```

The finite test covers \(2\le a\le10\), odd prime \(p\le3000\), and separately paired-prime exponents \(3\le a\le18\); it is neither a complete census for all parameters nor an independent proof. The theorem instead uses the exact valuation argument, elimination identities, and complete factorization of \(16\). No unproved primality assumption is used for a particular example, and no existence or infinitude beyond the conditional parameterization is asserted.
