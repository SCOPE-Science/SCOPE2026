---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For all L>=0, n<2^L and j>=0, Kummer identifies nu_2(binomial(5n,2n)) with binary carry-outs in 2n+3n. The three-bit state (previous n bit, carry forming 3n=n+2n, carry adding 3n+2n) has exactly the stated two transitions per input digit; only the second carry is weighted. Four forced zero-input steps clear every one of the eight states; the terminal weights (1,1,1,t,t,t,1,t^2) include all residual carries. The length-L transfer thus enumerates each n exactly once. Formal matrix inversion and coefficient extraction yield F_0=(1+z^3)/(1-z-z^2+z^3-z^4) and F_1=z(1-z^2)^2/(1-z-z^2+z^3-z^4)^2. In a newly written independent Python/SymPy checker the transfer and terminal weights were rebuilt, both rational identities cancelled exactly, and all histograms for L=0..13 (sum 2^L=16383 inputs) agreed with independent digit sums s_2(n)+s_2(3n)-s_2(5n). Git tree SHA-1 was independently reconstructed from all seven actual entries and matched the frozen assignment. The unrestricted theorem follows from Kummer plus state induction, not from finite tests.

## originality

PASS

Best-of-knowledge PASS for the exact all-level dyadic fibre distribution of the fixed ray binomial(5n,2n), especially its nonzero valuation-one rational function, not for the known Kummer theorem, the generic finite-transducer method, or the preexisting parity-count sequence. Primary comparison distinguishes fixed-row valuation distributions from a moving proportional ray and checks the highly pertinent OEIS bivariate word-count family. No checked primary result stated or directly implied the exact all-level ray formula. Unindexed general fixed-ratio carry enumeration is a genuine residual historical-priority risk; failed searches alone are not novelty proof.

## value

PASS

The 2-adic valuation of binomial(5n,2n) along a fixed proportional ray is a natural digital-arithmetic statistic, and exactly counting all fibre multiplicities over every dyadic interval is a definite infinite-family invariant that a number-theory researcher could reuse. The two distinct carry mechanisms produce nontrivial valuation-one counts and a squared quartic generating denominator, beyond the earlier parity/zero layer. The work explicitly computes this natural case rather than presenting a generic relabeling, a few sampled values or an unsupported major breakthrough. No generic arbitrary-slope theorem or asymptotic universality is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
