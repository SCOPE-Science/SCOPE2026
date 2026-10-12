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

The proof is analytic and symbolic, conditional only on established published Lemma 3.3 of Somu--Kukla--Tran, Dirichlet's theorem, and elementary unique divisor factorization / CRT. The main numerical identity is the telescoping product \(\prod_{m=3}^{\infty}(1-m^{-2})=2/3\). The resulting ratio \(\varphi(z)/z>1/4\) holds for every sufficiently late minimal-crossing odd prime block, not merely for the blocks checked computationally.

The accompanying `verify.py` tests a small fixed-modulus version of the Dirichlet residue lemma for \(z=6\), checks a sample of coprime Zumkeller multiples using exact divisor partitions, and checks the \(15015\) odd prime-block example. It prints its own passing checks. These are finite examples and are *not* proofs of the eventual block lemma, infinitude of Dirichlet primes, or natural-density convergence.

Scientific limitations: no effective uniform \(B_r\) or explicit error term is given; the result concerns Zumkeller-plus-prime only. Independent audit and external validation have not been performed.
