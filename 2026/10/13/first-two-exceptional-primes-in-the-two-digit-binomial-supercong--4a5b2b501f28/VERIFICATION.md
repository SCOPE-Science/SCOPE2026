---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Independent reproduction computed exact integer binomial sums at each of 19 odd primes through 71 and t=3,4,5 (57 cases). All sums are zero modulo p² and have nonzero residues modulo p⁴. Normalized residues give valuation 2 except at 7 and 71, where the p³ units are respectively 1 mod 7 and 5 mod 71 for all three truncations. To extend to every t>=5, write A_t-A_5=p^5 h with h a nonnegative integer. For 1<=j<=K<p², the identity j*binom(p^5 h,j)=p^5 h*binom(p^5 h-1,j-1) puts every j>0 Vandermonde term at 0 mod p⁴; the zero shift is trivial. Thus the nonzero residues mod p⁴ certify exact orders and nonzero S at every t>=3, not just sampled t. At t=2 complementary binomial terms cancel, so it must remain excluded. The repaired RESULT.md qualifies the nonliteral zero-digit specialization of González and supplies the correct prior implication from Ichino–Prasanna: the same Vandermonde polynomial identity at the p-adic shift p^t/2, with p-integrality of each binomial polynomial and v_p(j)<=1, transfers the p² layer from -1/2 to A_t. No theorem, range, or residue was changed. Replay: /workspace/branches/e388a124-0a48-4ac4-b16f-a293c5ef6921/{check_record3.py,check_record3.out}. The supplied verifier was inspected, not executed.

## originality

PASS

The generic p² layer is covered and is not a novel component. The supported remaining contribution is the exact finite-prime sharpness classification, including the exact order at the two exceptional primes uniformly in truncation length. Neither known divisibility at other digit depths nor a table of Fermat quotients alone gives these exact orders.

## value

PASS

The valuation invariant tests the sharpness of a known digit-depth supercongruence on its smallest nontrivial four-term slice. The bound 71 is the point at which the second exception is attained, not a claim about an arbitrary range of primes. The computations distinguish ordinary sharpness, extra cancellation and exact termination at the next p-adic digit at both exceptional primes; the answer holds for every eligible truncation rather than just small input binomial coefficients. Even recognizing the equivalent Fermat-quotient test for extra divisibility does not supply these exact exceptional orders.

The dated certificate retains the supplied scientific assessment, sources and limitations.
