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

The proof was reconstructed from the definitions rather than inferred from numerical data. The critical identities checked are:

1. For each prime \(p\), \(D_p(N)=\lfloor N/p\rfloor-\lfloor N/(p+1)\rfloor\) is exactly the number of witness integers \(k\) with \(\lfloor N/k\rfloor=p\).
2. The adjacent-step identity is exactly \(D_p(N)-D_p(N-1)=\mathbf 1_{p\mid N}-\mathbf 1_{p+1\mid N}\).
3. If \(p\le\sqrt{N-1}\), then \(D_p(N-1)>0\) and \(D_p(N)>0\).
4. If \(p\ge\sqrt N\), both relevant witness intervals have length below one, so their counts are zero or one.
5. For odd \(N\ge5\), every such large prime is odd, hence \(p+1\nmid N\). Thus large primes never leave and a large prime enters exactly when it divides \(N\).
6. At most one prime divisor can be at least \(\sqrt N\); equality can occur only for a prime square.

The bundled `verify.py` recomputes the floor-set prime count directly for every odd \(N\) from \(5\) through \(100000\) and checks all distinct odd-prime triples of product at most \(100000\). Expected output:

`VERIFY_OK odd_n=49998 triple_cases=10618 max_n=100000`

This computation is a regression check only. It does not certify the infinite theorem; the symbolic proof above does.
